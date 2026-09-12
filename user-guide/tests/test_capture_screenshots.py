import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts.capture_screenshots import (
    ConfigurationError,
    capture_screenshot,
    expand_environment,
    resolve_url,
    run_action,
    selected_screenshots,
    validate_config,
)


def valid_config():
    return {
        "version": 1,
        "base_url": "http://localhost:8000",
        "output_dir": "source",
        "screenshots": [
            {"id": "toolbar", "output": "tutorial/images/toolbar.png"}
        ],
    }


class EnvironmentExpansionTests(unittest.TestCase):
    def test_expands_values_and_defaults_recursively(self):
        with patch.dict(os.environ, {"CMS_HOST": "cms.test"}, clear=True):
            value = expand_environment(
                {"url": "https://${CMS_HOST}/${LANGUAGE:-en}", "items": ["${PORT:-8000}"]}
            )

        self.assertEqual(value, {"url": "https://cms.test/en", "items": ["8000"]})

    def test_missing_required_variable_is_an_error(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            self.assertRaisesRegex(ConfigurationError, "CMS_PASSWORD"),
        ):
            expand_environment("${CMS_PASSWORD}")

    def test_can_preserve_missing_variables_for_a_dry_run(self):
        with patch.dict(os.environ, {}, clear=True):
            value = expand_environment("${CMS_PASSWORD}", allow_missing=True)

        self.assertEqual(value, "${CMS_PASSWORD}")


class ValidationTests(unittest.TestCase):
    def test_accepts_minimal_configuration(self):
        validate_config(valid_config())

    def test_rejects_output_outside_output_directory(self):
        config = valid_config()
        config["screenshots"][0]["output"] = "../private.png"

        with self.assertRaisesRegex(ConfigurationError, "inside output_dir"):
            validate_config(config)

    def test_rejects_unknown_action_before_browser_starts(self):
        config = valid_config()
        config["screenshots"][0]["actions"] = [{"launch_missiles": True}]

        with self.assertRaisesRegex(ConfigurationError, "Unsupported action"):
            validate_config(config)


class SelectionTests(unittest.TestCase):
    def test_skips_disabled_and_matches_id_or_output(self):
        screenshots = [
            {"id": "toolbar-overview", "output": "tutorial/images/02-toolbar.jpg"},
            {
                "id": "project-menu",
                "output": "tutorial/images/02-project.jpg",
                "enabled": False,
            },
            {"id": "version-menu", "output": "tutorial/images/08-version.jpg"},
        ]

        selected = selected_screenshots(screenshots, ["toolbar-*", "*/08-*"])

        self.assertEqual([item["id"] for item in selected], ["toolbar-overview", "version-menu"])

    def test_can_include_disabled_items_when_listing(self):
        screenshots = [
            {"id": "ready", "output": "ready.png"},
            {"id": "template", "output": "template.png", "enabled": False},
        ]

        selected = selected_screenshots(screenshots, [], include_disabled=True)

        self.assertEqual([item["id"] for item in selected], ["ready", "template"])

    def test_resolves_relative_and_root_urls(self):
        base = "https://example.com/cms/"

        self.assertEqual(resolve_url(base, "en/"), "https://example.com/cms/en/")
        self.assertEqual(resolve_url(base, "/admin/"), "https://example.com/admin/")


class BrowserActionTests(unittest.TestCase):
    def test_fill_can_target_an_element_in_a_frame(self):
        page = MagicMock()
        locator = page.frame_locator.return_value.locator.return_value

        run_action(
            page,
            {
                "fill": {
                    "frame": "iframe.editor",
                    "selector": "input[name=title]",
                    "value": "Welcome",
                }
            },
            "http://localhost:8000",
        )

        page.frame_locator.assert_called_once_with("iframe.editor")
        locator.fill.assert_called_once_with("Welcome")

    def test_select_option_accepts_a_label(self):
        page = MagicMock()
        locator = page.locator.return_value

        run_action(
            page,
            {"select_option": {"selector": "select", "label": "English"}},
            "http://localhost:8000",
        )

        locator.select_option.assert_called_once_with(label="English")


class CaptureTests(unittest.TestCase):
    def test_successful_capture_atomically_replaces_existing_image(self):
        page = MagicMock()

        def write_capture(*, path, **options):
            Path(path).write_bytes(b"new screenshot")

        page.screenshot.side_effect = write_capture
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            target = output_dir / "images" / "toolbar.png"
            target.parent.mkdir()
            target.write_bytes(b"old screenshot")

            result = capture_screenshot(
                page,
                {"id": "toolbar", "output": "images/toolbar.png"},
                output_dir,
            )

            self.assertEqual(result, target.resolve())
            self.assertEqual(target.read_bytes(), b"new screenshot")
            self.assertEqual(list(target.parent.glob(".*.tmp.png")), [])

    def test_failed_capture_preserves_existing_image(self):
        page = MagicMock()
        page.screenshot.side_effect = RuntimeError("browser closed")
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            target = output_dir / "toolbar.png"
            target.write_bytes(b"old screenshot")

            with self.assertRaisesRegex(RuntimeError, "browser closed"):
                capture_screenshot(
                    page,
                    {"id": "toolbar", "output": "toolbar.png"},
                    output_dir,
                )

            self.assertEqual(target.read_bytes(), b"old screenshot")


if __name__ == "__main__":
    unittest.main()
