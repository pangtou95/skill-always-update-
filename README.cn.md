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
| 学习与深度研究助手 | `deeptutor-cli` | 操作 DeepTutor 的辅导、深度解题、测验、研究、知识库、笔记本、记忆、会话、Partner、API 和本地 Web 应用流程 |
| Prompt 与结构化输出 | `dspy`、`guidance`、`outlines`、`instructor` | 编写可控 prompt、结构化 JSON 输出、约束式生成、prompt 优化和程序化提示工程 |
| 安全与对齐 | `constitutional-ai`、`llamaguard`、`nemo-guardrails`、`prompt-guard` | 做安全策略、内容过滤、prompt injection 防护、护栏设计和对齐方法研究 |
| 多模态与生成模型 | `opennana-image-video-prompt-studio`、`gpt-image-2-style-library`、`stable-diffusion`、`segment-anything`、`clip`、`blip-2`、`llava`、`whisper`、`audiocraft` | 制作结构化生图/生视频提示词包，衔接图转视频，并处理图像生成、理解、分割、视觉语言模型、语音和音频 |
| 论文与科研写作 | `ml-paper-writing`、`systems-paper-writing`、`academic-plotting`、`presenting-conference-talks` | 写 ML/系统论文、实验图表、会议演讲稿、研究叙事和投稿材料 |
| 研究创意与自动研究 | `0-autoresearch-skill`、`brainstorming-research-ideas`、`creative-thinking-for-research` | 生成研究方向、拆解论文想法、设计实验、做技术路线探索 |
| 前端与视觉设计 | `hallmark`、`border-beam-ui`、`frontend-design`、`web-design-engineer`、`open-design` | 生成和审计具有结构差异的网页、组件、发光状态边框、仪表盘、演示文稿、海报、社媒图、交互原型和设计系统 |
| 前端动效 | `border-beam-ui`、`gsap-core`、`gsap-timeline`、`gsap-scrolltrigger`、`gsap-react`、`gsap-plugins`、`gsap-utils`、`gsap-performance`、`gsap-frameworks` | 编写和审查克制的边框动效、GSAP 动画、时间线、ScrollTrigger、插件、框架生命周期、低动态模式和性能 |
| 内容创作者运营 | `human-writing`、`content-research-brief`、`seo-aeo-outline`、`viral-hook-title`、`script-writer`、`platform-repurpose`、`brand-voice-guard`、`fact-check-citation`、`content-calendar-planner`、`asset-prompt-pack`、`publish-metadata-ops`、`aitoearn-compliance-ops` | 先写有材料支撑的自然中文，再做选题调研、大纲、标题、脚本、平台改写、品牌语气检查、事实核查、内容日历、视觉提示词包、发布元数据和 AiToEarn 合规自动化风控 |
| 视频导演、提示词与媒体生成 | `opennana-image-video-prompt-studio`、`video-director-studio`、`seedance-2-5-prompt-studio`、`seedance-director-compat`、`seedance2-skill`、`seedance-prompt-zh`、`seedance-prompt-en`、`pixelle-video-workflows`、`rw-generate-video` | 把想法和素材整理成题材选型、提示词包、导演方案、时间轴、参考职责/角色隔离、镜头/连续性/声音包，再编译为各模型提示词或媒体生成集成 |
| 可编辑视频制作 | `chatcut-plugin-basics`、`chatcut-asset-import`、`chatcut-transcription`、`chatcut-create-motion-graphics`、`chatcut-voice`、`chatcut-music`、`chatcut-export`、`chatcut-verification` | 通过 ChatCut MCP 操作可编辑视频项目：导入素材、编辑时间线、添加字幕、制作 MG 动效、生成配音/音乐/视频素材、导出并验证可见结果 |
| 爬虫与内容工具 | `scrapling-official`、`video-downloader`、`youtube-clipper`、`cangjie-skill` | 做网页抓取、合规下载媒体、保留转写和元数据、把长内容蒸馏为经过测试的 skills，以及 YouTube 内容裁剪 |
| 求职与日本就业 | `career-ops`、`offer-toolkit-japan` | 扫描和跟踪申请，分析日文/英文 JD，制作履歴書、職務経歴書和英文简历，准备双语面试，并审查内定、劳动条件和在留资格问题 |
| 全网触达与跨平台研究 | `agent-reach` | 在网页、RSS、GitHub、YouTube、B站、V2EX、语义搜索和可选登录态社交平台之间路由研究任务 |
| 交互研究与网页情报 | `jupyter-live-kernel`、`arxiv`、`firecrawl*`、`wigolo` | 做有状态 Python 探索、论文检索、网页搜索/抓取/监控，以及本地优先的 MCP 研究 |
| 规划、写作与演示 | `plan`、`human-writing`、`humanizer`、`research-paper-writing`、`powerpoint`、`grill-me` | 写实施计划，创作和修改自然中文，制作科研论文与可编辑 PPT，并通过高强度追问检验方案 |

## Human Writing 中文写作 Skill

本次导出安装了 [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) `1.1.0`，对应上游提交 `4fda173f3fef7fb808f3eba991eeb2528ea4b189`。MIT 许可的完整 Skill、参考规则、Lite 版本、Agent 元数据和文风检查脚本均已保留在 `codex-skills/human-writing/`、`project-agent-skills/human-writing/` 与 `user-agent-skills/human-writing/`。

使用 `$human-writing` 可以写知乎回答、公众号文章、论坛长帖、博客、人物稿、行业与产品解读、评测、故事、脚本和口播。它会先判断中文长篇非虚构的材料是否充分，区分现实事实与虚构内容，再按文体读取对应规则，完成中文语序、节奏和段落推进的修改，最后还可以运行 `scripts/check_prose.py` 做诊断。

原有 `humanizer` 遇到中文文章类任务时，现在会优先路由到 `human-writing`。`script-writer`、`platform-repurpose` 和 `brand-voice-guard` 也已接入中文终稿检查。事实、引用、法律表述、品牌规范、平台限制和用户真实语气始终优先。系统不会为了制造活人感而编造第一人称经历或观点，也不会把文章专用的标点规则强加给代码、URL、机器元数据及无关的技术或学术格式。

Terminal 中可以这样调用：

```text
使用 $human-writing，把这些已经核实的材料写成一篇中文公众号文章。先检查事实边界，再写初稿，最后运行文风检查。
```

## 内容创作者 Top 10 Skills

本次更新安装了截图里的 10 个内容创作者 skills。每个 skill 都保留截图里的名称作为触发入口，并把上游材料放在 `references/upstream/` 下面。

| Skill | 来源 | 状态 |
| --- | --- | --- |
| `content-research-brief` | `Affitor/affiliate-skills` | 已安装 |
| `seo-aeo-outline` | `rampstackco/claude-skills` 的 `seo-aeo-geo` | 作为聚焦 wrapper 安装 |
| `viral-hook-title` | `EvolutionAPI/evo-nexus` 的 `social-hook-writer` | 作为聚焦 wrapper 安装 |
| `script-writer` | `Affitor/affiliate-skills` 的 `tiktok-script-writer` | 作为聚焦 wrapper 安装 |
| `platform-repurpose` | `Affitor/affiliate-skills` 的 `content-repurposer` | 作为聚焦 wrapper 安装 |
| `brand-voice-guard` | `anthropics/knowledge-work-plugins` 的 `brand-voice-enforcement` | 作为聚焦 wrapper 安装 |
| `fact-check-citation` | `petar-nauka/fact-check-skill` | 作为聚焦 wrapper 安装 |
| `content-calendar-planner` | `rampstackco/claude-skills` 的 `content-strategy` | 作为聚焦 wrapper 安装 |
| `asset-prompt-pack` | `Affitor/affiliate-skills` 的 `infographic-generator` | 作为聚焦 wrapper 安装 |
| `publish-metadata-ops` | 截图里的来源仓库未公开可访问 | 作为本地整理版安装 |

## Narrator AI CLI Skill

本次导出加入了 [NarratorAI-Studio/narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill)，用于 AI 电影/短剧解说视频的完整制作流程：

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `narrator-ai-cli-skill` | `codex-skills/`、`project-agent-skills/`、`user-agent-skills/` | 搜索内置影视素材，选择 BGM、配音和解说模板，生成文案，合成视频，可选 Magic Video 模板，并按规范轮询任务状态 |

运行说明：该 skill 需要 `narrator-ai-cli` 命令，以及有效的 `NARRATOR_APP_KEY` 或已配置的 app key。

## AiToEarn 合规运营 Skill

本次导出加入了 [yikart/AiToEarn](https://github.com/yikart/AiToEarn) 的合规运营自动化 skill。上游项目提供 Create、Publish、Engage、Monetize、MCP/API、Docker 和 Relay 等多平台内容运营能力；这个本地 skill 在外部平台写操作前增加保守风控层。

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `aitoearn-compliance-ops` | `codex-skills/`、`project-agent-skills/` | 为 AiToEarn 发布、回复、互动、变现和排期流程增加官方 API/OAuth 优先、人工审批、账号健康检查、冷却、审计日志和拒绝绕风控策略 |

内置辅助脚本：`scripts/risk_check.py` 会把结构化 action JSON 与 `assets/default_policy.json` 对比，并返回 `allow`、`approve`、`delay` 或 `block`。

## ChatCut Agent Plugin Skills

本次导出加入了 [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin.git) 的 ChatCut 技能包。上游项目是面向 Codex 的可编辑视频制作插件；本仓库将其中的工作流 skills 以 `chatcut-*` 命名空间导出，并保留必要 helper 脚本，同时去掉体积较大的 FFmpeg 压缩二进制，方便上传 GitHub。

| 技能组 | 位置 | 主要用途 |
| --- | --- | --- |
| `chatcut-*` | `codex-skills/`、`project-agent-skills/` | ChatCut MCP 设置、项目定位、素材导入、时间线编辑、转写字幕、口播视频清理、Motion Graphic JSX 编写、图像/视频/配音/音乐生成、shader 效果、导出和可见结果验证 |

运行提示：真正编辑 ChatCut 项目需要配置 ChatCut MCP server 并完成 ChatCut 登录。优先从 `chatcut-plugin-basics` 开始；如果 MCP 没有配置，先看它的 `references/plugin-setup.md`。

## 视频下载与长内容蒸馏 Skills

本次导出把 [davila7/claude-code-templates 的 video-downloader](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/media/video-downloader) 和 [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) 整合成一条连续工作流：

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `video-downloader` | `codex-skills/`、`project-agent-skills/` | 用 `yt-dlp` 下载用户有权使用的在线视频/音频，选择清晰度和格式，保留字幕、元数据和缩略图，检查播放列表，验证结果，并拒绝 DRM 或访问控制绕过 |
| `cangjie-skill` | `codex-skills/`、`project-agent-skills/` | 用 RIA-TV++、五类提取、三重验证、知识链接和压力测试，把书籍、长视频转写、播客、课程、访谈和资料集蒸馏成原子化、可追溯、可续跑的 skills |

`video-downloader` 带有可执行的 `scripts/download_media.py`，默认使用保守参数并支持 dry-run。`cangjie-skill` 保留上游方法论、提取器和输出模板，同时适配 Codex 安装路径与 frontmatter 规范。

## 日本求职 Offer Toolkit

本次导出把 [yanliudesign/offer-toolkit-skill](https://github.com/yanliudesign/offer-toolkit-skill) 升级为面向日本求职、以证据为基础的完整工作流。保留上游的 JD 分析、简历模板和 STAR/CAR 面试方法，同时去掉作者电脑固定路径、强制推广内容和没有依据的“面试概率”精确数字。

| Skill | 安装位置 | 主要用途 |
| --- | --- | --- |
| `offer-toolkit-japan` | `codex-skills/`、`project-agent-skills/` | 分流新卒、第二新卒、中途、外资和国际团队岗位；分析 JD 与公司；制作履歴書、職務経歴書、Entry Sheet 和英文 resume；用证据卡和追问树准备日英双语面试；审查内定、固定残业、転勤和在留资格支持 |

该 skill 内置日本求职文档模板、上游 MIT 许可的 13 套英文简历版式、130+ 面试问题、面试阶段/岗位分层、短期离职与职业一贯性深挖、领导/系统交付/AI 辅助事实边界，以及基于 2025-2026 招聘方资料和候选人案例的动态情报流程。`scripts/interview_pack_audit.py` 检查题库覆盖和表述边界，`scripts/japan_offer_audit.py` 检查劳动条件。批量岗位扫描、申请跟踪和 pipeline 管理继续配合 `career-ops` 使用。

## Video Director Studio 视频导演工作台

本次导出新增了一个模型无关的视频导演层，来源是对 [Liblib/LibTV Skill 页面](https://www.liblib.tv/skill)公开元数据的综合分析。2026-07-14 页面共返回 103 个条目，覆盖专业影视、商业广告、动漫游戏、自媒体、短剧漫剧、通用工具和音乐 MV。仓库没有复制创作者未公开的 Skill 正文或案例素材，而是把反复出现的方法提炼成可组合的原创制作系统。

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `video-director-studio` | `codex-skills/`、`project-agent-skills/` | 选择成片类型和特征化导演语法；规划素材、角色、世界观、产品锁定、节拍、镜头、连续性、表演、光线、剪辑和声音；再编译给 Seedance、Runway、WAN/LTX、Pixelle、LibTV 或 ChatCut |

该 Skill 包含 37 套导演语法、20 种成片蓝图、18 个制作模块、结构化导演包模板、`scripts/director_pack_audit.py` 审计器和 `scripts/liblib_catalog.py` 公开目录刷新工具。现有 Seedance、Runway 和 Pixelle 项目 Skill 已接入该导演层，复杂多镜头任务会先完成导演包再生成。

## DeepTutor 与 Hallmark Skills

本次导出加入了 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) 和 [nutlope/hallmark](https://github.com/nutlope/hallmark) 的学习研究与界面设计 Skills，并完成 Codex 兼容和独立安装修复。

| Skill | 安装位置 | 主要用途 |
| --- | --- | --- |
| `deeptutor-cli` | `codex-skills/`、`project-agent-skills/` | 检查、安装、初始化和操作 DeepTutor 1.5.2，覆盖辅导、深度解题、题目生成、研究、可视化、文档知识库、笔记本、会话、记忆、Partner、API 服务和本地 Web 应用 |
| `hallmark` | `codex-skills/`、`project-agent-skills/` | 设计、审计、重设计和研究界面，提供 21 种宏观结构、20 套主题、响应式/交互状态检查、可移植 design tokens 和 58 项反模板化审查 |

`deeptutor-cli` 是操作 Skill，不包含 DeepTutor 应用本体。真正运行前仍需安装外部 `deeptutor` 命令，并配置用户选择的模型和 embedding 服务。Hallmark 是纯指令 Skill，不需要 Hallmark 程序；本次打包补入了上游独立 Skill 目录遗漏的主题 token 和案例参考。两份包均保留 Apache-2.0 或 MIT 许可证说明。

## Border Beam UI 边框动效 Skill

本次导出新增 `border-beam-ui`，基于 MIT 许可的 [Jakubantalik/border-beam](https://github.com/Jakubantalik/border-beam) React 组件和[交互演示站](https://beam.jakubantalik.com/)，把上游效果预设整理成适用于按钮、图标控件、输入框、搜索栏、选中卡片、加载状态和短暂成功反馈的克制设计规则。

| Skill | 安装位置 | 主要用途 |
| --- | --- | --- |
| `border-beam-ui` | `codex-skills/`、`project-agent-skills/` | 选择 `sm`、`md`、`line`、`pulse-inner` 或 `pulse-outside`；接入 React 18+ 官方包或跨框架 CSS 回退；映射产品 token；审计焦点、低动态模式、裁切、明暗主题、密度和性能 |

2026-08-05 已检查上游提交 `647d26e2a27f26587110fea5a8410c80deb5ac5e` 的组件 API、渲染层、主题/配色、启停淡入淡出、脉冲离屏暂停和约 30 fps 共享驱动。当时仓库 manifest 为 `1.4.0`，npm `latest` 仍是 `1.3.0`，因此 Skill 要求先核对实际安装版本再采用精确默认值。它不会让所有组件一起发光：密集业务界面默认只在事件发生时启动，并始终保留稳定细边、语义状态和清晰键盘焦点。`scripts/audit_beam_usage.py` 可检查常见接入错误。

## OpenNana 生图与生视频提示词工作台

本次导出新增了一个跨模型原创提示词层，来源是对 [OpenNana 生图画廊](https://opennana.com/awesome-prompt-gallery?media_type=image)和[生视频画廊](https://opennana.com/awesome-prompt-gallery?media_type=video)公开组织方式与元数据的综合分析。仓库不会复制锁定/付费提示词、创作者素材或整站提示词正文。

| Skill | 安装位置 | 主要用途 |
| --- | --- | --- |
| `opennana-image-video-prompt-studio` | `codex-skills/`、`project-agent-skills/` | 分流生图、生视频与图转视频任务；选择成片题材；为参考素材分配单一职责；制作构图或时间轴；控制文字/声音；检查权利；设计变量并校验结构化提示词包 |

2026-08-05 检查时，图片端可见 Nano Banana Pro、Nano Banana 2、ChatGPT、Grok 模型筛选，视频端可见 Seedance 2.0。服务端渲染的图片页面显示 14,110 条，而同一页面使用的公开列表 API 返回 15,962 条；视频页面与 API 均返回 613 条。Skill 会记录这种动态差异，不把数量或社区案例当成永久的模型能力承诺。包内附原创图像/视频模式库、图转视频模板、JSON 模板和 `scripts/validate_prompt_pack.py`。

## Seedance 2.0 与 2.5 Skills

本仓库保留 [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) 的 2.0 双语资料，并新增基于 [ByteDance Seed 官方发布](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)和 [EvoLink 公开提示词画廊](https://evolink.ai/seedance-2-5-prompts)提炼的 2.5 制作层。没有批量复制网页提示词，而是审计 122 个公开卡片后提炼成原创结构、模板和验证规则。

| Skill | 位置 | 主要用途 |
| --- | --- | --- |
| `seedance2-skill` | `codex-skills/seedance2-skill` | 完整双语 Seedance 2.0 提示词包，根目录为英文说明，`zh/` 下为中文说明，并保留上游 README |
| `seedance-prompt-en` | `project-agent-skills/seedance-prompt-en` | 英文 Seedance 2.0 提示词流程，覆盖多模态引用、运镜语言、分镜节奏、特效、广告、短剧和科普视频 |
| `seedance-prompt-zh` | `project-agent-skills/seedance-prompt-zh` | 中文 Seedance 2.0 提示词流程，已对齐上游 `zh/SKILL.md` |
| `seedance-2-5-prompt-studio` | `codex-skills/`、`project-agent-skills/` | 为 Seedance 2.5 生成 30 秒分幕、12 类成片格式、单职责参考图、角色/九宫格隔离、原生声音/对白、时间戳编辑、负面约束和验收清单 |
| `seedance-director-compat` | `codex-skills/`、`project-agent-skills/` | 制作 Seedance 2.0/2.5 兼容的中英双语物理与连续性合同，并在模型不可用时编译 WAN/LTX 回退包 |

2026-08-05 核验状态：Seedance 2.5 已于 2026-07-31 官方发布并在即梦/豆包 Pro 滚动开放；官方公布单次最长 30 秒、最多 30 图片/10 视频/10 音频、多轮延长和时间戳编辑。EvoLink 当日仍是文档已发布、生成路由未开放，并称第一方 API 将于 2026-08-07 开放，因此 Skill 要求每次执行前重新核验具体平台，不能把模型能力直接当成可调用 API。

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

## 截图提取的高级 Skills 与 Agent 工具

本次核对了两张截图。第一张的 11 个名称此前都没有以同名 Skill 安装，现已补齐；其中 `writing-plans / plan` 按当前上游名称安装为 `plan`。`firecrawl` 还补入 9 个官方配套路由，避免主 Skill 内的相对链接和分流能力缺失。

| Skill | 来源 | 状态与用途 |
| --- | --- | --- |
| `jupyter-live-kernel` | `moltis-org/moltis` / Hermes 来源 | 用 `hamelnb` 运行可持续状态的 Jupyter kernel |
| `plan` | `NousResearch/hermes-agent` | 只写计划、不执行，覆盖截图中的 `writing-plans / plan` |
| `claude-design`、`sketch` | `NousResearch/hermes-agent` | 生成一次性 HTML 设计成品，或并排比较 2-3 个交互草图 |
| `powerpoint` | `bojieli/ai-agent-book` 的 Apache-2.0 `pptx` 示例改编 | 从结构化大纲生成并验证可编辑 `.pptx`；没有复制禁止再分发的 Anthropic 版本 |
| `humanizer` | `NousResearch/hermes-agent` | 清理通用 AI 腔；中文文章类内容交给 `human-writing`，同时保留原意、事实和作者声音 |
| `arxiv`、`research-paper-writing` | `NousResearch/hermes-agent` | 检索 arXiv，并完成研究设计、实验、引用、写作与投稿检查 |
| `firecrawl` + 9 个 `firecrawl-*` | `firecrawl/cli` | 搜索、抓取、站点地图、爬取、交互、下载、解析和变化监控 |
| `grill-me` | `feiskyer/codex-settings` | 显式触发的高强度方案追问、术语表和 ADR 维护 |
| `popular-web-designs` | `NousResearch/hermes-agent` | 54 套真实产品设计系统参考与 HTML/CSS 规则 |

第二张图展示的是完整项目，不是都能直接作为 Skill 调用。本仓库为它们增加了诚实的操作层，不打包应用本体，也不会把“安装成功”误报为“任务已经运行”。

| Skill | 对应项目 | 主要用途 |
| --- | --- | --- |
| `ai-agent-book-guide` | `bojieli/ai-agent-book` | 按 10 章路线学习和实践 Agent、上下文、记忆、工具、评估、训练、多模态与协作 |
| `code-review-graph` | `tirth8205/code-review-graph` | 安装 Codex MCP，构建本地代码图谱，做影响分析、审查、调试和重构 |
| `voicebox-studio` | `jamiepine/voicebox` | 通过本地 REST/MCP 做 TTS、转写、voice profile 和 Agent 语音输出 |
| `wigolo` | `KnockOutEZ/wigolo` | Node 20+ 的本地优先搜索、抓取、爬取、缓存、提取和研究 MCP |
| `ktransformers-ops` | `kvcache-ai/ktransformers` | 评估硬件，规划和排查 CPU-GPU 异构 MoE 推理与 LLaMA-Factory SFT |

终端中可以直接点名，例如：`用 $grill-me 追问我的方案`、`用 $arxiv 搜索这篇论文`、`用 $code-review-graph 审查当前 diff`。外部工具型 Skill 仍需先安装对应 CLI、应用、运行时或模型。

## 本次新增的 GitHub 仓库分析技能

最近更新新增了一批直接来自或从公开 GitHub 仓库提炼出来的 skills：

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
| `aitoearn-compliance-ops` | `yikart/AiToEarn` | AiToEarn 内容运营合规自动化，覆盖发布、互动、账号健康、审批门禁、冷却、审计日志、MCP/API、Docker/Relay 和拒绝绕风控 |
| `chatcut-*` | `ChatCut-Inc/agent-plugin` | 通过 ChatCut MCP 做可编辑视频制作：素材导入、时间线编辑、字幕转写、口播清理、MG 动效、图像/视频/配音/音乐生成、shader 效果、导出和验证 |
| `video-downloader` | `davila7/claude-code-templates` | 面向授权素材的视频/音频下载，支持清晰度与格式选择、字幕/元数据保存、播放列表控制、dry-run、输出验证和禁止绕过限制 |
| `cangjie-skill` | `kangarooking/cangjie-skill` | 用 RIA-TV++ 把长内容蒸馏成可追溯、有关联、经过压力测试的 agent skills，并支持状态断点续跑和模板化交付 |
| `offer-toolkit-japan` | `yanliudesign/offer-toolkit-skill` + 日本官方及近期市场资料 | 面向日本市场的岗位分流、证据化 JD 匹配、履歴書/職務経歴書/Entry Sheet/英文简历、带追问树与事实边界的 130+ 面试题库，以及内定、劳动条件、固定残业、転勤和在留资格审查 |
| `video-director-studio` | `liblib.tv/skill` 公开元数据综合分析 | 模型无关的 AI 视频导演编排，覆盖特征化导演语法、TVC/短剧/MV/动画/UGC 蓝图、制作模块、镜头与连续性合同、模型适配和结构化质检 |
| `deeptutor-cli` | `HKUDS/DeepTutor` | DeepTutor 1.5.2 的 Codex 兼容 CLI 操作层，包含运行预检、修正后的安装路径、证据化学习流程和破坏性操作保护 |
| `hallmark` | `nutlope/hallmark` | Hallmark 1.1.0 界面设计与审计流程，包含完整上游参考、补齐的 20 主题 token、修复后的独立链接和 Codex UI 元数据 |

这些技能放在 `project-agent-skills/` 目录下；包括 `agent-reach`、`offer-toolkit-japan`、`video-director-studio`、`deeptutor-cli` 和 `hallmark` 在内的直接使用包也同时导出到 `codex-skills/`。

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

可以结合 `hallmark`、`open-design`、`frontend-design`、`web-design-engineer`、`taste-skill-frontend-direction`、`seedance2-skill`、`seedance-prompt-zh`、Runway 系列 skills，让 Agent 帮你：

- 生成网页、App 原型、仪表盘和落地页；
- 制作 PPT、海报、社媒图、报告和视觉模板；
- 把模糊视频想法整理成导演方案、分镜、镜头/连续性/声音包和模型专用提示词；
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
用 aitoearn-compliance-ops 帮我设计一个带风控门禁的 AiToEarn 合规发布流程
用 chatcut-plugin-basics 和 chatcut-asset-import 帮我在 ChatCut 里编辑这个本地视频
用 chatcut-transcription 和 chatcut-export 帮我加字幕并导出成片
用 video-downloader 帮我把我拥有版权的视频下载成 1080p MP4，并保留字幕和元数据
用 cangjie-skill 把这份已授权课程转写稿蒸馏成可复用、经过测试的 skills
用 offer-toolkit-japan 分析这个东京岗位，制作履歴書和職務経歴書，并在不虚构经历的前提下准备日英双语面试包
用 deeptutor-cli 把这些 PDF 建成知识库，并生成带依据的中文测验
用 hallmark audit 审查这个前端，然后在保留现有路由和组件架构的前提下重设计
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
