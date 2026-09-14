#!/usr/bin/env python3
"""Dependency-free integrity checks for the benchmark catalog."""

from __future__ import annotations

import json
import pathlib
import re
import sys
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = {
    "id", "name", "category", "kind", "url", "summary", "signals",
    "grading", "environment", "limitation",
}
KINDS = {"benchmark", "study", "watchlist", "infrastructure"}


def _source_key(url: str, redirects: dict[str, str]) -> str:
    """Normalize a source URL, resolving GitHub owner/repo redirects from audit data."""
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower()
    path = parsed.path.strip("/")
    if host == "github.com":
        parts = path.split("/")
        if len(parts) >= 2:
            requested = f"{parts[0]}/{parts[1]}".lower()
            resolved = redirects.get(requested, requested).lower()
            suffix = "/".join(parts[2:])
            return f"github:{resolved}{('/' + suffix.lower()) if suffix else ''}"
    return f"url:{host}{('/' + path).rstrip('/').lower()}?{parsed.query}"


def validate_catalog(catalog: dict, audit: dict | None = None) -> list[str]:
    entries = catalog.get("entries", [])
    errors: list[str] = []
    entry_ids: set[str] = set()
    alias_owners: dict[str, str] = {}
    sources: dict[str, str] = {}
    redirects: dict[str, str] = {}
    if audit:
        for record in audit.get("repositories", []):
            requested = record.get("requested_repo")
            resolved = record.get("repo")
            if requested and resolved:
                redirects[requested.strip("/").lower()] = resolved.strip("/").lower()

    for index, entry in enumerate(entries):
        missing = REQUIRED - entry.keys()
        if missing:
            errors.append(f"entry {index}: missing {sorted(missing)}")
            continue
        entry_id = entry.get("id", "")
        if entry_id in entry_ids:
            errors.append(f"duplicate id: {entry_id}")
        entry_ids.add(entry_id)
        if not re.match(r"^[a-z0-9][a-z0-9-]*$", entry_id):
            errors.append(f"{entry_id}: invalid id")
        if entry.get("kind") not in KINDS:
            errors.append(f"{entry_id}: invalid kind")
        if not re.match(r"^https?://", entry.get("url", "")):
            errors.append(f"{entry_id}: invalid URL")
        if not entry.get("signals"):
            errors.append(f"{entry_id}: no capability tags")
        if "aliases" in entry:
            alias_values = entry["aliases"]
            aliases_are_strings = isinstance(alias_values, list) and all(
                isinstance(alias, str) for alias in alias_values
            )
            if not aliases_are_strings or len(alias_values) != len(set(alias_values)):
                errors.append(f"{entry_id}: aliases must be unique")
            for alias in alias_values if isinstance(alias_values, list) else []:
                if not isinstance(alias, str) or not re.match(r"^[a-z0-9][a-z0-9-]*$", alias):
                    errors.append(f"{entry_id}: invalid alias {alias!r}")
                if alias in alias_owners and alias_owners[alias] != entry_id:
                    errors.append(f"duplicate alias: {alias}")
                alias_owners[alias] = entry_id
        source_key = _source_key(entry.get("url", ""), redirects)
        previous = sources.get(source_key)
        if previous and previous != entry_id:
            errors.append(f"duplicate canonical source: {entry_id} and {previous} -> {source_key}")
        sources[source_key] = entry_id

    for alias, owner in alias_owners.items():
        if alias in entry_ids and alias != owner:
            errors.append(f"{owner}: alias collides with id: {alias}")
    if catalog.get("as_of") != "2026-09-13":
        errors.append("catalog as_of must be updated explicitly")
    if len(entries) < 50:
        errors.append("catalog unexpectedly contains fewer than 50 entries")
    return errors


def main() -> int:
    catalog = json.loads((ROOT / "data/catalog.json").read_text(encoding="utf-8"))
    audit = json.loads((ROOT / "data/source-audit.json").read_text(encoding="utf-8"))
    errors = validate_catalog(catalog, audit)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"catalog valid: {len(catalog['entries'])} entries, {len({e['category'] for e in catalog['entries']})} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
