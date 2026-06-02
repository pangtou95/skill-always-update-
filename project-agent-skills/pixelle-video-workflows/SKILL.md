---
name: pixelle-video-workflows
description: Use when installing, configuring, running, debugging, extending, packaging, or using AIDC-AI/Pixelle-Video, an AI automated short-video engine with Streamlit WebUI, FastAPI REST API, ComfyUI/RunningHub workflows, direct image/video model APIs, TTS, HTML templates, BGM, and video composition.
---

# Pixelle-Video Workflows

Source analyzed: https://github.com/AIDC-AI/Pixelle-Video

Use this skill for Pixelle-Video setup, WebUI/API operation, Docker deployment, provider configuration, video generation, template/workflow customization, and troubleshooting.

## What This Skill Can And Cannot Do

This skill can guide Codex to install and operate Pixelle-Video, edit its configuration, add templates/workflows, call its API, and debug failures.

This skill does not bundle model weights, API keys, ComfyUI models, RunningHub credentials, or paid provider access. Pixelle-Video is an orchestration engine; actual generation depends on configured LLM, image/video, TTS, ComfyUI, RunningHub, or direct API providers.

## Repository Shape

- Web UI: `web/app.py`, `web/pages/`, `web/utils/`, `web/i18n/`.
- FastAPI backend: `api/app.py`, `api/routers/`, `api/schemas/`, `api/tasks/`.
- Core services: `pixelle_video/services/`.
- Provider clients: `pixelle_video/services/api_services/`.
- Built-in workflows: `workflows/selfhost/` and `workflows/runninghub/`.
- HTML frame templates: `templates/<width>x<height>/`.
- Default BGM: `bgm/default.mp3`.
- Example config: `config.example.yaml`.
- Docker deployment: `Dockerfile`, `docker-compose.yml`, `docker-start.sh`.
- Windows package tooling: `packaging/windows/`.
- Docs: `docs/`, `README.md`, `README_EN.md`.

## Core Product Model

Pixelle-Video creates short videos from a topic or fixed script:

1. Generate or accept narration/script.
2. Plan scene/frame content.
3. Generate images or video clips through a selected workflow/provider.
4. Generate narration audio through TTS.
5. Render HTML frame templates.
6. Compose final video with BGM and media.
7. Store output under `output/`.

Supported modes:

- `generate`: LLM writes the script from a topic.
- `fixed`: user provides a complete script.

## Quick Source Install

Requirements:

- Python `>=3.11`.
- `uv`.
- `ffmpeg`.
- Browser dependencies for Playwright/Chromium when frame rendering needs them.

Common setup:

```bash
git clone https://github.com/AIDC-AI/Pixelle-Video.git
cd Pixelle-Video
cp config.example.yaml config.yaml
uv run streamlit run web/app.py
```

The WebUI opens at `http://localhost:8501`.

Start the API server:

```bash
uv run python api/app.py --host 0.0.0.0 --port 8000
```

Swagger docs are available at `http://localhost:8000/docs`.

## Docker Deployment

Use Docker when the user wants a packaged service or reproducible deployment:

```bash
cp config.example.yaml config.yaml
docker compose up -d --build
```

Or use the helper:

```bash
bash docker-start.sh
```

Ports:

- WebUI: `http://localhost:8501`
- API: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`

For China mirror builds:

```bash
USE_CN_MIRROR=true docker compose up -d --build
```

Docker volumes persist:

- `config.yaml`
- `data/`
- `output/`

For local ComfyUI from Docker:

- Mac/Windows: use `host.docker.internal:8188`.
- Linux: use the host IP address or a shared Docker network.

## Configuration Workflow

Never commit `config.yaml` with secrets. Start from `config.example.yaml`.

Main sections:

- `llm`: OpenAI-compatible API key, base URL, and model for script generation.
- `api_providers`: direct image/video/VLM providers such as OpenAI, DashScope, Volcengine ARK/Seedream/Seedance, and Kling.
- `comfyui`: local ComfyUI URL, optional ComfyUI API key, RunningHub API key, and concurrency.
- `comfyui.image`: default image workflow and prompt prefix.
- `comfyui.video`: default video workflow and prompt prefix.
- `comfyui.tts`: default TTS workflow.
- `template`: default HTML frame template.

Common LLM presets:

```yaml
llm:
  api_key: "..."
  base_url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
  model: "qwen-max"
```

```yaml
llm:
  api_key: "..."
  base_url: "https://api.openai.com/v1"
  model: "gpt-4o"
```

```yaml
llm:
  api_key: "..."
  base_url: "http://localhost:11434/v1"
  model: "llama3.2"
```

## Workflow Selection

Workflow files live in:

- `workflows/selfhost/`: local ComfyUI workflows.
- `workflows/runninghub/`: cloud RunningHub workflows.

Representative workflows:

- TTS: `selfhost/tts_edge.json`, `selfhost/tts_index2.json`, `runninghub/tts_edge.json`.
- Image: `selfhost/image_flux.json`, `selfhost/image_qwen.json`, `runninghub/image_flux.json`, `runninghub/image_sdxl.json`.
- Video: `selfhost/video_wan2.1_fusionx.json`, `runninghub/video_wan2.1_fusionx.json`, `runninghub/video_wan2.2.json`.
- Analysis: `selfhost/analyse_image.json`, `selfhost/analyse_video.json`, `runninghub/video_understanding.json`.

If a workflow path begins with `api/...`, verify that the matching provider credentials are configured under `api_providers`.

## Template Work

Templates live under `templates/<resolution>/`.

Naming convention:

- `static_*.html`: static text/layout templates with no generated media.
- `image_*.html`: templates requiring generated images.
- `video_*.html`: templates requiring generated video clips.

Common dimensions:

- `1080x1920`: portrait/short-video.
- `1920x1080`: landscape.
- `1080x1080`: square.

When editing templates:

1. Preserve template metadata used to derive media size.
2. Keep text readable at target video resolution.
3. Test with template preview before full generation.
4. Keep assets local or URL-stable.
5. Add custom templates under `data/templates/` for Docker deployments when overriding built-ins.

## REST API Usage

Start API:

```bash
uv run uvicorn api.app:app --host 0.0.0.0 --port 8000
```

Health:

```bash
curl http://localhost:8000/health
```

Synchronous video generation for short jobs:

```bash
curl -X POST http://localhost:8000/api/video/generate/sync \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Why you should develop a reading habit",
    "mode": "generate",
    "n_scenes": 5,
    "frame_template": "1080x1920/image_default.html",
    "title": "The Power of Reading"
  }'
```

Asynchronous generation for longer jobs:

```bash
curl -X POST http://localhost:8000/api/video/generate/async \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Why humans love stories",
    "mode": "generate",
    "n_scenes": 8,
    "frame_template": "1080x1920/image_default.html"
  }'
```

Then poll:

```bash
curl http://localhost:8000/api/tasks/<task_id>
```

Useful request fields:

- `text`: topic or full script.
- `mode`: `generate` or `fixed`.
- `n_scenes`: scene count, usually `1-20`.
- `title`: optional title.
- `frame_template`: e.g. `1080x1920/image_default.html`.
- `media_workflow`: image or video workflow.
- `tts_workflow`: TTS workflow.
- `ref_audio`: path for voice cloning workflows.
- `prompt_prefix`: image/video style prefix.
- `bgm_path`: BGM path.
- `bgm_volume`: `0.0-1.0`.
- `template_params`: custom HTML template parameters.

## WebUI Usage Checklist

On first run:

1. Expand system configuration.
2. Configure LLM provider.
3. Configure one media path:
   - local ComfyUI,
   - RunningHub,
   - or direct API provider.
4. Choose TTS workflow.
5. Choose image/video workflow.
6. Choose frame template.
7. Choose generation mode: AI-generated script or fixed script.
8. Generate and inspect `output/`.

## Custom Media And Resources

User-overridable resources:

- `data/bgm/`: custom background music.
- `data/templates/`: custom templates.
- `data/workflows/`: custom ComfyUI or RunningHub workflows.
- `output/`: generated videos.

Keep secrets in `config.yaml` or environment-specific secret storage, not in committed templates/workflows.

## Troubleshooting

If WebUI does not start:

1. Check Python version.
2. Check `uv --version`.
3. Check `ffmpeg -version`.
4. Run from repository root.
5. Inspect Streamlit logs.

If frame rendering fails:

1. Ensure Playwright Chromium is installed.
2. Re-run dependency install with `uv run playwright install --with-deps chromium` when needed.
3. Check template HTML and media dimensions.

If generation hangs or fails:

1. Check LLM config first.
2. Verify ComfyUI or RunningHub connectivity.
3. Confirm provider keys and base URLs.
4. Reduce `n_scenes`.
5. Use async API for longer jobs.
6. Inspect `output/`, `data/`, and terminal logs.

If Docker cannot reach local ComfyUI:

1. Use `host.docker.internal:8188` on Mac/Windows.
2. Use host IP or Docker networking on Linux.
3. Test the ComfyUI URL from inside the container.

If API returns a local file path instead of a usable URL:

1. Use the documented `/api/files/...` endpoint.
2. Check that `output/` is mounted and readable.
3. Confirm request host/proxy headers if behind a reverse proxy.

## Safety And Cost Discipline

- Do not commit API keys.
- Warn users that OpenAI, DashScope, ARK, Kling, RunningHub, and similar providers may incur costs.
- For free/local operation, prefer Ollama for LLM and local ComfyUI for media generation when the machine can support it.
- Respect provider content policies, copyright, likeness, and voice-cloning consent requirements.

