"""Offline tests for the optional Jev adapter; no browser or API keys needed."""

import argparse
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "codex-skills/jev-fast-web/scripts/jev_fast_web.py"
spec = importlib.util.spec_from_file_location("jev_fast_web_adapter", SCRIPT)
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


class JevFastWebTests(unittest.TestCase):
    def test_exact_host_parsing(self):
        self.assertEqual(adapter.hostname("https://example.org/a"), "example.org")
        for url in ("file:///tmp/page", "https://user:secret@example.org/", "example.org"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                adapter.hostname(url)

    def test_live_flag_required_before_import_or_network(self):
        args = argparse.Namespace(
            url="https://example.org/", allow_host=["example.org"], goal="Open page",
            max_actions=3, live=False, expect_url_prefix=None, expect_text=None,
        )
        with self.assertRaisesRegex(ValueError, "--live"):
            adapter.run(args)

    def test_host_allowlist_checked_before_import_or_network(self):
        args = argparse.Namespace(
            url="https://evil.example/", allow_host=["example.org"], goal="Open page",
            max_actions=3, live=True, expect_url_prefix=None, expect_text=None,
        )
        with self.assertRaisesRegex(ValueError, "allowlisted"):
            adapter.run(args)

    def test_missing_keys_block_live_calls(self):
        args = argparse.Namespace(
            url="https://example.org/", allow_host=["example.org"], goal="Open page",
            max_actions=3, live=True, expect_url_prefix=None, expect_text=None,
        )
        with patch.dict("os.environ", {"TYPESAFE_API_KEY": "", "TEXT_MODEL_API_KEY": ""}):
            with self.assertRaisesRegex(RuntimeError, "TYPESAFE_API_KEY"):
                adapter.run(args)

    def test_probe_bounds(self):
        for count in (0, 101):
            with self.subTest(count=count), self.assertRaises(ValueError):
                adapter.probe(count)


if __name__ == "__main__":
    unittest.main()
