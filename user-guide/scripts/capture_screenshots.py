#!/usr/bin/env python3
"""Generate documentation screenshots from a YAML recipe using Playwright."""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import socket
import subprocess
import sys
import tempfile
import time
import uuid
from collections.abc import Mapping, Sequence
from contextlib import contextmanager, suppress
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import urlopen

DEFAULT_CONFIG = Path(__file__).resolve().parent.parent / "screenshots.yml"
SUPPORTED_ACTIONS = {
    "check",
    "click",
    "double_click",
    "evaluate",
    "fill",
    "goto",
    "hover",
    "press",
    "reload",
    "scroll_into_view",
    "select_option",
    "uncheck",
    "wait_for",
    "wait_for_load_state",
    "wait_for_timeout",
}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}
INSIDE_LABEL_POSITIONS = {"top-left", "top-right", "bottom-left", "bottom-right"}
OUTSIDE_LABEL_POSITIONS = {
    "outside-bottom",
    "outside-bottom-left",
    "outside-bottom-right",
    "outside-left",
    "outside-right",
    "outside-top",
}
LABEL_POSITIONS = INSIDE_LABEL_POSITIONS | OUTSIDE_LABEL_POSITIONS
LABEL_SETTINGS = {"color", "frame", "position", "selector", "text"}
BROWSER_SETTINGS = {
    "accept_downloads",
    "channel",
    "color_scheme",
    "device_scale_factor",
    "extra_http_headers",
    "geolocation",
    "has_touch",
    "http_credentials",
    "ignore_https_errors",
    "is_mobile",
    "java_script_enabled",
    "locale",
    "name",
    "navigation_timeout",
    "offline",
    "permissions",
    "proxy",
    "reduced_motion",
    "service_workers",
    "storage_state",
    "timeout",
    "timezone_id",
    "user_agent",
    "viewport",
}
ENVIRONMENT_VARIABLE = re.compile(
    r"\$\{(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?::-((?P<default>[^}]*)))?\}"
)
TEMPORARY_USERNAME = "admin"
TEMPORARY_PASSWORD = "djangocms-screenshots"
TEMPORARY_PAGE_PATH = "/en/welcome/?toolbar_on"

ADD_ELEMENT_LABEL_SCRIPT = """
(element, options) => {
    const document = element.ownerDocument;
    const window = document.defaultView;
    const bounds = element.getBoundingClientRect();
    if (!bounds.width || !bounds.height) {
        throw new Error(`Cannot label an element without dimensions: ${options.selector}`);
    }

    const outline = document.createElement("div");
    outline.dataset.screenshotLabelGroup = options.group;
    outline.setAttribute("aria-hidden", "true");
    Object.assign(outline.style, {
        position: "absolute",
        left: `${bounds.left + window.scrollX}px`,
        top: `${bounds.top + window.scrollY}px`,
        width: `${bounds.width}px`,
        height: `${bounds.height}px`,
        boxSizing: "border-box",
        border: `3px solid ${options.color}`,
        borderRadius: "2px",
        pointerEvents: "none",
        zIndex: "2147483646",
    });

    const badge = document.createElement("span");
    badge.dataset.screenshotLabelGroup = options.group;
    badge.textContent = options.text;
    Object.assign(badge.style, {
        position: "absolute",
        boxSizing: "border-box",
        padding: "3px 7px",
        background: options.color,
        color: "white",
        font: "600 13px/18px system-ui, -apple-system, sans-serif",
        letterSpacing: "0.01em",
        whiteSpace: "nowrap",
        textShadow: "none",
    });

    const placements = {
        "top-left": {top: "-3px", left: "-3px"},
        "top-right": {top: "-3px", right: "-3px"},
        "bottom-left": {bottom: "-3px", left: "-3px"},
        "bottom-right": {bottom: "-3px", right: "-3px"},
        "outside-top": {bottom: "100%", left: "-3px"},
        "outside-right": {top: "-3px", left: "100%"},
        "outside-bottom-left": {top: "100%", left: "-3px"},
        "outside-bottom": {
            top: "100%",
            left: "50%",
            transform: "translateX(-50%)",
        },
        "outside-bottom-right": {top: "100%", right: "-3px"},
        "outside-left": {top: "-3px", right: "100%"},
    };
    Object.assign(badge.style, placements[options.position]);
    outline.appendChild(badge);
    (document.body || document.documentElement).appendChild(outline);
}
"""

REMOVE_ELEMENT_LABELS_SCRIPT = """
(root, group) => {
    root.ownerDocument
        .querySelectorAll(`[data-screenshot-label-group="${CSS.escape(group)}"]`)
        .forEach((element) => element.remove());
}
"""


class ConfigurationError(ValueError):
    """Raised when the screenshot recipe is invalid."""


def expand_environment(value: Any, *, allow_missing: bool = False) -> Any:
    """Recursively expand ${NAME} and ${NAME:-default} in YAML values."""

    if isinstance(value, str):

        def replace(match: re.Match[str]) -> str:
            name = match.group("name")
            current = os.environ.get(name)
            if current:
                return current
            default = match.group("default")
            if default is not None:
                return default
            if allow_missing:
                return match.group(0)
            raise ConfigurationError(f"Environment variable {name!r} is required")

        return ENVIRONMENT_VARIABLE.sub(replace, value)
    if isinstance(value, list):
        return [expand_environment(item, allow_missing=allow_missing) for item in value]
    if isinstance(value, dict):
        return {
            key: expand_environment(item, allow_missing=allow_missing)
            for key, item in value.items()
        }
    return value


def load_config(path: Path, *, allow_missing_environment: bool = False) -> dict[str, Any]:
    try:
        import yaml
    except ImportError as error:
        raise ConfigurationError(
            "PyYAML is not installed. Run `make screenshots-install` first."
        ) from error

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ConfigurationError(f"Configuration file does not exist: {path}") from error
    except yaml.YAMLError as error:
        raise ConfigurationError(f"Could not parse {path}: {error}") from error

    config = expand_environment(raw, allow_missing=allow_missing_environment)
    validate_config(config)
    return config


def _require_mapping(value: Any, location: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ConfigurationError(f"{location} must be a mapping")
    return value


def _require_positive_int(value: Any, location: str) -> None:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ConfigurationError(f"{location} must be a positive integer")


def _validate_actions(actions: Any, location: str) -> None:
    if actions is None:
        return
    if not isinstance(actions, list):
        raise ConfigurationError(f"{location} must be a list")
    for index, action in enumerate(actions):
        item_location = f"{location}[{index}]"
        item = _require_mapping(action, item_location)
        if len(item) != 1:
            raise ConfigurationError(
                f"{item_location} must contain exactly one browser action"
            )
        name = next(iter(item))
        if name not in SUPPORTED_ACTIONS:
            choices = ", ".join(sorted(SUPPORTED_ACTIONS))
            raise ConfigurationError(
                f"Unsupported action {name!r} at {item_location}; choose from {choices}"
            )


def _validate_labels(labels: Any, location: str) -> None:
    if labels is None:
        return
    if not isinstance(labels, list):
        raise ConfigurationError(f"{location} must be a list")
    for index, raw_label in enumerate(labels):
        item_location = f"{location}[{index}]"
        label = _require_mapping(raw_label, item_location)
        unknown_settings = set(label) - LABEL_SETTINGS
        if unknown_settings:
            raise ConfigurationError(
                f"Unknown {item_location} setting(s): "
                f"{', '.join(sorted(unknown_settings))}"
            )
        for name in ("selector", "text"):
            if not isinstance(label.get(name), str) or not label[name]:
                raise ConfigurationError(
                    f"{item_location}.{name} must be a non-empty string"
                )
        frame = label.get("frame")
        if frame is not None and (not isinstance(frame, str) or not frame):
            raise ConfigurationError(f"{item_location}.frame must be a string")
        position = label.get("position", "top-left")
        if position not in LABEL_POSITIONS:
            choices = ", ".join(sorted(LABEL_POSITIONS))
            raise ConfigurationError(
                f"{item_location}.position must be one of {choices}"
            )
        color = label.get("color", "#d40055")
        if not isinstance(color, str) or not color:
            raise ConfigurationError(f"{item_location}.color must be a string")


def validate_config(config: Any) -> None:
    config = _require_mapping(config, "configuration")
    if config.get("version") != 1:
        raise ConfigurationError("configuration.version must be 1")
    if not isinstance(config.get("base_url"), str) or not config["base_url"]:
        raise ConfigurationError("configuration.base_url must be a non-empty string")
    if not isinstance(config.get("output_dir"), str) or not config["output_dir"]:
        raise ConfigurationError("configuration.output_dir must be a non-empty string")

    browser = _require_mapping(config.get("browser", {}), "configuration.browser")
    unknown_browser_settings = set(browser) - BROWSER_SETTINGS
    if unknown_browser_settings:
        raise ConfigurationError(
            "Unknown configuration.browser setting(s): "
            f"{', '.join(sorted(unknown_browser_settings))}"
        )
    if browser.get("name", "chromium") not in {"chromium", "firefox", "webkit"}:
        raise ConfigurationError("configuration.browser.name is not supported")
    viewport = _require_mapping(
        browser.get("viewport", {"width": 1440, "height": 1000}),
        "configuration.browser.viewport",
    )
    _require_positive_int(viewport.get("width"), "configuration.browser.viewport.width")
    _require_positive_int(
        viewport.get("height"), "configuration.browser.viewport.height"
    )
    _require_positive_int(
        browser.get("timeout", 10_000), "configuration.browser.timeout"
    )
    _require_positive_int(
        browser.get("navigation_timeout", 30_000),
        "configuration.browser.navigation_timeout",
    )

    _validate_actions(config.get("setup"), "configuration.setup")
    _validate_actions(config.get("before_each"), "configuration.before_each")

    screenshots = config.get("screenshots")
    if not isinstance(screenshots, list) or not screenshots:
        raise ConfigurationError("configuration.screenshots must be a non-empty list")
    known_ids: set[str] = set()
    for index, raw_screenshot in enumerate(screenshots):
        location = f"configuration.screenshots[{index}]"
        screenshot = _require_mapping(raw_screenshot, location)
        if not isinstance(screenshot.get("enabled", True), bool):
            raise ConfigurationError(f"{location}.enabled must be true or false")
        screenshot_id = screenshot.get("id")
        if not isinstance(screenshot_id, str) or not screenshot_id:
            raise ConfigurationError(f"{location}.id must be a non-empty string")
        if screenshot_id in known_ids:
            raise ConfigurationError(f"Duplicate screenshot id {screenshot_id!r}")
        known_ids.add(screenshot_id)

        output = screenshot.get("output")
        if not isinstance(output, str) or not output:
            raise ConfigurationError(f"{location}.output must be a non-empty string")
        output_path = Path(output)
        if output_path.is_absolute() or ".." in output_path.parts:
            raise ConfigurationError(f"{location}.output must stay inside output_dir")
        if output_path.suffix.lower() not in IMAGE_SUFFIXES:
            raise ConfigurationError(f"{location}.output must be a PNG or JPEG file")
        if "url" in screenshot and (
            not isinstance(screenshot["url"], str) or not screenshot["url"]
        ):
            raise ConfigurationError(f"{location}.url must be a non-empty string")

        _validate_actions(screenshot.get("actions"), f"{location}.actions")
        _validate_labels(screenshot.get("labels"), f"{location}.labels")
        capture = _require_mapping(screenshot.get("capture", {}), f"{location}.capture")
        selector = capture.get("selector")
        if selector is not None and (not isinstance(selector, str) or not selector):
            raise ConfigurationError(f"{location}.capture.selector must be a string")
        if not isinstance(capture.get("full_page", False), bool):
            raise ConfigurationError(f"{location}.capture.full_page must be boolean")
        if capture.get("selector") and capture.get("full_page"):
            raise ConfigurationError(
                f"{location}.capture cannot combine selector and full_page"
            )
        padding = capture.get("padding", 0)
        if not isinstance(padding, (int, float)) or isinstance(padding, bool) or padding < 0:
            raise ConfigurationError(f"{location}.capture.padding cannot be negative")
        quality = capture.get("quality")
        if quality is not None and (
            not isinstance(quality, int)
            or isinstance(quality, bool)
            or not 0 <= quality <= 100
        ):
            raise ConfigurationError(
                f"{location}.capture.quality must be an integer from 0 to 100"
            )
        if quality is not None and output_path.suffix.lower() == ".png":
            raise ConfigurationError(
                f"{location}.capture.quality is only available for JPEG output"
            )


def resolve_url(base_url: str, value: str) -> str:
    """Resolve a recipe URL against the configured django CMS instance."""

    return urljoin(f"{base_url.rstrip('/')}/", value)


def selected_screenshots(
    screenshots: Sequence[Mapping[str, Any]],
    patterns: Sequence[str],
    *,
    include_disabled: bool = False,
) -> list[Mapping[str, Any]]:
    enabled = [
        item
        for item in screenshots
        if include_disabled or item.get("enabled", True)
    ]
    if not patterns:
        return enabled
    return [
        item
        for item in enabled
        if any(
            fnmatch.fnmatchcase(str(item["id"]), pattern)
            or fnmatch.fnmatchcase(str(item["output"]), pattern)
            for pattern in patterns
        )
    ]


def _locator(page: Any, parameters: Mapping[str, Any]) -> Any:
    selector = parameters.get("selector")
    if not isinstance(selector, str) or not selector:
        raise ConfigurationError("A non-empty selector is required for this action")
    frame = parameters.get("frame")
    scope = page.frame_locator(frame) if frame else page
    return scope.locator(selector)


def _parameters(value: Any, simple_key: str = "selector") -> dict[str, Any]:
    if isinstance(value, str):
        return {simple_key: value}
    return dict(_require_mapping(value, "action parameters"))


def run_action(page: Any, action: Mapping[str, Any], base_url: str) -> None:
    name, raw_parameters = next(iter(action.items()))

    if name == "goto":
        parameters = _parameters(raw_parameters, "url")
        target = parameters.pop("url", None)
        if not isinstance(target, str) or not target:
            raise ConfigurationError("goto requires a non-empty url")
        page.goto(resolve_url(base_url, target), **parameters)
        return
    if name == "reload":
        parameters = {} if raw_parameters is None else _parameters(raw_parameters)
        parameters.pop("selector", None)
        page.reload(**parameters)
        return
    if name == "wait_for_timeout":
        milliseconds = (
            raw_parameters.get("milliseconds")
            if isinstance(raw_parameters, Mapping)
            else raw_parameters
        )
        _require_positive_int(milliseconds, "wait_for_timeout")
        page.wait_for_timeout(milliseconds)
        return
    if name == "wait_for_load_state":
        parameters = _parameters(raw_parameters, "state")
        state = parameters.pop("state", "load")
        page.wait_for_load_state(state, **parameters)
        return
    if name == "evaluate":
        parameters = _parameters(raw_parameters, "expression")
        expression = parameters.get("expression")
        if not isinstance(expression, str) or not expression:
            raise ConfigurationError("evaluate requires a non-empty expression")
        page.evaluate(expression, parameters.get("argument"))
        return

    parameters = _parameters(raw_parameters)
    locator = _locator(page, parameters)
    parameters.pop("selector", None)
    parameters.pop("frame", None)

    if name in {"click", "double_click", "hover", "check", "uncheck"}:
        method_name = "dblclick" if name == "double_click" else name
        getattr(locator, method_name)(**parameters)
    elif name == "fill":
        value = parameters.pop("value", None)
        if not isinstance(value, str):
            raise ConfigurationError("fill requires a string value")
        locator.fill(value, **parameters)
    elif name == "press":
        key = parameters.pop("key", None)
        if not isinstance(key, str) or not key:
            raise ConfigurationError("press requires a non-empty key")
        locator.press(key, **parameters)
    elif name == "select_option":
        option = parameters.pop("option", None)
        if option is not None:
            locator.select_option(option, **parameters)
        elif any(key in parameters for key in ("value", "label", "index")):
            locator.select_option(**parameters)
        else:
            raise ConfigurationError(
                "select_option requires option, value, label, or index"
            )
    elif name == "wait_for":
        locator.wait_for(**parameters)
    elif name == "scroll_into_view":
        locator.scroll_into_view_if_needed(**parameters)
    else:  # validate_config prevents this; keep the guard for direct API use.
        raise ConfigurationError(f"Unsupported action {name!r}")


def run_actions(page: Any, actions: Sequence[Mapping[str, Any]], base_url: str) -> None:
    for action in actions:
        run_action(page, action, base_url)


def _capture_options(page: Any, capture: Mapping[str, Any]) -> dict[str, Any]:
    options: dict[str, Any] = {
        "animations": capture.get("animations", "disabled"),
        "caret": capture.get("caret", "hide"),
        "omit_background": capture.get("omit_background", False),
        "scale": capture.get("scale", "css"),
    }
    for key in ("quality", "mask_color"):
        if key in capture:
            options[key] = capture[key]
    if capture.get("mask"):
        options["mask"] = [
            _locator(page, _parameters(target)) for target in capture["mask"]
        ]
    return options


@contextmanager
def element_labels(page: Any, labels: Sequence[Mapping[str, Any]]):
    """Temporarily draw labelled outlines over selected page elements."""

    group = uuid.uuid4().hex
    document_roots: dict[str | None, Any] = {}
    document_scopes: dict[str | None, Any] = {}
    try:
        for raw_label in labels:
            label = dict(raw_label)
            frame = label.get("frame")
            scope = page.frame_locator(frame) if frame else page
            document_roots.setdefault(frame, scope.locator("html"))
            document_scopes.setdefault(frame, scope)
            locator = scope.locator(str(label["selector"]))
            locator.wait_for(state="visible")
            locator.evaluate(
                ADD_ELEMENT_LABEL_SCRIPT,
                {
                    "color": label.get("color", "#d40055"),
                    "group": group,
                    "position": label.get("position", "top-left"),
                    "selector": label["selector"],
                    "text": label["text"],
                },
            )
        overlay_selector = f'[data-screenshot-label-group="{group}"]'
        yield [scope.locator(overlay_selector) for scope in document_scopes.values()]
    finally:
        # Navigation or a browser failure may already have destroyed a document.
        # Cleanup is deliberately best-effort so it cannot hide the capture error.
        for root in document_roots.values():
            with suppress(Exception):
                root.evaluate(REMOVE_ELEMENT_LABELS_SCRIPT, group)


def _capture_clip(
    locator: Any,
    overlay_locators: Sequence[Any],
    padding: float,
) -> dict[str, float]:
    """Return a clip containing the capture target, padding, and label overlays."""

    box = locator.bounding_box()
    if box is None:
        raise RuntimeError("Could not determine bounds for the capture selector")
    left = box["x"] - padding
    top = box["y"] - padding
    right = box["x"] + box["width"] + padding
    bottom = box["y"] + box["height"] + padding
    for overlays in overlay_locators:
        for index in range(overlays.count()):
            overlay_box = overlays.nth(index).bounding_box()
            if overlay_box is None:
                continue
            left = min(left, overlay_box["x"])
            top = min(top, overlay_box["y"])
            right = max(right, overlay_box["x"] + overlay_box["width"])
            bottom = max(bottom, overlay_box["y"] + overlay_box["height"])
    clipped_left = max(0, left)
    clipped_top = max(0, top)
    return {
        "x": clipped_left,
        "y": clipped_top,
        "width": right - clipped_left,
        "height": bottom - clipped_top,
    }


def capture_screenshot(
    page: Any,
    screenshot: Mapping[str, Any],
    output_dir: Path,
) -> Path:
    capture = dict(screenshot.get("capture", {}))
    target = (output_dir / str(screenshot["output"])).resolve()
    try:
        target.relative_to(output_dir.resolve())
    except ValueError as error:
        raise ConfigurationError(f"Output escapes output_dir: {target}") from error
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(
        f".{target.stem}.{uuid.uuid4().hex}.tmp{target.suffix.lower()}"
    )

    style_handle = None
    hide = capture.get("hide", [])
    if hide:
        if not isinstance(hide, list) or not all(isinstance(item, str) for item in hide):
            raise ConfigurationError("capture.hide must be a list of CSS selectors")
        rules = ",\n".join(hide)
        style_handle = page.add_style_tag(content=f"{rules} {{ visibility: hidden !important; }}")

    try:
        options = _capture_options(page, capture)
        selector = capture.get("selector")
        padding = capture.get("padding", 0)
        locator = None
        if selector:
            locator_parameters = {"selector": selector}
            if capture.get("frame"):
                locator_parameters["frame"] = capture["frame"]
            locator = _locator(page, locator_parameters)
            locator.scroll_into_view_if_needed()

        labels = screenshot.get("labels", [])
        has_outside_label = any(
            label.get("position") in OUTSIDE_LABEL_POSITIONS for label in labels
        )
        with element_labels(page, labels) as overlay_locators:
            if locator is not None and (padding or has_outside_label):
                options["clip"] = _capture_clip(locator, overlay_locators, padding)
                page.screenshot(path=temporary, **options)
            elif locator is not None:
                locator.screenshot(path=temporary, **options)
            else:
                options["full_page"] = capture.get("full_page", False)
                page.screenshot(path=temporary, **options)
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()
        if style_handle is not None:
            style_handle.evaluate("element => element.remove()")
    return target


def create_cms_site(
    project_dir: Path,
    *,
    username: str,
    password: str,
) -> str:
    """Create and seed a django CMS project using the installed CLI."""

    project_dir.mkdir(parents=True, exist_ok=False)
    djangocms = Path(sys.executable).with_name("djangocms")
    if not djangocms.is_file():
        raise RuntimeError("djangocms is not installed; run `make install` first")

    command = [
        str(djangocms),
        "screenshot_site",
        str(project_dir),
        "--noinput",
        "--username",
        username,
        "--email",
        "admin@example.com",
        "--use-bundled-install-rules",
        "--mode",
        "traditional",
        "--no-versioning",
        "--no-moderation",
        "--no-alias",
        "--no-stories",
        "--no-history",
    ]
    print(f"creating temporary django CMS site in {project_dir}", flush=True)
    subprocess.run(command, check=True)

    seed_script = Path(__file__).with_name("seed_screenshot_site.py")
    result = subprocess.run(
        [
            sys.executable,
            str(seed_script),
            str(project_dir),
            "--username",
            username,
            "--password",
            password,
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(f"Could not seed temporary site:\n{result.stdout.rstrip()}")
    for line in reversed(result.stdout.splitlines()):
        if line.startswith("PAGE_URL="):
            return line.removeprefix("PAGE_URL=")
    raise RuntimeError("The fixture seed did not report its page URL")


def _available_port() -> int:
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        return int(listener.getsockname()[1])


@contextmanager
def run_cms_server(project_dir: Path, page_url: str):
    """Run the generated development server until screenshot capture completes."""

    port = _available_port()
    base_url = f"http://127.0.0.1:{port}"
    log_path = project_dir / "runserver.log"
    with log_path.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "manage",
                "runserver",
                f"127.0.0.1:{port}",
                "--noreload",
            ],
            cwd=project_dir,
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            deadline = time.monotonic() + 30
            ready_url = resolve_url(base_url, page_url)
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    log.flush()
                    raise RuntimeError(
                        "Temporary django CMS server exited early:\n"
                        + log_path.read_text(encoding="utf-8")
                    )
                try:
                    with urlopen(ready_url, timeout=1):
                        break
                except HTTPError:
                    # An HTTP response proves that the development server is ready;
                    # Playwright will report a bad route more clearly if necessary.
                    break
                except URLError:
                    time.sleep(0.1)
            else:
                raise RuntimeError("Timed out waiting for temporary django CMS server")
            print(f"temporary django CMS site ready at {ready_url}")
            yield base_url
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


def generate(
    config: Mapping[str, Any],
    config_path: Path,
    screenshots: Sequence[Mapping[str, Any]],
    *,
    headed: bool,
    fail_fast: bool,
) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "error: Playwright is not installed; run `make screenshots-install` first",
            file=sys.stderr,
        )
        return 2

    browser_config = dict(config.get("browser", {}))
    base_url = str(config["base_url"])
    output_dir = Path(str(config["output_dir"]))
    if not output_dir.is_absolute():
        output_dir = config_path.parent / output_dir
    output_dir = output_dir.resolve()

    browser_name = browser_config.pop("name", "chromium")
    viewport = browser_config.pop("viewport", {"width": 1440, "height": 1000})
    timeout = browser_config.pop("timeout", 10_000)
    navigation_timeout = browser_config.pop("navigation_timeout", 30_000)
    channel = browser_config.pop("channel", None)
    context_keys = BROWSER_SETTINGS - {
        "channel",
        "name",
        "navigation_timeout",
        "timeout",
        "viewport",
    }
    unknown = set(browser_config) - context_keys
    if unknown:
        raise ConfigurationError(
            f"Unknown browser setting(s): {', '.join(sorted(unknown))}"
        )
    context_options = {"viewport": viewport, **browser_config}
    failures: list[tuple[str, Exception]] = []

    with sync_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)
        launch_options: dict[str, Any] = {"headless": not headed}
        if channel:
            launch_options["channel"] = channel
        browser = browser_type.launch(**launch_options)
        context = browser.new_context(**context_options)
        page = context.new_page()
        page.set_default_timeout(timeout)
        page.set_default_navigation_timeout(navigation_timeout)
        try:
            run_actions(page, config.get("setup", []), base_url)
            for screenshot in screenshots:
                screenshot_id = str(screenshot["id"])
                try:
                    if screenshot.get("url"):
                        page.goto(resolve_url(base_url, str(screenshot["url"])))
                    run_actions(page, config.get("before_each", []), base_url)
                    run_actions(page, screenshot.get("actions", []), base_url)
                    target = capture_screenshot(page, screenshot, output_dir)
                    print(f"captured {screenshot_id}: {target}")
                # A bad selector, browser failure, or configuration error should be
                # attributed to this recipe while the remaining independent captures
                # can still run.
                except Exception as error:  # noqa: BLE001
                    failures.append((screenshot_id, error))
                    print(f"failed {screenshot_id}: {error}", file=sys.stderr)
                    if fail_fast:
                        break
        finally:
            context.close()
            browser.close()

    if failures:
        print(f"{len(failures)} screenshot(s) failed", file=sys.stderr)
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", type=Path, default=DEFAULT_CONFIG, help="YAML recipe to use"
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="GLOB",
        help="capture ids or output paths matching GLOB (repeatable)",
    )
    parser.add_argument(
        "--base-url", help="override base_url (useful for another CMS version)"
    )
    parser.add_argument("--output-dir", type=Path, help="override output_dir")
    parser.add_argument("--headed", action="store_true", help="show the browser")
    parser.add_argument("--list", action="store_true", help="list selected screenshots")
    parser.add_argument(
        "--dry-run", action="store_true", help="validate and show output paths only"
    )
    parser.add_argument(
        "--fail-fast", action="store_true", help="stop after the first failed capture"
    )
    parser.add_argument(
        "--temporary-site",
        action="store_true",
        help="create, seed, serve, and remove a temporary django CMS project",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    config_path = arguments.config.resolve()
    try:
        if arguments.temporary_site and arguments.base_url:
            raise ConfigurationError(
                "--temporary-site and --base-url cannot be used together"
            )
        if arguments.temporary_site:
            username = os.environ.get("DJANGOCMS_USERNAME") or TEMPORARY_USERNAME
            password = os.environ.get("DJANGOCMS_PASSWORD") or TEMPORARY_PASSWORD
            original_page_path = os.environ.get("DJANGOCMS_PAGE_PATH")
            os.environ["DJANGOCMS_USERNAME"] = username
            os.environ["DJANGOCMS_PASSWORD"] = password
            os.environ["DJANGOCMS_PAGE_PATH"] = TEMPORARY_PAGE_PATH

        config = load_config(
            config_path,
            allow_missing_environment=arguments.list or arguments.dry_run,
        )
        if arguments.base_url:
            config["base_url"] = arguments.base_url
        if arguments.output_dir:
            config["output_dir"] = str(arguments.output_dir.resolve())
        screenshots = selected_screenshots(
            config["screenshots"],
            arguments.only,
            include_disabled=arguments.list,
        )
        if not screenshots:
            raise ConfigurationError("No enabled screenshots matched the selection")

        output_dir = Path(str(config["output_dir"]))
        if not output_dir.is_absolute():
            output_dir = config_path.parent / output_dir
        if arguments.list or arguments.dry_run:
            for screenshot in screenshots:
                status = "disabled" if not screenshot.get("enabled", True) else "enabled"
                print(
                    f"{screenshot['id']}\t{status}\t"
                    f"{output_dir / str(screenshot['output'])}"
                )
            return 0
        if arguments.temporary_site:
            try:
                with tempfile.TemporaryDirectory(
                    prefix="djangocms-user-guide-"
                ) as temporary_root:
                    project_dir = Path(temporary_root) / "site"
                    page_url = create_cms_site(
                        project_dir,
                        username=username,
                        password=password,
                    )
                    with run_cms_server(project_dir, page_url) as base_url:
                        config["base_url"] = base_url
                        return generate(
                            config,
                            config_path,
                            screenshots,
                            headed=arguments.headed,
                            fail_fast=arguments.fail_fast,
                        )
            finally:
                if original_page_path is None:
                    os.environ.pop("DJANGOCMS_PAGE_PATH", None)
                else:
                    os.environ["DJANGOCMS_PAGE_PATH"] = original_page_path
        return generate(
            config,
            config_path,
            screenshots,
            headed=arguments.headed,
            fail_fast=arguments.fail_fast,
        )
    except ConfigurationError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    # Browser launch, navigation, and one-time setup failures are operational
    # errors; report them without exposing an implementation traceback.
    except Exception as error:  # noqa: BLE001
        print(f"error: screenshot session failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
