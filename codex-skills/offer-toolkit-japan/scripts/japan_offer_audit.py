#!/usr/bin/env python3
"""Check a structured Japan offer for missing terms and follow-up questions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


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


CORE_FIELDS = {
    "employing_entity": "Confirm the legal employing entity.",
    "employment_type": "Confirm the employment type.",
    "contract_term.fixed": "Confirm whether the contract has a fixed term.",
    "probation.present": "Confirm whether a probation period applies.",
    "job_duties.initial": "Confirm initial job duties.",
    "job_duties.change_scope": "Confirm the scope of possible duty changes.",
    "work_location.initial": "Confirm the initial work location.",
    "work_location.change_scope": "Confirm the scope of possible location changes.",
    "compensation.base_salary": "Confirm base salary separately from variable pay.",
    "compensation.payment_frequency": "Confirm salary payment frequency.",
    "working_time.schedule": "Confirm working hours and schedule.",
    "working_time.breaks": "Confirm break time.",
    "working_time.overtime": "Confirm whether overtime applies and expected scope.",
    "leave.holidays": "Confirm holidays.",
    "leave.annual_paid_leave": "Confirm paid-leave grant timing and amount.",
    "insurance": "Confirm applicable social insurance coverage.",
    "start_date": "Confirm the employment start date.",
}


def audit(data: dict[str, Any]) -> dict[str, Any]:
    missing: list[dict[str, str]] = []
    follow_up: list[str] = []
    warnings: list[str] = []

    for path, question in CORE_FIELDS.items():
        if not present(get(data, path)):
            missing.append({"field": path, "question": question})

    fixed = get(data, "contract_term.fixed")
    if fixed is True:
        for path, question in {
            "contract_term.period": "Confirm the fixed contract period.",
            "contract_term.renewal_criteria": "Confirm renewal criteria.",
            "contract_term.renewal_limit": "Confirm whether a renewal limit applies.",
        }.items():
            if not present(get(data, path)):
                missing.append({"field": path, "question": question})

    probation = get(data, "probation.present")
    if probation is True and not present(get(data, "probation.duration")):
        missing.append(
            {
                "field": "probation.duration",
                "question": "Confirm the probation duration and any different conditions.",
            }
        )

    fixed_overtime = get(data, "compensation.fixed_overtime.included")
    if fixed_overtime is True:
        for path, question in {
            "compensation.fixed_overtime.hours": "Confirm covered overtime hours.",
            "compensation.fixed_overtime.amount": "Confirm the fixed overtime amount.",
            "compensation.fixed_overtime.excess_paid": "Confirm additional payment beyond covered hours.",
        }.items():
            if not present(get(data, path)):
                missing.append({"field": path, "question": question})
        warnings.append("Fixed overtime is included; compare guaranteed base pay separately.")

    system = str(get(data, "working_time.system") or "").lower()
    if "discretion" in system or "裁量" in system:
        if not present(get(data, "working_time.deemed_hours")):
            missing.append(
                {
                    "field": "working_time.deemed_hours",
                    "question": "Confirm deemed working hours for the discretionary-labor system.",
                }
            )

    visa_needed = get(data, "visa_support.needed")
    if visa_needed is True:
        if not present(get(data, "visa_support.details")):
            follow_up.append("Get written details of status-of-residence support.")
        if not present(get(data, "visa_support.responsible_party")):
            follow_up.append("Confirm who owns the immigration process and document preparation.")

    if not present(get(data, "compensation.bonus.details")):
        follow_up.append("Clarify bonus eligibility, calculation, timing, and whether it is discretionary.")
    if not present(get(data, "work_location.transfer_expectation")):
        follow_up.append("Clarify transfer and relocation expectations.")
    if not present(get(data, "work_location.remote_policy")):
        follow_up.append("Clarify remote/hybrid conditions and whether they are contractual or policy-based.")

    supplied_questions = get(data, "open_questions")
    if isinstance(supplied_questions, list):
        follow_up.extend(str(item) for item in supplied_questions if present(item))

    status = "complete_for_review"
    if missing:
        status = "needs_clarification"
    if len(missing) >= 6:
        status = "critical_terms_missing"

    return {
        "status": status,
        "missing_count": len(missing),
        "missing": missing,
        "follow_up": list(dict.fromkeys(follow_up)),
        "warnings": warnings,
        "disclaimer": "Completeness check only; not legal, labor, tax, or immigration advice.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("offer_json", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.offer_json.read_text(encoding="utf-8"))
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
