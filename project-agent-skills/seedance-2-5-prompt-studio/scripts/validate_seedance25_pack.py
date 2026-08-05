#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED = {
    "availability",
    "model_profile",
    "mode",
    "format_family",
    "duration_seconds",
    "aspect_ratio",
    "reference_roles",
    "timeline",
    "global_locks",
    "negative_constraints",
    "ending_state",
    "final_prompt",
    "evaluation",
    "source_refs",
}
MODES = {"t2v", "i2v", "r2v", "edit", "extend"}
STATUSES = {"verified-live", "rolling-out", "docs-only", "prompt-only", "unknown"}
REFERENCE_ROLES = {
    "identity",
    "product",
    "environment",
    "style",
    "motion",
    "camera",
    "timing",
    "voice",
    "music",
    "first_frame",
    "last_frame",
    "clay_layout",
    "edit_source",
}


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

    availability = payload.get("availability")
    if not isinstance(availability, dict):
        errors.append("availability must be an object")
    else:
        if not str(availability.get("surface", "")).strip():
            errors.append("availability.surface is required")
        if availability.get("status") not in STATUSES:
            errors.append("availability.status must be one of: " + ", ".join(sorted(STATUSES)))
        if availability.get("status") == "verified-live" and not str(availability.get("verified_at", "")).strip():
            errors.append("verified-live requires availability.verified_at")

    duration = payload.get("duration_seconds")
    if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration <= 0:
        errors.append("duration_seconds must be a positive number")
    elif str(payload.get("model_profile", "")).lower().startswith("seedance 2.5") and duration > 30:
        errors.append("single-pass Seedance 2.5 packs must not exceed 30 seconds")

    roles = payload.get("reference_roles")
    if not isinstance(roles, list):
        errors.append("reference_roles must be an array")
        roles = []
    seen_tags = set()
    for index, role in enumerate(roles):
        if not isinstance(role, dict):
            errors.append(f"reference_roles[{index}] must be an object")
            continue
        tag = str(role.get("tag", "")).strip()
        primary = role.get("primary_role")
        if not tag:
            errors.append(f"reference_roles[{index}].tag is required")
        elif tag in seen_tags:
            errors.append(f"reference tag appears more than once: {tag}")
        else:
            seen_tags.add(tag)
        if primary not in REFERENCE_ROLES:
            errors.append(f"reference_roles[{index}].primary_role is invalid")
        for field in ("preserve", "exclude", "active_beats"):
            if field in role and not isinstance(role[field], list):
                errors.append(f"reference_roles[{index}].{field} must be an array")

    timeline = payload.get("timeline")
    if not isinstance(timeline, list) or not timeline:
        errors.append("timeline must be a non-empty array")
        timeline = []
    previous_end = 0.0
    for index, beat in enumerate(timeline):
        if not isinstance(beat, dict):
            errors.append(f"timeline[{index}] must be an object")
            continue
        try:
            start = float(beat["start"])
            end = float(beat["end"])
        except (KeyError, TypeError, ValueError):
            errors.append(f"timeline[{index}] requires numeric start and end")
            continue
        if end <= start:
            errors.append(f"timeline[{index}] end must be greater than start")
        if index == 0 and abs(start) > 0.05:
            errors.append("timeline must start at 0")
        if index and abs(start - previous_end) > 0.05:
            errors.append(f"timeline gap or overlap before beat {index + 1}")
        previous_end = end
        for field in ("purpose", "subject_action", "camera", "transition_or_endpoint"):
            if not str(beat.get(field, "")).strip():
                warnings.append(f"timeline[{index}].{field} is empty")

    if timeline and isinstance(duration, (int, float)) and abs(previous_end - float(duration)) > 0.05:
        errors.append("timeline must end at duration_seconds")
    if isinstance(duration, (int, float)) and duration >= 20 and not 4 <= len(timeline) <= 6:
        warnings.append("20-30 second prompts usually work best with 4-6 beats")

    dialogue = payload.get("dialogue", [])
    if not isinstance(dialogue, list):
        errors.append("dialogue must be an array")
    else:
        for index, line in enumerate(dialogue):
            if not isinstance(line, dict) or not all(str(line.get(k, "")).strip() for k in ("speaker", "language", "text")):
                errors.append(f"dialogue[{index}] requires speaker, language, and text")

    if not str(payload.get("ending_state", "")).strip():
        warnings.append("ending_state is empty")
    if not str(payload.get("final_prompt", "")).strip():
        warnings.append("final_prompt is empty")
    if not payload.get("negative_constraints"):
        warnings.append("negative_constraints is empty; add only task-specific failures")
    if not payload.get("source_refs"):
        warnings.append("source_refs is empty; retain current capability sources")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate a Seedance 2.5 prompt pack JSON file.")
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
