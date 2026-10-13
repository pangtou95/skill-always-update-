---
name: matt-engineering-workflows
description: Apply Matt Pocock-inspired engineering methods to difficult bug diagnosis, behavior-driven TDD, module design, specification handoffs or issue triage. Use when the task needs a focused engineering workflow, not a replacement project framework.
---

# Composable Engineering Workflows

Original Codex distillation of [mattpocock/skills](https://github.com/mattpocock/skills). Select only the relevant mode in `references/methods.md`. This adapter does not install the upstream plugin, call a nonexistent Skill tool or require its setup documents.

- Bug or performance regression: build a symptom-specific feedback loop, minimize the repro, test ranked hypotheses and retain a regression test.
- Test-first implementation: one observable behavior, a failing test, minimal implementation, then the next behavior. Use independently justified expectations.
- Module design: evaluate caller complexity and meaningful dependency variation before adding interfaces or abstractions.
- Specification/handoff: specify outcomes, scope, acceptance evidence and dependency order; implementation plans are not permission to post or merge.
- Triage: separate classification, verification and readiness. Prepare tracker changes for the user's requested scope; do not contact reporters or mutate labels merely because the workflow mentions them.
- Decision interview: use the existing `$grill-me` when the user requests a stress-test. Ordinary coding work does not require an interview.

Keep the repository's naming, ADRs and test boundaries. Do not force a glossary, persistent notes or a new architecture for a small fix. Read available code to answer factual questions; use subagents only when the user or applicable instructions authorize them. Continue routine reversible work without extra approval gates. Stop at a genuine information/access blocker and describe the missing evidence.

Invocation: `$matt-engineering-workflows 用可复现的反馈循环诊断这个问题，再补能捕获同一问题的测试。`
