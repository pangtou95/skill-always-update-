# Japan Offer Review

Review the actual 内定通知書, 労働条件通知書 and contract. A job ad or verbal explanation is not enough for final comparison.

## Required Review Areas

### Employment And Scope

- employing legal entity
- employment type and fixed/indefinite term
- probation period and conditions
- initial job duties and scope of future changes
- initial work location and scope of future changes
- transfer, relocation and travel expectations
- start date

### Compensation

- base salary and payment frequency
- allowances and reimbursement
- fixed overtime: included amount, covered hours and additional payment beyond the allowance
- bonus: guaranteed or discretionary, formula and timing
- salary review timing
- equity or stock terms, if any
- estimated gross annual compensation without counting uncertain items as guaranteed

### Time And Leave

- daily/weekly hours and breaks
- flex core time or discretionary-labor deemed hours
- overtime expectation and historical team evidence
- holidays and annual holiday count
- paid leave grant timing and special leave
- remote/hybrid conditions

### Benefits And Restrictions

- health insurance, pension, employment insurance and workers' compensation
- commuting, housing, relocation and equipment support
- retirement allowance or defined contribution plan
- side-job policy
- intellectual property, confidentiality, non-solicit and non-compete clauses
- resignation notice and termination provisions

### International Candidate

- status-of-residence support and responsible party
- required documents and expected timeline
- whether role duties align with the intended status
- relocation and initial housing support
- language support for employment terms

## Red Flags Or Questions, Not Automatic Legal Conclusions

- fixed overtime without hours, amount or excess-payment wording
- material terms differ between ad, interview and written notice
- broad role/location change clauses that conflict with candidate constraints
- unclear fixed-term renewal criteria or renewal limit
- bonus/equity presented as guaranteed when discretionary
- visa support described vaguely after the candidate disclosed the need
- pressure to sign before receiving written terms
- request to begin work before proper authorization

Escalate legal or immigration uncertainty to an appropriate professional or official authority.

## Comparison Output

Compare offers using both numbers and preferences:

- guaranteed annual cash
- realistic variable compensation scenario
- hours and commute cost
- role scope and growth
- stability and contract risk
- language and immigration fit
- manager/team evidence
- downside and open questions

Keep a separate list of assumptions. Do not collapse every factor into one opaque score.

## Audit Script

Populate `assets/offer-terms.json.template`, then run:

```bash
python3 scripts/japan_offer_audit.py offer-terms.json
```

The output reports missing written terms and conditional follow-ups. It does not decide whether a clause is lawful.
