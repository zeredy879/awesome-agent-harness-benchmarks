# Catalog data

`catalog.json` is the source of truth for the inventory. The stable `id` is the key used by downstream tooling. `category` describes the main harness responsibility made visible by the workload, while `kind` distinguishes a task benchmark from a study, watchlist item, or runner/environment layer. `signals` is a set of capability tags. `grading`, `environment`, and `limitation` explain how to interpret the evidence.

The 2026-09-13 snapshot contains 116 entries across 13 categories. New or fast-moving projects are included only when a public task/evaluator, maintained source, or clearly documented study is available; a dated snapshot is not a claim of universal completeness.

`source-audit.json` is a point-in-time availability audit for the GitHub repositories referenced by the catalog. It records repository metadata and a SHA-256 hash of each README blob. It does not claim that the benchmark was independently reproduced and it never includes benchmark answers or credentials.

The JSON structure is described by [`catalog.schema.json`](catalog.schema.json). Run `python3 scripts/validate_catalog.py` after editing the catalog.
