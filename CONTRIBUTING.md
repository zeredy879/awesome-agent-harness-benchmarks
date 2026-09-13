# Contributing

Thanks for improving the catalog.

Before opening a pull request, check that the item is specifically useful for evaluating an agent harness or one of its execution responsibilities. Include the canonical paper, project, or benchmark URL; the task and environment scope; the evaluator or verifier; the capability tags; and one limitation that affects interpretation.

Please use the entry schema in `data/catalog.json`. Keep the README entry concise and factual. Do not copy leaderboard numbers without a link to the original run or release, and do not turn a planned benchmark into a measured result. If a repository is inaccessible, record `needs-review` in the audit instead of silently dropping the item.

For comparisons, state which variables are fixed. The preferred design is a paired comparison: same model endpoint, prompt, tools, task snapshot, sandbox, budget, timeout and seed; harness is the treatment. Report multiple trials and retain raw traces or a reproducible pointer to them.

Run the local checks before submitting:

```bash
python3 scripts/validate_catalog.py
python3 scripts/research_sources.py --catalog --audit
```

