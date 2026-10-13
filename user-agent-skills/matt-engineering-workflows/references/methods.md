# Focused Engineering Methods

## Diagnosis

Choose a feedback loop at the interface where the user's failure happens: a focused test, request replay, CLI fixture, browser assertion or timing harness. Run it before concluding the cause. Confirm that it catches the stated symptom rather than merely successful execution. Minimize one dimension at a time. For intermittent bugs, preserve seeds/timestamps and report observation counts rather than asserting determinism.

Rank falsifiable hypotheses and change one variable per experiment. Inspect debuggers, traces or targeted logs; redact secrets from captured artifacts. For slowness, record baseline conditions and compare equivalent workloads. Remove temporary instrumentation, run the original scenario and record remaining uncertainty. When reproduction is unavailable, explain hypotheses as hypotheses; do not fabricate a successful red/green run.

## TDD

Test behavior through the existing public interface. The expected result comes from requirements, a worked example or known-good fixture, not the algorithm under test. Add one failing behavior and the smallest implementation to satisfy it. Continue in vertical slices. Avoid mocks that replace the behavior being tested and snapshots that simply reproduce the current bug. Refactor only when justified within the requested scope, then rerun applicable checks.

## Module Design

Compare what callers must know with the complexity hidden by the module. Prefer interfaces that concentrate real variation, failure handling and maintenance. A wrapper which merely moves complexity to more layers is not automatically an improvement. Identify actual alternate dependencies before inventing adapters. Preserve project vocabulary and side-effect contracts; not every function must be pure or every private helper directly tested.

## Specification And Handoff

Record problem, requested outcome, non-goals, constraints, observable acceptance criteria, dependencies and unanswered questions. Small independently verifiable slices are preferable to a long speculative task list. Keep evidence paths and commands in a handoff when another engineer must resume. Do not turn draft specifications into external tickets without authorization.

## Triage

For the explicitly requested tracker scope, distinguish bugs from enhancements and unverified reports from reproduced problems. Map readiness to the project's actual label conventions rather than creating a new label taxonomy automatically. For external PRs, inspect both the requested behavior and attached code. Ambiguous ownership or conflicting labels are unresolved facts, not permission to merge. If authorized to post an AI-prepared brief, identify it clearly and exclude secrets.

Source modules reviewed: diagnosing-bugs, tdd, codebase-design, research, triage and productivity/grilling. Upstream's rigid terminology, mandatory background agents, setup requirements and extra approval gates are intentionally not inherited.
