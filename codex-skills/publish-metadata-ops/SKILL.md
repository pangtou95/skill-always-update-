---
name: publish-metadata-ops
description: Prepare publish-ready metadata and operations checklists for videos, podcasts, blog posts, newsletters, and social content. Use when the user asks for titles, descriptions, tags, hashtags, captions, subtitles, chapters, upload settings, publish checklists, distribution metadata, or YouTube/Bilibili/Douyin/Xiaohongshu publishing prep.
---

# publish-metadata-ops

Prepare the metadata and final publishing checklist that turns finished content into a clean upload package.

## Source Status

The screenshot source for this item appears to reference `AgricDaniel/claude-youtube`, but that repository was not publicly accessible during installation. This local skill is derived from the screenshot's described use case: title, description, tags, subtitles, chapters, and publishing checklist operations.

## When To Use

- User has a finished video, article, podcast, newsletter, or social post and wants publishing metadata.
- User asks for SEO titles, YouTube descriptions, Bilibili/Douyin/Xiaohongshu metadata, tags, hashtags, chapters, subtitles, or release checklist.
- User wants a final pre-publish QA pass.

## Workflow

1. Identify platform and content type.
2. Extract the core topic, audience, promise, keywords, entities, and CTA.
3. Generate metadata variants:
   - Primary title and 5-10 alternatives
   - Short description and long description
   - Tags, hashtags, keywords, entities
   - Thumbnail/cover text suggestions
   - Chapters or timestamps when relevant
   - Subtitle/caption notes when relevant
4. Run publish checks:
   - Link/CTA present
   - Disclosure or sponsorship note present when needed
   - Claims supported by citations or softened
   - Platform length limits respected
   - Accessibility basics covered: captions, alt text, readable title
5. Return a copy-paste upload pack.

## Output Template

```markdown
# Publish Metadata Pack

## Platform

## Primary Title

## Title Alternatives

## Description

## Tags / Keywords

## Hashtags

## Chapters / Timestamps

## Thumbnail / Cover Suggestions

## Captions / Subtitle Notes

## Pre-Publish Checklist

## Risks Or Missing Inputs
```
