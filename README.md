# Harness Engineering Blog

A Markdown-first Astro site about harness engineering, agent-ready repositories, AGENTS.md, and repo-level context engineering for coding agents.

## Purpose

This blog is a satellite content hub for growing the category around agent-ready repositories and sending qualified developers to [`harness-experimental`](https://github.com/hoangnb24/harness-experimental).

## Local development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## Deploy

Cloudflare Pages deployment is documented here:

```text
docs/deploy-cloudflare-pages.md
```

Recommended Cloudflare Pages settings:

- Framework preset: `Astro`
- Build command: `npm run build`
- Build output directory: `dist`
- Production branch: `main`

## Initial content architecture

- `/` — homepage
- `/agent-ready-repository/` — pillar page
- `/agents-md-template/` — reusable AGENTS.md template page
- `/projects/harness-experimental/` — project conversion page
- `/blog/` — blog index

## Status

Initial scaffold created. Deployment target and production domain are still undecided.
