import struct
import tempfile
import unittest
import zlib
from pathlib import Path

from scripts.fit_odt_images import fit


def write_png(path: Path, width: int, height: int):
    """Write a minimal, valid PNG of the given size."""

    def chunk(kind: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + kind
            + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        )

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", header)
        + chunk(b"IDAT", zlib.compress(b"\x00" * (width * 3 + 1) * height))
        + chunk(b"IEND", b"")
    )


class FitTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_constrains_image_that_has_no_dimensions(self):
        write_png(self.base / "wide.png", 2000, 500)
        html, resized, _ = fit('<img src="wide.png" />', self.base, 600)

        self.assertEqual(resized, 1)
        self.assertIn('width="600"', html)
        self.assertIn('height="150"', html)  # aspect ratio preserved

    def test_scales_down_dimensions_declared_on_the_tag(self):
        # Sphinx writes width/height attributes for ":scale:" images.
        html, resized, _ = fit(
            '<img src="x.png" width="800" height="400" />', self.base, 600
        )

        self.assertEqual(resized, 1)
        self.assertIn('width="600"', html)
        self.assertIn('height="300"', html)

    def test_leaves_images_that_already_fit(self):
        write_png(self.base / "small.png", 300, 200)
        source = '<img alt="small" src="small.png" />'
        html, resized, _ = fit(source, self.base, 600)

        self.assertEqual(resized, 0)
        self.assertEqual(html, source)

    def test_leaves_percentage_widths_to_pandoc(self):
        source = '<img src="missing.png" width="50%" />'
        html, resized, skipped = fit(source, self.base, 600)

        self.assertEqual((resized, skipped), (0, 1))
        self.assertEqual(html, source)

    def test_ignores_remote_images(self):
        source = '<img src="https://example.com/banner.png" />'
        html, resized, skipped = fit(source, self.base, 600)

        self.assertEqual((resized, skipped), (0, 1))
        self.assertEqual(html, source)

    def test_keeps_the_tag_self_closing_and_other_attributes(self):
        write_png(self.base / "wide.png", 1200, 600)
        html, _, _ = fit('<img alt="A toolbar" src="wide.png" />', self.base, 600)

        self.assertTrue(html.endswith("/>"), html)
        self.assertIn('alt="A toolbar"', html)

    def test_is_idempotent(self):
        write_png(self.base / "wide.png", 2000, 500)
        once, _, _ = fit('<img src="wide.png" />', self.base, 600)
        twice, resized, _ = fit(once, self.base, 600)

        self.assertEqual(once, twice)
        self.assertEqual(resized, 0)


if __name__ == "__main__":
    unittest.main()
