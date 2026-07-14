#!/usr/bin/env python3
"""Audit a structured Video Director Studio production pack."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


RIGHTS_VALUES = {"owned", "licensed", "public-domain", "authorized", "unknown"}
EXECUTION_VALUES = {"prompt-only", "planned", "generating", "completed"}


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def get_path(data: dict[str, Any], path: str) -> Any:
    current: Any = data
    for key in path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def audit(pack: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    required_paths = [
        "schema_version",
        "execution.status",
        "brief.objective",
        "brief.audience",
        "brief.platform",
        "brief.duration_sec",
        "brief.aspect_ratio",
        "director_profile.format_id",
        "director_profile.primary_grammar_id",
        "director_profile.composition",
        "director_profile.lens",
        "director_profile.camera",
        "director_profile.palette",
        "director_profile.lighting",
        "director_profile.performance",
        "director_profile.edit",
        "director_profile.sound",
        "creative.premise",
        "creative.hook",
        "creative.payoff",
        "modules",
        "shots",
    ]
    for path in required_paths:
        if not nonempty(get_path(pack, path)):
            errors.append(f"missing required field: {path}")

    execution = pack.get("execution") if isinstance(pack.get("execution"), dict) else {}
    status = execution.get("status")
    if status not in EXECUTION_VALUES:
        errors.append(f"execution.status must be one of {sorted(EXECUTION_VALUES)}")
    if status in {"generating", "completed"}:
        for key in ("provider", "model", "verified_at"):
            if not nonempty(execution.get(key)):
                errors.append(f"execution.{key} is required when status is {status}")

    brief = pack.get("brief") if isinstance(pack.get("brief"), dict) else {}
    duration = brief.get("duration_sec")
    if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration <= 0:
        errors.append("brief.duration_sec must be a positive number")

    profile = pack.get("director_profile") if isinstance(pack.get("director_profile"), dict) else {}
    if nonempty(profile.get("format_id")) and not str(profile["format_id"]).startswith("F-"):
        errors.append("director_profile.format_id must use an F-* blueprint ID")
    if nonempty(profile.get("primary_grammar_id")) and not str(profile["primary_grammar_id"]).startswith("G-"):
        errors.append("director_profile.primary_grammar_id must use a G-* grammar ID")
    accent = profile.get("accent_grammar_id")
    if nonempty(accent) and not str(accent).startswith("G-"):
        errors.append("director_profile.accent_grammar_id must be empty or use a G-* grammar ID")
    if profile.get("named_influences") and not profile.get("trait_translation"):
        errors.append("named influences require director_profile.trait_translation")

    modules = pack.get("modules")
    if isinstance(modules, list):
        invalid = [module for module in modules if not isinstance(module, str) or not module.startswith("M-")]
        if invalid:
            errors.append(f"invalid module IDs: {invalid}")
        for base in ("M-BRIEF", "M-RIGHTS", "M-LOOK", "M-QC"):
            if base not in modules:
                warnings.append(f"recommended base module missing: {base}")
    elif modules is not None:
        errors.append("modules must be an array")

    assets = pack.get("asset_register") or []
    if not isinstance(assets, list):
        errors.append("asset_register must be an array")
        assets = []
    asset_ids: set[str] = set()
    for index, asset in enumerate(assets):
        prefix = f"asset_register[{index}]"
        if not isinstance(asset, dict):
            errors.append(f"{prefix} must be an object")
            continue
        asset_id = asset.get("id")
        if not nonempty(asset_id):
            errors.append(f"{prefix}.id is required")
        elif asset_id in asset_ids:
            errors.append(f"duplicate asset id: {asset_id}")
        else:
            asset_ids.add(str(asset_id))
        for key in ("type", "role", "rights_status"):
            if not nonempty(asset.get(key)):
                errors.append(f"{prefix}.{key} is required")
        rights = asset.get("rights_status")
        if nonempty(rights) and rights not in RIGHTS_VALUES:
            errors.append(f"{prefix}.rights_status must be one of {sorted(RIGHTS_VALUES)}")
        if rights == "unknown":
            message = f"{prefix} has unresolved rights"
            (errors if status in {"generating", "completed"} else warnings).append(message)

    shots = pack.get("shots") or []
    if not isinstance(shots, list):
        errors.append("shots must be an array")
        shots = []
    shot_ids: list[str] = []
    shot_duration = 0.0
    shot_required = [
        "id",
        "editorial_function",
        "duration_sec",
        "opening_state",
        "visible_beat",
        "physical_consequence",
        "performance",
        "motivated_light",
        "audio",
        "end_state",
        "positive_prompt",
        "negative_constraints",
    ]
    camera_required = ["framing", "lens_intent", "primary_move", "endpoint"]
    for index, shot in enumerate(shots):
        prefix = f"shots[{index}]"
        if not isinstance(shot, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for key in shot_required:
            if not nonempty(shot.get(key)):
                errors.append(f"{prefix}.{key} is required")
        shot_id = shot.get("id")
        if nonempty(shot_id):
            if str(shot_id) in shot_ids:
                errors.append(f"duplicate shot id: {shot_id}")
            shot_ids.append(str(shot_id))
        shot_seconds = shot.get("duration_sec")
        if not isinstance(shot_seconds, (int, float)) or isinstance(shot_seconds, bool) or shot_seconds <= 0:
            errors.append(f"{prefix}.duration_sec must be a positive number")
        else:
            shot_duration += float(shot_seconds)
        camera = shot.get("camera")
        if not isinstance(camera, dict):
            errors.append(f"{prefix}.camera must be an object")
        else:
            for key in camera_required:
                if not nonempty(camera.get(key)):
                    errors.append(f"{prefix}.camera.{key} is required")
        negatives = shot.get("negative_constraints")
        if negatives is not None and not isinstance(negatives, list):
            errors.append(f"{prefix}.negative_constraints must be an array")

    if isinstance(duration, (int, float)) and not isinstance(duration, bool) and duration > 0 and shots:
        tolerance = max(0.5, min(1.0, float(duration) * 0.03))
        if not math.isclose(shot_duration, float(duration), abs_tol=tolerance):
            errors.append(
                f"shot durations total {shot_duration:g}s but brief.duration_sec is {duration:g}s "
                f"(tolerance {tolerance:g}s)"
            )

    if len(shots) > 1 and not pack.get("continuity_anchors"):
        warnings.append("multi-shot packs should define continuity_anchors")

    edit_plan = pack.get("edit_plan")
    if isinstance(edit_plan, dict):
        order = edit_plan.get("order") or []
        if not isinstance(order, list):
            errors.append("edit_plan.order must be an array")
        else:
            missing = [shot_id for shot_id in shot_ids if shot_id not in order]
            unknown = [shot_id for shot_id in order if shot_id not in shot_ids]
            if missing:
                errors.append(f"edit_plan.order is missing shots: {missing}")
            if unknown:
                errors.append(f"edit_plan.order contains unknown shots: {unknown}")
    else:
        warnings.append("edit_plan is missing")

    if not pack.get("sources"):
        warnings.append("sources are missing; record research and reference provenance")

    if errors:
        result_status = "needs_work"
    elif status == "prompt-only":
        result_status = "ready_prompt_only"
    else:
        result_status = "ready_for_generation"
    return {
        "status": result_status,
        "error_count": len(errors),
        "warning_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
        "metrics": {
            "shots": len(shots),
            "assets": len(assets),
            "planned_duration_sec": duration,
            "shot_duration_sec": shot_duration,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        pack = json.loads(args.pack.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "invalid_json", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    if not isinstance(pack, dict):
        print(json.dumps({"status": "invalid_pack", "error": "top-level JSON must be an object"}, indent=2))
        return 2
    result = audit(pack)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] != "needs_work" else 1


if __name__ == "__main__":
    raise SystemExit(main())
