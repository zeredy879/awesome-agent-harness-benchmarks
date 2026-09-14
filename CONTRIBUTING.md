# Contributing

Thanks for improving the catalog.

You can [suggest a benchmark](https://github.com/zeredy879/awesome-agent-harness-benchmarks/issues/new?template=benchmark.yml) or [report a correction](https://github.com/zeredy879/awesome-agent-harness-benchmarks/issues/new?template=correction.yml) with a source link and a few sentences. Preparing JSON or running an evaluation is not required to open an issue.

## Propose a catalog change

Before opening a pull request, check that the item is specifically useful for evaluating an agent harness or one of its execution responsibilities. Include the canonical paper, project, or benchmark URL; the task and environment scope; the evaluator or verifier; the capability tags; and one limitation that affects interpretation.

Please use the entry schema in `data/catalog.json`. Check existing names, URLs, and GitHub redirects for duplicates. If a project was renamed, retain the earlier stable ID and preserve retired IDs in `aliases`. Do not copy leaderboard numbers without a link to the original run or release, and do not turn a planned benchmark into a measured result. If a repository is inaccessible, record `needs-review` in the audit instead of silently dropping the item.

The full inventory is generated into `docs/catalog.md`; the root README is a short selection guide. Update its shortlist when the advice changes, and record material additions or corrections in `docs/updates.md`. Edit translated guidance in `scripts/build_localized_readmes.py` before regenerating the localized READMEs.

For comparisons, state the intervention and which variables are fixed. Native harness defaults may belong to the treatment; component ablations should change one feature. Report multiple trials and retain raw traces or a reproducible pointer to them. The [comparison template](docs/comparison-template.md) covers the information readers need.

Run the local checks before submitting:

```bash
python3 scripts/validate_catalog.py
python3 scripts/research_sources.py --catalog --audit
python3 scripts/build_catalog_docs.py
python3 scripts/build_localized_readmes.py
python3 scripts/build_site.py
python3 -m unittest discover -s tests
npx --yes awesome-lint README.md
git diff --check
```
