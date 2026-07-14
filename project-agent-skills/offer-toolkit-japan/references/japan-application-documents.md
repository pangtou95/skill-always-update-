# Japan Application Documents

## Choose The Required Set

Never assume a single resume format. Read the employer's instructions first.

| Document | Main purpose | Common use |
| --- | --- | --- |
| 履歴書 | identity, education/work timeline, qualifications, concise motivation | Japanese hiring processes |
| 職務経歴書 | detailed professional evidence and self-promotion | mid-career and experienced candidates |
| Entry Sheet | company-specific questions and motivation | new-graduate recruiting |
| English resume/CV | role-focused evidence | foreign companies and international teams |
| Portfolio/GitHub | work samples | design, product, engineering, research and creative roles |

## Shared Source Of Truth

Create one structured candidate profile containing:

- names as legally/officially used and kana/romanization where requested
- contact details and current location
- education and employment dates
- status of residence only where relevant/requested
- languages and dated certifications
- skills, projects, responsibilities and verified results
- desired conditions and availability

Generate every document from this profile. Run a cross-document consistency check before submission.

## 履歴書

Use the current employer-specified form or the MHLW sample as a neutral starting point. Follow these rules:

- Keep era or Gregorian years consistent throughout.
- Verify every school/employer legal name and entry/exit month.
- Use a professional photo only when the employer/form asks for one; do not invent a universal requirement.
- Keep 志望動機 specific: company/role reason + candidate evidence + intended contribution.
- Use 本人希望記入欄 for genuine conditions, not a second essay. If there is no special request, use a conventional neutral statement only when appropriate.
- List certificates with official names, scores and dates. Do not claim “business level” from a test alone.

Use `assets/rirekisho.md.template` as a drafting schema, then transfer content into the requested form.

## 職務経歴書

Prefer A4, readable structure, and evidence matched to the role. A useful order is:

1. 職務要約
2. 活かせる経験・知識・技術
3. 職務経歴 by employer/project
4. achievements and measurable contribution
5. qualifications/languages if relevant
6. 自己PR

For each role include business/context, period, team/role, responsibilities, candidate actions, technology/method, and verified outcomes. Distinguish team results from personal contribution.

Use `assets/shokumukeirekisho.md.template`.

## Entry Sheet

Respect character limits. Answer the exact question first, then evidence, then connection to the company. Common themes include:

- 学生時代に力を入れたこと
- 自己PR
- 志望動機
- research or study theme
- challenge, teamwork, failure and learning
- desired work and future contribution

Do not recycle the same paragraph without adapting the requested angle.

## English Resume

Use role-first content and ATS-safe single-column layout for online applications. The bundled 13 HTML templates originate from the upstream offer toolkit; prefer `classic-ats.html` or `ledger.html` for automated screening. Visual templates are better for direct human review or portfolio contexts.

## Translation Rules

- Translate meaning and professional function, not word-for-word titles.
- Preserve facts, scope and metrics across languages.
- Keep a terminology glossary for company/product names and domain terms.
- Japanese self-promotion should sound natural and speakable, not machine-translated.
- Mark uncertain translations for review by the user.

## Final QA

- dates and names match across all documents
- no placeholder/example content remains
- all numbers have evidence or `[待确认]`
- filenames are professional and company-specific where needed
- private information is minimized for public portfolios
- PDF text remains selectable and layout does not clip
- application answers match the submitted version retained in the workspace
