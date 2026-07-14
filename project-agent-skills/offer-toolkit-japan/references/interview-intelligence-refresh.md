# Current Interview Intelligence Refresh

Interview questions change by company, role, interviewer and stage. Refresh current evidence before company-specific preparation.

## Source Tiers

| Tier | Source type | Use |
| --- | --- | --- |
| A | current employer hiring pages, interviewer guides, recruiting-company surveys | infer evaluation axes and selection format |
| B | moderated candidate reports with company, role, stage and event date | discover likely questions and sequence |
| C | personal blogs, Note, Reddit, forums and social posts | discover edge cases and candidate friction |

Official government sources still govern labor, visa and fair-hiring facts. Non-official evidence is for interview intelligence, not legal conclusions or success probabilities.

## Freshness Rules

- Prefer event dates from the last 24 months.
- Record both `event_date` and `published_or_updated_at`.
- Match `new_grad/mid_career`, role family, seniority and interview stage.
- Do not treat a new publication describing an old interview as a current event.
- Keep older reports only when the company process appears stable and label them historical.

## Research Workflow

1. Read the current JD, company hiring page and stated selection flow.
2. Search current moderated reports for the exact company + role + stage.
3. Search current hiring-side guidance for the role family.
4. Add two or more candidate reports from other companies in the same role family.
5. Add anecdotal posts only for unexpected questions or foreign-candidate friction.
6. Cluster repeated evaluation intents, not just identical wording.
7. Build `base question -> follow-up -> evidence required -> risk` cards.
8. Mark every company-specific inference with confidence and source date.

## Search Recipes

Use Japanese and English variations:

```text
"<company>" "<role>" 中途 面接 質問 2025
"<company>" 選考体験談 <stage>
"<role>" 実際に聞かれた 面接 質問 2026
外国人 ITエンジニア 日本 転職 面接 体験談
インフラエンジニア 面接 AWS ネットワーク 障害対応
ITコンサル 中途 面接 ケース プロジェクト 役割
site:plus.onecareer.jp <company> <role> 面接
site:reddit.com/r/JapanJobs interview <role> Japan
```

Search result summaries are leads. Open the direct page before storing a claim.

## Extraction Record

For each useful source, save:

```yaml
url: ""
source_tier: A|B|C
company: ""
role: ""
lane: mid_career|new_grad|unknown
stage: casual|hr|manager|technical|case|final|unknown
event_date: ""
published_or_updated_at: ""
question_paraphrase: ""
evaluation_intent: ""
candidate_context: ""
confidence: high|medium|low
limitations: ""
```

Paraphrase candidate reports. Do not copy long answer text.

## 2025-2026 Signals To Include

Current hiring-side and candidate material supports preparing for:

- deeper verification of departure reason, action taken and recurrence risk;
- exact role and personal contribution in difficult projects;
- problem solving, failure, conflict, deadlines and reporting style;
- technical reasoning plus portfolio, artifacts or tests beyond verbal claims;
- AI-assisted applications and answers, making natural speech and evidence more important;
- casual interviews, web interviews, reference checks, video selection and AI interviews as possible selection formats;
- foreign-candidate language use, Japan career intent and status-of-residence logistics;
- role-specific overlays such as cases for consulting and troubleshooting for infrastructure.

These are market signals, not guarantees for a specific employer.

## Anti-Overfitting

- Do not promise that a question will be asked because one report contains it.
- Do not infer a company's current culture from one anonymous review.
- Do not copy a successful candidate's answer; fit evidence and language to the user.
- Do not optimize for ceremonial Japanese at the cost of clarity.
- Do not let live AI answer during an interview unless explicitly allowed by the employer.
- Treat candidate reports as survivorship-biased and incomplete.

## Output

Produce a short intelligence appendix containing:

- research date;
- selected source list with tier and event date;
- repeated evaluation intents;
- company-specific questions with confidence;
- role overlay;
- unknowns to ask the recruiter;
- changes made to the mock interview set.
