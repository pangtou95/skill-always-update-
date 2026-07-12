# Skills GitHub Export

Export created on 2026-06-01 from local Codex/agent skill directories.

## Contents

- `codex-skills/` - contents from `~/.codex/skills`
- `user-agent-skills/` - contents from `~/.agents/skills`
- `project-agent-skills/` - contents from this project's `.agents/skills`
- `SKILLS_MANIFEST.txt` - generated list of all `SKILL.md` files in this export

Symlinks were dereferenced during export, so linked skills such as Orchestra AI Research skills are copied as real directories instead of broken links.

## Counts

- Total `SKILL.md` files found after export: 552
- Export size before compression: about 234 MB

## Notes Before Publishing

Some skills may come from third-party repositories or installed packages. Check upstream licenses before making the GitHub repository public.

To install a skill manually into Codex, copy a skill directory into:

```bash
~/.codex/skills/
```

Then restart Codex so the new skill list is refreshed.

## Curated additions

- `codex-skills/seedance-director-compat` — first-frame-first directing, reference-role mapping, audio sidecars, sequence continuity, and prompt-only Seedance compatibility with WAN/LTX fallbacks. This is a reduced MIT-compatible integration informed by `Emily2040/seedance-2.0`; it does not require a connected Seedance model.
