#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TEXT_SUFFIXES = {".css", ".scss", ".sass", ".less", ".html", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".json"}


def files_for(path: Path):
    if path.is_file():
        return [path]
    return [p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES and "node_modules" not in p.parts]


def audit(path: Path):
    errors, warnings, notes = [], [], []
    files = files_for(path)
    corpus_parts = []
    for file in files:
        try:
            corpus_parts.append(file.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
    corpus = "\n".join(corpus_parts)
    uses_package = bool(re.search(r"from\s+['\"]border-beam['\"]|require\(['\"]border-beam['\"]\)", corpus))
    tags = re.findall(r"<BorderBeam\b[^>]*>", corpus, re.S)
    instances = len(tags)
    rotate = any(
        not re.search(r"size=['\"](?:pulse-inner|pulse-outside)['\"]", tag)
        for tag in tags
    )
    pulse_outside = "pulse-outside" in corpus

    if not instances and not re.search(r"beam-(?:shell|host|border)|data-beam", corpus):
        warnings.append("no border-beam usage detected")
        return errors, warnings, notes
    if uses_package:
        notes.append(f"detected {instances} BorderBeam component instance(s)")
    if instances > 6:
        warnings.append("more than six BorderBeam instances found; verify visual restraint and offscreen pausing")
    if rotate and "prefers-reduced-motion" not in corpus:
        errors.append("rotate/line BorderBeam usage requires a consumer reduced-motion strategy")
    if pulse_outside and re.search(r"overflow\s*:\s*(?:['\"])?(?:hidden|clip)", corpus):
        warnings.append("pulse-outside and clipped overflow coexist; inspect every ancestor for bloom cropping")
    if re.search(r"<button\b", corpus, re.I) and "focus-visible" not in corpus:
        warnings.append("button usage detected without a visible :focus-visible rule in the scanned files")
    if re.search(r"<BorderBeam\b[^>]*active=\{true\}", corpus, re.S):
        warnings.append("explicit always-active beam found; prefer event/state gating in product UI")
    if re.search(r"pointer-events\s*:\s*(auto|all)", corpus) and re.search(r"beam", corpus, re.I):
        warnings.append("pointer-events may be enabled near beam layers; confirm decoration cannot intercept input")
    return errors, warnings, notes


def main():
    parser = argparse.ArgumentParser(description="Audit border-beam UI usage for motion, focus, clipping, and restraint.")
    parser.add_argument("path")
    args = parser.parse_args()
    path = Path(args.path)
    if not path.exists():
        print(json.dumps({"ok": False, "errors": [f"path not found: {path}"], "warnings": [], "notes": []}, indent=2))
        return 2
    errors, warnings, notes = audit(path)
    print(json.dumps({"ok": not errors, "errors": errors, "warnings": warnings, "notes": notes}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
