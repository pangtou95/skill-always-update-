# AiToEarn Compliance Implementation Notes

## Integration Points

- MCP/API usage requires an AiToEarn API key and an environment-matched endpoint:
  - Global: `https://aitoearn.ai/api/unified/mcp`
  - China: `https://aitoearn.cn/api/unified/mcp`
- Use the `x-api-key` header for MCP clients.
- For self-hosted Docker deployments, configure Relay only with an API key from the same environment as `RELAY_SERVER_URL`.
- Prefer official API/OAuth/Relay integrations over browser automation for write actions.

## Minimal Action JSON

```json
{
  "platform": "x",
  "action_type": "publish",
  "mode": "semi-auto",
  "method": "official_api",
  "account": {
    "age_days": 45,
    "recent_warnings": 0
  },
  "recent": {
    "publish_today": 1,
    "engagement_today": 0,
    "minutes_since_last_write": 90,
    "failure_rate": 0.02
  },
  "platform_state": {
    "status_code": 200,
    "login_challenge": false,
    "captcha": false,
    "verification_required": false
  },
  "content": {
    "text": "Platform-specific draft text.",
    "duplicate_similarity": 0.2
  }
}
```

## Audit Log Fields

Capture at least:

- `timestamp`
- `operator`
- `platform`
- `account_id`
- `content_id`
- `action_type`
- `mode`
- `risk_decision`
- `risk_reasons`
- `approval_id`
- `external_request_id`
- `platform_status_code`
- `platform_response_summary`
- `rollback_or_pause_action`

Do not store raw passwords, session cookies, one-time codes, private tokens, or unredacted personal contact data in logs.

## Conservative Defaults

When the platform or account status is unknown, use `draft-only`. When a write action is needed, require approval. When a platform returns a warning, challenge, or rate limit, stop writes and review the account before resuming.
