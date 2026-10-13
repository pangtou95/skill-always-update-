"""Copy the explicitly reviewed October skills and regenerate the manifest."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("ui-refs", "matt-engineering-workflows", "rea-analysis", "grill-me",
         "ai-shortfilm-prompts", "video-shotcraft", "short-drama-director")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-root", type=Path, required=True)
    args = parser.parse_args()
    for name in NAMES:
        source = args.local_root / name
        if not (source / "SKILL.md").is_file():
            raise SystemExit("Missing reviewed skill: " + name)
        for group in ("codex-skills", "project-agent-skills", "user-agent-skills"):
            dest = ROOT / group / name
            # Only these named exports are owned by this explicit sync operation.
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(source, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    paths = sorted(str(p.relative_to(ROOT)) for group in
                   ("codex-skills", "project-agent-skills", "user-agent-skills")
                   for p in (ROOT / group).rglob("SKILL.md"))
    (ROOT / "SKILLS_MANIFEST.txt").write_text("\n".join(paths) + "\n")
    print("Exported", len(NAMES), "reviewed skills; manifest entries:", len(paths))


if __name__ == "__main__":
    main()
