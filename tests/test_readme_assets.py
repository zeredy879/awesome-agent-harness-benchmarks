from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class ReadmeImages(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.sources = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "img":
            self.images.append(attributes)
        elif tag == "source":
            self.sources.append(attributes)


class ReadmeAssetTests(unittest.TestCase):
    def test_readme_picture_assets_resolve_and_have_fallback_text(self):
        for readme in ROOT.glob("README*.md"):
            with self.subTest(readme=readme.name):
                parser = ReadmeImages()
                parser.feed(readme.read_text(encoding="utf-8"))
                self.assertTrue(parser.images, "A picture needs a fallback image")
                self.assertTrue(parser.sources, "A picture needs a theme source")
                for image in parser.images:
                    self.assertTrue(image.get("alt", "").strip())
                    self.assertNotIn("height", image, "Keep the cover responsive")
                for asset in [i["src"] for i in parser.images] + [s["srcset"] for s in parser.sources]:
                    self.assertFalse(urlsplit(asset).scheme, "Keep cover assets local")
                    self.assertTrue((readme.parent / asset).is_file(), asset)

    def test_svg_covers_are_accessible_and_self_contained(self):
        for asset in (ROOT / "assets").glob("readme-hero-*.svg"):
            with self.subTest(asset=asset.name):
                root = ET.parse(asset).getroot()
                self.assertEqual(root.attrib.get("role"), "img")
                ids = {node.attrib.get("id"): node for node in root.iter()}
                labels = root.attrib.get("aria-labelledby", "").split()
                self.assertTrue(labels)
                for label in labels:
                    self.assertTrue(ids[label].text.strip())
                for node in root.iter():
                    self.assertNotIn(node.tag.split("}")[-1], {"script", "foreignObject", "image"})
                    for name in node.attrib:
                        self.assertFalse(name.lower().startswith("on"))
                        self.assertFalse(name.endswith("href"))


if __name__ == "__main__":
    unittest.main()
