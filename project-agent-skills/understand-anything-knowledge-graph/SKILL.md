---
name: understand-anything-knowledge-graph
description: Use when analyzing or building codebase/knowledge-base graph tooling, Understand-Anything plugin workflows, /understand commands, dashboard graph UX, semantic batching, code structure extraction, diff impact analysis, or onboarding/explain flows based on Lum1104/Understand-Anything.
---

# Understand Anything Knowledge Graph

Source analyzed: https://github.com/Lum1104/Understand-Anything

Use this skill for codebase comprehension pipelines that extract structure, build knowledge graphs, render interactive dashboards, and answer architecture questions.

## Repository Shape

- Main plugin code is under `understand-anything-plugin/src/`.
- Dashboard app is under `understand-anything-plugin/packages/dashboard/`.
- Built-in skills live in `understand-anything-plugin/skills/`.
- Homepage is under `homepage/`.
- Specs and implementation plans live in `docs/superpowers/`.
- Tests are in `understand-anything-plugin/src/__tests__/` and dashboard utility test folders.

The project uses pnpm 10, TypeScript, Vitest, and ESLint.

## Core Commands

User-facing plugin commands include:

```text
/understand
/understand-dashboard
/understand-chat <question>
/understand-diff
/understand-explain <path-or-symbol>
/understand-onboard
/understand-domain
/understand-knowledge <wiki-path>
```

Useful options:

```text
/understand --language zh
/understand --auto-update
/understand src/frontend
```

Development commands:

```bash
pnpm install
pnpm build
pnpm test
pnpm dev:dashboard
pnpm lint
```

## Pipeline Model

Understand Anything turns a repository or wiki into navigable graph data:

1. Scope the project or knowledge base.
2. Extract files, functions, classes, dependencies, and domain concepts.
3. Summarize nodes in plain language.
4. Build graph relationships and guided tours.
5. Save graph data to `.understand-anything/knowledge-graph.json`.
6. Render the dashboard for search, pan/zoom, filtering, and node inspection.
7. Support follow-up chat, explanation, onboarding, and diff impact views.

For very large repositories, scope to a subdirectory or use incremental mode before full re-analysis.

## Codebase Analysis Guidance

When explaining a codebase using this pattern:

1. Start with entrypoints, package boundaries, and config files.
2. Identify architectural layers: UI, API, service, data, utilities, scripts.
3. Build dependency direction before narrating feature flow.
4. Explain concrete user/business flows separately from structural modules.
5. Use diff impact analysis to list touched nodes, downstream callers, and tests to run.
6. Produce an onboarding order: concepts first, high-traffic files second, edge cases last.

Avoid dumping every file. The product philosophy is a graph that teaches how pieces fit together.

## Dashboard Work

Dashboard components live under `understand-anything-plugin/packages/dashboard/src/components/`. Important areas:

- graph views: `GraphView`, `DomainGraphView`, `KnowledgeGraphView`;
- node rendering: `CustomNode`, `FlowNode`, `ContainerNode`, cluster nodes;
- inspection: `NodeInfo`, `CodeViewer`, `LearnPanel`;
- navigation: `Breadcrumb`, `SearchBar`, `FilterPanel`;
- mobile: `MobileLayout`, `MobileDrawer`, `MobileBottomNav`;
- layout utilities: `utils/layout.ts`, `utils/elk-layout.ts`, `utils/edgeAggregation.ts`.

When changing graph UX:

1. Keep node labels readable under zoom.
2. Preserve search and keyboard navigation.
3. Test large graphs with generated fixtures when possible.
4. Keep mobile interactions explicit and touch-friendly.
5. Avoid layout algorithms that are non-deterministic unless the UI exposes refresh/reflow intentionally.

## Knowledge Base Mode

For `/understand-knowledge`, the analyzed repo describes a Karpathy-pattern LLM wiki:

- `index.md` anchors the wiki.
- Wikilinks and categories are parsed deterministically.
- LLM agents can add implicit relationships, entities, and claims.

When applying this to a docs/wiki task, separate:

- explicit links from inferred links;
- source claims from generated summaries;
- categories from communities/clusters.

## Multi-Platform Install Notes

The repository supports multiple agent/IDE targets through install scripts:

```bash
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash -s codex
```

Windows uses PowerShell install. Cursor and VS Code/Copilot can auto-discover plugin manifests when the repo is cloned.

## Testing Notes

For parser or builder changes, run targeted Vitest tests near:

- `context-builder.test.ts`
- `explain-builder.test.ts`
- `diff-analyzer.test.ts`
- `extract-structure.test.mjs`
- dashboard utility tests for layout, filters, edge aggregation, and containers.

For output changes, check localized text behavior when `--language` is used.

