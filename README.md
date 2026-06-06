# My AI Skills Library

This repository is a curated export of local Codex / AI Agent skills. It collects reusable skill instructions for research engineering, model training, inference, RAG, agents, frontend design, media generation, automation, and project-specific workflows.

In practice, each skill is a professional operating guide for an AI agent. A `SKILL.md` tells the agent when the skill should trigger, what workflow to follow, which files or tools to inspect, and what kind of output to produce. The goal is to make one general agent behave more like a domain-aware specialist when a task matches a known area.

Chinese version: [README.cn.md](README.cn.md)

## What Is Included

The repository is organized into three exported skill groups:

```text
.
├── codex-skills/            # Global Codex skills, including AI research, ML engineering, frontend, design, and media workflows
├── project-agent-skills/    # Project-level agent skills, including Runway, Seedance, scraping, career ops, and repository-derived skills
├── user-agent-skills/       # User-level agent skills
├── SKILLS_MANIFEST.txt      # Generated list of all SKILL.md files
├── README.md
└── README.cn.md
```

Symlinks were dereferenced during export, so cloned copies contain real files instead of local-machine-only links.

## Capability Map

| Area | Representative skills | What they help an agent do |
| --- | --- | --- |
| Model training and fine-tuning | `axolotl`, `llama-factory`, `peft`, `unsloth`, `trl-fine-tuning` | Plan SFT, LoRA, QLoRA, DPO, data formats, training configs, and training issue triage |
| Post-training and RL | `verl`, `openrlhf`, `grpo-rl-training`, `simpo`, `slime`, `torchforge` | Design RLHF, DPO, GRPO, SimPO workflows, reward analysis, rollouts, memory, and throughput debugging |
| Inference and deployment | `vllm`, `sglang`, `llama-cpp`, `tensorrt-llm`, `speculative-decoding` | Deploy OpenAI-compatible model services and optimize latency, throughput, batching, KV cache, and quantization |
| Distributed training | `deepspeed`, `accelerate`, `megatron-core`, `pytorch-fsdp2`, `ray-train`, `torchtitan` | Work through multi-GPU training, FSDP, ZeRO, pipeline/tensor parallelism, checkpoints, and performance tuning |
| Compression and optimization | `awq`, `gptq`, `gguf`, `bitsandbytes`, `hqq`, `flash-attention` | Quantize models, convert formats, reduce memory use, and improve inference speed |
| Architectures and research systems | `nanogpt`, `litgpt`, `mamba`, `rwkv`, `moe-training`, `long-context` | Explore Transformer variants, Mamba, RWKV, MoE, long-context methods, merging, pruning, and distillation |
| Data and evaluation | `nemo-curator`, `ray-data`, `lm-evaluation-harness`, `bigcode-evaluation-harness`, `nemo-evaluator` | Build data pipelines, clean datasets, run benchmarks, evaluate code models, and track experiments |
| RAG and vector databases | `faiss`, `qdrant`, `chroma`, `pinecone`, `sentence-transformers` | Design chunking, embeddings, indexing, retrieval, reranking, and vector database integrations |
| Agents and workflow automation | `langchain`, `llamaindex`, `crewai`, `autogpt`, `a-evolve` | Build multi-agent workflows, tool calling, task planning, knowledge-base QA, and autonomous research loops |
| Prompting and structured output | `dspy`, `guidance`, `outlines`, `instructor` | Create controlled prompts, structured JSON output, constrained generation, and programmatic prompt optimization |
| Safety and alignment | `constitutional-ai`, `llamaguard`, `nemo-guardrails`, `prompt-guard` | Build safety policies, content filters, prompt-injection defenses, guardrails, and alignment workflows |
| Multimodal and generative media | `stable-diffusion`, `segment-anything`, `clip`, `blip-2`, `llava`, `whisper`, `audiocraft` | Handle image generation, image understanding, segmentation, VLMs, speech recognition, and audio generation |
| Academic and research writing | `ml-paper-writing`, `systems-paper-writing`, `academic-plotting`, `presenting-conference-talks` | Draft papers, improve research narratives, build academic plots, and prepare conference talks |
| Research ideation | `0-autoresearch-skill`, `brainstorming-research-ideas`, `creative-thinking-for-research` | Generate research directions, decompose paper ideas, design experiments, and explore technical routes |
| Frontend and visual design | `frontend-design`, `web-design-engineer`, `open-design` | Build web apps, dashboards, landing pages, slide decks, social graphics, reports, and design systems |
| Frontend animation | `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-react`, `gsap-plugins`, `gsap-utils`, `gsap-performance`, `gsap-frameworks` | Build and review GSAP animations, timelines, ScrollTrigger effects, plugins, React/Vue/Svelte lifecycle patterns, and performance-sensitive motion |
| Video prompts and media APIs | `seedance2-skill`, `seedance-prompt-zh`, `seedance-prompt-en`, `rw-generate-image`, `rw-generate-video`, `rw-generate-audio`, `rw-integrate-*` | Write Seedance 2.0 multimodal video prompts, use Runway APIs, generate media, and integrate generation into projects |
| Scraping and content tools | `scrapling-official`, `youtube-clipper`, `career-ops` | Scrape websites, clip YouTube content, organize career materials, extract information, and automate content workflows |
| Internet reach and cross-platform research | `agent-reach` | Route research across web pages, RSS, GitHub, YouTube, Bilibili, V2EX, semantic search, and optional authenticated social platforms |

## Seedance 2.0 Skill Update

This export includes the latest [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) package:

| Skill | Location | Main use |
| --- | --- | --- |
| `seedance2-skill` | `codex-skills/seedance2-skill` | Full bilingual Seedance 2.0 prompt package with English root instructions, Chinese instructions under `zh/`, and upstream README files |
| `seedance-prompt-en` | `project-agent-skills/seedance-prompt-en` | English Seedance 2.0 prompt workflow for multimodal references, camera language, timing, effects, ads, short dramas, and education clips |
| `seedance-prompt-zh` | `project-agent-skills/seedance-prompt-zh` | Chinese Seedance 2.0 prompt workflow aligned with the upstream `zh/SKILL.md` |

## Official GSAP Skills

The latest update also installs the official [greensock/gsap-skills](https://github.com/greensock/gsap-skills) package as top-level skills:

| Skill | Main use |
| --- | --- |
| `gsap-core` | Core tweens, `gsap.to()`, `from()`, `fromTo()`, eases, staggers, transforms |
| `gsap-timeline` | Timeline sequencing, labels, nesting, playback control, position parameter |
| `gsap-scrolltrigger` | Scroll-linked animation, scrub, pinning, markers, refresh, scroller patterns |
| `gsap-react` | React and Next.js animation with `useGSAP`, refs, scope, cleanup, SSR-safe patterns |
| `gsap-plugins` | Flip, Draggable, Observer, SplitText, MorphSVG, ScrollToPlugin, ScrollSmoother, easing and SVG plugins |
| `gsap-utils` | `gsap.utils` helpers such as clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe |
| `gsap-performance` | Smooth animation practices: transforms, opacity, batching, `will-change`, avoiding layout thrash |
| `gsap-frameworks` | Vue, Nuxt, Svelte, SvelteKit and other lifecycle-based framework patterns |

These official copies are available under both `codex-skills/` and `project-agent-skills/`.

## Newly Added Repository-Derived Skills

The latest updates add eight project-level skills sourced from or distilled from public GitHub repositories:

| Skill | Source repository | Main use |
| --- | --- | --- |
| `freedomain-dns-ops` | `DigitalPlatDev/FreeDomain` | Free-domain registration, DNS hosting, nameserver setup, WHOIS service design, dashboard templates, and abuse-aware support |
| `claude-mem-operations` | `thedotmack/claude-mem` | Persistent agent memory, lifecycle hooks, worker service operations, SQLite/Chroma search, MCP tools, and privacy-aware debugging |
| `twenty-crm-development` | `twentyhq/twenty` | Twenty CRM app development, Nx/Yarn monorepo navigation, NestJS/React work, SDK generation, e2e tests, Docker, and Helm deployment |
| `understand-anything-knowledge-graph` | `Lum1104/Understand-Anything` | Codebase and knowledge-base graph analysis, dashboard graph UX, semantic batching, diff impact, explain, and onboarding flows |
| `taste-skill-frontend-direction` | `leonxlnx/taste-skill` | Anti-generic frontend direction, redesign audits, image-to-code workflows, brand kits, minimalist/brutalist variants, and design skill packaging |
| `ppf-contact-solver-workflows` | `st-tech/ppf-contact-solver` | GPU/CUDA contact simulation, Docker, JupyterLab, Blender add-on workflows, MCP control, Python API usage, and Windows native builds |
| `pixelle-video-workflows` | `AIDC-AI/Pixelle-Video` | AI short-video engine setup, Streamlit WebUI, FastAPI REST API, Docker deployment, ComfyUI/RunningHub workflows, direct media model APIs, TTS, templates, and troubleshooting |
| `agent-reach` | `Panniantong/Agent-Reach` | Cross-platform internet research routing, channel health checks, safe installation guidance, web/RSS/video/code/social search, and optional authenticated platform setup |

These are stored under `project-agent-skills/`; `agent-reach` is also exported under `codex-skills/` for direct Codex installation.

## Example Use Cases

### Train Or Fine-Tune A Model

Combine skills such as `llama-factory`, `axolotl`, `peft`, `deepspeed`, and `accelerate` to help an agent:

- choose SFT, LoRA, QLoRA, DPO, or GRPO;
- prepare training data formats;
- generate training configs;
- estimate GPU memory requirements;
- debug loss spikes, OOMs, slow throughput, and checkpoint issues.

### Deploy An Inference Service

Combine `vllm`, `sglang`, `llama-cpp`, `tensorrt-llm`, `gguf`, `awq`, and `gptq` to help an agent:

- choose the inference framework;
- configure an OpenAI-compatible API;
- optimize batching, concurrency, KV cache, and GPU memory;
- perform quantization and format conversion;
- analyze latency, throughput, and deployment cost.

### Build A RAG Or Agent App

Combine `langchain`, `llamaindex`, `faiss`, `qdrant`, `chroma`, `sentence-transformers`, and `dspy` to help an agent:

- design chunking, embedding, indexing, and retrieval strategies;
- connect vector databases;
- design tool-calling and multi-agent workflows;
- add structured outputs, observability, and evaluation.

### Write Research Papers And Talks

Combine `ml-paper-writing`, `systems-paper-writing`, `academic-plotting`, and `presenting-conference-talks` to help an agent:

- clarify contributions;
- draft introduction, related work, methods, and experiments;
- build academic plots;
- prepare conference talks and rebuttal material.

### Design Frontends And Generate Media

Combine `open-design`, `frontend-design`, `web-design-engineer`, `taste-skill-frontend-direction`, `seedance2-skill`, `seedance-prompt-zh`, and Runway skills to help an agent:

- build web apps, prototypes, dashboards, and landing pages;
- create slide decks, posters, reports, and social assets;
- write Seedance 2.0 multimodal video prompts;
- generate images, video, and audio;
- integrate media generation APIs into products.

### Work With The GitHub-Derived Skills

Ask directly for the skill by name or describe the task:

```text
Use the twenty-crm-development skill to help me add a custom CRM object.
Use claude-mem-operations to debug why memory is not appearing.
Use freedomain-dns-ops to walk me through Cloudflare nameserver setup.
Use understand-anything-knowledge-graph to map this repository for onboarding.
Use taste-skill-frontend-direction to redesign this landing page.
Use ppf-contact-solver-workflows to run a Docker/Jupyter contact simulation.
Use pixelle-video-workflows to install Pixelle-Video and generate a 5-scene short video.
Use gsap-scrolltrigger and gsap-react to build a pinned scroll animation in Next.js.
```

## How To Use In Codex

Copy the skill directory you need into Codex's skills directory:

```bash
cp -R codex-skills/<skill-name> ~/.codex/skills/
```

Or copy all exported global Codex skills:

```bash
cp -R codex-skills/* ~/.codex/skills/
```

For project-level skills, copy from `project-agent-skills/`:

```bash
mkdir -p .agents/skills
cp -R project-agent-skills/<skill-name> .agents/skills/
```

Restart Codex or reload the agent session so the skill list is refreshed.

## Notes Before Publishing

- This repository is an export of local skills from multiple sources.
- Some skills may depend on third-party tools, API keys, GPUs, or external services.
- Some skills originate from third-party repositories or installed packages; check upstream licenses and attribution requirements before public redistribution.
- The repository-derived skills are compact workflow summaries and do not vendor the original repositories.
