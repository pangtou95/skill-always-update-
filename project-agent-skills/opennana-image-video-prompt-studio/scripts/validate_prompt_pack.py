#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROUTES = {"image", "video", "bridge"}
ROLES = {
    "identity", "product", "environment", "style", "composition",
    "first_frame", "last_frame", "motion", "camera", "timing",
    "voice", "music", "edit_source",
}
REQUIRED = {
    "route", "family", "model_surface", "deliverable", "aspect_ratio",
    "reference_roles", "locks", "negative_constraints", "final_prompt",
    "variants", "evaluation", "rights", "source_refs",
}


def validate(payload):
    errors, warnings = [], []
    if not isinstance(payload, dict):
        return ["root must be a JSON object"], warnings
    missing = sorted(REQUIRED - set(payload))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    route = payload.get("route")
    if route not in ROUTES:
        errors.append("route must be image, video, or bridge")
    if not str(payload.get("family", "")).strip():
        errors.append("family is required")
    if not str(payload.get("aspect_ratio", "")).strip():
        errors.append("aspect_ratio is required")

    surface = payload.get("model_surface")
    if not isinstance(surface, dict) or not str(surface.get("name", "")).strip():
        errors.append("model_surface.name is required")

    roles = payload.get("reference_roles")
    if not isinstance(roles, list):
        errors.append("reference_roles must be an array")
        roles = []
    seen = set()
    for index, ref in enumerate(roles):
        if not isinstance(ref, dict):
            errors.append(f"reference_roles[{index}] must be an object")
            continue
        tag = str(ref.get("tag", "")).strip()
        if not tag:
            errors.append(f"reference_roles[{index}].tag is required")
        elif tag in seen:
            errors.append(f"duplicate reference tag: {tag}")
        seen.add(tag)
        if ref.get("primary_role") not in ROLES:
            errors.append(f"reference_roles[{index}].primary_role is invalid")

    duration = payload.get("duration_seconds")
    timeline = payload.get("timeline", [])
    if route in {"video", "bridge"}:
        if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration <= 0:
            errors.append("video and bridge routes require positive duration_seconds")
        if not isinstance(timeline, list) or not timeline:
            errors.append("video and bridge routes require a timeline")
        else:
            previous = 0.0
            for index, beat in enumerate(timeline):
                try:
                    start, end = float(beat["start"]), float(beat["end"])
                except (KeyError, TypeError, ValueError):
                    errors.append(f"timeline[{index}] requires numeric start and end")
                    continue
                if end <= start:
                    errors.append(f"timeline[{index}] end must be greater than start")
                if abs(start - previous) > 0.05:
                    errors.append(f"timeline gap or overlap before beat {index + 1}")
                previous = end
            if isinstance(duration, (int, float)) and abs(previous - float(duration)) > 0.05:
                errors.append("timeline must end at duration_seconds")

    rights = payload.get("rights")
    if not isinstance(rights, dict):
        errors.append("rights must be an object")
    elif roles and not rights.get("references_authorized"):
        errors.append("reference assets require rights.references_authorized=true")

    if not str(payload.get("final_prompt", "")).strip():
        warnings.append("final_prompt is empty")
    if not payload.get("evaluation"):
        warnings.append("evaluation is empty")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate an OpenNana-derived image/video prompt pack.")
    parser.add_argument("path")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(json.dumps({"ok": False, "errors": [str(error)], "warnings": []}, ensure_ascii=False, indent=2))
        return 2
    errors, warnings = validate(payload)
    print(json.dumps({"ok": not errors, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
