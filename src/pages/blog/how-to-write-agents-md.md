---
layout: ../../layouts/MarkdownLayout.astro
title: "How to Write an AGENTS.md That Actually Works"
description: "A practical guide to writing AGENTS.md that coding agents will read, follow, and not ignore. Move beyond generic instructions to durable operating context."
target_keyword: "how to write AGENTS.md"
secondary_keywords:
  - AGENTS.md template
  - AI coding agent instructions
  - agent-ready repository setup
  - repo context for coding agents
status: "published"
date: "2026-05-28"
image: /assets/agents-md-hero.jpg
tags:
  - How-to
  - English
---

# How to Write an AGENTS.md That Actually Works

Most AGENTS.md files nobody reads.

They are too long, too vague, or templated from a blog post that looked good but did not age well. The agent scans them once, files the content in context the moment, and goes back to inferring everything from the code.

That is not a tooling problem. It is a writing problem.

Here is how to write an AGENTS.md that coding agents actually use.

---

## The test

Before you finish writing, ask one question:

> *If I deleted every line from this file and replaced it with "just read the code and do a good job," would the agent be meaningfully worse off?*

If yes, keep the line. If no, cut it.

---

## What belongs in AGENTS.md

Three things only:

**1. How to validate the work**
Not "run tests." Give the exact command. Specify which check covers which change type. Agents use this to decide what to run before handing anything back.

**2. Which files matter and why**
Not a full architecture doc. A short map — which directories contain what, which boundaries should not be crossed, which files are risky. Agents use this to orient themselves before they start editing.

**3. What should not happen without a human**
Agents need to know where the guardrails are. One line listing risky areas is enough. Agents use this to avoid the kind of changes that require emergency rollbacks.

Everything else — product context, coding conventions, PR templates — belongs in linked documents. The top of AGENTS.md should fit on one screen.

---

## What does not belong

**The README.** Do not copy-paste your README into AGENTS.md. The README is for humans who chose to visit your repo. AGENTS.md is for agents dropped into the middle of a task with no preamble.

**Task-specific context.** The current sprint, the ticket you are working on, the reason you chose a particular library — that is temporary. It belongs in a story packet or a task prompt, not in durable context.

**Obvious instructions.** "Be careful with production data" is obvious to humans. "Do not run `DROP TABLE` without explicit human approval" is the kind of thing agents actually need.

---

## The format

```md
# AGENTS.md — [Project Name]

## Project overview
[2–4 sentences. What it does. Who it serves.]

## Validate before handing back
- Docs only: [exact command]
- Frontend changes: [exact command + what to check]
- API changes: [exact command + integration step]
- Refactors: [exact command]

## Files and boundaries
- `src/api/` — [one line description]
- `src/domain/` — [one line description]
- `tests/fixtures/` — [do not modify unless explicitly requested]

## Do not do without asking first
- Update migration files
- Change authentication logic
- Touch billing or payment code
- Remove or skip existing tests to make a check pass

## Tool notes
- [Any tool-specific quirks, e.g. "disable auto-fix in lint mode for migrations"]
```

---

## How to know it is working

After a few agent sessions, ask:

1. Did the agent run the right validation command before handing back work?
2. Did the agent ask before changing a risky area?
3. Did the agent report an error in the right place?

If answers are yes, the AGENTS.md is doing its job. If agents are making guessy changes or skipping checks, the file needs another revision.

The harness improves with feedback, just like the code.

---

## Example: What most people write vs. what works

### ❌ Too vague

```md
## Commands

Run tests before committing.

## Architecture

The codebase uses a standard structure.

## Conventions

Follow the existing code style.
```

### ✅ Specific enough to use

```md
## Validate before handing back

Run these exact commands before every PR:

| Change type | Command |
|---|---|
| Docs or config | `npm run lint && npm run typecheck` |
| Frontend component | `npm test -- --testPathPattern=components && npm run build` |
| Backend logic | `npm test && npm run typecheck && npm run build` |
| Database migration | `npm run migration:validate` then ask a human |

## Where not to touch without asking first

- `src/auth/` — authentication logic
- `db/migrations/` — migrations, ever
- `src/billing/` — payment and subscription code
```

The second version is shorter. It is also the one an agent will actually use.

---

## Start today

You do not need a perfect AGENTS.md. You need one that is better than nothing.

Pick your most-used project. Write the three sections above. Put it at the root.

Then run one task with a coding agent and watch whether it improves the output.

Iterate from there.

---

*See also: [What Is an Agent-Ready Repository?](/agent-ready-repository/) — the broader context for why AGENTS.md alone is not enough, but is the right starting point.*
