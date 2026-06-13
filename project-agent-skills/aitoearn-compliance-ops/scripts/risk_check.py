#!/usr/bin/env python3
"""Local risk gate for AiToEarn-style operations.

The script is intentionally offline. It evaluates structured action metadata
against a conservative policy and returns one of: allow, approve, delay, block.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def load_json(path: str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalized_action(value: Any) -> str:
    return str(value or "unknown").strip().lower().replace("-", "_")


def count_links(text: str) -> int:
    return len(re.findall(r"https?://|www\\.", text, flags=re.IGNORECASE))


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate an AiToEarn operation before execution.")
    parser.add_argument("--policy", required=True, help="Path to policy JSON.")
    parser.add_argument("--action", required=True, help="Path to action JSON.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    policy = load_json(args.policy)
    action = load_json(args.action)

    platform = str(action.get("platform") or "unknown").strip().lower()
    action_type = normalized_action(action.get("action_type"))
    mode = normalized_action(action.get("mode") or policy.get("default_mode"))
    method = normalized_action(action.get("method"))
    platform_policy = policy.get("platform_defaults", {}).get(
        platform,
        policy.get("platform_defaults", {}).get("unknown", {}),
    )

    account = action.get("account", {}) or {}
    recent = action.get("recent", {}) or {}
    content = action.get("content", {}) or {}
    platform_state = action.get("platform_state", {}) or {}

    reasons: list[str] = []
    cooldown_minutes = 0
    decision = "allow"

    if method in set(policy.get("blocked_methods", [])):
        decision = max_decision(decision, "block")
        reasons.append(f"blocked method: {method}")

    if platform_state.get("login_challenge") or platform_state.get("captcha") or platform_state.get("verification_required"):
        decision = max_decision(decision, "block")
        cooldown_minutes = max(cooldown_minutes, policy.get("cooldowns", {}).get("login_challenge_minutes", 10080))
        reasons.append("platform login/challenge/verification signal")

    if int(platform_state.get("status_code") or 0) == 429:
        decision = max_decision(decision, "delay")
        cooldown_minutes = max(cooldown_minutes, policy.get("cooldowns", {}).get("rate_limit_minutes", 1440))
        reasons.append("platform returned 429 rate limit")

    if int(account.get("age_days") or 0) < int(policy.get("new_account_days", 30)):
        decision = max_decision(decision, "approve")
        reasons.append("new account requires conservative approval")

    if int(account.get("recent_warnings") or 0) > int(policy.get("max_recent_warning_count", 0)):
        decision = max_decision(decision, "delay")
        cooldown_minutes = max(cooldown_minutes, policy.get("cooldowns", {}).get("warning_minutes", 10080))
        reasons.append("recent platform/account warning")

    if float(recent.get("failure_rate") or 0.0) > float(policy.get("max_recent_failure_rate", 0.15)):
        decision = max_decision(decision, "approve")
        reasons.append("recent failure rate above policy threshold")

    write_actions = set(policy.get("write_actions", []))
    if action_type in write_actions:
        if mode == "draft_only":
            decision = max_decision(decision, "approve")
            reasons.append("draft-only mode blocks direct external writes")
        if platform_policy.get("requires_approval", True):
            decision = max_decision(decision, "approve")
            reasons.append("platform policy requires approval for writes")

    if action_type == "publish" and int(recent.get("publish_today") or 0) >= int(platform_policy.get("max_publish_per_day", 1)):
        decision = max_decision(decision, "delay")
        cooldown_minutes = max(cooldown_minutes, 24 * 60)
        reasons.append("daily publish limit reached")

    if action_type in {"reply", "comment", "dm", "like", "follow"}:
        if int(recent.get("engagement_today") or 0) >= int(platform_policy.get("max_engagement_per_day", 0)):
            decision = max_decision(decision, "delay")
            cooldown_minutes = max(cooldown_minutes, 24 * 60)
            reasons.append("daily engagement limit reached")

    minutes_since_write = recent.get("minutes_since_last_write")
    if minutes_since_write is not None and int(minutes_since_write) < int(platform_policy.get("min_minutes_between_writes", 240)):
        decision = max_decision(decision, "delay")
        cooldown_minutes = max(
            cooldown_minutes,
            int(platform_policy.get("min_minutes_between_writes", 240)) - int(minutes_since_write),
        )
        reasons.append("minimum spacing between write actions not met")

    text = str(content.get("text") or "")
    if count_links(text) > int(policy.get("max_links_per_post", 2)):
        decision = max_decision(decision, "approve")
        reasons.append("too many links in content")

    if float(content.get("duplicate_similarity") or 0.0) > float(policy.get("max_duplicate_similarity", 0.86)):
        decision = max_decision(decision, "approve")
        reasons.append("content duplicate similarity above threshold")

    lowered_text = text.lower()
    matched_terms = [term for term in policy.get("sensitive_terms", []) if str(term).lower() in lowered_text]
    if matched_terms:
        decision = max_decision(decision, "approve")
        reasons.append("sensitive claim terms require review: " + ", ".join(matched_terms[:5]))

    if not reasons:
        reasons.append("no policy threshold triggered")

    output = {
        "decision": decision,
        "mode": mode,
        "platform": platform,
        "action_type": action_type,
        "cooldown_minutes": cooldown_minutes,
        "reasons": reasons,
        "next_step": policy.get("decisions", {}).get(decision, ""),
    }

    print(json.dumps(output, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


def max_decision(current: str, candidate: str) -> str:
    order = {"allow": 0, "approve": 1, "delay": 2, "block": 3}
    return candidate if order[candidate] > order.get(current, 0) else current


if __name__ == "__main__":
    raise SystemExit(main())
