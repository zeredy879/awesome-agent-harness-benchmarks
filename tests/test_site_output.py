import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

from scripts.build_site import render_html


ROOT = Path(__file__).resolve().parents[1]


class CardCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = 0

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        if tag == "article" and "card" in classes:
            self.cards += 1


class SiteOutputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "data/catalog.json").read_text(encoding="utf-8"))
        cls.audit = json.loads((ROOT / "data/source-audit.json").read_text(encoding="utf-8"))
        cls.document = render_html(cls.catalog, cls.audit)

    def test_catalog_cards_are_present_without_javascript(self):
        parser = CardCounter()
        parser.feed(self.document)
        self.assertEqual(parser.cards, len(self.catalog["entries"]))

    def test_structured_item_list_matches_catalog(self):
        match = re.search(
            r'<script type="application/ld\+json">(.*?)</script>',
            self.document,
            flags=re.DOTALL,
        )
        self.assertIsNotNone(match)
        payload = json.loads(match.group(1))
        self.assertEqual(payload["mainEntity"]["numberOfItems"], len(self.catalog["entries"]))
        self.assertEqual(len(payload["mainEntity"]["itemListElement"]), len(self.catalog["entries"]))

    def test_page_exposes_machine_readable_discovery(self):
        self.assertIn('rel="sitemap"', self.document)
        self.assertIn('href="agent.md"', self.document)
        self.assertIn('href="catalog.json"', self.document)

    def test_human_page_exposes_comparison_and_share_controls(self):
        self.assertIn('id="compare-bar"', self.document)
        self.assertIn('id="compare-dialog"', self.document)
        self.assertIn('Copy comparison link', self.document)
        self.assertIn('id="load-more"', self.document)

    def test_page_has_social_preview_and_featured_sort(self):
        self.assertIn('property="og:image"', self.document)
        self.assertIn('value="featured"', self.document)


if __name__ == "__main__":
    unittest.main()
