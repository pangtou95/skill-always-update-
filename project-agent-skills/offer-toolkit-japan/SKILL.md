---
name: offer-toolkit-japan
description: Japan-focused job-search and interview toolkit for decoding Japanese or English job descriptions, researching employers and current market conditions, deciding whether to apply, producing 履歴書・職務経歴書・English resumes, tailoring 志望動機 and 自己PR, building bilingual STAR story banks, practicing Japanese interviews, reviewing 内定 and employment terms, and checking work-status or visa questions against official sources. Use for 日本求职, 転職, 就活, 新卒, 中途採用, 外資系, JD analysis, resume/CV, behavioral interviews, 面接対策, offer comparison, salary research, or visa sponsorship. Do not fabricate candidate facts, promise interview probabilities, provide unverified immigration/legal conclusions, auto-submit applications, or spam employers.
---

# Offer Toolkit Japan

把“找岗位 -> 判断 -> 准备材料 -> 面试 -> 审查内定”做成一条证据化、可复用的日本求职流程。

## 核心原则

1. **不杜撰**：公司、经历、职责、成果、数字、日语水平和签证情况必须有来源。缺失项写 `[待确认]`。
2. **先分市场再优化**：区分新卒/既卒/第二新卒/中途、日企/外资/国际团队、人在日本/海外申请、日语工作/英语工作。
3. **不制造虚假精度**：输出证据等级和差距，不宣称“拿面概率 73%”。评分只能用于比较，不是预测结果。
4. **日本材料不是英文简历翻译**：按目标公司决定是否需要履歴書、職務経歴書、Entry Sheet、英文 resume 或作品集。
5. **动态信息必须现查**：薪资、招聘渠道、签证手续、劳动规则和公司现状优先查官方或一手来源；面试情报同时查近期招聘方资料、经过整理的候选人报告和实际复盘，并标注事件日期与来源等级。
6. **人工提交**：可以准备字段和草稿，不自动批量投递、不代替用户作虚假声明、不违反招聘网站条款。
7. **个人材料隔离**：用户过去的面试稿、简历和经历可用于个性化，但不得写入公开 skill。只在用户授权的工作区、附件、任务历史或连接来源中读取，并把个性化输出留在求职工作区。

## 第一步：建立求职画像

优先从用户已有简历、职位链接和上下文提取；只补问会改变策略的缺项：

- 求职路线：新卒 / 既卒 / 第二新卒 / 中途 / 管理职
- 目标岗位、行业、级别和期望入职时间
- 日语与英语的实际工作能力；JLPT/TOEIC 等只作为证据之一
- 当前居住地、在留资格、期限、是否需要新办或变更资格
- 可接受地点、remote/出社、転勤、出差和雇用形态
- 当前/期望总年收及不可妥协条件
- 真实经历、成果证据、作品集和推荐人情况

将画像保存到当前求职工作区的 `profile/candidate-profile.md`。不要把个人资料写回 skill 安装目录。

详细分流见 `references/japan-market-routing.md`。

## 路由

| 用户意图 | 执行内容 | 必读引用 |
| --- | --- | --- |
| 找岗位、选择渠道、了解市场 | 生成渠道组合、关键词和每周搜索计划 | `references/search-channels.md`, `references/japan-market-routing.md` |
| 分析 JD、该不该投、比较岗位 | 解码需求、证据匹配、差距和申请决策 | `references/jd-company-research.md`, `references/generic-methods.md` |
| 写或改日本简历 | 生成履歴書 + 職務経歴書；按需英文 resume | `references/japan-application-documents.md` |
| 准备面试、志望動機、自己PR | 建分阶段题库、证据卡、追问树、双语答案和模拟面试 | `references/japan-interview.md`, `references/interview-question-bank.md`, `references/interview-claim-boundaries.md` |
| 查近期面试题、真实案例和招聘趋势 | 按来源等级和事件日期刷新公司/岗位情报 | `references/interview-intelligence-refresh.md`, `references/sources.md` |
| 审查内定、比较 offer | 核对劳动条件、固定残业、签证和风险点 | `references/japan-offer-review.md` |
| 批量扫描、申请跟踪、pipeline | 使用现有 `$career-ops`，将本 skill 的日本规则作为市场配置 | `references/japan-market-routing.md` |

## 标准工作流

### 1. Research

读取 JD 原文和公司招聘页。补充研究时遵循以下顺序：

1. 日本政府、JASSO、公司招聘页和正式披露
2. 招聘平台原始职位页、公司技术博客、员工访谈和当前招聘方调查
3. 标明公司、岗位、阶段和面试事件日期的候选人报告
4. 薪资调查和职位聚合数据
5. 评价网站、个人博客、论坛和社交帖子，仅作为线索并标注偏差

### 2. Decide

输出：

- `must-have / preferred / hidden constraints`
- 每项“满足 / 部分满足 / 未证实 / 明确不满足”及候选证据
- 日本特有门槛：语言、所在地、在留资格、学历/专业与工作内容关系、出社和転勤
- 值得投、条件性值得投或不建议投，并给出机会成本与补救动作

### 3. Prepare

按目标公司要求生成材料，不默认只做一页英文简历：

- 履歴書：事实时间线、资格、志望動機、本人希望
- 職務経歴書：职业摘要、技能、项目/职责、成果、自己PR
- Entry Sheet：按题目和字数限制定制
- 英文 resume：外资、国际团队或明确要求时生成
- 面试包：20/60/120 秒答案、每段职历的入退社理由、证据卡、追问树、角色边界、岗位专项题和逆質問

面试准备必须先读取用户已有材料。如果用户提到“之前的面接想定问答”，先在用户授权范围内定位并复用题型与已确认事实，再生成新版；不要从零做一份通用稿覆盖旧内容。

### 4. Interview Intelligence And Drill

1. 根据 `references/interview-question-bank.md` 建立 `P0/P1/P2/LIVE` 覆盖表。
2. 对短期离职、职业方向变化、领导经验、客户接触、系统规模、AI辅助工作和陌生资格证执行 `references/interview-claim-boundaries.md`。
3. 按 `references/interview-intelligence-refresh.md` 查过去24个月的同公司、同岗位、同阶段情报；单个匿名报告不得当作确定流程。
4. 使用 `assets/interview-master-pack.md.template`，为高风险题准备主回答和至少三条追问分支。
5. 模拟面试一次只问一题，先测自然回答，再给一个优先修改点并重答。不要让用户逐字背AI稿。

### 5. Verify

- 对齐所有文档的日期、公司名、职称、指标和离职原因。
- 将每个重要数字映射到用户证据；无法确认则保留占位符。
- 对当前法规和签证问题附官方链接与“非法律意见”说明。
- 生成文件到用户工作区，例如 `applications/<company>/<role>/`，不要使用作者电脑的固定路径。

### 6. Structured Audits

面试包可先复制 `assets/interview-pack.json.template` 到用户工作区，再运行：

```bash
python3 scripts/interview_pack_audit.py path/to/interview-pack.json
```

脚本检查覆盖和事实边界，不预测通过率。

收到内定通知、労働条件通知書或合同后，运行：

```bash
python3 scripts/japan_offer_audit.py path/to/offer-terms.json
```

脚本只检查信息完整性和需要追问的项目，不替代律师、行政书士、社劳士或入管确认。

## 输出标准

- 区分事实、推断、用户偏好和待核实项。
- 每份市场研究标注 `researched_at` 和直接来源 URL。
- 默认给中文策略说明；申请材料使用目标公司要求的日语/英语。
- 日语面试稿同时给“自然口语版”和中文意图，不写难以说出口的书面敬语。
- 面试情报区分招聘方资料、经过整理的候选人报告和匿名轶事；记录 `event_date`，不只看网页更新时间。
- 面试答案区分正式PL/PM与跨部门推进、客户本番系统与内部工具/PoC、本人负责与AI辅助、资格领域相近与官方等价。
- 不强迫所有回答使用“理由は2点あります”，也不输出整齐到失去个人语言习惯的背诵稿。
- 先生成可审阅文本，再渲染 HTML/PDF。可使用 `assets/resume-templates/` 的 13 个上游模板制作英文 resume；日本标准材料优先使用本 skill 的日本模板。

## 来源与边界

本 skill 基于 `yanliudesign/offer-toolkit-skill` 的 MIT 许可框架，并吸收现有 `$career-ops` 的本地化、pipeline 和 human-in-the-loop 思路。日本规则来自 JASSO、厚生劳动省、Hello Work、JETRO 和出入国在留管理厅等来源；面试情报还综合当前招聘方调查、招聘顾问资料、经过整理的选考报告和带偏差说明的候选人复盘。查看 `references/sources.md`。
