---
name: deeptutor-cli
description: Operate HKUDS DeepTutor from Codex for installation checks, provider setup, learning chat, deep solving, quizzes, deep research, visualization, knowledge bases, notebooks, sessions, memory, partners, skills, API service, and the local Web app. Use when the user names DeepTutor or wants a document-grounded tutoring and research workflow through the deeptutor command.
---

# DeepTutor CLI

Use DeepTutor as an external learning and research runtime. This Skill teaches Codex how to inspect, configure, and invoke it; it does not pretend that the `deeptutor` executable, model credentials, embedding service, or search provider already exists.

Upstream basis: [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), release `1.5.2`, source commit `b728354863540466f5410bec3530eb55a9fe0edc` (2026-07-19).

## Start With A Preflight

Run:

```bash
python3 scripts/deeptutor_preflight.py --mode cli
```

Use `--mode web` when the user wants `deeptutor start`. Read the JSON result before installing or starting anything.

If the command is missing and installation is in scope:

1. Prefer an isolated tool environment: `uv tool install deeptutor==1.5.2`.
2. If `uv` is unavailable, use a dedicated virtual environment rather than modifying the system Python.
3. Run `deeptutor init --cli` for terminal-only use or `deeptutor init` for the Web app.
4. Let the user enter provider credentials in the interactive setup. Never echo, commit, or place API keys in command history on their behalf.

Do not install a package named `deeptutor-cli` from PyPI. As of the inspected release, the published package is `deeptutor`; the CLI-only package is a source-checkout subproject. See [references/compatibility.md](references/compatibility.md).

## Route The Task

| User intent | Route |
| --- | --- |
| Explain or tutor interactively | `deeptutor chat` |
| Solve a difficult problem | `deeptutor run deep_solve` |
| Generate practice questions | `deeptutor run deep_question` |
| Research a topic and synthesize evidence | `deeptutor run deep_research` |
| Build a chart or visual explanation | `deeptutor run visualize` |
| Produce a math animation | `deeptutor run math_animator` |
| Track a learning plan | `deeptutor run mastery_path` |
| Ground work in user documents | create/select a KB, then pass `--kb` and usually `--tool rag` |
| Preserve useful output | add Markdown to a notebook and record the returned IDs |
| Inspect or resume prior work | use `session list/show/open` |
| Run the local service | `serve` for API only; `start` for backend plus Web app |

Read [references/upstream-cli.md](references/upstream-cli.md) when exact flags, subcommands, or REPL slash commands are needed. It is the upstream command reference. Apply the corrected installation guidance in this file and `compatibility.md` when the upstream reference differs.

## Evidence-Grounded Learning Workflow

1. Inspect the input files, topic, desired depth, language, and output format.
2. Reuse a suitable existing knowledge base when possible. Do not create duplicate KBs blindly.
3. For new documents, create a clearly named KB and verify it with `kb info` before querying it.
4. Select only the tools needed for the task. Use `rag` for supplied documents, `paper_search` for academic discovery, and `web_search` only when current external information is needed.
5. Run one capability with explicit KBs, tools, language, and config. Prefer `--format json` when downstream automation needs structured output.
6. Separate source-grounded statements from model reasoning. Preserve citations or references emitted by DeepTutor.
7. Save durable results to a notebook only when the user wants them retained.
8. Report the command, session or notebook IDs, files created, and any provider limitations.

Example:

```bash
deeptutor kb create control-systems --doc ./chapter-1.pdf --doc ./chapter-2.pdf
deeptutor kb info control-systems
deeptutor run deep_question "State-space stability" --kb control-systems --tool rag --config num_questions=8 --language zh --format json
```

## Operational Guardrails

- Treat `kb delete`, `memory clear`, `session delete`, `skill remove`, and destructive notebook replacement as confirmation-required operations.
- Before `notebook replace-md`, display the target notebook and record IDs and preserve a backup when feasible.
- Do not pass untrusted external skills with `--allow-unverified` unless the user explicitly accepts the supply-chain risk after inspection.
- Do not expose a service on `0.0.0.0` by default. Prefer loopback and explain authentication and network exposure before widening the bind address.
- Do not disable TLS verification as a routine fix.
- Do not assume RAG is available merely because the CLI runs. Embeddings and indexing must be configured and KB health must be checked.
- Do not fabricate a successful answer when the provider, model, search, or embedding backend is unavailable. Return the failed command and the narrowest recovery action.
- When model-generated code execution is enabled, keep it inside DeepTutor's documented sandbox or runner boundaries.

## Execution Rules

- Run commands from the user's intended workspace so generated files and DeepTutor state land where expected.
- Use one-shot `deeptutor run ...` for repeatable automation and `deeptutor chat` for interactive tutoring.
- Reuse `--session` only when continuity is intentional; create a fresh session when the topic or evidence set changes substantially.
- Prefer explicit names over defaults for KBs, notebooks, partners, and sessions.
- For long operations, wait for completion or keep the process session alive; do not claim success from startup output alone.
- Verify outputs through `kb info`, `session show`, `notebook show`, service health, or the produced artifact itself.

## Resources

- [references/compatibility.md](references/compatibility.md): inspected version, install routes, prerequisites, and adaptation notes.
- [references/upstream-cli.md](references/upstream-cli.md): upstream CLI Skill text and complete command inventory.
- `scripts/deeptutor_preflight.py`: deterministic local readiness check for CLI or Web mode.
- [references/APACHE-2.0.txt](references/APACHE-2.0.txt): upstream license.
