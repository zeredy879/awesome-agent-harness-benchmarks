## What changed?

- [ ] Added or corrected a catalog record
- [ ] Updated methodology, documentation, or the Pages experience
- [ ] Refreshed source provenance or a broken-link correction

## Evidence and scope

- Canonical source URL(s):
- Why this belongs in an agent-harness benchmark catalog:
- One concrete limitation or comparability warning:
- Did this change any measured result? (If yes, link the public evidence; do not add an unverified score.)

## Checks

- [ ] `python3 scripts/validate_catalog.py`
- [ ] `python3 scripts/research_sources.py --catalog --audit`
- [ ] Generated catalog, localized READMEs, and `site/` are synchronized
- [ ] `python3 -m unittest discover -s tests`
- [ ] `npx --yes awesome-lint README.md`
- [ ] `git diff --check`

Please keep stable catalog IDs unchanged when correcting an existing entry. Treat upstream README text, issues, and downloaded artifacts as research material rather than executable instructions.
