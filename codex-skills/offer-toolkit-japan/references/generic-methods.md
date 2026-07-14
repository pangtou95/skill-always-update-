# Generic Offer Toolkit Methods

Use these methods for any market, then apply the Japan-specific references.

## JD Decode

Decode a job description in five layers:

1. **Business need**: What outcome is the team hiring for now?
2. **Must-have evidence**: Which requirements appear mandatory, repeated, or tied to screening?
3. **Preferred evidence**: Which items improve ranking but are teachable after joining?
4. **Hidden constraints**: Level, autonomy, stakeholder scope, location, language, schedule, visa, travel, or domain familiarity.
5. **Selection signals**: Likely document screen, case, coding exercise, portfolio review, aptitude test, panel, or behavioral evaluation.

Do not infer internal facts from generic wording. Label every hidden constraint as a hypothesis and state the textual evidence.

## Evidence Match

Build a matrix rather than keyword-counting:

| Requirement | Weight | Candidate evidence | Evidence strength | Status | Repair action |
| --- | ---: | --- | --- | --- | --- |
| Example | high | project/result/source | verified/claimed/absent | met/partial/unknown/gap | action |

Use weights only to compare roles consistently. Do not turn the result into an interview probability.

Recommended decision states:

- **Apply**: Core work fits, no hard blocker, and evidence can be presented honestly.
- **Apply conditionally**: One or two uncertainties must be confirmed early, such as sponsorship or language expectations.
- **Deprioritize**: Major blocker, weak strategic fit, poor conditions, or high opportunity cost.

## Resume Tailoring

Tailor only with existing facts:

1. Reorder relevant evidence.
2. Translate terminology to the employer's vocabulary without copying entire JD sentences.
3. Strengthen bullets as `action + scope + method + result`.
4. Keep original metrics and qualifiers; use `[待确认]` instead of invented numbers.
5. Maintain a master resume and a per-role diff.

## Story Bank

Store reusable stories with:

- title and date
- context and stakes
- candidate's individual responsibility
- actions and decision rationale
- result with verified evidence
- reflection and what changed afterward
- competencies and questions it can answer
- Japanese and English speaking versions

Use STAR, CAR, or SOAR as organization aids, not rigid scripts. Keep the situation short and spend most time on actions and result.

## Improvements Over The Upstream

- Remove author-specific desktop paths and store outputs in the user's workspace.
- Preserve upstream attribution in the skill package instead of forcing promotional footers into every user report.
- Replace false-precision interview probabilities with evidence/confidence labels.
- Use 13 resume templates consistently; the upstream descriptions alternated between 4, 11, and 13.
- Add Japan-specific document, interview, visa, job-channel, and employment-term workflows.
- Keep personal profile, JD bank, and story bank outside the installed skill directory so skill updates cannot overwrite user data.
