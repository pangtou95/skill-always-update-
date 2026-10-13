"""Read-only source audit; never replaces skills or installs upstream runtimes."""
import argparse
import concurrent.futures
import datetime
import json
import re
import subprocess
from pathlib import Path

ROOTS = ("codex-skills", "project-agent-skills", "user-agent-skills")
URL = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+)")
SHA = re.compile(r"\b[0-9a-f]{40}\b")


def inventory(root):
    entries = []
    for group in ROOTS:
        for skill in sorted((root / group).glob("*/SKILL.md")):
            folder = skill.parent
            records = [p for p in folder.rglob("*") if p.is_file()
                       and p.name in {"SOURCE.md", "PROVENANCE.json"}
                       and "upstream" not in p.relative_to(folder).parts]
            text = "\n".join(p.read_text(errors="replace") for p in records)
            # Entrypoint links are hints, not verified provenance.
            hints = sorted(set(URL.findall(skill.read_text(errors="replace"))))
            repos = sorted(set(x.removesuffix(".git") for x in URL.findall(text)))
            base_commit = None
            provenance = folder / "PROVENANCE.json"
            if provenance.exists():
                try:
                    base_commit = json.loads(provenance.read_text()).get("commit")
                except (ValueError, AttributeError):
                    pass
            entries.append({"skill": folder.name, "group": group, "base_commit": base_commit,
                            "records": [str(p.relative_to(root)) for p in records],
                            "repositories": repos, "pinned_commits": sorted(set(SHA.findall(text))),
                            "unverified_link_hints": hints})
    return entries


def remote_head(repo):
    try:
        result = subprocess.run(["git", "ls-remote", "https://github.com/" + repo + ".git", "HEAD"],
                                capture_output=True, text=True, timeout=35, check=True)
        sha = result.stdout.split()[0]
        if not SHA.fullmatch(sha):
            raise ValueError("invalid HEAD")
        return {"repository": repo, "head": sha}
    except (subprocess.SubprocessError, ValueError, IndexError) as exc:
        return {"repository": repo, "error": type(exc).__name__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    entries = inventory(args.root)
    repos = sorted({r for e in entries for r in e["repositories"]})
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        heads = {r["repository"]: r for r in pool.map(remote_head, repos)}
    for entry in entries:
        entry["status"] = "no-pinned-provenance"
        if entry["repositories"]:
            if any("error" in heads[r] for r in entry["repositories"]):
                entry["status"] = "upstream-unavailable"
            elif entry["pinned_commits"]:
                entry["status"] = ("head-matches-pin" if all(heads[r]["head"] in entry["pinned_commits"]
                                    for r in entry["repositories"]) else "review-needed")
                if (entry["status"] == "head-matches-pin" and entry["base_commit"]
                        and any(heads[r]["head"] != entry["base_commit"] for r in entry["repositories"])):
                    entry["status"] = "reviewed-head-local-base-preserved"
    report = {"checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "scope": "Top-level exported skills only; not bundled plugins or nested snapshots.",
              "warning": "HEAD drift is a review candidate, not proof a skill is outdated. No source record means no latest-version claim.",
              "repositories": list(heads.values()), "entries": entries}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    counts = {s: sum(e["status"] == s for e in entries) for s in sorted({e["status"] for e in entries})}
    print(json.dumps({"export_copies": len(entries), "unique_names": len({e["skill"] for e in entries}),
                      "upstreams": len(repos), "statuses": counts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
