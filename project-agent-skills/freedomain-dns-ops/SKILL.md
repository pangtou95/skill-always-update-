---
name: freedomain-dns-ops
description: Use when helping with DigitalPlat FreeDomain style free-domain registration, DNS hosting setup, nameserver changes, WHOIS lookup/service design, free-domain abuse handling, or domain dashboard/template maintenance based on DigitalPlatDev/FreeDomain.
---

# FreeDomain DNS Operations

Source analyzed: https://github.com/DigitalPlatDev/FreeDomain

Use this skill for practical free-domain onboarding, DNS setup, domain dashboard workflows, WHOIS server stubs, and abuse-policy aware support.

## Repository Shape

- Public-facing docs live in `documents/`, including beginner tutorials and FAQ.
- Dashboard HTML/Jinja-style templates live in `opensource/frontend/`.
- WHOIS sample server lives in `opensource/whois_server/whois.py`; its `get_whois()` storage lookup is intentionally left for implementers.
- Static assets and an email template live under `opensource/static/` and `opensource/email_template/`.

## Core Model

DigitalPlat FreeDomain provides free subdomains under extensions such as `.dpdns.org`, `.us.kg`, `.qzz.io`, `.xx.kg`, and `.qd.je`. The important user journey is:

1. Register an account on the dashboard.
2. Claim an allowed domain name.
3. Configure DNS hosting, commonly with Cloudflare.
4. Replace assigned nameservers in the DigitalPlat dashboard.
5. Add DNS records at the DNS provider.
6. Wait for propagation before debugging application-level failures.

Default policy in the analyzed FAQ: one free domain per user account unless an exception or expansion program applies.

## DNS Support Workflow

When asked to help a user set up a DigitalPlat-style free domain:

1. Identify the exact domain and extension.
2. Confirm whether the task is nameserver delegation, DNS record creation, WHOIS lookup, renewal, or privacy.
3. For Cloudflare setup:
   - Add the domain to Cloudflare.
   - Choose the free plan when appropriate.
   - Copy Cloudflare nameservers.
   - Paste those nameservers into the FreeDomain dashboard domain manager.
   - Add `A`, `AAAA`, `CNAME`, `MX`, or `TXT` records in Cloudflare as needed.
4. Remind that newly created or changed records may need propagation time.
5. If debugging, check delegation first, then authoritative records, then CDN/proxy and app configuration.

Prefer DNS commands such as:

```bash
dig NS example.dpdns.org
dig A example.dpdns.org
dig TXT example.dpdns.org
whois -h whois.digitalplat.org "example.dpdns.org"
```

## Dashboard Template Work

The frontend templates are server-rendered HTML with placeholders such as `{{domain_name}}`, `{{domains}}`, and loops like `{% for domain in domains_list %}`. Preserve template syntax when editing.

Important template areas:

- `register.html`: account creation and Turnstile/reCAPTCHA style challenge.
- `login.html`: account sign-in.
- `domainreg.html`: domain registration, policy acknowledgements, extension picker.
- `domainmgr.html`: list and search owned domains.
- `domain_view.html`: nameserver updates, renewal, WHOIS privacy controls.
- `whois.html`: browser WHOIS lookup form.
- `panel.html`: dashboard shell and navigation.

When changing templates:

1. Keep policy links visible near registration and domain registration flows.
2. Treat anti-abuse copy as part of the product contract, not decorative text.
3. Do not remove CAPTCHA/challenge hooks without replacing the abuse-control mechanism.
4. Keep domain-management actions explicit and auditable.

## WHOIS Server Work

The sample WHOIS server is a port-43 TCP server pattern. Its missing piece is the persistence lookup.

When implementing `get_whois(query)`:

1. Normalize domain input: lowercase, trim whitespace, reject control characters.
2. Validate it is under an allowed suffix.
3. Query a trusted domain registry database, not user-supplied HTML.
4. Return plain-text WHOIS content with privacy redaction rules applied.
5. Rate-limit by IP and add logging for abuse reports.

Never expose private registrant data when WHOIS privacy is enabled.

## Abuse And Safety

Free-domain services are abuse-prone. For support and feature design, keep these controls in scope:

- Per-account domain limits and manual exceptions.
- CAPTCHA or Turnstile on registration and password reset.
- WHOIS privacy status that is explicit to the user.
- Abuse-report intake with domain, evidence, timestamps, and reporter contact.
- Suspension/delete flows that preserve audit logs.

Do not advise bypassing domain limits, verification, DNS ownership checks, or abuse controls.

## Useful Checks

For a claimed domain that does not resolve:

```bash
dig NS example.dpdns.org +short
dig SOA example.dpdns.org
dig +trace example.dpdns.org
dig @1.1.1.1 example.dpdns.org
```

For Cloudflare:

- If using orange-cloud proxy, origin IP checks may differ from public DNS.
- For email, verify `MX`, `SPF`, `DKIM`, and `DMARC`.
- For GitHub Pages, Vercel, Netlify, or similar hosts, check provider-specific `CNAME` or verification `TXT` records.

