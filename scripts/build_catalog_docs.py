#!/usr/bin/env python3
"""Build the complete Markdown inventory; README stays an editorial guide."""

from collections import Counter
import html
import json
from pathlib import Path

from build_site import CATEGORY_LABELS

ROOT = Path(__file__).resolve().parents[1]


def build():
    catalog = json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))
    counts = Counter(entry['category'] for entry in catalog['entries'])
    lines = [
        '# Agent benchmark catalog', '',
        '[Selection guide](../README.md) · [Search and filter online](https://zeredy879.github.io/awesome-agent-harness-benchmarks/) · [JSON](../data/catalog.json)', '',
        f"{len(catalog['entries'])} resources across {len(counts)} areas. Source snapshot: {catalog['as_of']}.", '',
        'Generated from the canonical inventory. Resource types describe what a project provides, not its quality or independent verification. Every record includes a limitation.', '',
        '## Contents', '',
    ]
    for category, label in CATEGORY_LABELS.items():
        if counts[category]:
            lines.append(f'- [{label}](#{category}) ({counts[category]})')
    for category, label in CATEGORY_LABELS.items():
        if not counts[category]:
            continue
        lines.extend(['', f'<a id="{html.escape(category)}"></a>', '', f'## {label}', ''])
        for entry in sorted((e for e in catalog['entries'] if e['category'] == category), key=lambda e: e['name'].casefold()):
            for anchor in [entry['id'], *entry.get('aliases', [])]:
                lines.extend([f'<a id="{html.escape(anchor)}"></a>', ''])
            lines.extend([
                f"### [{entry['name']}]({entry['url']})", '',
                f"**{entry['kind']}** · ID: `{entry['id']}`", '',
                entry['summary'], '',
                f"- Measures: {', '.join(entry['signals'])}.",
                f"- Grading: {entry['grading']}",
                f"- Environment: {entry['environment']}",
                f"- Limitation: {entry['limitation']}",
            ])
            if entry.get('paper'):
                lines.append(f"- [Paper / technical report]({entry['paper']})")
            if entry.get('aliases'):
                lines.append('- Former record IDs: ' + ', '.join(f'`{alias}`' for alias in entry['aliases']))
            lines.append('')
    (ROOT / 'docs/catalog.md').write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')


if __name__ == '__main__':
    build()
