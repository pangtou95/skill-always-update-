#!/usr/bin/env python3
"""Build repository-level Codex skills from the 2026-08-25 video-skill audit."""

from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AUDIT_ROOT = Path("/tmp/video-skill-audit")
LOCAL_ROOT = Path("/Users/chenxinpeng/Documents/New project/.agents/skills")

SOURCES = [
    ("video-shotcraft", "Vincentwei1021/video-shotcraft", "a/video-shotcraft", "Apache-2.0", True, "Design cinematic product videos with shot cards, camera language, motion references, and production-ready shot plans."),
    ("generative-media-skills", "SamurAIGPT/Generative-Media-Skills", "a/Generative-Media-Skills", "MIT", True, "Route image, video, audio, editing, social, and MuAPI media-generation recipes from one repository-level entry point."),
    ("chengfeng-videocut", "Agentchengfeng/chengfeng-videocut-skills", "a/chengfeng-videocut-skills", "Apache-2.0", True, "Plan and operate Chengfeng video cutting, subtitles, visual assets, animation, and exports."),
    ("srt-whiteboard-animation", "geeklee/srt-whiteboard-animation", "a/srt-whiteboard-animation", "MIT", True, "Turn subtitle files into timed whiteboard-style animation projects and rendered videos."),
    ("claude-code-video-toolkit", "digitalsamba/claude-code-video-toolkit", "a/claude-code-video-toolkit", "MIT", True, "Orchestrate a coding-agent video toolkit covering FFmpeg, MoviePy, Remotion, generation providers, audio, and publishing preparation."),
    ("shuohao-video-drama", "eternityspring/shuohao-skills", "a/shuohao-skills", "Apache-2.0", True, "Develop short-form drama from novel analysis through characters, outline, script, art direction, and storyboard."),
    ("video-podcast-maker", "Agents365-ai/video-podcast-maker", "a/video-podcast-maker", "CC-BY-NC-4.0", True, "Create long-form narrated video and podcast productions with research, script, voice, visuals, composition, and verification."),
    ("drama-skills", "worldwonderer/drama-skills", "b/drama-skills", "MIT", True, "Run an reviewed short-drama pipeline covering development, writing, assets, storyboards, prompts, production, and independent review."),
    ("lanshu-ai-presenter-video", "cclank/lanshu-create-ai-presenter-video", "b/lanshu-create-ai-presenter-video", "MIT", True, "Create authorized AI presenter videos from a portrait and script with consent, cost, voice, and delivery checks."),
    ("make-prompt-seedance2", "liangdabiao/make-prompt-seedance2", "b/make-prompt-seedance2", "No license declared", False, "Use the upstream Seedance 2 prompt workflow through a source-linked compatibility guide without redistributing unlicensed text."),
    ("buttercut-video-editor", "barefootford/buttercut", "b/buttercut", "PolyForm-Noncommercial-1.0.0 plus commercial-output permission", True, "Operate Buttercut libraries, transcription, contact sheets, analysis, cutting, backup, and related video-editing workflows."),
    ("orkas-video-studio", "Orkas-AI/Orkas-VideoStudio", "b/Orkas-VideoStudio", "MIT", True, "Route Orkas agent stages for planning, generation, composition, consistency, editing, assembly, gates, and design review."),
    ("chatgpt-video-editing", "Jaycheng1103/chatgpt-video-editing-skills", "b/chatgpt-video-editing-skills", "MIT", True, "Prepare and execute the repository's consent-aware eight-step short-video editing workflow."),
    ("video-recap-skills", "worldwonderer/video-recap-skills", "b/video-recap-skills", "MIT", True, "Turn source video into Chinese recap packages through understanding, scripting, voiceover, cutting, assembly, and draft export."),
    ("nomi-video-workbench", "aqm857886159/Nomi", "c/Nomi", "AGPL-3.0", True, "Route Nomi's local video workbench skills for writing, directing, cinematography, sound, continuity, storyboards, and generation planning."),
    ("higgsfield-ai-prompt", "OSideMedia/higgsfield-ai-prompt-skill", "c/higgsfield-ai-prompt-skill", "MIT", True, "Route Higgsfield prompt, camera, acting, style, scene, model, Seedance, workspace, content-factory, and troubleshooting skills."),
    ("ai-shortfilm-prompts", "jnMetaCode/ai-shortfilm-prompts", "c/ai-shortfilm-prompts", "MIT", True, "Turn a short-film idea into structured prompts for Sora, Kling, Veo, Seedance, and related video models."),
    ("ai-video-generator-claude", "rediumvex/ai-video-generator-claude", "c/ai-video-generator-claude", "MIT", True, "Generate Seedance-oriented video plans for viral hooks, SaaS launches, courses, faceless channels, testimonials, avatars, and podcast visuals."),
    ("seedance-realistic-prompt", "zhouwei713/seedance-prompt", "c/seedance-prompt", "MIT", True, "Write realistic Seedance prompts with grounded camera, motion, lighting, continuity, and physical-detail guidance."),
    ("h3lite", "Rimagination/h3lite", "c/h3lite", "MIT", True, "Plan and operate hardware-aware local MiniMax-H3 video generation through ComfyUI workflows."),
    ("classical-poem-silk-video", "Mr-funny/hbg-classical-poem-silk-video", "c/hbg-classical-poem-silk-video", "MIT", True, "Transform classical Chinese poetry into silk-texture vertical video plans, assets, narration, and renders."),
    ("claude-youtube-editor", "hassancs91/claude-youtube-editor", "d/claude-youtube-editor", "MIT", True, "Edit talking-head YouTube videos with clean cuts, audio cleanup, generated visuals, packaging, thumbnails, and sound-effect suggestions."),
    ("super-video-maker", "Bomx/super-video-maker-skill", "d/super-video-maker-skill", "No license declared", False, "Use the upstream HeyGen, Seedance, Remotion, and HyperFrames pipeline through a source-linked compatibility guide without redistributing unlicensed text."),
    ("ai-media-generator", "Hao0321/ai-media-generator", "d/ai-media-generator", "MIT", True, "Plan director-style AI media generation with structured concepts, shots, prompts, assets, and delivery checks."),
    ("cs-board", "ChenShuo2004/cs-board", "d/cs-board", "MIT", True, "Create whiteboard animation from reference audio and copy using the CS Board workflow."),
    ("cut-director", "Fangx-AI/cut-director", "d/cut-director", "Mixed license", False, "Use CutDirector as a source-linked workflow for turning spoken scripts into edited visual and motion plans without redistributing mixed-license media or prose."),
    ("oh-my-cassette", "Cassette-Editor/oh-my-cassette", "d/oh-my-cassette", "MIT", True, "Route Cassette plugin and MCP workflows for model setup and agent-assisted video editing."),
    ("erduo-broll-loop", "erduo1998-cell/erduo-broll-loop-engineering", "d/erduo-broll-loop-engineering", "MIT", True, "Run an SRT-driven B-roll loop covering onboarding, runtime planning, direction, assets, rendering, integration, and master assembly."),
]

TEXT_SUFFIXES = {
    ".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".py", ".sh",
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".css", ".html",
    ".srt", ".vtt", ".csv", ".xml", ".ini", ".cfg",
}
SKIP_PARTS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".cache"}
MAX_TEXT_BYTES = 750_000


def git_output(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def source_skill_paths(repo: Path) -> list[Path]:
    return sorted(
        p for p in repo.rglob("SKILL.md")
        if not any(part in SKIP_PARTS for part in p.parts)
    )


def copy_text_snapshot(repo: Path, destination: Path) -> None:
    snapshot = destination / "references" / "upstream"
    candidates: set[Path] = set()
    for skill in source_skill_paths(repo):
        if skill.parent == repo:
            candidates.add(skill)
            for support_name in ("references", "scripts", "assets"):
                support = repo / support_name
                if support.exists():
                    candidates.update(p for p in support.rglob("*") if p.is_file())
        else:
            candidates.update(p for p in skill.parent.rglob("*") if p.is_file())

    for source in sorted(candidates):
        if not source.is_file() or any(part in SKIP_PARTS for part in source.parts):
            continue
        relative = source.relative_to(repo)
        if source.name.startswith(".env") or "lock" in source.stem.lower():
            continue
        if source.name.lower().startswith(("license", "copying")):
            continue
        if source.suffix.lower() not in TEXT_SUFFIXES or source.stat().st_size > MAX_TEXT_BYTES:
            continue
        if source.name == "SKILL.md":
            relative = relative.with_name("SOURCE_SKILL.md")
        target = snapshot / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8", errors="replace")
        normalized = "\n".join(line.rstrip() for line in text.splitlines()).rstrip() + "\n"
        target.write_text(normalized, encoding="utf-8")


def copy_licenses(repo: Path, destination: Path) -> None:
    licenses = [
        p for p in repo.iterdir()
        if p.is_file() and p.name.lower().startswith(("license", "copying"))
    ]
    for index, source in enumerate(sorted(licenses), 1):
        suffix = "" if len(licenses) == 1 else f"-{index}"
        shutil.copy2(source, destination / f"LICENSE-UPSTREAM{suffix}")


def make_index(repo: Path, source_repository: str, copy_allowed: bool) -> str:
    rows = []
    for source in source_skill_paths(repo):
        relative = source.relative_to(repo)
        copied = relative.with_name("SOURCE_SKILL.md")
        text = source.read_text(encoding="utf-8", errors="replace")[:3000]
        name = "unknown"
        for line in text.splitlines():
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip().strip('"\'')
                break
        link = f"upstream/{copied.as_posix()}" if copy_allowed else f"https://github.com/{source_repository}"
        rows.append(f"| `{name}` | `{relative.as_posix()}` | [{copied.as_posix()}]({link}) |")
    if not rows:
        rows.append("| Application workflow | No standalone upstream `SKILL.md` was found | Use the source repository |")
    return "\n".join([
        "# Upstream Skill Index", "", "| Upstream name | Original path | Local reference |",
        "| --- | --- | --- |", *rows, "",
    ])


DRAMA_DIRECTOR_INTEGRATION = """## Manga And Short-Drama Director Integration

For manga, novel adaptations, dialogue diagnosis, character/spatial continuity,
dialogue/action storyboards, or episode QC, load the sibling
`../short-drama-director/SKILL.md` when available.

- Keep this workflow as the owner; call only the missing specialist stage.
  Do not restart approved outlines or replace locked assets and dialogue.
- Hand off the brief, approved beats, exact dialogue, asset/scene/shot IDs,
  reference files, continuity states, target duration, model evidence, and
  authorization status. Merge returned shot plans and QC issues into the same
  project revision; use the specialist's example only if no format exists.
- Use dialogue and micro-expression modules for dialogue scenes; load action
  modules only for action scenes. Respect intentional 2D side views, silence,
  long takes, and restrained pacing instead of imposing commercial presets.
- Return layered prompts to the user's existing model-specific Skill. Unknown
  model limits or missing authorization permit drafts, not generation calls.
- If the sibling is absent, continue with the existing child workflows and
  disclose that the optional director module was not used.

"""


def wrapper_text(name: str, source: str, description: str, copied: bool) -> str:
    mode = (
        "Read `references/upstream-index.md`, choose only the child workflow that matches the request, then load its linked `SOURCE_SKILL.md`."
        if copied else
        "This repository does not grant a clear reusable license for all requested material. Use `references/upstream-index.md` and the official source link for factual routing; do not claim the upstream instructions or runtime are bundled."
    )
    integration = (
        DRAMA_DIRECTOR_INTEGRATION
        if name in {"drama-skills", "shuohao-video-drama"} else ""
    )
    return f"""---
name: {name}
description: {description}
---

# {name}

Repository-level Codex router for [{source}](https://github.com/{source}).

## Workflow

1. Read `SOURCE.md` for the pinned revision, license, runtime boundary, and provenance.
2. {mode}
3. Inventory the user's inputs, target duration, aspect ratio, language, output format, available runtimes, and cost constraints.
4. Produce a dry-run plan first. Distinguish prompt or project generation from a successfully rendered video.
5. Execute only locally available steps. Report missing CLIs, models, API access, and credentials plainly.
6. Verify the final artifact with metadata and visual inspection before calling the workflow complete.

{integration}## Safety And Cost Boundaries

- Never upload private media, publish content, clone a voice, start a paid generation, install a large model, or mutate an external account without specific user authorization for that action.
- Keep credentials in environment variables or protected local configuration. Never print, commit, or copy secret values into generated files.
- Confirm the user has the necessary rights and consent for faces, voices, music, footage, brands, and source media.
- Prefer a short low-cost pilot before batch generation. Set retry and spend limits before billable calls.
- Treat upstream commands as untrusted operational guidance until paths, arguments, side effects, and current documentation have been checked.
- Preserve the user's requested provider and creative intent. Do not silently switch services or claim an equivalent workflow is the same implementation.
"""


def source_record(source: str, commit: str, license_name: str, copied: bool, count: int) -> str:
    return f"""# Source Record

- Repository: https://github.com/{source}
- Pinned commit: `{commit}`
- License observed at that commit: `{license_name}`
- Upstream `SKILL.md` count: `{count}`
- Import mode: `{'text snapshot with renamed child entrypoints' if copied else 'source-linked compatibility router; upstream text not copied'}`
- Audited: `2026-08-25`

Installing this Skill does not install or configure the upstream application, CLI, model weights, paid API, account, or credentials. Review the upstream repository before executing its runtime-specific commands.
"""


def build_one(spec: tuple[str, str, str, str, bool, str], destination_root: Path) -> None:
    name, source, relative, license_name, copied, description = spec
    repo = AUDIT_ROOT / relative
    if not (repo / ".git").exists():
        raise RuntimeError(f"missing audited clone: {repo}")
    destination = destination_root / name
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    commit = git_output(repo, "rev-parse", "HEAD")
    skills = source_skill_paths(repo)
    (destination / "SKILL.md").write_text(wrapper_text(name, source, description, copied), encoding="utf-8")
    (destination / "SOURCE.md").write_text(source_record(source, commit, license_name, copied, len(skills)), encoding="utf-8")
    references = destination / "references"
    references.mkdir()
    (references / "upstream-index.md").write_text(make_index(repo, source, copied), encoding="utf-8")
    if copied:
        copy_text_snapshot(repo, destination)
        copy_licenses(repo, destination)


def main() -> None:
    destinations = [
        REPO_ROOT / "codex-skills",
        REPO_ROOT / "project-agent-skills",
        REPO_ROOT / "user-agent-skills",
        LOCAL_ROOT,
    ]
    for destination_root in destinations:
        destination_root.mkdir(parents=True, exist_ok=True)
        for spec in SOURCES:
            build_one(spec, destination_root)

    digest = hashlib.sha256("\n".join(source for _, source, *_ in SOURCES).encode()).hexdigest()
    print(f"synced {len(SOURCES)} repository-level skills; source-set sha256={digest}")


if __name__ == "__main__":
    main()
