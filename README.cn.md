# 我的 AI Skills 工具库

这是一个面向 Codex / AI Agent 的本地 skills 汇总仓库，整理了我当前工作环境里常用的研究、工程、设计、内容生成和自动化能力。

简单说：这些 skill 是给 AI Agent 使用的“专业工作说明书”。它们会告诉 Agent 在面对特定任务时该读取哪些资料、遵循哪些流程、调用哪些工具、产出什么格式，从而让同一个 Agent 在不同领域里表现得更像一个熟悉业务的专家。

## 这个仓库能做什么

这套 skills 覆盖的能力很宽，大致可以分为以下几类：

| 方向 | 代表 skills | 能实现的功能 |
| --- | --- | --- |
| 大模型训练与微调 | `axolotl`、`llama-factory`、`peft`、`unsloth`、`trl-fine-tuning` | 设计和实现 SFT、LoRA、QLoRA、指令微调、训练配置、数据格式转换、训练问题排查 |
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
| Runway 与媒体生成 | `rw-generate-image`、`rw-generate-video`、`rw-generate-audio`、`rw-integrate-*` | 对接 Runway API，生成图片、视频、音频，并把生成能力集成到项目里 |
| 爬虫与内容工具 | `scrapling-official`、`youtube-clipper`、`career-ops` | 做网页抓取、YouTube 内容裁剪、职业材料整理、信息提取和自动化脚本 |

## 适合哪些场景

- 想让 Codex 更懂 AI 研究工程，例如训练、微调、推理部署、评测和论文写作。
- 想快速搭建一个大模型实验项目，从数据、训练、推理到评估都有可参考流程。
- 想做 RAG、Agent、多模态应用，但希望 Agent 能按成熟工具链来规划和实现。
- 想让 Agent 具备设计能力，能创建前端应用、展示页面、PPT、视觉内容和多媒体素材。
- 想把本地工作流沉淀成可复用的专业技能库，方便迁移到新的 Codex 环境。

## 目录结构

```text
.
├── codex-skills/            # Codex 全局 skills，包含 AI Research、设计、前端等主要能力
├── project-agent-skills/    # 当前项目内的 agent skills，例如 Runway、多媒体、爬虫等
├── user-agent-skills/       # 用户级 agent skills
├── SKILLS_MANIFEST.txt      # 所有 SKILL.md 文件清单
└── README.md
```

## 重点能力示例

### 训练一个模型

可以结合 `llama-factory`、`axolotl`、`peft`、`deepspeed`、`accelerate` 等 skills，让 Agent 帮你：

- 选择 SFT / LoRA / QLoRA / DPO / GRPO 等训练方案
- 整理训练数据格式
- 生成训练配置
- 估算显存需求
- 排查 loss 异常、OOM、吞吐低、checkpoint 错误等问题

### 部署一个推理服务

可以结合 `vllm`、`sglang`、`llama-cpp`、`tensorrt-llm`、`gguf`、`awq`、`gptq` 等 skills，让 Agent 帮你：

- 选择推理框架
- 配置 OpenAI-compatible API
- 优化 batch、并发、KV cache 和显存
- 做量化与格式转换
- 分析延迟、吞吐和部署成本

### 做一个 RAG / Agent 应用

可以结合 `langchain`、`llamaindex`、`faiss`、`qdrant`、`chroma`、`sentence-transformers`、`dspy` 等 skills，让 Agent 帮你：

- 设计文档切分、embedding、索引和召回策略
- 接入向量数据库
- 设计工具调用和多 Agent 流程
- 增加结构化输出、观测和评测

### 写论文和做科研表达

可以结合 `ml-paper-writing`、`systems-paper-writing`、`academic-plotting`、`presenting-conference-talks` 等 skills，让 Agent 帮你：

- 梳理论文贡献点
- 写 introduction、related work、method、experiment
- 设计实验图表
- 准备 conference talk 和 rebuttal 材料

### 做视觉设计和内容生成

可以结合 `open-design`、`frontend-design`、`web-design-engineer`、`rw-generate-image`、`rw-generate-video`、`stable-diffusion` 等 skills，让 Agent 帮你：

- 生成网页、App 原型、仪表盘和落地页
- 制作 PPT、海报、社媒图、报告和视觉模板
- 生成图片、视频、音频素材
- 把媒体生成 API 集成进项目

## 如何在 Codex 中使用

把需要的 skill 目录复制到 Codex 的 skills 目录：

```bash
cp -R codex-skills/<skill-name> ~/.codex/skills/
```

或者批量复制：

```bash
cp -R codex-skills/* ~/.codex/skills/
```

复制后重启 Codex，让新的 skill 列表重新加载。

使用时可以直接对 Codex 说：

```text
用 vllm skill 帮我部署这个模型
用 verl skill 帮我设计 GRPO 训练流程
用 ml-paper-writing skill 帮我改论文 introduction
用 open-design skill 做一个产品展示页
```

## 说明

- 本仓库是本地 skills 的导出集合，包含多个来源的 skill。
- 原本是符号链接的 skill 已经被展开为真实文件，clone 后不会因为本地路径不同而失效。
- 部分 skill 可能依赖第三方工具、API Key、GPU 环境或外部服务。
- 如果要公开发布，请根据每个 skill 的来源检查对应许可证和引用要求。
