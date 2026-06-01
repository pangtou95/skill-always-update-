---
name: claude-mem-operations
description: Use when installing, configuring, debugging, extending, or explaining claude-mem persistent memory, memory compression, lifecycle hooks, worker service, SQLite/Chroma search, MCP tools, or cross-agent context continuity based on thedotmack/claude-mem.
---

# Claude-Mem Operations

Source analyzed: https://github.com/thedotmack/claude-mem

Use this skill for persistent agent memory systems, Claude Code/Codex/Gemini/OpenCode integrations, worker-service debugging, lifecycle hooks, memory search, and privacy handling.

## Repository Shape

- Runtime and service code is in `src/services/`.
- Worker HTTP routes are in `src/services/worker/http/routes/`.
- SQLite storage is in `src/services/sqlite/`.
- Search orchestration is in `src/services/worker/search/`.
- UI viewer is in `src/ui/viewer/`.
- Plugin hooks, scripts, skills, and manifests are packaged under `plugin/`.
- CLI entrypoint is exported as `claude-mem` from `dist/npx-cli/index.js`.

The project is TypeScript ESM, expects Node 20+ and Bun 1+, and uses Apache-2.0.

## Mental Model

Claude-Mem captures coding-session observations, compresses them into summaries, stores them, and makes them searchable for future sessions. Its main system pieces are:

- lifecycle hooks for session start, prompt submit, tool use, stop, and session end;
- a Bun-managed worker service on port `37777`;
- SQLite for sessions, observations, summaries, timelines, and FTS-style lookup;
- optional Chroma vector search for hybrid semantic retrieval;
- a web viewer UI for live memory inspection;
- MCP/search tools that expose progressive disclosure: search index first, detailed record second.

## Install And Setup

Preferred install path:

```bash
npx claude-mem install
```

For other IDE/agent integrations, use the installer flag when applicable:

```bash
npx claude-mem install --ide gemini-cli
npx claude-mem install --ide opencode
```

Do not suggest `npm install -g claude-mem` as the main setup path; the README says that installs the SDK/library but does not register plugin hooks or worker service.

## Development Commands

Use the package scripts already provided:

```bash
npm run build
npm run typecheck
npm test
npm run worker:start
npm run worker:status
npm run worker:logs
npm run worker:restart
```

Targeted tests:

```bash
npm run test:sqlite
npm run test:search
npm run test:context
npm run test:infra
npm run test:server
```

When debugging hook or process behavior, also inspect:

- `src/supervisor/`
- `src/services/infrastructure/`
- `src/services/hooks/`
- `plugin/hooks/`
- `plugin/scripts/worker-service.cjs`

## Debugging Workflow

For "memory is not appearing":

1. Check install path and whether hooks are registered for the active agent.
2. Check worker status and logs.
3. Confirm port `37777` is reachable.
4. Inspect SQLite/session records before blaming vector search.
5. Check context settings and privacy filters.
6. Search by recent project/session/time range.

For "worker does not start":

1. Confirm Node and Bun versions.
2. Run the worker status/log scripts.
3. Look for stale processes in the process registry.
4. Check environment sanitization if a spawned model/CLI fails.
5. Restart the worker after rebuilding hook artifacts.

For "search quality is poor":

1. Distinguish keyword/SQLite, Chroma vector, and hybrid strategy behavior.
2. Inspect `SearchOrchestrator`, strategy classes, filters, and result formatting.
3. Verify summaries/observations are being generated, not just raw sessions.
4. Keep progressive disclosure: compact search result first, detail fetch only when needed.

## Privacy Discipline

Claude-Mem supports privacy exclusion with `<private>` tags. When designing or debugging:

- Never store secrets, credentials, private keys, raw tokens, or private user messages.
- Preserve privacy validators and redaction checks.
- Treat observation IDs and viewer URLs as sensitive if they expose local work context.
- When adding routes or UI views, avoid accidental broad dumps of session content.

## Architecture Extension Rules

When adding features:

1. Keep hooks lightweight; push durable work to the worker service.
2. Prefer typed route handlers and shared validation middleware.
3. Add SQLite migrations or store changes deliberately; check search/timeline consumers.
4. For new search modes, implement a strategy and route it through the orchestrator.
5. Keep UI viewer reads API-driven; avoid duplicating storage logic in the frontend.
6. Add tests close to the changed layer.

## Common File Targets

- Memory routes: `src/services/worker/http/routes/MemoryRoutes.ts`
- Search routes: `src/services/worker/http/routes/SearchRoutes.ts`
- Context generation: `src/services/context-generator.ts`
- Session lifecycle: `src/services/worker/SessionManager.ts`
- Observation storage: `src/services/sqlite/observations/`
- Summaries: `src/services/sqlite/summaries/`
- Viewer UI: `src/ui/viewer/`

