"""Refresh only two reviewed text snapshots while preserving their local routers."""
import argparse
import importlib.util
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("wave", ROOT / "tools/sync_video_skill_wave.py")
wave = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wave)
TARGETS = {"ai-shortfilm-prompts": ("jnMetaCode/ai-shortfilm-prompts", "MIT", "shortfilm"),
           "video-shotcraft": ("Vincentwei1021/video-shotcraft", "Apache-2.0", "shotcraft")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, choices=TARGETS)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--local-root", type=Path, required=True)
    parser.add_argument("--reviewed-commit", required=True)
    args = parser.parse_args()
    repo, license_id, _ = TARGETS[args.name]
    sha = wave.git_output(args.checkout, "rev-parse", "HEAD")
    if sha != args.reviewed_commit:
        raise SystemExit("Checkout does not match the explicitly reviewed commit")
    license_text = (args.checkout / "LICENSE").read_text()
    if ("Permission is hereby granted" if license_id == "MIT" else "Apache License") not in license_text:
        raise SystemExit("License changed; review before copying")
    local = args.local_root / args.name
    router = (local / "SKILL.md").read_bytes()
    with tempfile.TemporaryDirectory() as temp:
        stage = Path(temp) / args.name
        stage.mkdir()
        wave.copy_text_snapshot(args.checkout, stage)
        # These repositories link root-level templates outside the skill directory.
        for dirname in ("templates", "template"):
            folder = args.checkout / dirname
            if not folder.exists():
                continue
            for source in folder.rglob("*"):
                if (not source.is_file() or any(p in wave.SKIP_PARTS for p in source.parts)
                        or source.suffix.lower() not in wave.TEXT_SUFFIXES
                        or source.stat().st_size > wave.MAX_TEXT_BYTES
                        or source.name.startswith(".env") or "lock" in source.stem.lower()):
                    continue
                target = stage / "references/upstream" / source.relative_to(args.checkout)
                if target.name == "SKILL.md":
                    target = target.with_name("SOURCE_SKILL.md")
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        wave.copy_licenses(args.checkout, stage)
        (stage / "references/upstream-index.md").write_text(wave.make_index(args.checkout, repo, True))
        source_text = (f"# Source Record\n\n- Repository: https://github.com/{repo}\n"
                       f"- Pinned commit: `{sha}`\n- License observed: `{license_id}`\n"
                       "- Audited: `2026-10-13`\n- Import mode: reviewed text snapshot; local router preserved.\n"
                       "- Runtime installed: false. Media, dependencies and the complete executable project are not bundled.\n"
                       "- Root templates included to resolve instruction dependencies; renamed child entrypoints are reference material.\n")
        (stage / "SOURCE.md").write_text(source_text)
        # Preserve the router and other locally owned files; replace only owned snapshot paths.
        for relative in ("references/upstream", "references/upstream-index.md", "SOURCE.md"):
            target = local / relative
            if target.is_dir():
                shutil.rmtree(target)
            elif target.exists():
                target.unlink()
            source = stage / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)
        for license_file in stage.glob("LICENSE-UPSTREAM*"):
            shutil.copy2(license_file, local / license_file.name)
    assert (local / "SKILL.md").read_bytes() == router
    print(args.name, sha, "router preserved")


if __name__ == "__main__":
    main()
