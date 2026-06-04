---
layout: ../../layouts/MarkdownLayout.astro
title: "How to Prepare Your Repository for Codex"
description: "OpenAI Codex needs structured repository context to produce reliable code changes. Here is how to prepare your repository so Codex understands your codebase, follows conventions, and hands back reviewable output."
target_keyword: "prepare repository for Codex"
secondary_keywords:
  - Codex repository setup
  - Codex setup
  - OpenAI Codex repository context
  - Codex AGENTS.md
  - coding agent repository setup
status: "published"
date: "2026-05-31"
image: /assets/comparison-hero.jpg
tags:
  - How-to
  - English
---

# How to Prepare Your Repository for Codex

OpenAI Codex is the model family powering GitHub Copilot and the Copilot API. It reads code, understands context, and generates changes — but like all coding agents, it works best when the repository tells it what it needs to know.

This post shows how to prepare a repository so Codex produces reliable, reviewable output instead of plausible but wrong code.

---

## What Codex reads at startup

When Codex enters a repository — via Copilot, the API, or a CLI tool built on top of it — it reads the files in scope for the current task. It does not have a fixed startup sequence the way Claude Code does with `AGENTS.md`, but it does benefit from the same structural context:

- **Explicit project instructions** in files like `AGENTS.md` give Codex durable operating context that survives across sessions.
- **Architecture notes** help Codex understand which files matter and which boundaries should not be crossed.
- **Validation commands** let Codex know exactly which checks prove a change is correct before handing it back.

Without these, Codex works primarily from what it can infer from the surrounding code and the current task prompt — which means it often guesses wrong on non-trivial changes.

---

## The minimum viable setup

You do not need a full harness to get better results from Codex. Start with this:

### 1. Add AGENTS.md

`AGENTS.md` at the root is the single highest-impact change you can make for any coding agent, including Codex. It should answer:

- **What this project does** — one or two sentences
- **Where to start reading** — key entry points and important files
- **What not to touch** — safety boundaries, irreversible changes
- **How to validate** — exact commands for each change type

Example:

```md
# Project: Order management API

Node.js + Fastify REST API. Handles order creation, fulfillment, and
status tracking. PostgreSQL via Prisma ORM.

# Key files

- `src/index.ts` — server entry point
- `src/routes/` — all HTTP handlers
- `src/services/` — business logic
- `prisma/schema.prisma` — database schema

# Do not touch

- `src/auth/` — shared with another team, get approval first
- `prisma/migrations/` — never modify directly

# Validation

All changes must pass before handing back:
- `npm test`
- `npm run lint`
- `npm run build`
```

### 2. Document the validation matrix

 Codex can run commands, but it needs to know which commands apply to which change type. A simple table in `AGENTS.md` makes this explicit:

| Change type | Required checks |
|---|---|
| Frontend component | `npm test -- --testPathPattern=components && npm run build` |
| API route | `npm test && npm run typecheck && npm run build` |
| Database migration | `npx prisma migrate validate` then ask a human |
| Config or docs | `npm run lint` |

### 3. Add architecture notes for non-trivial projects

If the project has non-obvious structure, a short architecture note helps Codex avoid destructive changes:

```md
# Architecture

- Express API on port 3000
- PostgreSQL via Prisma ORM
- Auth via JWT — tokens expire after 24h
- Background jobs via BullMQ — Redis on port 6379
- Frontend is a separate repo — do not serve static files here
```

---

## Beyond the minimum: full harness

For teams working on shared or high-stakes codebases, the full harness adds:

### Decision records

Decision records document why the codebase is the way it is. They prevent Codex from reopening settled questions or undoing deliberate choices.

```md
# Decision: Chose PostgreSQL over MongoDB for orders

**Date:** 2024-11-03
**Status:** accepted

**Why:** Financial transactions require ACID compliance. MongoDB's eventual
consistency creates edge cases we cannot afford for order state.

**What would reopen this:** A demonstrated inability of the team to work
with PostgreSQL at scale, or a specific technical requirement that
MongoDB solves and PostgreSQL cannot.
```

### Story packets

A story packet replaces a vague task description with a structured unit of work:

```md
## Story packet

**What to build:** [one sentence]
**Where to work:** [specific files]
**Acceptance criteria:** [checklist]
**Validation commands:** [exact commands]
**What not to touch:** [safety boundaries]
```

When Codex receives a story packet instead of a free-form prompt, the output is more bounded and more reviewable.

---

## Common mistakes

### No explicit validation commands

"Run tests" is not a validation command. "Run `npm test` for unit tests and `npm run integration-tests` for API behavior" is. Be specific — Codex will run whatever you tell it to run, so make sure what you tell it actually proves correctness.

### Missing safety boundaries

The most common Codex failure: it modifies a shared utility, an auth layer, or a migration file that other things depend on. Be explicit about what not to touch. One line in `AGENTS.md` prevents emergency rollbacks.

### Including too much in AGENTS.md

If `AGENTS.md` is more than one screen of text, it loses coherence. Keep the top-level instructions concise. Move detailed architecture docs and decision records into linked files so agents can find them but are not forced to read everything upfront.

### No feedback loop

If Codex keeps making the same mistake, the repo context should improve. Update `AGENTS.md`. Add a decision record. The harness grows from real failure cases, not from templates applied in advance.

---

## Quick checklist

Before your next Codex session:

- [ ] `AGENTS.md` exists at the root
- [ ] `AGENTS.md` says what the project does in one sentence
- [ ] `AGENTS.md` lists key files and directories
- [ ] `AGENTS.md` specifies what not to touch
- [ ] `AGENTS.md` has exact validation commands for each change type
- [ ] Architecture context is documented if the project is non-trivial
- [ ] Decision records exist for non-obvious choices

That is the minimum viable setup. Run a session and watch where Codex needs to guess — those gaps are where you add context.

---

## How this differs from preparing for Claude Code

Both Claude Code and Codex benefit from the same repository-level context. The difference is in tool behavior:

| | Claude Code | Codex (GitHub Copilot) |
|---|---|---|
| Reads AGENTS.md | Yes — at every invocation | Yes — as part of project context |
| Runs validation commands | Yes — built-in | Yes — via natural language or explicit prompts |
| Supports story packets | Yes — native format | Yes — via structured task prompts |
| Tool-specific quirks | Reads `.claude/commands.md` | Best via explicit AGENTS.md validation matrix |

The core principle is the same: make the repository legible so agents do not have to guess. The exact file placement and command format may differ slightly by tool, but `AGENTS.md` at the root works for both.

---

## Related pages

- [What Is an Agent-Ready Repository?](/agent-ready-repository/) — foundational concept
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/) — the parent framework
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/) — practical guide
- [AGENTS.md Template](/agents-md-template/) — copy and adapt for your project

## See also

- [How to Prepare Your Repository for Claude Code](/blog/prepare-repo-for-claude-code/) — the parallel guide for Claude Code users
- [AGENTS.md vs Cursor Rules](/blog/agents-md-vs-cursor-rules/) — choosing the right context file approach
- [`repository-harness` on GitHub](https://github.com/hoangnb24/repository-harness) — the open-source implementation