---
layout: ../../layouts/MarkdownLayout.astro
title: "How to Prepare Your Repository for Claude Code"
description: "Claude Code needs more than a README to work reliably. Here is how to prepare your repository so Claude Code understands your codebase, respects your conventions, and produces reviewable output."
target_keyword: "prepare repository for Claude Code"
secondary_keywords:
  - Claude Code repository setup
  - Claude Code setup
  - how to use Claude Code
  - Claude Code AGENTS.md
  - claude code repository context
  - coding agent repository setup
status: "published"
date: "2026-05-30"
image: /assets/claude-code-hero.jpg
tags:
  - How-to
  - English
---

# How to Prepare Your Repository for Claude Code

Claude Code is Anthropic's official CLI for coding with Claude. It reads the repository, plans changes, runs commands, and hands back work — in a loop that keeps going until the task is done.

The default experience with Claude Code is: it boots up, sees your code, and starts working. That works for small projects with obvious structure. For anything real, it needs more than that.

This post shows how to prepare a repository so Claude Code produces reliable, reviewable output instead of guesswork.

---

## What Claude Code reads at startup

When Claude Code starts, it reads in this approximate order:

1. `README.md` — project overview
2. `AGENTS.md` at the root — if it exists, this is the primary operating context
3. `.claude/` directory — contains `commands.md` and project-level settings
4. Directory structure — to understand file layout

If you have an `AGENTS.md`, Claude Code reads it first. If you do not, it falls back to `README.md` and whatever it can infer from the file structure.

The difference between an unprepared repo and a Claude-Code-ready repo is entirely in that first read.

---

## The minimum viable setup

You do not need a full harness to get value from Claude Code. Start with this:

### 1. Add AGENTS.md

`AGENTS.md` is the file Claude Code reads before doing anything else. It should answer:

- **What this project does** — one sentence
- **Where to start reading** — main entry points, key files
- **What not to touch** — safety boundaries, irreversible changes
- **How to validate** — exact commands for each change type

Example:

```md
# Project

API service for a mobile game backend. Built with Node.js + Fastify.

# Important files

- `src/index.ts` — server entry point
- `src/routes/` — all HTTP route handlers
- `src/db/` — database models and migrations

# Do not touch

- `src/auth/` — auth layer is shared with another team, ask before modifying
- `node_modules/` — never modify directly

# Validation

All changes must pass before handing back:
- `npm test`
- `npm run lint`
- `npm run build`
```

### 2. Add a `.claude/commands.md` for custom commands

The `.claude/` directory can hold a `commands.md` file that defines reusable slash commands for your project:

```md
# Test and validate everything
Runs the full validation suite.

---
npm test && npm run lint && npm run build
```

Claude Code can then run `/test-all` as a single command. This is especially useful for repos with multiple test suites or complex validation flows.

### 3. Add architecture context if the project is non-trivial

For projects with non-obvious architecture, add a short architecture note. Where is the data? What controls access? What is the deployment model?

For example:

```md
# Architecture

- Express API on port 3000
- PostgreSQL via Prisma ORM
- Auth via JWT — tokens last 24h, refresh via `/auth/refresh`
- Background jobs via BullMQ — Redis on port 6379
- Frontend is a separate repo — do not serve static files here
```

Claude Code does not need to be told this explicitly. But when it knows it, it will not write code that accidentally bypasses the auth layer or creates a hard-to-debug circular dependency.

---

## Beyond the minimum: the full harness

If you are working on a team or a project that needs stricter coordination, the full harness adds:

### Story packets

A story packet is a structured task description that replaces a free-form prompt. It specifies:

- What to build (one sentence)
- Where to work (specific files)
- What "done" looks like (acceptance criteria)
- Exact validation commands

When you give Claude Code a story packet instead of a paragraph in a chat, the output is more bounded and more reviewable.

### Decision records

Decision records document why the codebase is the way it is. They prevent Claude Code from reopening settled questions.

Format:

```md
# Decision: Chose JWT over session cookies for auth

**Date:** 2024-11-03
**Status:** accepted

**Decision:** JWT tokens with 24h expiry stored in httpOnly cookies.

**Why:** Session cookies require a session store. JWT is stateless and works
across multiple app instances without a centralized session backend.

**What would reopen this:** A demonstrated security vulnerability in the JWT
implementation that cannot be patched without breaking the session model.
```

### Validation matrix

A table mapping change types to exact commands:

| Change type | Required checks |
|---|---|
| Frontend component | `npm test -- --testPathPattern=components && npm run build` |
| API route | `npm test && npm run typecheck && npm run build` |
| Database migration | `npm run migration:validate` then ask a human |
| Config change | `npm test && npm run build` |

Claude Code uses this before handing back any change. Humans use it to review faster.

---

## Common mistakes

### Adding too much to AGENTS.md

Claude Code reads all of `AGENTS.md`. If it is more than one screen of text, it starts losing coherence. Keep it focused. Link to deeper docs rather than including them inline.

### Not specifying what not to touch

The most common Claude Code failure: it modifies a shared utility, an auth layer, or a configuration file that other things depend on. Be explicit about boundaries.

### Skipping validation commands

"Run tests" is not a validation command. "Run the integration suite against the staging database" is. Be specific. Claude Code will run whatever you tell it to run — make sure what you tell it to run actually proves correctness.

### Forgetting to update context when things change

If a new architectural pattern lands, update `AGENTS.md`. If a new decision gets made, add a decision record. Claude Code's context is only as good as what you maintain in the repo.

---

## Quick checklist

Before your next Claude Code session:

- [ ] `AGENTS.md` exists at the root
- [ ] `AGENTS.md` says what the project does in one sentence
- [ ] `AGENTS.md` lists the key files and directories
- [ ] `AGENTS.md` specifies what not to touch
- [ ] `AGENTS.md` has exact validation commands for each change type
- [ ] `.claude/commands.md` exists (optional but useful)
- [ ] Architecture context is documented if the project is non-trivial
- [ ] Decision records exist for non-obvious choices

That is the minimum viable setup. Run a session and watch where Claude Code needs to guess — those gaps are where you add context.

---

## See also

- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/) — the full template and writing guide
- [What Is an Agent-Ready Repository?](/agent-ready-repository/) — the broader checklist
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/) — the framework behind this