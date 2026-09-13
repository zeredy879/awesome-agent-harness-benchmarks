#!/usr/bin/env python3
"""Fast, dependency-free integrity checks for the catalog."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / 'data/catalog.json').read_text())
entries = catalog.get('entries', [])
required = {'id', 'name', 'category', 'kind', 'url', 'summary', 'signals', 'grading', 'environment', 'limitation'}
errors = []
ids = set()
for i, entry in enumerate(entries):
    missing = required - entry.keys()
    if missing:
        errors.append(f'entry {i}: missing {sorted(missing)}')
    if entry.get('id') in ids:
        errors.append(f'duplicate id: {entry.get("id")}')
    ids.add(entry.get('id'))
    if not re.match(r'^https?://', entry.get('url', '')):
        errors.append(f'{entry.get("id")}: invalid URL')
    if not entry.get('signals'):
        errors.append(f'{entry.get("id")}: no capability tags')
if catalog.get('as_of') != '2026-09-13':
    errors.append('catalog as_of must be updated explicitly')
if len(entries) < 50:
    errors.append('catalog unexpectedly contains fewer than 50 entries')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'catalog valid: {len(entries)} entries, {len({e["category"] for e in entries})} categories')
