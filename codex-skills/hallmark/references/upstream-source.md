# Upstream Source

- Repository: https://github.com/nutlope/hallmark
- Version: `1.1.0`
- Commit: `aeb42fb354ff4efa36ab475773a082315a3af2ce`
- Commit date: 2026-06-04
- Inspection date: 2026-07-22
- License: MIT; see `../LICENSE`

## Codex Packaging Changes

- Removed the nonstandard `version` frontmatter field so Codex's Skill validator accepts the package.
- Added `agents/openai.yaml` for Codex UI discovery.
- Bundled the upstream 20-theme token catalog as `catalog-tokens.css` because the upstream npm `files` list exports only `skills/`, while the Skill links to `site/css/tokens.css` outside that directory.
- Bundled the two upstream worked-example documents referenced by `SKILL.md`.
- Repointed optional example links to their public upstream GitHub locations.

No Hallmark executable or paid API is required for the instruction Skill itself. External image generation, browsing, fonts, or hosted model calls may still have their own availability and cost rules.
