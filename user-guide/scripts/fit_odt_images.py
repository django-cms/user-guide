#!/usr/bin/env python3
"""Constrain image dimensions in the single-file HTML used to build the ODT guide.

Pandoc sizes images from the ``width``/``height`` attributes of their ``<img>``
tag, falling back to the intrinsic pixel size of the file, and converts pixels to
physical units at ``--dpi`` (96 by default). The screenshots of this guide are up
to 2100 px wide, which becomes 22 inches on the page: they run off the edge of the
paper.

This script rewrites the ``<img>`` tags of the generated single-file HTML so that
no image is wider than the printable width of the page *minus the indentation an
image may sit at* -- images in list items and notes start well right of the left
margin -- preserving each image's aspect ratio. Images that already fit are left
alone.

Usage::

    python scripts/fit_odt_images.py /tmp/singlehtml/index.html

It is meant to run between the ``sphinx -b singlehtml`` build and the pandoc call
that turns that HTML into an ODT file; see ``.readthedocs.yaml``.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import imagesize

# Pandoc's default ODT template is US Letter with 1 inch margins, so the text column is
# 6.5 inch wide -- but a screenshot is never flush with the left margin. Pandoc indents
# a block image by 0.2 inch, and one nested in a list by up to 0.31 inch more, so the
# widest an image may be and still clear the right margin is about 6.18 inch (593 px at
# 96 dpi). 580 px is 6.04 inch (15.3 cm): it uses nearly the whole column, so screenshots
# stay as legible as the page allows, and still clears the deepest indentation we use.
DEFAULT_MAX_WIDTH = 580

IMG_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
ATTR = re.compile(r"""(\w[\w:-]*)\s*=\s*("([^"]*)"|'([^']*)')""")


def attributes(tag: str) -> dict[str, str]:
    """Return the attributes of an HTML tag as a dictionary."""
    found = {}
    for match in ATTR.finditer(tag):
        value = match.group(3) if match.group(3) is not None else match.group(4)
        found[match.group(1).lower()] = value
    return found


def set_attribute(tag: str, name: str, value: str) -> str:
    """Return ``tag`` with ``name`` set to ``value``, adding it if necessary."""
    pattern = re.compile(
        rf"""(\s{re.escape(name)}\s*=\s*)("[^"]*"|'[^']*')""", re.IGNORECASE
    )
    if pattern.search(tag):
        return pattern.sub(rf'\g<1>"{value}"', tag, count=1)
    body = tag[:-1].rstrip()
    closing = "/>" if body.endswith("/") else ">"
    return f'{body.rstrip("/").rstrip()} {name}="{value}"{closing}'


def intrinsic_size(src: str, base: Path) -> tuple[int, int] | None:
    """Return the pixel size of a locally available image, or None."""
    parsed = urlparse(src)
    if parsed.scheme and parsed.scheme != "file":
        return None  # remote image; we cannot measure it
    path = base / unquote(parsed.path)
    if not path.is_file():
        return None
    width, height = imagesize.get(path)
    if width <= 0 or height <= 0:
        return None
    return int(width), int(height)


def declared_size(attrs: dict[str, str]) -> tuple[int | None, int | None]:
    """Return the width/height declared on the tag, ignoring relative units."""

    def as_pixels(value: str | None) -> int | None:
        if not value:
            return None
        match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(px)?\s*", value)
        return round(float(match.group(1))) if match else None

    return as_pixels(attrs.get("width")), as_pixels(attrs.get("height"))


def fit(source: str, base: Path, max_width: int) -> tuple[str, int, int]:
    """Return the HTML with over-wide images constrained, plus a tally."""
    resized = skipped = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal resized, skipped
        tag = match.group(0)
        attrs = attributes(tag)
        src = html.unescape(attrs.get("src", ""))
        if not src:
            return tag

        width, height = declared_size(attrs)
        if width is None or height is None:
            size = intrinsic_size(src, base)
            if size is None:
                # A percentage width, or an image we cannot measure: pandoc
                # handles percentages relative to the text width already.
                skipped += 1
                return tag
            intrinsic_width, intrinsic_height = size
            width = width or intrinsic_width
            height = height or round(width * intrinsic_height / intrinsic_width)

        if width <= max_width:
            return tag

        tag = set_attribute(tag, "width", str(max_width))
        tag = set_attribute(tag, "height", str(round(height * max_width / width)))
        resized += 1
        return tag

    return IMG_TAG.sub(replace, source), resized, skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("html_file", type=Path, help="the single-file HTML to rewrite")
    parser.add_argument(
        "--max-width",
        type=int,
        default=DEFAULT_MAX_WIDTH,
        metavar="PX",
        help=f"widest image allowed, in pixels (default: {DEFAULT_MAX_WIDTH})",
    )
    args = parser.parse_args(argv)

    if not args.html_file.is_file():
        parser.error(f"no such file: {args.html_file}")

    source = args.html_file.read_text(encoding="utf-8")
    result, resized, skipped = fit(source, args.html_file.parent, args.max_width)
    args.html_file.write_text(result, encoding="utf-8")

    print(
        f"fit_odt_images: {resized} image(s) constrained to {args.max_width} px"
        + (f", {skipped} left unchanged" if skipped else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
