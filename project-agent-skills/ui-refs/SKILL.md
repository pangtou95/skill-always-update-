---
name: ui-refs
description: Find real UI references by industry, page type and visual style before designing or restyling a website, product interface, EDM or key visual. Use when a design brief needs concrete visual references rather than a generic aesthetic.
---

# UI Reference Research

Use [Creght UI Refs](https://github.com/creght-dev/ui-refs) as a reference source, not a template to copy. This is an original Codex adapter; source and rights boundaries are in `SOURCE.md`.

1. Identify the actual product, audience, screen type and existing design constraints. Keep operational interfaces work-focused; references do not turn an app request into a landing page.
2. Retrieve `data/vocab.json` and `data/refs.json` from the repository's current branch, or use a verified local checkout. Parse JSON rather than matching text. Map the brief to actual vocabulary strings (many tags are Chinese); do not invent tags.
3. Filter by industry and page type, then narrow by site type/style. If there are few matches, relax one filter and report that distinction. Inspect a small shortlist, not the entire image collection.
4. Select two or three contrasting directions. Inspect the relevant `image` or `parts[].image`, especially the section being designed. Use an available browser/image viewer and respect its media restrictions. Do not claim visual inspection when only summaries were read.
5. Record each reference's `id`, `source`, `pageUrl`, inspected section and useful pattern. Translate layout, hierarchy, rhythm and states into the user's design system; keep original text, logos and photography out of the implementation unless separately licensed.
6. Build the requested interface. Check responsive text fit, actual content, keyboard/focus states and reduced motion. A reference shortlist alone is not implementation completion.

`sections` is the page skeleton; `parts` contains sectional images. Single KVs may have neither. Do not assume the first screenshot is a full page.

Data tags/summaries are CC BY 4.0 and require attribution when reused. Screenshots retain their owners' copyright. This package contains no gallery images or copied dataset. Credentials and private user designs must not be submitted to a reference service.

Invocation: `$ui-refs 为这个产品界面寻找三个不同的真实参考，说明各自适合借鉴的布局，然后按现有设计系统实现。`
