# Harness Engineering Blog Growth Operating Policy

This document defines how the blog can be grown autonomously.

## Goal

Grow the `harness-engineering-blog` site into the canonical content hub for:

- agent-ready repositories
- harness engineering for coding agents
- repo-level context engineering
- AGENTS.md templates and practices
- practical repository preparation for Claude Code, Codex, Cursor, and other coding agents

The blog should support the larger goal of growing [`hoangnb24/harness-experimental`](https://github.com/hoangnb24/harness-experimental) to 5,000 GitHub stars.

## Autonomy level

The site can be improved autonomously without waiting for prior approval.

Allowed autonomous actions:

- draft new blog pages and posts
- edit existing blog content for clarity, SEO, internal linking, and conversion
- add supporting Astro pages/components
- add metadata, canonical URLs, OpenGraph tags, schema, RSS, sitemap, robots, and related technical SEO improvements
- run local validation commands
- commit and push changes to `hoangnb24/harness-engineering-blog`
- deploy to Cloudflare Pages using Wrangler when credentials are available
- report back with what changed and deployed URLs
- prepare X/Twitter distribution drafts and posts when within the existing harness/growth scope

## Approval gates

Ask before doing any of the following:

- paid tools or paid subscriptions
- account-sensitive setup such as Google Search Console, Bing Webmaster Tools, analytics accounts, Cloudflare account settings, or OAuth flows that require user account action
- custom domain purchases or DNS changes
- posting outside already-approved channels
- DMs, outreach, or community posting that could be perceived as promotional
- changes to `hoangnb24/harness-experimental` itself unless explicitly approved

If a scheduled autonomous run hits an approval-gated action, it should skip the action and report what is needed.

## Publishing principles

The blog should prioritize durable, high-signal content rather than generic AI content.

Every published page should satisfy these checks:

1. Clear search intent
2. Strong category fit
3. Original point of view
4. Practical examples or checklists
5. Internal links to related pages
6. Clear CTA toward `harness-experimental` when relevant
7. Clean metadata and readable URL
8. No internal draft notes, distribution snippets, or private planning content in public pages

## Initial content cluster

Recommended cluster order:

1. `/agent-ready-repository/` — published
2. `/context-engineering-for-coding-agents/`
3. `/harness-engineering-for-coding-agents/`
4. `/agents-md-template/`
5. `/blog/coding-agents-need-better-repositories/`
6. `/blog/agents-md-vs-cursor-rules/`
7. `/blog/how-to-write-agents-md/`
8. `/blog/prepare-repo-for-claude-code/`
9. `/blog/prepare-repo-for-codex/`
10. `/blog/repo-harness-vs-app-template/`

## Technical SEO backlog

Prioritize:

- sitemap generation
- RSS feed
- canonical URL verification
- JSON-LD for Article, FAQPage, BreadcrumbList where appropriate
- reusable SEO component
- OpenGraph image template
- internal related-links component
- project CTA component
- table of contents for long guides
- clean 404 page

## Reporting format

When changes are published, report:

- pages changed or added
- commit SHA
- deployment URL
- verification result
- next recommendation

## Current production URL

```text
https://harness-engineering-blog.pages.dev
```
