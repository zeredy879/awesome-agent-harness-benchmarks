import unittest

from scripts.validate_catalog import validate_catalog


def entry(entry_id, url, aliases=None):
    item = {
        "id": entry_id,
        "name": entry_id,
        "category": "tools",
        "kind": "benchmark",
        "url": url,
        "summary": "A test benchmark entry.",
        "signals": ["tools"],
        "grading": "Executable checks",
        "environment": "Test sandbox",
        "limitation": "Synthetic test record only.",
    }
    if aliases is not None:
        item["aliases"] = aliases
    return item


def catalog(entries):
    return {"schema_version": 1, "as_of": "2026-09-13", "scope": "test", "entries": entries + [
        entry(f"filler-{i}", f"https://example.com/filler-{i}") for i in range(50)
    ]}


class CatalogIntegrityTests(unittest.TestCase):
    def test_redirected_github_repositories_cannot_be_counted_twice(self):
        audit = {"repositories": [
            {"requested_repo": "openclaw/clawbench", "repo": "openclaw/shellbench"},
            {"requested_repo": "openclaw/shellbench", "repo": "openclaw/shellbench"},
        ]}
        errors = validate_catalog(catalog([
            entry("old", "https://github.com/openclaw/clawbench"),
            entry("new", "https://github.com/openclaw/shellbench"),
        ]), audit)
        self.assertTrue(any("duplicate canonical source" in error for error in errors))

    def test_alias_cannot_collide_with_another_id(self):
        errors = validate_catalog(catalog([
            entry("retained", "https://example.com/retained", ["retired"]),
            entry("retired", "https://example.com/other"),
        ]))
        self.assertTrue(any("alias collides with id" in error for error in errors))

    def test_retained_id_with_alias_is_valid(self):
        errors = validate_catalog(catalog([
            entry("retained", "https://example.com/retained", ["retired"]),
        ]))
        self.assertFalse([error for error in errors if "alias" in error or "duplicate" in error])


if __name__ == "__main__":
    unittest.main()
