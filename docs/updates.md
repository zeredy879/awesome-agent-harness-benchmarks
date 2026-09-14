# Catalog updates

This log records material changes to selection guidance and source records. Automated availability checks are recorded separately in the [source audit](../data/source-audit.json).

## September 14, 2026

- Corrected a duplicate: OpenClaw ClawBench redirects to ShellBench. Both GitHub paths resolve to repository ID `1204210218`. The inventory now contains **115 resources**, including **97 benchmark records**, and **98 unique GitHub source paths**. The original record ID `clawbench-openclaw` remains stable; `shellbench` is retained in its `aliases` field.
- Removed the unsupported “broadest public direct comparison” claim for Harness-Bench. Native configuration comparisons and component ablations now have separate explanations.
- Clarified that benchmark, study, infrastructure, and watchlist are resource types, not evidence grades.
- Updated ToolSandbox's canonical repository owner and made LongMemEval's LLM judge explicit.
- Replaced the repeated homepage inventory with a selection guide, a complete generated Markdown catalog, and a reusable comparison report template. The website supports shareable filters and expandable environment/limitation details.
- Refined the public entry point after a zero-shot review: README selection tables became mobile-friendly lists, the Pages directory now opens with an editorial set of starting points, and readers can compare up to three records with a shareable URL.
- Added generated sitemap/robots metadata, social preview metadata, a citation file, a pull-request checklist, and CI checks that fail when Pages or localized exports drift from their generators.

These are corrections to the September 13 source snapshot, not a new comprehensive literature scan.

## September 13, 2026

Published the initial catalog, expanded the inventory across 13 areas, and added Chinese, Japanese, and Korean entry points, a searchable website, Markdown/JSON exports, and weekly GitHub availability checks. The initial 116-entry total included the renamed-project duplicate corrected above.

[Selection guide](../README.md) · [Full catalog](catalog.md)
