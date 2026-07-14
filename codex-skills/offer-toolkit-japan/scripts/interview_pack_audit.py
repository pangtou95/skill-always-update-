#!/usr/bin/env python3
"""Audit a structured Japan interview pack for coverage and claim boundaries."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TARGET = ("company", "role", "stage", "language")

REQUIRED_COVERAGE = {
    "self_intro": "Prepare a concise self-introduction.",
    "career_summary": "Prepare a coherent career summary.",
    "each_job_join_leave": "Explain why the candidate joined and left every employer.",
    "why_company_role_now": "Connect why this company, role, and timing.",
    "strength_with_evidence": "Support strengths with verified evidence.",
    "hardest_project": "Prepare the hardest-project story and personal role.",
    "failure_learning": "Prepare a failure and observable learning story.",
    "teamwork_conflict": "Prepare teamwork or conflict evidence.",
    "leadership_boundary": "State the exact leadership and decision-right boundary.",
    "technical_or_role_depth": "Prepare the role-specific technical or case overlay.",
    "career_plan": "Prepare a realistic three-to-five-year direction.",
    "reverse_questions": "Prepare targeted reverse questions.",
}

LEADERSHIP_LEVELS = {
    "none",
    "observed",
    "assisted",
    "task_owner",
    "main_implementer",
    "workstream_coordinator",
    "formal_pl_pm",
    "people_manager",
}

DELIVERY_LEVELS = {
    "study",
    "prototype",
    "poc",
    "internal_tool",
    "production_workflow",
    "customer_production_system",
}


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def get(data: dict[str, Any], path: str) -> Any:
    value: Any = data
    for key in path.split("."):
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def add_missing(missing: list[dict[str, str]], field: str, action: str) -> None:
    missing.append({"field": field, "action": action})


def audit(data: dict[str, Any]) -> dict[str, Any]:
    missing: list[dict[str, str]] = []
    warnings: list[str] = []

    for field in REQUIRED_TARGET:
        if not present(get(data, f"target.{field}")):
            add_missing(missing, f"target.{field}", f"Set the target {field}.")

    for field, action in REQUIRED_COVERAGE.items():
        if get(data, f"coverage.{field}") is not True:
            add_missing(missing, f"coverage.{field}", action)

    risks = get(data, "profile_risks") or {}
    conditional = []
    if isinstance(risks, dict):
        if risks.get("short_tenure") is True:
            conditional.append(("short_tenure_explanation", "Prepare objective facts, reflection, and recurrence prevention."))
        if risks.get("career_changes") is True:
            conditional.append(("career_consistency", "Prepare an evidence-backed career axis."))
        if risks.get("foreign_candidate") is True:
            conditional.extend(
                [
                    ("why_japan", "Prepare a job-relevant reason for working in Japan."),
                    ("work_language_examples", "Prepare examples of practical work communication."),
                    ("residence_status_logistics", "Confirm residence-status and start-date logistics."),
                ]
            )
        if risks.get("lesser_known_certification") is True:
            conditional.append(("certification_explanation", "Explain issuer, domain, topics, and official level without false equivalence."))

    for field, action in conditional:
        if get(data, f"coverage.{field}") is not True:
            add_missing(missing, f"coverage.{field}", action)

    people_claimed = get(data, "claim_boundaries.formal_people_management.claimed")
    direct_reports = get(data, "claim_boundaries.formal_people_management.direct_reports")
    people_evidence = get(data, "claim_boundaries.formal_people_management.evidence_refs")
    if people_claimed is True:
        if not isinstance(direct_reports, int) or direct_reports <= 0:
            add_missing(
                missing,
                "claim_boundaries.formal_people_management.direct_reports",
                "A people-management claim requires a verified positive direct-report count.",
            )
        if not present(people_evidence):
            add_missing(
                missing,
                "claim_boundaries.formal_people_management.evidence_refs",
                "Attach evidence for formal people-management authority.",
            )

    leadership = get(data, "claim_boundaries.project_leadership.level")
    if leadership not in LEADERSHIP_LEVELS:
        add_missing(
            missing,
            "claim_boundaries.project_leadership.level",
            "Use a supported leadership level.",
        )
    elif leadership not in {"none", "observed"} and not present(
        get(data, "claim_boundaries.project_leadership.evidence_refs")
    ):
        add_missing(
            missing,
            "claim_boundaries.project_leadership.evidence_refs",
            "Attach evidence for the selected project-leadership level.",
        )

    delivery = get(data, "claim_boundaries.delivery.level")
    if delivery not in DELIVERY_LEVELS:
        add_missing(
            missing,
            "claim_boundaries.delivery.level",
            "Use a supported delivery level.",
        )
    elif delivery in {"production_workflow", "customer_production_system"}:
        for field, action in {
            "actual_users": "Identify actual users or a verified usage group.",
            "operations_owner": "Identify the production operations owner.",
            "failure_handling": "Explain failure detection and handling.",
            "evidence_refs": "Attach evidence supporting the production-use claim.",
        }.items():
            if not present(get(data, f"claim_boundaries.delivery.{field}")):
                add_missing(missing, f"claim_boundaries.delivery.{field}", action)

    ai_used = get(data, "claim_boundaries.ai_use.used")
    if ai_used is True:
        for field, action in {
            "human_owned_steps": "List human-owned decisions and implementation steps.",
            "ai_assisted_steps": "List the steps assisted by AI.",
            "verification": "Explain human verification and accountability.",
        }.items():
            if not present(get(data, f"claim_boundaries.ai_use.{field}")):
                add_missing(missing, f"claim_boundaries.ai_use.{field}", action)

    equivalence = get(data, "claim_boundaries.certification_comparison.equivalence_status")
    if equivalence == "claimed_equivalent" and not present(
        get(data, "claim_boundaries.certification_comparison.official_mapping_source")
    ):
        add_missing(
            missing,
            "claim_boundaries.certification_comparison.official_mapping_source",
            "Do not claim certification equivalence without an official mapping source.",
        )

    answers = get(data, "answers")
    if not isinstance(answers, list) or not answers:
        add_missing(missing, "answers", "Add structured answer cards.")
    else:
        seen: set[str] = set()
        for index, answer in enumerate(answers):
            prefix = f"answers[{index}]"
            if not isinstance(answer, dict):
                add_missing(missing, prefix, "Each answer must be an object.")
                continue
            question_id = answer.get("question_id")
            if not present(question_id):
                add_missing(missing, f"{prefix}.question_id", "Set a question-bank ID.")
            elif str(question_id) in seen:
                warnings.append(f"Duplicate question_id: {question_id}")
            else:
                seen.add(str(question_id))
            if answer.get("facts_verified") is not True:
                add_missing(missing, f"{prefix}.facts_verified", "Verify all factual claims.")
            if not present(answer.get("evidence_refs")):
                add_missing(missing, f"{prefix}.evidence_refs", "Attach one or more evidence references.")
            versions = answer.get("spoken_versions")
            if not isinstance(versions, dict):
                add_missing(missing, f"{prefix}.spoken_versions", "Add spoken answer versions.")
            else:
                for duration in ("20s", "60s"):
                    if not present(versions.get(duration)):
                        add_missing(
                            missing,
                            f"{prefix}.spoken_versions.{duration}",
                            f"Prepare the {duration} spoken version.",
                        )
            if not present(answer.get("follow_ups")):
                warnings.append(f"{question_id or prefix} has no follow-up branches.")

    status = "ready_for_mock_interview"
    if missing:
        status = "needs_clarification"
    if len(missing) >= 8:
        status = "critical_gaps"

    return {
        "status": status,
        "missing_count": len(missing),
        "missing": missing,
        "warnings": warnings,
        "disclaimer": "Completeness and claim-boundary audit only; it does not predict interview success.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("interview_pack_json", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.interview_pack_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print(json.dumps({"error": "Root JSON value must be an object."}), file=sys.stderr)
        return 2

    print(json.dumps(audit(data), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
