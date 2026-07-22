#!/usr/bin/env python3
"""Report whether the local machine is ready to run DeepTutor."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def command_version(command: str, *args: str) -> dict[str, object]:
    path = shutil.which(command)
    result: dict[str, object] = {"command": command, "path": path, "available": bool(path)}
    if not path:
        return result

    try:
        completed = subprocess.run(
            [path, *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=8,
        )
        output = (completed.stdout or completed.stderr).strip().splitlines()
        result.update(
            {
                "exit_code": completed.returncode,
                "first_line": output[0] if output else "",
                "responded": completed.returncode == 0,
            }
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        result.update({"responded": False, "error": str(exc)})
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("cli", "web"), default="cli")
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when not ready")
    args = parser.parse_args()

    python_ok = sys.version_info >= (3, 11)
    deeptutor = command_version("deeptutor", "--help")
    node = command_version("node", "--version")
    uv = command_version("uv", "--version")
    workspace = args.workspace.expanduser().resolve()
    workspace_ok = workspace.exists() and workspace.is_dir()

    node_major = None
    first_line = node.get("first_line")
    if isinstance(first_line, str) and first_line.startswith("v"):
        try:
            node_major = int(first_line[1:].split(".", 1)[0])
        except ValueError:
            pass
    node_ok = bool(node.get("available")) and node_major is not None and node_major >= 20

    ready = python_ok and workspace_ok and bool(deeptutor.get("responded"))
    if args.mode == "web":
        ready = ready and node_ok

    actions: list[str] = []
    if not python_ok:
        actions.append("Install Python 3.11 or newer in an isolated environment.")
    if not workspace_ok:
        actions.append(f"Create or select a valid workspace: {workspace}")
    if not deeptutor.get("available"):
        installer = "uv tool install deeptutor==1.5.2" if uv.get("available") else "install deeptutor==1.5.2 in a dedicated virtual environment"
        actions.append(installer)
    elif not deeptutor.get("responded"):
        actions.append("Repair the deeptutor installation; `deeptutor --help` did not succeed.")
    if args.mode == "web" and not node_ok:
        actions.append("Install Node.js 20 or newer and place it on PATH for Web mode.")
    if ready:
        actions.append("Run `deeptutor init --cli` or `deeptutor init` if provider setup is not complete.")

    report = {
        "mode": args.mode,
        "ready": ready,
        "workspace": {"path": str(workspace), "available": workspace_ok},
        "python": {"version": sys.version.split()[0], "meets_3_11": python_ok},
        "deeptutor": deeptutor,
        "node": {**node, "major": node_major, "meets_20": node_ok},
        "uv": uv,
        "recommended_actions": actions,
    }
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 1 if args.strict and not ready else 0


if __name__ == "__main__":
    raise SystemExit(main())
