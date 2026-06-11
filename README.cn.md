# 我的 AI Skills 工具库

这是一个面向 Codex / AI Agent 的本地 skills 汇总仓库，整理了我当前工作环境里常用的研究、工程、设计、内容生成、自动化和项目专项能力。

简单说：这些 skill 是给 AI Agent 使用的“专业工作说明书”。一个 `SKILL.md` 会告诉 Agent：什么时候触发这个能力、要遵循什么流程、该检查哪些文件或工具、最后应该产出什么格式。这样同一个通用 Agent 在不同领域里也能更像一个熟悉业务的专家。

English version: [README.md](README.md)

## 仓库包含什么

这个仓库分成三类导出的技能目录：

```text
.
├── codex-skills/            # Codex 全局 skills，包含 AI 研究、ML 工程、前端、设计和媒体工作流
├── project-agent-skills/    # 项目级 agent skills，包含 Runway、Seedance、爬虫、职业材料和仓库分析技能
├── user-agent-skills/       # 用户级 agent skills
├── SKILLS_MANIFEST.txt      # 自动生成的 SKILL.md 文件清单
├── README.md
└── README.cn.md
```

导出时已经把符号链接展开成真实文件，所以 clone 之后不会因为本地路径不同而失效。

## 能力地图

| 方向 | 代表 skills | 能实现的功能 |
| --- | --- | --- |
| 大模型训练与微调 | `axolotl`、`llama-factory`、`peft`、`unsloth`、`trl-fine-tuning` | 设计和实现 SFT、LoRA、QLoRA、DPO、训练配置、数据格式转换、训练问题排查 |
| 后训练与强化学习 | `verl`、`openrlhf`、`grpo-rl-training`、`simpo`、`slime`、`torchforge` | 搭建 RLHF、DPO、GRPO、SimPO 等后训练流程，分析 reward、rollout、显存和吞吐问题 |
| 推理与部署 | `vllm`、`sglang`、`llama-cpp`、`tensorrt-llm`、`speculative-decoding` | 部署大模型推理服务，优化吞吐、延迟、batch、KV cache、量化和多 GPU 推理 |
| 分布式训练 | `deepspeed`、`accelerate`、`megatron-core`、`pytorch-fsdp2`、`ray-train`、`torchtitan` | 处理多卡训练、FSDP、ZeRO、pipeline/tensor parallel、checkpoint、训练稳定性和性能优化 |
| 模型压缩与优化 | `awq`、`gptq`、`gguf`、`bitsandbytes`、`hqq`、`flash-attention` | 做量化、低比特推理、模型格式转换、注意力优化、显存压缩和速度调优 |
| 模型架构与新技术 | `nanogpt`、`litgpt`、`mamba`、`rwkv`、`moe-training`、`long-context` | 研究 Transformer、Mamba、RWKV、MoE、长上下文、模型合并、剪枝、知识蒸馏等技术 |
| 数据处理与评测 | `nemo-curator`、`ray-data`、`lm-evaluation-harness`、`bigcode-evaluation-harness`、`nemo-evaluator` | 构建训练数据流水线，清洗数据，做 benchmark、代码模型评测、自动化评估和实验记录 |
| RAG 与向量数据库 | `faiss`、`qdrant`、`chroma`、`pinecone`、`sentence-transformers` | 搭建检索增强生成系统，设计 embedding、索引、召回、rerank 和向量库集成 |
| Agent 与工作流 | `langchain`、`llamaindex`、`crewai`、`autogpt`、`a-evolve` | 构建多 Agent 协作、工具调用、任务规划、知识库问答和自动化研究流程 |
| Prompt 与结构化输出 | `dspy`、`guidance`、`outlines`、`instructor` | 编写可控 prompt、结构化 JSON 输出、约束式生成、prompt 优化和程序化提示工程 |
| 安全与对齐 | `constitutional-ai`、`llamaguard`、`nemo-guardrails`、`prompt-guard` | 做安全策略、内容过滤、prompt injection 防护、护栏设计和对齐方法研究 |
| 多模态与生成模型 | `stable-diffusion`、`segment-anything`、`clip`、`blip-2`、`llava`、`whisper`、`audiocraft` | 处理图像生成、图像理解、分割、视觉语言模型、语音识别、音频生成和多模态应用 |
| 论文与科研写作 | `ml-paper-writing`、`systems-paper-writing`、`academic-plotting`、`presenting-conference-talks` | 写 ML/系统论文、实验图表、会议演讲稿、研究叙事和投稿材料 |
| 研究创意与自动研究 | `0-autoresearch-skill`、`brainstorming-research-ideas`、`creative-thinking-for-research` | 生成研究方向、拆解论文想法、设计实验、做技术路线探索 |
| 前端与视觉设计 | `frontend-design`、`web-design-engineer`、`open-design` | 生成网页、仪表盘、演示文稿、海报、社媒图、交互原型和设计系统 |
| 前端动效 | `gsap-core`、`gsap-timeline`、`gsap-scrolltrigger`、`gsap-react`、`gsap-plugins`、`gsap-utils`、`gsap-performance`、`gsap-frameworks` | 编写和审查 GSAP 动画、时间线、ScrollTrigger 滚动效果、插件、React/Vue/Svelte 生命周期模式和高性能动效 |
| 视频提示词与媒体生成 | `seedance2-skill`、`seedance-prompt-zh`、`seedance-prompt-en`、`narrator-ai-cli-skill`、`rw-generate-image`、`rw-generate-video`、`rw-generate-audio`、`rw-integrate-*` | 撰写 Seedance 2.0 多模态视频提示词，制作 AI 电影/短剧解说视频，对接 Runway API，生成媒体内容，并把生成能力集成到项目里 |
| 爬虫与内容工具 | `scrapling-official`、`youtube-clipper`、`career-ops` | 做网页抓取、YouTube 内容裁剪、职业材料整理、信息提取和自动化脚本 |
| 全网触达与跨平台研究 | `agent-reach` | 在网页、RSS、GitHub、YouTube、B站、V2EX、语义搜索和可选登录态社交平台之间路由研究任务 |

## Narrator AI CLI Skill

本次导出加入了 [NarratorAI-Studio/narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill)，用于 AI 电影/短剧解说视频的完整制作流程：

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `narrator-ai-cli-skill` | `codex-skills/`、`project-agent-skills/`、`user-agent-skills/` | 搜索内置影视素材，选择 BGM、配音和解说模板，生成文案，合成视频，可选 Magic Video 模板，并按规范轮询任务状态 |

运行说明：该 skill 需要 `narrator-ai-cli` 命令，以及有效的 `NARRATOR_APP_KEY` 或已配置的 app key。

## Seedance 2.0 Skill 更新

本次导出同步了最新的 [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) 包：

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `seedance2-skill` | `codex-skills/seedance2-skill` | 完整双语 Seedance 2.0 提示词包，根目录为英文说明，`zh/` 下为中文说明，并保留上游 README |
| `seedance-prompt-en` | `project-agent-skills/seedance-prompt-en` | 英文 Seedance 2.0 提示词流程，覆盖多模态引用、运镜语言、分镜节奏、特效、广告、短剧和科普视频 |
| `seedance-prompt-zh` | `project-agent-skills/seedance-prompt-zh` | 中文 Seedance 2.0 提示词流程，已对齐上游 `zh/SKILL.md` |

## 官方 GSAP Skills

最新更新也安装了官方 [greensock/gsap-skills](https://github.com/greensock/gsap-skills) 包，并作为顶层 skills 使用：

| Skill | 主要用途 |
| --- | --- |
| `gsap-core` | 核心 tween、`gsap.to()`、`from()`、`fromTo()`、缓动、stagger、transform |
| `gsap-timeline` | 时间线编排、label、嵌套、播放控制、position parameter |
| `gsap-scrolltrigger` | 滚动联动动画、scrub、pin、markers、refresh、scroller 模式 |
| `gsap-react` | React / Next.js 中使用 `useGSAP`、refs、scope、cleanup 和 SSR 安全模式 |
| `gsap-plugins` | Flip、Draggable、Observer、SplitText、MorphSVG、ScrollToPlugin、ScrollSmoother、缓动和 SVG 插件 |
| `gsap-utils` | `gsap.utils` 辅助方法，例如 clamp、mapRange、normalize、interpolate、random、snap、toArray、wrap、pipe |
| `gsap-performance` | 高性能动画实践：transform、opacity、batching、`will-change`、避免 layout thrash |
| `gsap-frameworks` | Vue、Nuxt、Svelte、SvelteKit 和其它生命周期型框架里的 GSAP 模式 |

这些官方副本同时放在 `codex-skills/` 和 `project-agent-skills/` 下。

## 本次新增的 GitHub 仓库分析技能

最近更新新增了 9 个直接来自或从公开 GitHub 仓库提炼出来的项目级 skills：

| 技能 | 来源仓库 | 主要用途 |
| --- | --- | --- |
| `freedomain-dns-ops` | `DigitalPlatDev/FreeDomain` | 免费域名注册、DNS 托管、nameserver 设置、WHOIS 服务设计、域名后台模板和反滥用支持 |
| `claude-mem-operations` | `thedotmack/claude-mem` | 持久记忆、生命周期 hooks、worker 服务运维、SQLite/Chroma 搜索、MCP 工具和隐私安全调试 |
| `twenty-crm-development` | `twentyhq/twenty` | Twenty CRM 应用开发、Nx/Yarn monorepo 导航、NestJS/React 开发、SDK 生成、e2e 测试、Docker 和 Helm 部署 |
| `understand-anything-knowledge-graph` | `Lum1104/Understand-Anything` | 代码库/知识库图谱分析、Dashboard 图谱 UX、语义分批、diff 影响分析、解释和新人 onboarding |
| `taste-skill-frontend-direction` | `leonxlnx/taste-skill` | 前端审美与反模板化设计、重设计审计、image-to-code、品牌套件、极简/粗野主义变体和设计技能打包 |
| `ppf-contact-solver-workflows` | `st-tech/ppf-contact-solver` | GPU/CUDA 接触物理仿真、Docker、JupyterLab、Blender 插件工作流、MCP 控制、Python API 和 Windows 原生构建 |
| `pixelle-video-workflows` | `AIDC-AI/Pixelle-Video` | AI 全自动短视频引擎安装配置、Streamlit WebUI、FastAPI REST API、Docker 部署、ComfyUI/RunningHub 工作流、直连媒体模型 API、TTS、模板和排障 |
| `agent-reach` | `Panniantong/Agent-Reach` | 跨平台互联网研究路由、渠道健康检查、安全安装指导、网页/RSS/视频/代码/社交搜索，以及可选登录态平台配置 |
| `narrator-ai-cli-skill` | `NarratorAI-Studio/narrator-ai-cli-skill` | AI 电影/短剧解说视频制作，覆盖内置素材、BGM、配音角色、解说模板、文案生成、视频合成、任务轮询和 Magic Video 规则 |

这些技能放在 `project-agent-skills/` 目录下；`agent-reach` 还同时导出到 `codex-skills/`，可直接安装到 Codex。

## 重点能力示例

### 训练或微调一个模型

可以结合 `llama-factory`、`axolotl`、`peft`、`deepspeed`、`accelerate` 等 skills，让 Agent 帮你：

- 选择 SFT / LoRA / QLoRA / DPO / GRPO 等训练方案；
- 整理训练数据格式；
- 生成训练配置；
- 估算显存需求；
- 排查 loss 异常、OOM、吞吐低、checkpoint 错误等问题。

### 部署一个推理服务

可以结合 `vllm`、`sglang`、`llama-cpp`、`tensorrt-llm`、`gguf`、`awq`、`gptq` 等 skills，让 Agent 帮你：

- 选择推理框架；
- 配置 OpenAI-compatible API；
- 优化 batch、并发、KV cache 和显存；
- 做量化与格式转换；
- 分析延迟、吞吐和部署成本。

### 做一个 RAG / Agent 应用

可以结合 `langchain`、`llamaindex`、`faiss`、`qdrant`、`chroma`、`sentence-transformers`、`dspy` 等 skills，让 Agent 帮你：

- 设计文档切分、embedding、索引和召回策略；
- 接入向量数据库；
- 设计工具调用和多 Agent 流程；
- 增加结构化输出、观测和评测。

### 写论文和做科研表达

可以结合 `ml-paper-writing`、`systems-paper-writing`、`academic-plotting`、`presenting-conference-talks` 等 skills，让 Agent 帮你：

- 梳理论文贡献点；
- 写 introduction、related work、method、experiment；
- 设计实验图表；
- 准备 conference talk 和 rebuttal 材料。

### 做视觉设计和内容生成

可以结合 `open-design`、`frontend-design`、`web-design-engineer`、`taste-skill-frontend-direction`、`seedance2-skill`、`seedance-prompt-zh`、Runway 系列 skills，让 Agent 帮你：

- 生成网页、App 原型、仪表盘和落地页；
- 制作 PPT、海报、社媒图、报告和视觉模板；
- 撰写 Seedance 2.0 视频提示词，支持图片、视频、音频和文本的多模态引用；
- 生成图片、视频、音频素材；
- 把媒体生成 API 集成进项目。

### 使用这些 GitHub 仓库分析技能

可以直接点名技能，也可以描述任务：

```text
用 twenty-crm-development skill 帮我新增一个 CRM 对象
用 claude-mem-operations 帮我排查为什么记忆没有出现
用 freedomain-dns-ops 帮我配置 Cloudflare nameserver
用 understand-anything-knowledge-graph 帮我给这个仓库做新人 onboarding 图谱
用 taste-skill-frontend-direction 帮我重设计这个 landing page
用 ppf-contact-solver-workflows 帮我跑一个 Docker/Jupyter 接触仿真实验
用 pixelle-video-workflows 帮我安装 Pixelle-Video 并生成一个 5 分镜短视频
用 gsap-scrolltrigger 和 gsap-react 帮我在 Next.js 里做一个 pinned scroll 动画
```

## 如何在 Codex 中使用

把需要的 skill 目录复制到 Codex 的 skills 目录：

```bash
cp -R codex-skills/<skill-name> ~/.codex/skills/
```

或者批量复制：

```bash
cp -R codex-skills/* ~/.codex/skills/
```

项目级 skills 可以从 `project-agent-skills/` 复制：

```bash
mkdir -p .agents/skills
cp -R project-agent-skills/<skill-name> .agents/skills/
```

复制后重启 Codex 或刷新 Agent 会话，让新的 skill 列表重新加载。

## 说明

- 本仓库是本地 skills 的导出集合，包含多个来源的 skill。
- 部分 skill 可能依赖第三方工具、API Key、GPU 环境或外部服务。
- 如果要公开发布，请根据每个 skill 的来源检查对应许可证和引用要求。
- 这些仓库分析技能是紧凑的工作流总结，没有把原仓库源码打包进来。
