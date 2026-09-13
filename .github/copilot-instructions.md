# Agent Harness Benchmarks maintenance

The canonical inventory is `data/catalog.json`; `data/catalog.schema.json` defines its shape. `data/source-audit.json` is a point-in-time GitHub metadata audit and is not an independent reproduction of benchmark claims.

For catalog changes, preserve stable IDs, cite canonical sources, record the evaluator and environment, and state limitations. Run:

```bash
python scripts/validate_catalog.py
python scripts/research_sources.py --catalog --audit
python scripts/build_site.py
```

The Pages site is generated from the catalog and exposes `agent.md`, `index.md`, `catalog.json`, `research.md`, `source-audit.json`, and `llms.txt` for machine consumption.
