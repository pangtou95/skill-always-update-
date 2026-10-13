---
name: rea-analysis
description: Plan and operate REA (Reverse Engineer Anything) CLI or MCP investigations of authorized binaries, JavaScript/Electron apps, .NET assemblies and web behavior, with evidence-linked findings and provider readiness checks.
---

# REA Evidence-Based Analysis

Original adapter for [morluto/rea](https://github.com/morluto/rea). Read `references/operations.md` for setup and target-specific prerequisites. Skill installation alone does not register MCP, install REA or install Hopper/Ghidra/IDA.

1. Define the authorized target and narrow question. Record artifact path, hash, version and desired evidence. Work on copies; do not run an unknown executable merely to inspect it.
2. Identify the artifact type and check only relevant runtime/provider readiness. Source code analysis and binary reverse engineering have different requirements. Do not claim universal support from a list of CLI commands.
3. Start with static metadata, strings, imports, module boundaries and call relationships. Request deeper analysis only where it can answer the question. Runtime tracing, attaching to processes and network capture require a suitable isolated environment and task-specific authorization.
4. Maintain findings as `claim / artifact-and-location / observation / inference / confidence / unknowns`. Decompiled output is not original source. Missing symbols and obfuscation can limit conclusions; negative searches are not proof of absence.
5. If requested, implement the independently understood behavior in the user's project and test it against authorized examples. Do not copy protected assets, extract secrets, defeat licensing/DRM, bypass authentication or inspect third-party systems without permission.
6. Report which commands actually ran, provider/version, evidence and unresolved limitations. Do not report native analysis success when only a JavaScript fixture or readiness check ran.

Invocation: `$rea-analysis 分析我有权检查的这个 Electron 应用，先静态查明模块与调用关系，给出证据和不确定项，不执行应用。`
