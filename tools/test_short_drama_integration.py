#!/usr/bin/env python3
"""Offline packaging, router and example-contract checks; no generation calls."""

import json
import os
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "codex-skills" / "short-drama-director"
EXPORTS = [ROOT / name for name in (
    "codex-skills", "project-agent-skills", "user-agent-skills"
)]
LOCAL = os.environ.get("SKILLS_LOCAL_ROOT")


def snapshot(path):
    return {
        p.relative_to(path).as_posix(): p.read_bytes()
        for p in path.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }


class ShortDramaIntegrationTests(unittest.TestCase):
    def test_provenance_and_license(self):
        source = json.loads((SKILL / "PROVENANCE.json").read_text())
        self.assertEqual(source["license"], "MIT")
        self.assertEqual(source["upstream_version"], "6.0")
        self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")
        self.assertIn(source["commit"], (SKILL / "SKILL.md").read_text())
        license_text = (SKILL / source["license_file"]).read_text()
        self.assertIn("Permission is hereby granted", license_text)
        self.assertIn("Short-Drama Director Suite contributors", license_text)

    def test_reference_modules_and_entrypoint(self):
        source = json.loads((SKILL / "PROVENANCE.json").read_text())
        refs = list((SKILL / "references").glob("*.md"))
        self.assertEqual(len(refs), source["reference_modules"])
        text = (SKILL / "SKILL.md").read_text()
        for name in set(re.findall(r"([\w-]+\.md)", text)) - {"SKILL.md"}:
            self.assertTrue((SKILL / "references" / name).is_file(), name)
        self.assertEqual(list(SKILL.rglob("SKILL.md")), [SKILL / "SKILL.md"])

    def test_export_copies_match(self):
        expected = snapshot(SKILL)
        for root in EXPORTS:
            with self.subTest(root=root):
                self.assertEqual(snapshot(root / SKILL.name), expected)

    def test_installed_copies_match(self):
        if not LOCAL:
            self.skipTest("Set SKILLS_LOCAL_ROOT to verify installed copies")
        local_root = Path(LOCAL)
        for name in ("short-drama-director", "drama-skills", "shuohao-video-drama", "video-director-studio"):
            with self.subTest(name=name):
                self.assertEqual(
                    snapshot(local_root / name), snapshot(ROOT / "codex-skills" / name)
                )

    def test_regenerated_drama_routes_are_preserved(self):
        module = runpy.run_path(str(ROOT / "tools" / "sync_video_skill_wave.py"))
        for name, source, _, _, copied, description in module["SOURCES"]:
            if name not in {"drama-skills", "shuohao-video-drama"}:
                continue
            expected = module["wrapper_text"](name, source, description, copied)
            for root in EXPORTS:
                self.assertEqual((root / name / "SKILL.md").read_text(), expected)
            self.assertIn("../short-drama-director/SKILL.md", expected)
        unrelated = module["wrapper_text"]("video-shotcraft", "example/repo", "Example", True)
        self.assertNotIn("../short-drama-director/SKILL.md", unrelated)

    def test_director_route(self):
        expected = (ROOT / "codex-skills/video-director-studio/SKILL.md").read_text()
        self.assertIn("../short-drama-director/SKILL.md", expected)
        self.assertEqual(
            (ROOT / "project-agent-skills/video-director-studio/SKILL.md").read_text(),
            expected,
        )

    def test_example_timeline_and_references(self):
        example = json.loads((SKILL / "assets/handoff.example.json").read_text())
        assets = {asset["asset_id"] for asset in example["assets"]}
        scenes = {scene["scene_id"] for scene in example["scenes"]}
        ids = set()
        cursor = 0
        previous_exit = None
        for shot in example["shots"]:
            self.assertNotIn(shot["shot_id"], ids)
            ids.add(shot["shot_id"])
            self.assertIn(shot["scene_id"], scenes)
            self.assertTrue(set(shot["asset_ids"]) <= assets)
            self.assertGreater(shot["duration_s"], 0)
            self.assertEqual(shot["start_s"], cursor)
            self.assertEqual(shot["exact_dialogue"], [])
            if previous_exit is not None:
                self.assertEqual(shot["entry_state"], previous_exit)
            previous_exit = shot["exit_state"]
            cursor += shot["duration_s"]
        self.assertEqual(cursor, example["brief"]["target_duration_s"])
        self.assertEqual(example["transitions"]["overlap_s"], 0)

    def test_example_has_no_execution_authorization(self):
        example = json.loads((SKILL / "assets/handoff.example.json").read_text())
        self.assertTrue(example["fictional_example"])
        self.assertEqual(example["status"], "draft")
        self.assertIsNone(example["model"]["max_clip_duration_s"])
        self.assertEqual(example["execution"]["mode"], "draft-only")
        self.assertFalse(example["execution"]["paid_generation_authorized"])
        self.assertFalse(example["execution"]["upload_authorized"])
        self.assertEqual(example["qc"]["status"], "pending")

    def test_upstream_package_checker(self):
        result = subprocess.run(
            [sys.executable, str(SKILL / "scripts/check_package.py")],
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_module_is_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            broken = Path(temporary) / SKILL.name
            shutil.copytree(SKILL, broken)
            (broken / "references/asset-spatial-ledger.md").unlink()
            result = subprocess.run(
                [sys.executable, str(broken / "scripts/check_package.py")],
                capture_output=True, text=True, timeout=30,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("asset-spatial-ledger.md", result.stdout)

    def test_manifest_contains_all_new_entries(self):
        entries = (ROOT / "SKILLS_MANIFEST.txt").read_text().splitlines()
        for root in EXPORTS:
            entry = f"{root.name}/short-drama-director/SKILL.md"
            self.assertEqual(entries.count(entry), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
