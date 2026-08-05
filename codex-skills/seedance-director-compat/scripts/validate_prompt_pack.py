#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED = {
    "availability", "model_connected", "model_profile", "mode", "reference_roles",
    "clip_contract", "continuity_anchors", "scene_type", "physics_contract_zh", "physics_contract_en",
    "script_zh", "script_en", "positive_prompt_zh", "positive_prompt_en", "negative_prompt_zh", "negative_prompt_en",
    "audio_prompt_zh", "audio_prompt_en", "audio_negative_zh", "audio_negative_en", "fallbacks", "source_refs",
}
MODES = {"t2v", "i2v", "v2v", "r2v", "flf2v", "edit", "extend"}
CAMERA_TERMS = ("push", "pull", "dolly", "track", "orbit", "pan", "tilt", "handheld", "推进", "拉远", "跟随", "环绕", "横摇", "上摇", "手持")


def load_payload(path: str):
    if path == "-":
        return json.load(sys.stdin)
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def validate(payload):
    errors, warnings = [], []
    if not isinstance(payload, dict):
        return ["root must be a JSON object"], warnings
    missing = sorted(REQUIRED - set(payload))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if payload.get("mode") not in MODES:
        errors.append("mode must be one of: " + ", ".join(sorted(MODES)))
    if payload.get("availability") == "prompt-only" and payload.get("model_connected") is not False:
        errors.append("prompt-only packs must set model_connected to false")
    for field in ("script_zh", "script_en", "positive_prompt_zh", "positive_prompt_en", "negative_prompt_zh", "negative_prompt_en", "audio_prompt_zh", "audio_prompt_en", "audio_negative_zh", "audio_negative_en"):
        if field in payload and not isinstance(payload[field], str):
            errors.append(f"{field} must be a string")
    roles = payload.get("reference_roles", [])
    if not isinstance(roles, list):
        errors.append("reference_roles must be an array")
    else:
        for index, role in enumerate(roles):
            if not isinstance(role, dict) or not role.get("tag") or not role.get("role"):
                errors.append(f"reference_roles[{index}] requires tag and role")
    contract = payload.get("clip_contract")
    if not isinstance(contract, dict):
        errors.append("clip_contract must be an object")
    else:
        for field in ("visible_beat", "camera", "end_state"):
            if not str(contract.get(field, "")).strip():
                errors.append(f"clip_contract.{field} is required")
        camera = str(contract.get("camera", "")).lower()
        moves = [term for term in CAMERA_TERMS if term in camera]
        if len(moves) > 2:
            warnings.append("camera may contain several competing moves: " + ", ".join(moves))
    if payload.get("mode") == "i2v":
        has_first = any(isinstance(role, dict) and role.get("role") == "first_frame" for role in roles if isinstance(roles, list))
        if not has_first and "@Image1" not in str(payload.get("positive_prompt_en", "")) and "@图片1" not in str(payload.get("positive_prompt_zh", "")):
            errors.append("i2v packs require a first-frame reference role or literal first-frame tag")
    for field in ("script_en", "physics_contract_en", "positive_prompt_en", "negative_prompt_en", "audio_prompt_en", "audio_negative_en"):
        if any("\u3400" <= char <= "\u9fff" for char in str(payload.get(field, ""))):
            errors.append(f"{field} must be English-only")
    compatibility = str(payload.get("model_profile", "")).lower().startswith("seedance")
    if compatibility and not payload.get("source_refs"):
        warnings.append("Seedance compatibility pack should retain an upstream/source reference")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate a Seedance-compatible prompt pack JSON file.")
    parser.add_argument("path", help="JSON file path or - for stdin")
    args = parser.parse_args()
    try:
        payload = load_payload(args.path)
    except (OSError, json.JSONDecodeError) as error:
        print(json.dumps({"ok": False, "errors": [str(error)], "warnings": []}, ensure_ascii=False, indent=2))
        return 2
    errors, warnings = validate(payload)
    print(json.dumps({"ok": not errors, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
