---
name: aitoearn-compliance-ops
description: Use when planning, configuring, auditing, or operating AiToEarn content automation with platform-compliant risk controls. Covers Create, Publish, Engage, Monetize workflows, MCP/API setup, official API/OAuth preference, approval gates, rate limits, account health, audit logs, cooldowns, and refusal of ban-evasion tactics.
---

# AiToEarn Compliance Ops

Source analyzed: https://github.com/yikart/AiToEarn

Use this skill for sustainable AiToEarn operations: AI content creation, multi-platform publishing, engagement assistance, creator monetization tasks, and account-risk control. The goal is compliant automation, not bypassing platform defenses.

## Non-Negotiable Safety Boundary

Always reduce risk by respecting platform rules and using conservative automation.

Never help with captcha bypass, phone/email verification bypass, fingerprint spoofing, proxy rotation for evasion, cookie theft, credential sharing, account farming, ban evasion, mass registration, deceptive human simulation, or appeal automation that hides automation abuse.

If a user asks for those tactics, refuse that portion and redirect to compliant alternatives: official APIs, OAuth, lower volume, manual review, content quality, opt-outs, audit logs, and staged rollout.

## AiToEarn Capability Map

- Create: generate drafts, images, video concepts, scripts, and platform-specific variants.
- Publish: schedule and distribute content across supported channels through official integrations where available.
- Engage: assist with comments, replies, lead signals, and brand monitoring. Treat auto-like, auto-follow, auto-comment, and DMs as high-risk write actions.
- Monetize: evaluate tasks, campaign fit, deliverables, and proof requirements before accepting or publishing.
- MCP/API: configure AiToEarn through `x-api-key`; China keys use `aitoearn.cn`, global keys use `aitoearn.ai`. Keep environment and key source matched.
- Docker/Relay: Relay can simplify OAuth credential setup, but it does not remove platform-policy obligations.

## Default Operating Modes

Choose the least risky mode that satisfies the task:

| Mode | Use When | External Writes |
| --- | --- | --- |
| `draft-only` | New account, unknown policy, unverified workflow, sensitive niche | None |
| `semi-auto` | Normal production with human approval | Only after approval |
| `controlled-auto` | Mature account, official channel, healthy metrics, low-risk action | Allowed after risk check |

Unknown platform rules, new accounts, account warnings, login challenges, or unusual API responses always downgrade to `draft-only` or `semi-auto`.

## Required Workflow

1. Identify the action type: `publish`, `reply`, `comment`, `dm`, `like`, `follow`, `collect`, `monitor`, `create`, or `monetize`.
2. Confirm whether the action writes to an external platform. Read-only research and draft generation are lower risk; posting and engagement are higher risk.
3. Load the risk policy:
   - Use `assets/default_policy.json` as the baseline.
   - If the project has a stricter platform policy, use the stricter value.
4. Run the local checker when structured action data is available:
   ```bash
   python3 scripts/risk_check.py --policy assets/default_policy.json --action action.json
   ```
5. Apply the decision:
   - `allow`: proceed only through official API/OAuth/Relay or a platform-permitted integration.
   - `approve`: show the draft/action, risk reasons, and ask for explicit approval before any write.
   - `delay`: schedule after the returned cooldown; do not rush or parallelize.
   - `block`: do not perform the action. Provide the reason and a safer alternative.
6. Log every write-action attempt with platform, account id, content id, operator, decision, timestamp, reason, and platform response.

## Risk Signals To Check

- Platform: published policy unknown, platform warning, 401/403/429, login challenge, OAuth failure, permission failure.
- Account: age under 30 days, incomplete profile, low trust, recent warnings, high failure rate, abnormal verification, recent lock.
- Action: follow, like, comment, DM, bulk publish, cross-post duplicate, high link density, mass tagging, external shortened links.
- Content: duplicate text, copied claims, medical/legal/financial claims without sources, prohibited claims, misleading calls to action, unsafe affiliate or giveaway language.
- Workflow: browser automation for write actions, unapproved headless flows, credential sharing, unsourced scraping, hidden automation.

## Recommended Playbooks

### Publish

Generate draft -> repurpose per platform -> brand voice check -> fact/source check -> metadata check -> risk check -> schedule -> approval if required -> publish -> monitor response.

Use `platform-repurpose`, `brand-voice-guard`, `fact-check-citation`, `content-calendar-planner`, and `publish-metadata-ops` alongside this skill when those tasks are in scope.

### Engage

Collect comments/signals -> classify intent -> draft reply -> risk check -> approve high-risk replies -> send through official channel -> log response.

Default rule: replies can be suggested automatically, but sending replies, likes, follows, DMs, or comments requires `semi-auto` until the account has stable history.

### Multi-Account Operations

Only use multiple accounts for legitimate brands, regions, languages, stores, or business units. Keep calendars, content angles, ownership, and audience purpose distinct. Do not use accounts to create artificial engagement, bypass limits, or spam the same content.

### Monetize Tasks

Before accepting or executing a task, check campaign fit, deliverables, required proof, platform rules, disclosure requirements, brand safety, and whether the requested action would create artificial engagement.

## Incident Response

Immediately pause the account or platform integration when any of these occur:

- HTTP `429`, repeated `401/403`, OAuth challenge, login challenge, captcha, phone/email verification prompt.
- Platform warning, removed content, sudden publish failures, suspicious activity notice.
- Complaint spike, unusual unfollow/report pattern, or high negative reply rate.

Response sequence: stop writes -> save logs -> downgrade to `draft-only` -> review recent actions -> reduce volume or disable the risky action class -> resume only after manual approval.

## Output Format

When asked for an automation plan, return:

- Mode: `draft-only`, `semi-auto`, or `controlled-auto`
- Allowed actions
- Actions requiring approval
- Blocked actions
- Platform/account/content risk notes
- Required logs and rollback steps

When asked to execute or configure, prefer deterministic files and scripts over vague advice, and keep the implementation conservative by default.
