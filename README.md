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
| Learning and research assistants | `deeptutor-cli` | Operate DeepTutor tutoring, deep solve, quiz, research, knowledge-base, notebook, memory, session, partner, API, and Web-app workflows |
| Prompting and structured output | `dspy`, `guidance`, `outlines`, `instructor` | Create controlled prompts, structured JSON output, constrained generation, and programmatic prompt optimization |
| Safety and alignment | `constitutional-ai`, `llamaguard`, `nemo-guardrails`, `prompt-guard` | Build safety policies, content filters, prompt-injection defenses, guardrails, and alignment workflows |
| Multimodal and generative media | `opennana-image-video-prompt-studio`, `gpt-image-2-style-library`, `stable-diffusion`, `segment-anything`, `clip`, `blip-2`, `llava`, `whisper`, `audiocraft` | Build structured image/video prompt packs, route image-to-video work, and handle image generation, understanding, segmentation, VLMs, speech, and audio |
| Academic and research writing | `ml-paper-writing`, `systems-paper-writing`, `academic-plotting`, `presenting-conference-talks` | Draft papers, improve research narratives, build academic plots, and prepare conference talks |
| Research ideation | `0-autoresearch-skill`, `brainstorming-research-ideas`, `creative-thinking-for-research` | Generate research directions, decompose paper ideas, design experiments, and explore technical routes |
| Frontend and visual design | `hallmark`, `border-beam-ui`, `frontend-design`, `web-design-engineer`, `open-design` | Build and audit distinctive web apps, components, luminous state borders, dashboards, landing pages, slide decks, social graphics, reports, and design systems |
| Frontend animation | `border-beam-ui`, `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-react`, `gsap-plugins`, `gsap-utils`, `gsap-performance`, `gsap-frameworks` | Build and review restrained border motion, GSAP animations, timelines, ScrollTrigger effects, plugins, framework lifecycles, reduced motion, and performance-sensitive motion |
| Content creator operations | `human-writing`, `content-research-brief`, `seo-aeo-outline`, `viral-hook-title`, `script-writer`, `platform-repurpose`, `brand-voice-guard`, `fact-check-citation`, `content-calendar-planner`, `asset-prompt-pack`, `publish-metadata-ops`, `aitoearn-compliance-ops` | Write evidence-grounded Chinese prose, then research, outline, repurpose, QA, fact-check, plan calendars, create visual prompt packs, prepare publish metadata, and run compliant AiToEarn automation checks |
| Video direction, prompts, and media APIs | `opennana-image-video-prompt-studio`, `video-director-studio`, `seedance-2-5-prompt-studio`, `seedance-director-compat`, `seedance2-skill`, `seedance-prompt-zh`, `seedance-prompt-en`, `pixelle-video-workflows`, `rw-generate-video` | Turn ideas and assets into format-selected prompt packs, director treatments, timelines, reference/cast isolation, shot/continuity/sound packs, and provider-specific prompts or media integrations |
| Editable video production | `chatcut-plugin-basics`, `chatcut-asset-import`, `chatcut-transcription`, `chatcut-create-motion-graphics`, `chatcut-voice`, `chatcut-music`, `chatcut-export`, `chatcut-verification` | Operate ChatCut projects through MCP: import media, edit timelines, add captions, create motion graphics, generate voice/music/video assets, export, and verify visible edits |
| Scraping and content tools | `scrapling-official`, `video-downloader`, `youtube-clipper`, `cangjie-skill` | Scrape websites, download permitted media, preserve transcripts and metadata, distill long-form content into tested skills, and clip YouTube content |
| Career and Japan job search | `career-ops`, `offer-toolkit-japan` | Scan and track applications, decode Japanese or English JDs, prepare 履歴書・職務経歴書・English resumes, practice bilingual interviews, and review offers, labor terms, and residence-status questions |
| Internet reach and cross-platform research | `agent-reach` | Route research across web pages, RSS, GitHub, YouTube, Bilibili, V2EX, semantic search, and optional authenticated social platforms |
| Interactive research and web intelligence | `jupyter-live-kernel`, `arxiv`, `firecrawl*`, `wigolo` | Run stateful Python exploration, paper search, web search/scraping/monitoring, and local-first MCP research |
| Planning, writing, and presentations | `plan`, `human-writing`, `humanizer`, `research-paper-writing`, `powerpoint`, `grill-me` | Write implementation plans, create and revise natural Chinese prose, produce research papers and editable PPTX files, and pressure-test decisions |

## Human Writing Chinese Prose Skill

This export installs [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) version `1.1.0` from upstream commit `4fda173f3fef7fb808f3eba991eeb2528ea4b189`. The complete MIT-licensed Skill, references, Lite edition, agent metadata, and prose checker are preserved in `codex-skills/human-writing/`, `project-agent-skills/human-writing/`, and `user-agent-skills/human-writing/`.

Use `$human-writing` for Chinese articles, Zhihu answers, WeChat posts, forum prose, profiles, explainers, reviews, stories, scripts, and spoken narration. It checks whether long nonfiction has enough concrete material, separates factual and fictional claims, selects format-specific guidance, revises Chinese sentence and paragraph flow, and can run `scripts/check_prose.py` as a final diagnostic.

The existing `humanizer` now delegates Chinese article-like work to `human-writing`. `script-writer`, `platform-repurpose`, and `brand-voice-guard` also call it for their final Chinese prose pass. Facts, citations, legal wording, brand rules, platform limits, and the user's real voice remain higher-priority constraints. The integration never invents personal experiences or opinions to make text sound more human, and it does not force prose-only punctuation rules onto code, URLs, metadata, or unrelated technical and academic formats.

Example terminal prompt:

```text
Use $human-writing to turn these verified notes into a Chinese WeChat article. Check factual boundaries first, write the draft, then run the prose checker.
```

## Content Creator Top 10 Skills

The latest update installs the 10 content-creator skills from the shared screenshot. Each skill keeps the screenshot name as the public entry point and stores upstream material under `references/upstream/`.

| Skill | Source | Status |
| --- | --- | --- |
| `content-research-brief` | `Affitor/affiliate-skills` | Installed |
| `seo-aeo-outline` | `rampstackco/claude-skills` (`seo-aeo-geo`) | Installed as a focused wrapper |
| `viral-hook-title` | `EvolutionAPI/evo-nexus` (`social-hook-writer`) | Installed as a focused wrapper |
| `script-writer` | `Affitor/affiliate-skills` (`tiktok-script-writer`) | Installed as a focused wrapper |
| `platform-repurpose` | `Affitor/affiliate-skills` (`content-repurposer`) | Installed as a focused wrapper |
| `brand-voice-guard` | `anthropics/knowledge-work-plugins` (`brand-voice-enforcement`) | Installed as a focused wrapper |
| `fact-check-citation` | `petar-nauka/fact-check-skill` | Installed as a focused wrapper |
| `content-calendar-planner` | `rampstackco/claude-skills` (`content-strategy`) | Installed as a focused wrapper |
| `asset-prompt-pack` | `Affitor/affiliate-skills` (`infographic-generator`) | Installed as a focused wrapper |
| `publish-metadata-ops` | screenshot source was not publicly accessible | Installed as a local derived skill |

## Narrator AI CLI Skill

This export includes [NarratorAI-Studio/narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill), a full AI movie and short-drama narration production workflow:

| Skill | Locations | Main use |
| --- | --- | --- |
| `narrator-ai-cli-skill` | `codex-skills/`, `project-agent-skills/`, `user-agent-skills/` | Search built-in movie materials, choose BGM/dubbing/templates, generate narration scripts, compose videos, optionally run Magic Video templates, and manage task polling with `narrator-ai-cli` |

Runtime note: the skill requires the `narrator-ai-cli` command plus a valid `NARRATOR_APP_KEY` or configured app key.

## AiToEarn Compliance Ops Skill

This export adds [yikart/AiToEarn](https://github.com/yikart/AiToEarn) as a compliant operations automation skill. The upstream project provides Create, Publish, Engage, Monetize, MCP/API, Docker, and Relay workflows for multi-platform creator operations; this local skill adds a conservative risk-control layer before external platform writes.

| Skill | Locations | Main use |
| --- | --- | --- |
| `aitoearn-compliance-ops` | `codex-skills/`, `project-agent-skills/` | Plan and gate AiToEarn publishing, reply, engagement, monetization, and scheduling workflows with official API/OAuth preference, approval gates, account health checks, cooldowns, audit logs, and refusal of ban-evasion tactics |

Bundled helper: `scripts/risk_check.py` evaluates structured action JSON against `assets/default_policy.json` and returns `allow`, `approve`, `delay`, or `block`.

## ChatCut Agent Plugin Skills

This export adds [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin.git) as a namespaced ChatCut skill bundle. The upstream package is a Codex plugin for editable video workflows; this repository exports its workflow skills as `chatcut-*` skills and keeps the helper script while omitting the large bundled FFmpeg archives for a lighter GitHub package.

| Skill group | Locations | Main use |
| --- | --- | --- |
| `chatcut-*` | `codex-skills/`, `project-agent-skills/` | ChatCut MCP setup, project targeting, media import, timeline editing guidance, transcription, captions, talking-head cleanup, Motion Graphic JSX authoring, image/video/voice/music generation, shader effects, export, and verification |

Runtime note: real project edits require the ChatCut MCP server and ChatCut authentication. Start with `chatcut-plugin-basics`; if the MCP server is missing, read its `references/plugin-setup.md`.

## Video Download And Content Distillation Skills

This export integrates [davila7/claude-code-templates video-downloader](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/media/video-downloader) and [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) as a connected workflow:

| Skill | Locations | Main use |
| --- | --- | --- |
| `video-downloader` | `codex-skills/`, `project-agent-skills/` | Download authorized online video/audio with `yt-dlp`, select quality and format, preserve subtitles/metadata/thumbnails, inspect playlists, verify outputs, and refuse DRM or access-control bypasses |
| `cangjie-skill` | `codex-skills/`, `project-agent-skills/` | Distill books, long-video transcripts, podcasts, courses, interviews, and source collections into atomic skills through RIA-TV++, five extraction passes, triple verification, cross-linking, pressure tests, and resumable audit artifacts |

The video downloader includes an executable `scripts/download_media.py` with conservative defaults and dry-run support. Cangjie keeps the upstream methodology, extractor prompts, and output templates while adapting installation and generated frontmatter for Codex.

## Japan Offer Toolkit

This export upgrades [yanliudesign/offer-toolkit-skill](https://github.com/yanliudesign/offer-toolkit-skill) into a Japan-focused, evidence-based workflow. It keeps the upstream JD analysis, resume templating, and STAR/CAR interview methods, while removing hard-coded author paths, promotional output, and false interview-probability precision.

| Skill | Locations | Main use |
| --- | --- | --- |
| `offer-toolkit-japan` | `codex-skills/`, `project-agent-skills/` | Route new-graduate, second-new-graduate, mid-career, foreign-company, and international-team searches; analyze JDs and employers; create 履歴書, 職務経歴書, Entry Sheets, and English resumes; prepare evidence-based Japanese/English interviews with follow-up trees; and review offer terms, fixed overtime, transfers, and residence-status support |

The skill includes Japan-specific document templates, 13 reusable English resume layouts from the MIT-licensed upstream project, a 130+ prompt interview bank, stage and role overlays, short-tenure and career-consistency drills, leadership/delivery/AI claim boundaries, and a current-intelligence workflow using 2025-2026 hiring-side research and candidate reports. `scripts/interview_pack_audit.py` checks interview coverage and claim boundaries, while `scripts/japan_offer_audit.py` checks structured employment terms. Use `career-ops` alongside it for bulk scanning, tracking, and pipeline management.

## Video Director Studio

This export adds a model-agnostic director layer distilled from the public metadata of [Liblib/LibTV's Skill catalog](https://www.liblib.tv/skill). The catalog returned 103 entries on 2026-07-14 across professional film, advertising, animation/games, creator media, short drama, utilities, and music video. The package does not copy hidden creator prompts or example media; it converts recurring production patterns into original, composable craft systems.

| Skill | Locations | Main use |
| --- | --- | --- |
| `video-director-studio` | `codex-skills/`, `project-agent-skills/` | Select a format blueprint and trait-based director grammar; plan assets, characters, world, product locks, beats, shots, continuity, performance, light, edit, and sound; then compile the pack for Seedance, Runway, WAN/LTX, Pixelle, LibTV, or ChatCut |

The skill includes 37 reusable director grammars, 20 format blueprints, 18 production modules, a structured director-pack template, `scripts/director_pack_audit.py`, and a public-metadata refresh tool, `scripts/liblib_catalog.py`. Existing Seedance, Runway, and Pixelle project Skills now route complex multi-shot work through this director layer first.

## DeepTutor And Hallmark Skills

This export adds the upstream learning/research and design Skills from [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) and [nutlope/hallmark](https://github.com/nutlope/hallmark), with Codex compatibility and standalone-package repairs.

| Skill | Locations | Main use |
| --- | --- | --- |
| `deeptutor-cli` | `codex-skills/`, `project-agent-skills/` | Preflight, install, initialize, and operate DeepTutor 1.5.2 for tutoring, deep solving, quiz generation, research, visualization, document knowledge bases, notebooks, sessions, memory, partners, API service, and the local Web app |
| `hallmark` | `codex-skills/`, `project-agent-skills/` | Design, audit, redesign, and study interfaces with structural variety, 21 macrostructures, 20 catalog themes, responsive/state checks, portable design tokens, and a 58-gate anti-slop review |

`deeptutor-cli` is an operations Skill, not a bundled copy of the DeepTutor application. The external `deeptutor` command and chosen model/embedding providers must be installed and configured before real runs. Hallmark is instruction-only and needs no Hallmark executable; this export adds the token catalog and worked references omitted by its standalone upstream Skill directory. Apache-2.0 and MIT license notices are retained in the respective packages.

## Border Beam UI Skill

This export adds `border-beam-ui`, a design and implementation layer based on the MIT-licensed [Jakubantalik/border-beam](https://github.com/Jakubantalik/border-beam) React component and its [interactive demo](https://beam.jakubantalik.com/). It turns the upstream effect presets into restrained rules for buttons, icon controls, inputs, search bars, selected cards, loading states, and short success moments.

| Skill | Locations | Main use |
| --- | --- | --- |
| `border-beam-ui` | `codex-skills/`, `project-agent-skills/` | Select `sm`, `md`, `line`, `pulse-inner`, or `pulse-outside`; integrate the React 18+ package or a framework-neutral CSS fallback; map colors to product tokens; and audit focus, reduced motion, overflow clipping, themes, density, and performance |

The package API, rendering layers, theme/color variants, active fades, offscreen pulse pausing, and approximately 30 fps shared pulse driver were checked at upstream commit `647d26e2a27f26587110fea5a8410c80deb5ac5e` on 2026-08-05. The repository manifest was `1.4.0` while npm `latest` was still `1.3.0`, so the Skill requires checking the installed version before relying on exact defaults. It does not make every surface glow: dense operational interfaces default to event-triggered effects and keep a stable hairline, semantic state, and visible keyboard focus underneath the decoration. `scripts/audit_beam_usage.py` checks common integration mistakes.

## OpenNana Image And Video Prompt Studio

This export adds an original cross-model prompt layer synthesized from the public organization and metadata of the [OpenNana image gallery](https://opennana.com/awesome-prompt-gallery?media_type=image) and [video gallery](https://opennana.com/awesome-prompt-gallery?media_type=video). It does not copy locked or paid prompt text, creator media, or the full public corpus.

| Skill | Locations | Main use |
| --- | --- | --- |
| `opennana-image-video-prompt-studio` | `codex-skills/`, `project-agent-skills/` | Route image, video, and image-to-video briefs; select production families; assign single-role references; build composition or timed beat plans; control visible text/audio; check rights; create variants; and validate structured prompt packs |

Inspection on 2026-08-05 found image filters for Nano Banana Pro, Nano Banana 2, ChatGPT, and Grok, plus a Seedance 2.0 video filter. The server-rendered image page displayed 14,110 entries while its public list API returned 15,962; both video surfaces returned 613. The Skill records this dynamic discrepancy instead of treating counts or community examples as permanent model guarantees. It includes original image/video pattern libraries, bridge templates, a JSON pack template, and `scripts/validate_prompt_pack.py`.

## Seedance 2.0 And 2.5 Skills

The repository keeps the bilingual 2.0 material from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) and adds a 2.5 production layer synthesized from [ByteDance Seed's official launch](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) and the [public EvoLink prompt gallery](https://evolink.ai/seedance-2-5-prompts). It does not bulk-copy the website prompts; it audits 122 public cards and turns their recurring structures into original templates and validation rules.

| Skill | Location | Main use |
| --- | --- | --- |
| `seedance2-skill` | `codex-skills/seedance2-skill` | Full bilingual Seedance 2.0 prompt package with English root instructions, Chinese instructions under `zh/`, and upstream README files |
| `seedance-prompt-en` | `project-agent-skills/seedance-prompt-en` | English Seedance 2.0 prompt workflow for multimodal references, camera language, timing, effects, ads, short dramas, and education clips |
| `seedance-prompt-zh` | `project-agent-skills/seedance-prompt-zh` | Chinese Seedance 2.0 prompt workflow aligned with the upstream `zh/SKILL.md` |
| `seedance-2-5-prompt-studio` | `codex-skills/`, `project-agent-skills/` | Build 30-second beat sheets, twelve format families, single-role references, cast/grid isolation, native audio/dialogue, timestamp edits, targeted negatives, and evaluation packs |
| `seedance-director-compat` | `codex-skills/`, `project-agent-skills/` | Build bilingual Seedance 2.0/2.5-compatible physics and continuity contracts, with WAN/LTX fallbacks when Seedance is unavailable |

Status verified on 2026-08-05: Seedance 2.5 officially launched on 2026-07-31 and was rolling out in Jimeng and Doubao Pro. ByteDance announced up to 30 seconds, up to 30 image/10 video/10 audio references, multi-round extension, and timestamp editing. EvoLink still showed docs ready but its generation route inactive and stated that first-party API access would open on 2026-08-07, so the Skill rechecks the selected surface instead of treating model claims as a callable API.

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

## Skills And Agent Tools Extracted From The Screenshots

Both screenshots were audited. None of the 11 names in the first image had previously been installed under the exact same Skill name. They are now included; the `writing-plans / plan` entry uses its current upstream name, `plan`. The Firecrawl router is accompanied by nine official focused Skills so its links and routing remain complete.

| Skill | Source | Status and purpose |
| --- | --- | --- |
| `jupyter-live-kernel` | `moltis-org/moltis`, originating in Hermes | Run a persistent Jupyter kernel through `hamelnb` |
| `plan` | `NousResearch/hermes-agent` | Plan without execution; covers the screenshot's `writing-plans / plan` entry |
| `claude-design`, `sketch` | `NousResearch/hermes-agent` | Build one-off HTML artifacts or compare 2-3 interactive design sketches |
| `powerpoint` | Adapted from the Apache-2.0 `pptx` example in `bojieli/ai-agent-book` | Generate and verify editable `.pptx` files without copying Anthropic's non-redistributable Skill |
| `humanizer` | `NousResearch/hermes-agent` | Remove general AI writing patterns; route Chinese article-like prose to `human-writing` while preserving meaning and factual boundaries |
| `arxiv`, `research-paper-writing` | `NousResearch/hermes-agent` | Search arXiv and handle research design, experiments, citations, writing, and submission checks |
| `firecrawl` plus nine `firecrawl-*` Skills | `firecrawl/cli` | Search, scrape, map, crawl, interact, download, parse, and monitor web content |
| `grill-me` | `feiskyer/codex-settings` | Explicit pressure-testing interviews with glossary and ADR maintenance |
| `popular-web-designs` | `NousResearch/hermes-agent` | Reference 54 real product design systems and their HTML/CSS rules |

The second screenshot shows full applications rather than ready-to-call Skills. This repository adds honest operation layers without bundling the applications or treating installation as successful execution.

| Skill | Project | Main use |
| --- | --- | --- |
| `ai-agent-book-guide` | `bojieli/ai-agent-book` | Follow a ten-chapter learning and implementation path for Agents, context, memory, tools, evaluation, training, multimodality, and collaboration |
| `code-review-graph` | `tirth8205/code-review-graph` | Configure its Codex MCP, build a local code graph, and perform impact analysis, review, debugging, and refactoring |
| `voicebox-studio` | `jamiepine/voicebox` | Use local REST/MCP routes for TTS, transcription, voice profiles, and agent speech |
| `wigolo` | `KnockOutEZ/wigolo` | Run Node 20+ local-first search, fetch, crawl, cache, extraction, and research tools over MCP |
| `ktransformers-ops` | `kvcache-ai/ktransformers` | Assess hardware and plan CPU-GPU heterogeneous MoE inference or LLaMA-Factory SFT |

They can be named directly in a terminal session, for example: `Use $grill-me to challenge this design`, `Use $arxiv to find this paper`, or `Use $code-review-graph to review the current diff`. Tool-backed Skills still require their external CLI, application, runtime, or models.

## Newly Added Repository-Derived Skills

The latest updates add repository-derived skills sourced from or distilled from public GitHub repositories:

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
| `narrator-ai-cli-skill` | `NarratorAI-Studio/narrator-ai-cli-skill` | AI movie and short-drama narration production with built-in materials, BGM, dubbing voices, narration templates, script generation, video composition, task polling, and Magic Video rules |
| `aitoearn-compliance-ops` | `yikart/AiToEarn` | Compliant AiToEarn creator-operations automation with risk checks for publishing, engagement, account health, approval gates, cooldowns, audit logs, MCP/API setup, Docker/Relay usage, and ban-evasion refusal |
| `chatcut-*` | `ChatCut-Inc/agent-plugin` | Editable ChatCut video production through MCP: media import, timeline editing, captions/transcription, talking-head cleanup, Motion Graphics, image/video/voice/music generation, shader effects, export, and verification |
| `video-downloader` | `davila7/claude-code-templates` | Permission-aware video/audio downloading with quality and format selection, subtitle/metadata preservation, playlist controls, dry runs, output verification, and anti-bypass boundaries |
| `cangjie-skill` | `kangarooking/cangjie-skill` | RIA-TV++ long-form content distillation into traceable, linked, pressure-tested agent skills with checkpointed execution and reusable templates |
| `offer-toolkit-japan` | `yanliudesign/offer-toolkit-skill` plus official and current market sources | Japan-focused job-market routing, evidence-based JD matching, 履歴書・職務経歴書・Entry Sheet and English resume preparation, a current 130+ prompt interview bank with follow-up and truth-boundary checks, and offer, labor-term, fixed-overtime, transfer, and residence-status review |
| `video-director-studio` | Public metadata synthesis of `liblib.tv/skill` | Model-agnostic AI video direction with trait-based grammars, TVC/drama/MV/animation/UGC blueprints, production modules, shot and continuity contracts, provider adapters, and structured QC |
| `deeptutor-cli` | `HKUDS/DeepTutor` | Codex-compatible DeepTutor 1.5.2 CLI operations with runtime preflight, corrected installation paths, evidence-grounded learning workflows, and destructive-operation safeguards |
| `hallmark` | `nutlope/hallmark` | Hallmark 1.1.0 interface design/audit workflow with the complete upstream reference set, a restored 20-theme token catalog, fixed standalone links, and Codex UI metadata |

These are stored under `project-agent-skills/`; selected direct-use packages, including `agent-reach`, `offer-toolkit-japan`, `video-director-studio`, `deeptutor-cli`, and `hallmark`, are also exported under `codex-skills/`.

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

Combine `hallmark`, `open-design`, `frontend-design`, `web-design-engineer`, `taste-skill-frontend-direction`, `video-director-studio`, `seedance2-skill`, `seedance-prompt-zh`, and Runway skills to help an agent:

- build web apps, prototypes, dashboards, and landing pages;
- create slide decks, posters, reports, and social assets;
- turn a rough video idea into a director treatment, storyboard, shot/continuity/sound pack, and generator-specific prompts;
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
Use aitoearn-compliance-ops to design a compliant AiToEarn publishing workflow with risk gates.
Use chatcut-plugin-basics and chatcut-asset-import to edit this local video in ChatCut.
Use chatcut-transcription and chatcut-export to add captions and render the final cut.
Use video-downloader to save this video I own, including subtitles and metadata, in 1080p MP4.
Use cangjie-skill to distill this authorized course transcript into reusable, tested skills.
Use offer-toolkit-japan to analyze this Tokyo role, prepare my 履歴書 and 職務経歴書, and build a bilingual interview pack without inventing experience.
Use deeptutor-cli to create a knowledge base from these PDFs and generate an evidence-grounded Chinese quiz.
Use hallmark audit on this frontend, then redesign it without replacing the existing routes or component architecture.
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
