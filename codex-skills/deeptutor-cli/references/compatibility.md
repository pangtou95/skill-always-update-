# DeepTutor Compatibility Notes

## Inspected Source

- Repository: https://github.com/HKUDS/DeepTutor
- Release: `1.5.2`
- Commit: `b728354863540466f5410bec3530eb55a9fe0edc`
- Commit date: 2026-07-19
- Inspection date: 2026-07-22
- License: Apache-2.0

## Packaging Facts

- The public PyPI package is `deeptutor`; version `1.5.2` was available at inspection time.
- The repository contains a CLI-only project at `packaging/deeptutor-cli`, but `deeptutor-cli` was not available as a public PyPI package at inspection time.
- Both the full package and the source CLI project expose the command `deeptutor`.
- Python `3.11+` is required.
- The full local Web app also requires Node.js `20+` on `PATH`.

## Recommended Install Routes

### Isolated full package

```bash
uv tool install deeptutor==1.5.2
deeptutor init
```

Use `deeptutor init --cli` when only terminal workflows are needed.

### Dedicated virtual environment

```bash
python3 -m venv .deeptutor-venv
source .deeptutor-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install deeptutor==1.5.2
deeptutor init --cli
```

### CLI-only from a trusted source checkout

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
```

Pin or inspect the source revision before installing from a checkout.

## Credential Boundary

`deeptutor init` configures model and optional embedding providers. Provider credentials belong in the DeepTutor runtime settings or supported authentication flow, never in this Skill repository. The `openai-codex` and `github-copilot` provider login commands are runtime authentication operations and may open interactive authorization.

## Adaptation Notes

The upstream root `SKILL.md` is included as `upstream-cli.md`. This Codex adaptation adds valid frontmatter, UI metadata, preflight checks, destructive-operation confirmation, network exposure guidance, and corrected public package instructions. It does not bundle DeepTutor's application source or claim that its external providers are free.
