---
name: voicebox-studio
description: Operate jamiepine/voicebox as a local-first AI voice studio from Codex for speech generation, transcription, voice profile selection, MCP voice output, and REST integration. Use when the user names Voicebox or wants local voice cloning, TTS, dictation, transcription, or an agent voice workflow.
---

# Voicebox Studio

Voicebox is an external desktop/runtime application. This Skill does not bundle models, voices, or the app itself.

## Start Safely

1. Confirm the platform and install Voicebox from its official release route or source instructions.
2. Start the app and verify the local service at `http://127.0.0.1:17493` before making requests.
3. Keep the service on loopback unless the user intentionally configures authentication and network exposure.
4. List profiles before selecting one. Never assume a profile name or clone a person's voice without authorization.

## Routes

- Generate speech: `POST /generate` with text, profile id, and language.
- Speak as an agent: `POST /speak` with `X-Voicebox-Client-Id`.
- Transcribe: `POST /transcribe` with a user-provided audio file.
- Inspect profiles: `GET /profiles`.
- MCP: connect Codex to `http://127.0.0.1:17493/mcp` when the current client supports HTTP MCP.

Use `voicebox.speak`, `voicebox.transcribe`, `voicebox.list_captures`, and `voicebox.list_profiles` only when those MCP tools are actually available. Verify generated audio exists and is playable; report the profile, language, output path, and any local model download still pending.

Do not use cloned voices for impersonation, deceptive consent, or unauthorized biometric processing. Read `references/source.md` for the inspected source and license.
