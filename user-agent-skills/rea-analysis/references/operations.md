# Runtime And Operations

Reviewed source package version: 6.4.0. This is a source-tree version, not proof of the latest npm release. Check registry metadata before selecting a published version.

At this revision REA requires Node 22.x >=22.19, 24.x >=24.11, or >=26. Versions 23/25 do not satisfy its declared range. npm is also required.

- JavaScript/Electron static inspection: extracted directory or ASAR. No native decompiler is required for the documented static workflow.
- Native binaries: an available, supported Hopper, Ghidra or IDA provider; commercial provider licenses are separate from REA's MIT license.
- .NET/APK/runtime/web analysis: read the target-specific current documentation and scoped readiness result. Do not install every optional backend preemptively.

Prefer a local verified CLI when available. The following are documented command shapes; replace `<verified-version>` only after checking the registry and runtime compatibility:

```sh
npx -y rea-agents@<verified-version> --help
npx -y rea-agents@<verified-version> doctor --json
npx -y rea-agents@<verified-version> analyze-javascript-application /absolute/path/to/authorized-fixture --json
npx -y rea-agents@<verified-version> setup --client codex --skill=false --dry-run
```

`npx` downloads and executes a package, so it is not a purely static readiness probe. Inspect provenance/dependencies before execution. For one-off analysis, avoid global installation or changing unrelated clients. If MCP registration is requested, review the dry-run's exact paths, preserve unrelated configuration and backups, apply only the requested client, then verify registration. Do not use `--all-detected` or auto-install Hopper as a routine default.

Upstream `setup` installs a separate bundled workflow by default; `--skill=false` prevents duplicate workflow installation when this adapter is used. Existing runtime upgrades are separate from skill text updates.

References: [installation](https://github.com/morluto/rea/blob/4f4f6cd7b5d7a400b90772a138d7b9f942c2a556/docs/installation.md), [CLI](https://github.com/morluto/rea/blob/4f4f6cd7b5d7a400b90772a138d7b9f942c2a556/docs/cli.md).
