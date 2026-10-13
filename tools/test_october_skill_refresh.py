import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("audit", ROOT / "tools/audit_skill_upstreams.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
NAMES = ("ui-refs", "matt-engineering-workflows", "rea-analysis", "grill-me",
         "ai-shortfilm-prompts", "video-shotcraft", "short-drama-director")


def snapshot(folder):
    return {str(p.relative_to(folder)): p.read_bytes() for p in folder.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts}


class RefreshTests(unittest.TestCase):
    def test_export_parity(self):
        for name in NAMES:
            expected = snapshot(ROOT / "codex-skills" / name)
            for group in ("project-agent-skills", "user-agent-skills"):
                self.assertEqual(expected, snapshot(ROOT / group / name), name)

    def test_new_entrypoints(self):
        for name in NAMES[:3]:
            folder = ROOT / "codex-skills" / name
            text = (folder / "SKILL.md").read_text()
            self.assertTrue(text.startswith("---\nname: " + name + "\n"))
            self.assertIn("\ndescription:", text)
            self.assertEqual(list(folder.rglob("SKILL.md")), [folder / "SKILL.md"])
            self.assertRegex((folder / "SOURCE.md").read_text(), r"[0-9a-f]{40}")
            for path in re.findall(r"`(references/[\w/-]+\.md)`", text):
                self.assertTrue((folder / path).is_file(), path)

    def test_runtime_and_rights_boundaries(self):
        ui = ROOT / "codex-skills/ui-refs"
        self.assertEqual(sorted(p.suffix for p in ui.rglob("*") if p.is_file()), [".md", ".md"])
        self.assertIn("CC BY 4.0", (ui / "SOURCE.md").read_text())
        rea = (ROOT / "codex-skills/rea-analysis/SKILL.md").read_text()
        self.assertIn("does not register MCP", rea)

    def test_snapshot_dependencies(self):
        shortfilm = ROOT / "codex-skills/ai-shortfilm-prompts/references/upstream"
        source = (shortfilm / "skills/shortfilm-prompt/SOURCE_SKILL.md").read_text()
        for path in set(re.findall(r"templates/[\w-]+\.md", source)):
            self.assertTrue((shortfilm / path).is_file(), path)
        shot = ROOT / "codex-skills/video-shotcraft/references/upstream"
        self.assertTrue((shot / "template/TEMPLATE.md").is_file())
        self.assertEqual(list(shortfilm.rglob("SKILL.md")), [])
        self.assertEqual(list(shot.rglob("SKILL.md")), [])

    def test_selective_drama_not_false_full_upgrade(self):
        folder = ROOT / "codex-skills/short-drama-director"
        data = json.loads((folder / "PROVENANCE.json").read_text())
        self.assertEqual(data["upstream_version"], "6.0")
        self.assertEqual(data["reviewed_upstream_version"], "6.9.9")
        self.assertIn("selective", data["update_mode"])
        self.assertEqual(len(list((folder / "references").glob("*.md"))), data["reference_modules"])

    def test_audit_ignores_nested_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "codex-skills/sample"
            (folder / "references/upstream").mkdir(parents=True)
            (folder / "SKILL.md").write_text("---\nname: sample\ndescription: fixture\n---\n")
            (folder / "SOURCE.md").write_text("https://github.com/owner/repo " + "a" * 40)
            (folder / "references/upstream/SOURCE.md").write_text("https://github.com/other/repo")
            records = audit.inventory(root)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["repositories"], ["owner/repo"])
            self.assertEqual(records[0]["pinned_commits"], ["a" * 40])


if __name__ == "__main__":
    unittest.main()
