---
layout: ../../layouts/MarkdownLayout.astro
title: "10 AGENTS.md Mistakes That Break Coding Agent Sessions"
description: "Most AGENTS.md files fail because they are too vague, stale, or unverifiable. Here are 10 mistakes that break Claude Code, Codex, Cursor, and other coding agents — and how to fix each one."
target_keyword: "AGENTS.md mistakes"
secondary_keywords:
  - "AGENTS.md best practices"
  - "AGENTS.md not working"
  - "Claude Code AGENTS.md mistakes"
  - "coding agent context mistakes"
  - "AI coding agent instructions"
  - "agent-ready repository checklist"
status: "published"
date: "2026-06-30"
image: /assets/agents-md-hero.jpg
tags:
  - AGENTS.md
  - Best Practices
  - Coding Agents
  - Context Engineering
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is the most common AGENTS.md mistake?","acceptedAnswer":{"@type":"Answer","text":"The most common mistake is leaving out exact validation commands. Agents need to know how to prove the change works before handing back work."}},{"@type":"Question","name":"Should AGENTS.md contain every project detail?","acceptedAnswer":{"@type":"Answer","text":"No. It should contain the operating contract: where to work, what not to touch, commands, conventions, and validation. Link to deeper docs instead of copying them."}},{"@type":"Question","name":"Why does Claude Code ignore parts of my AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Often the file is too long, contradictory, stale, or lacks clear hierarchy. Short, ordered sections work better than long onboarding prose."}},{"@type":"Question","name":"Should I use AGENTS.md or CLAUDE.md?","acceptedAnswer":{"@type":"Answer","text":"Use AGENTS.md for cross-agent repo instructions. Use CLAUDE.md for Claude-specific behavior if needed. Keep shared rules in one place to reduce drift."}},{"@type":"Question","name":"How often should AGENTS.md be updated?","acceptedAnswer":{"@type":"Answer","text":"Update it whenever test commands, build commands, generated files, repo structure, or major conventions change."}},{"@type":"Question","name":"Can AGENTS.md stop agents from editing the wrong files?","acceptedAnswer":{"@type":"Answer","text":"It can help if you explicitly list generated, vendor, build, or migration files that should not be touched without task-specific permission."}},{"@type":"Question","name":"What makes an AGENTS.md file agent-ready?","acceptedAnswer":{"@type":"Answer","text":"It is short, current, scoped, and verifiable: the agent can read it, make the requested change, run the right checks, and know when to stop."}}]}</script>

# 10 AGENTS.md Mistakes That Break Coding Agent Sessions

A weak AGENTS.md does not look broken. It usually looks reasonable: a paragraph about the stack, a few coding conventions, maybe a command or two. Then Claude Code, Codex, Cursor, or another coding agent touches the wrong files, skips the real test command, and hands back a change nobody can trust.

The issue is not that AGENTS.md is useless. The issue is that most AGENTS.md files are written like onboarding docs, not like execution contracts.

Most AGENTS.md files fail because they describe the project but do not give the agent a small, current, verifiable operating contract: where to work, what not to touch, which commands prove success, and when to stop.

If you want to see what good files look like before fixing yours, start with the companion post: [10 real-world AGENTS.md examples](/blog/agents-md-examples/). If you need the full writing framework, read [how to write an AGENTS.md that actually works](/blog/how-to-write-agents-md/) or copy the [AGENTS.md template](/agents-md-template/).

## Mistake summary

| # | Mistake | Symptom | Fix |
|---|---|---|---|
| 1 | No verification command | Agent says "done" without proof | Add exact test, lint, build, and typecheck commands |
| 2 | Too much prose, no hierarchy | Agent misses critical constraints | Use short ordered sections |
| 3 | No file boundaries | Agent edits generated or vendor files | Add explicit do-not-touch paths |
| 4 | Commands are stale | Agent runs old scripts | Keep commands in CI/package scripts and reference them |
| 5 | No task-specific entry points | Agent searches the repo blindly | Link to tests, fixtures, docs, examples, and key modules |
| 6 | Tool-specific assumptions | Works in one agent, fails in another | Separate universal repo rules from tool rules |
| 7 | No stop condition | Agent expands scope into refactors | Define success and stopping rules |
| 8 | Missing dependency/setup notes | Agent fails before editing | Add install and bootstrap prerequisites |
| 9 | No ownership of generated outputs | Agent edits artifacts or forgets to regenerate | Say which outputs are source vs generated |
| 10 | Not maintained after repo changes | AGENTS.md becomes actively misleading | Add AGENTS.md review to release and CI checklists |

## Mistake 1 — No verification command

**What it looks like:**

```md
Please write clean code and make sure everything works.
```

That sentence feels responsible. It is not actionable.

**Why it breaks agents:** coding agents need a concrete proof path. Without one, they often stop at compilation, rely on local reasoning, or say that tests were not run without giving the user a useful next step. The agent may be capable of running checks, but the repo has not told it which checks matter.

**Fix:** put validation near the top of the file.

```md
## Validation
Before handing back work, run:
- npm test
- npm run lint
- npm run build

If one command is too slow or environment-dependent, say so explicitly and run the closest local check.
```

For Python, the same section might be:

```md
## Validation
- uv run pytest
- uv run ruff check .
- uv run mypy src
```

This is the highest-return line in an AGENTS.md because it turns a session from "the agent changed files" into "the agent changed files and produced evidence."

## Mistake 2 — Too much prose, no hierarchy

**What it looks like:**

```md
This repository is a modern web application built with React, TypeScript,
Vite, Tailwind, Vitest, Playwright, and a few internal conventions. We care
a lot about clean code, maintainability, accessibility, performance, and good
user experience. Please follow the existing patterns and be thoughtful.
```

**Why it breaks agents:** long onboarding prose is easy to skim. The problem is not the word count by itself; the problem is that the important constraints are not ranked. A coding agent needs the same thing a human needs under time pressure: headings, commands, paths, and stop rules.

**Fix:** use a predictable hierarchy.

```md
# AGENTS.md

## Project overview
One-paragraph description of the repo.

## Where to work
- src/components/ — reusable UI
- src/routes/ — route-level screens
- tests/ — integration tests

## Commands
- npm run test -- --run
- npm run lint
- npm run typecheck

## Do not touch
- dist/**
- generated/**
- snapshots/** unless the task explicitly asks for snapshot updates

## Before handing back work
Run the relevant command and report the result.
```

A short file with clear sections beats a long file that tries to be a friendly tour.

## Mistake 3 — No file boundaries

**What it looks like:** AGENTS.md explains the stack but never says which files are generated, vendored, or dangerous.

**Why it breaks agents:** agents are very good at finding nearby files and editing them. That is useful when the nearby file is source code. It is harmful when the nearby file is generated output, a vendor copy, a migration, a lockfile, or a snapshot.

**Fix:** add an explicit "do not edit by hand" section.

```md
## Do not edit by hand
- dist/**
- generated/**
- vendor/**
- public/build/**
- package-lock.json unless dependencies changed
- database migrations unless the task explicitly asks for schema changes
```

You can also add source-of-truth hints:

```md
## Source of truth
- Edit `src/schema.ts`, then run `npm run generate`.
- Do not edit files under `src/generated/` directly.
```

This mistake is common in repos that already have a lot of automation. The automation is invisible unless AGENTS.md points to it.

## Mistake 4 — Commands are stale

**What it looks like:** AGENTS.md says `npm test`, but the repo now uses `pnpm test`; or it says `pytest`, but the repo moved to `uv run pytest`.

**Why it breaks agents:** stale commands create false failure. The agent spends half the session debugging the setup instead of solving the task, then reports that the project is broken.

**Fix:** avoid duplicating command logic in too many places. Put the real commands in package scripts, Makefile targets, justfiles, taskfiles, or CI workflows, then reference those stable names from AGENTS.md.

```md
## Commands
Use these repo-level commands. They mirror CI.
- `make test`
- `make lint`
- `make typecheck`
- `make build`
```

Then make `make test` the thing you update when the test runner changes.

A good AGENTS.md is only useful if it is current. Add it to the same review path as CI, release notes, and docs updates.

## Mistake 5 — No task-specific entry points

**What it looks like:** the file says "read the source code" or "follow existing patterns" but does not name the files an agent should inspect first.

**Why it breaks agents:** without entry points, the agent searches the repo blindly. It may pick the wrong test directory, miss the fixture that explains a behavior, or infer conventions from stale code.

**Fix:** give the agent a map.

```md
## Entry points
- CLI commands live in `src/commands/`; one file per subcommand.
- Parser behavior is covered by `tests/parser/*.test.ts`.
- Golden fixtures live in `tests/fixtures/`; read them before changing parser output.
- Public docs examples live in `docs/examples/`; update them for user-facing behavior changes.
```

This is where AGENTS.md shines: it can tell an agent what a directory means, not just that the directory exists.

## Mistake 6 — Tool-specific assumptions

**What it looks like:** the AGENTS.md assumes a single tool's behavior: Claude Code hooks, Cursor rules, GitHub Copilot file discovery, or a Codex CLI convention.

**Why it breaks agents:** AGENTS.md is becoming a cross-agent convention. Claude Code, Codex, Cursor, Copilot, Gemini, and Aider-style tools do not all read context the same way. If the shared file contains tool-specific behavior, it becomes fragile.

**Fix:** keep universal repo rules in AGENTS.md. Put tool-specific behavior in the tool-specific file.

```md
## Shared repo rules
- Validation commands
- File boundaries
- Coding conventions
- Generated-file rules
- Stop conditions

## Tool-specific context
- Claude Code: see `CLAUDE.md` for slash commands and session notes.
- Cursor: see `.cursorrules` for editor-specific preferences.
- Copilot: see `.github/copilot-instructions.md` for GitHub-specific instructions.
```

For the differences between these formats, use the comparison guide: [AGENTS.md vs CLAUDE.md vs .cursorrules vs copilot-instructions.md](/blog/coding-agent-context-file-formats/).

## Mistake 7 — No stop condition

**What it looks like:** AGENTS.md tells the agent what good code looks like but never tells it when to stop.

**Why it breaks agents:** agents often over-help. A request for a bug fix turns into a refactor. A typo fix turns into a style pass. A small feature touches public APIs that were not part of the task.

**Fix:** define scope discipline.

```md
## Scope discipline
Prefer the smallest change that solves the requested task.
Do not refactor unrelated modules, rename public APIs, or reformat large files unless explicitly asked.
If a broader cleanup looks useful, mention it as a follow-up instead of doing it.
```

This one section prevents a surprising amount of review noise.

## Mistake 8 — Missing dependency and setup notes

**What it looks like:** the agent runs the right command, but the repo was never bootstrapped. Dependencies are missing, a local database is required, or the test suite needs generated assets.

**Why it breaks agents:** a failed setup step looks like a project failure. Without setup notes, the agent either guesses or stops.

**Fix:** list the minimum bootstrap path.

```md
## Setup
- Node 22+ is required.
- Run `corepack enable` once.
- Run `pnpm install` before tests.
- For integration tests, copy `.env.example` to `.env.local` and use dummy local values.
```

Do not put secrets in AGENTS.md. Do put the non-secret shape of the environment in the file.

## Mistake 9 — No ownership of generated outputs

**What it looks like:** AGENTS.md does not say whether generated files should be committed, regenerated, or ignored.

**Why it breaks agents:** generated outputs create two opposite failure modes. The agent may edit the generated file directly, which gets overwritten later. Or it may edit the source file and forget to regenerate the output that the repo expects to be committed.

**Fix:** be explicit.

```md
## Generated outputs
- `src/generated/**` is generated from `schema/*.yaml`; never edit it directly.
- After changing `schema/*.yaml`, run `npm run generate`.
- Commit generated files when the command changes them.
```

This is especially important for API clients, protobufs, OpenAPI SDKs, docs, snapshots, lockfiles, and static-site output.

## Mistake 10 — Not maintained after repo changes

**What it looks like:** AGENTS.md was useful on the day it was written, then the repo changed. New test runner. New package manager. New generated files. New directory structure. Old instructions stayed.

**Why it breaks agents:** stale context is worse than missing context. Missing context forces the agent to inspect the repo. Stale context confidently points it in the wrong direction.

**Fix:** make AGENTS.md maintenance part of the repo's operating rhythm.

```md
## Maintenance rule
Update AGENTS.md when any of these change:
- validation commands
- package manager
- generated-file locations
- public API conventions
- test fixture layout
- release process
```

Add this to your PR template or release checklist:

```md
- [ ] If commands, repo structure, generated files, or conventions changed, update AGENTS.md.
```

AGENTS.md is not a document you write once. It is a small interface between your repository and every coding agent that works inside it.

## A bad AGENTS.md vs a useful one

Here is the kind of file that looks fine but fails in practice:

```md
# AGENTS.md

This is a TypeScript project. Please write clean code, follow best practices,
keep things maintainable, and make sure tests pass. Use the existing style.
```

It is polite, but it gives the agent almost nothing to execute.

Here is a compact version that is much more useful:

```md
# AGENTS.md

## Project map
- `src/commands/` — CLI entry points, one file per command
- `src/core/` — pure logic; prefer adding tests here
- `tests/fixtures/` — golden inputs and outputs; do not edit by hand

## Commands
- `pnpm test -- --run`
- `pnpm lint`
- `pnpm typecheck`

## Do not touch
- `dist/**`
- `src/generated/**`; update `schema/*.yaml` and run `pnpm generate`

## Scope discipline
Make the smallest change that solves the task. Do not refactor unrelated modules.

## Before handing back work
Run the relevant commands and report the result. If a command cannot run locally, explain why.
```

The useful version is not much longer. It is simply more operational.

## How repository-harness helps

[repository-harness](https://github.com/hoangnb24/repository-harness) treats agent-readiness as a repo surface, not a prompt-writing trick. It packages a copyable AGENTS.md template, validation expectations, and cross-agent context files for Claude Code, Codex, Cursor, and similar coding agents.

Use it if you want a starting point instead of inventing this from scratch. The broader category guide is [what is an agent-ready repository?](/agent-ready-repository/), and the copyable starting point is the [AGENTS.md template](/agents-md-template/).

## FAQ

### What is the most common AGENTS.md mistake?

Leaving out exact validation commands. Agents need to know how to prove a change works before handing back work.

### Should AGENTS.md contain every project detail?

No. It should contain the operating contract: where to work, what not to touch, commands, conventions, and validation. Link to deeper docs instead of copying them.

### Why does Claude Code ignore parts of my AGENTS.md?

Often the file is too long, contradictory, stale, or lacks clear hierarchy. Short, ordered sections work better than long onboarding prose.

### Should I use AGENTS.md or CLAUDE.md?

Use AGENTS.md for cross-agent repo instructions. Use CLAUDE.md for Claude-specific behavior if needed. Keep shared rules in one place to reduce drift. See the [context-file formats comparison](/blog/coding-agent-context-file-formats/) for details.

### How often should AGENTS.md be updated?

Update it whenever test commands, build commands, generated files, repo structure, or major conventions change.

### Can AGENTS.md stop agents from editing the wrong files?

It can help if you explicitly list generated, vendor, build, or migration files that should not be touched without task-specific permission.

### What makes an AGENTS.md file agent-ready?

It is short, current, scoped, and verifiable: the agent can read it, make the requested change, run the right checks, and know when to stop.
