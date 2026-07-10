# ChatCut Plugin Setup

Use this reference only when ChatCut MCP tools are missing, unauthenticated, or unclear.

## MCP server

The upstream ChatCut plugin connects Codex to this hosted MCP endpoint:

```json
{
  "mcpServers": {
    "chatcut": {
      "url": "https://api.chatcut.io/api/external-mcp/mcp",
      "oauth_resource": "https://api.chatcut.io/api/external-mcp/mcp",
      "http_headers": {
        "x-chatcut-mcp-surface": "codex"
      }
    }
  }
}
```

## Runtime checks

1. Check whether Codex already knows the server:

```bash
codex mcp get chatcut
```

2. If the server exists but is not authenticated, run:

```bash
codex mcp login chatcut
```

3. If the server is missing, install the full ChatCut plugin from:

```text
https://github.com/ChatCut-Inc/agent-plugin.git
```

## Boundaries

- Do not guess hidden ChatCut project, asset, timeline, or account IDs.
- Do not write directly to ChatCut databases or storage.
- Use the MCP tool schema as the runtime contract; these skills provide workflow guidance, not a replacement for the live tool manifest.
- If MCP auth fails, ask the user to complete the ChatCut sign-in flow before attempting project edits.
