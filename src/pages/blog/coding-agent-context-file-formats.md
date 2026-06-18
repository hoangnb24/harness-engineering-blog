---
layout: ../../layouts/MarkdownLayout.astro
title: "AGENTS.md vs CLAUDE.md vs .cursorrules vs .github/copilot-instructions.md: The Coding-Agent Context-File Formats Compared"
description: "Every major coding agent has its own context file format. AGENTS.md, CLAUDE.md, .cursorrules, .github/copilot-instructions.md, GEMINI.md, CONVENTIONS.md — they all aim to give agents durable project context but work differently and serve different scopes. Here is how to choose."
target_keyword: "coding agent context file formats"
secondary_keywords:
  - AGENTS.md vs CLAUDE.md
  - .cursorrules vs AGENTS.md
  - copilot-instructions.md
  - agent context file comparison
  - coding agent configuration
  - GEMINI.md
  - cross-agent instructions
status: "published"
date: "2026-06-18"
image: /assets/comparison-hero.jpg
tags:
  - Comparison
  - English
---

# AGENTS.md vs CLAUDE.md vs .cursorrules vs .github/copilot-instructions.md: The Coding-Agent Context-File Formats Compared

If you have set up Claude Code, Cursor, or GitHub Copilot in the last year, you have hit this question: **which context file do I write?** Every major coding agent now ships its own format. `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`, `GEMINI.md`, `CONVENTIONS.md`. They all aim to give the agent durable project context, but they work differently, live in different places, and serve different scopes.

This post compares them side by side and gives a single recommendation that works across the major agents.

## The formats at a glance

| Format | Agent(s) that read it | Where it lives | Committed? | Scope |
|---|---|---|---|---|
| `AGENTS.md` | Claude Code, Codex, Cursor, Aider, Gemini CLI, OpenCode, others | Repository root | Yes | Repo-wide, cross-agent |
| `CLAUDE.md` | Claude Code only | Repository root | Yes | Repo-wide, single-agent |
| `.cursorrules` | Cursor only | Repository root (or `.cursor/rules/`) | Yes | Repo-wide, single-agent |
| `.github/copilot-instructions.md` | GitHub Copilot | Repository `.github/` directory | Yes | Repo-wide, single-platform |
| `GEMINI.md` | Gemini CLI | Repository root | Yes | Repo-wide, single-agent |
| `CONVENTIONS.md` | OpenCode and a few others | Repository root | Yes | Repo-wide, single-agent |
| `.aider.conf.yml` | Aider | Repository root | Yes | Repo-wide, single-agent |
| Personal Cursor Rules (`.cursor/rules/*.mdc`) | Cursor only | Inside the user's local checkout | No (per-user) | Personal IDE preferences |

The fundamental split is between **cross-agent formats** (`AGENTS.md` is the only one shipping widely today) and **single-agent formats** (every other format on the list). Everything else is a question of where it lives and how discoverable it is.

## What each format is for

### `AGENTS.md`

A plain Markdown file at the repository root that any coding agent that follows the convention reads at the start of a session. Conceived by the open-source coding-agent community in 2025 and now adopted by Claude Code, Codex, Cursor (it reads AGENTS.md in addition to `.cursorrules`), Aider, Gemini CLI, OpenCode, and others. The format is intentionally minimal — Markdown, no schema, no required sections — so the same file works across tools without modification.

```markdown
# AGENTS.md

## What this project does
A short description.

## Where to start reading
Key entry points.

## Validation
Commands that prove a change is correct.

## Boundaries
Files and operations an agent must not touch without approval.
```

### `CLAUDE.md`

A Claude-Code-specific equivalent. Claude Code reads both `AGENTS.md` (the cross-agent file) and `CLAUDE.md` (its own file). When both exist, Claude Code reads `CLAUDE.md` first. The intended split is: put repo-wide context every coding agent should see in `AGENTS.md`, and put Claude-Code-specific behavior — shortcuts, custom slash-command conventions, Claude-Code-only workflows — in `CLAUDE.md`.

In practice most teams start with `AGENTS.md` and only add `CLAUDE.md` when they have Claude-Code-specific instructions worth separating.

### `.cursorrules`

Cursor's first-generation format. A single Markdown file at the repository root with project-wide rules Cursor should always follow. Most projects that adopted Cursor early (2023–2024) have one. Cursor reads `.cursorrules` *and* `AGENTS.md` if both exist; the former takes precedence for Cursor-specific instructions.

Cursor has since introduced `.cursor/rules/*.mdc` (a multi-file, scoped variant) for personal and project rules with glob-scoped applicability. That is the recommended format for new Cursor projects today; legacy `.cursorrules` continues to work.

### `.github/copilot-instructions.md`

GitHub Copilot's repository-level instructions file, introduced in 2024. Lives in `.github/` next to issue templates and workflows. Read by GitHub Copilot Chat and Copilot Coding Agent. Single-platform by definition — it does not affect Claude Code, Cursor, or Codex.

### `GEMINI.md`

Gemini CLI's repository-level context file. Follows the `AGENTS.md` convention but with a different filename so projects that want Gemini-specific guidance can keep it separate. Gemini CLI also reads `AGENTS.md` for cross-agent instructions.

### `.aider.conf.yml`

Aider's YAML-based configuration file. Stays at the repository root. Covers both repo-level context (analogous to AGENTS.md) and Aider-specific behavior — model selection, auto-commit conventions, file inclusion patterns. The only format in this list that mixes context with tool configuration.

## How they interact when more than one is present

The behavior is specific to each agent:

| Agent | Reads `AGENTS.md`? | Reads its own format? | Precedence when both exist |
|---|---|---|---|
| Claude Code | Yes | `CLAUDE.md` | `CLAUDE.md` content first, then `AGENTS.md` |
| Codex | Yes | None (uses AGENTS.md) | `AGENTS.md` only |
| Cursor | Yes | `.cursorrules`, `.cursor/rules/*.mdc` | Cursor-specific rules first, then `AGENTS.md` |
| GitHub Copilot | Yes (via convention) | `.github/copilot-instructions.md` | Copilot-specific instructions first, then `AGENTS.md` |
| Gemini CLI | Yes | `GEMINI.md` | `GEMINI.md` first, then `AGENTS.md` |
| Aider | Yes | `.aider.conf.yml` | Aider config first, then `AGENTS.md` |
| OpenCode | Yes | `CONVENTIONS.md` | `CONVENTIONS.md` first, then `AGENTS.md` |

The practical implication: if you write `AGENTS.md` well, every coding agent that follows the convention gets useful context without you writing a separate file for each.

## Which one should you write?

Start with `AGENTS.md`. It is the only cross-agent format shipping across the major tools today, and the content that makes a good `AGENTS.md` is the same content every coding agent needs: project purpose, where to start reading, validation, boundaries.

Add `CLAUDE.md` (or another single-agent file) only when you have Claude-Code-specific instructions worth separating. Most teams never reach this point. If you have a `.cursorrules` or `.github/copilot-instructions.md` already, leave it in place — Cursor and Copilot read both, so removing them would be a downgrade.

If you are starting a new project today, the minimum context stack is:

1. **`AGENTS.md`** at the repository root with project context, validation commands, and boundaries
2. **`README.md`** at the repository root for human readers (the two files serve different audiences and are not redundant)
3. **Single-agent files only when you have single-agent content.** If you are running Claude Code and have Claude-Code-specific workflows, add `CLAUDE.md`. If you have Cursor-specific personal formatting preferences, add `.cursor/rules/*.mdc`. Skip the rest.

## A working `AGENTS.md` template

The minimum that produces measurably better coding-agent output:

```markdown
# AGENTS.md

## What this project does
Two to three sentences. Include the user it serves and the problem it solves.

## Where to start reading
- `src/index.ts` — entry point
- `docs/architecture.md` — how the pieces fit together
- `tests/` — what "correct" looks like

## Validation
Run these before declaring a change done:
- `npm test`
- `npm run lint`
- `npm run typecheck`

## Boundaries
Files and operations an agent must not touch without explicit approval:
- Database migrations in `migrations/`
- Anything in `secrets/`
- The auth flow in `src/auth/`

## Conventions
- TypeScript strict mode. No `any`.
- Tests go next to the code they cover.
- Commit messages follow Conventional Commits.
```

The order matters. The first three sections are what every agent needs to know; the last two are project-specific guardrails.

## Common mistakes

**Writing the same content in two formats.** If `AGENTS.md` and `CLAUDE.md` (or `.cursorrules`) say the same thing, every agent reads the duplication. Put shared content in `AGENTS.md` and tool-specific content in the tool-specific file.

**Treating the README as a substitute.** READMEs are written for human readers. Coding agents that follow the AGENTS.md convention look for `AGENTS.md` specifically. A thorough README does not replace one.

**Writing vague instructions.** "Follow best practices" is not actionable. "Run `npm test` before committing" is. The agent has no idea what best practices are; it knows exactly what `npm test` does.

**Keeping a stale `CLAUDE.md`.** A `CLAUDE.md` that is six months out of date is worse than none, because Claude Code will trust it. Review quarterly.

**Not committing the file.** `AGENTS.md` is meant to be version-controlled. If your `.gitignore` is excluding it (it should not), every contributor — human and agent — will see a different picture.

## How this maps to your project

If you are using the `repository-harness` template, the `AGENTS.md` template ships ready to copy. It includes the four sections above with placeholders for your project, plus an example validation block tied to common stacks (Node, Python, Go, Rust). The template also generates a starter `CLAUDE.md` only if you check the optional Claude-Code-specific behavior box.

For a deeper dive on the cross-agent format itself, see [What Is an Agent-Ready Repository?](/agent-ready-repository/) and [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/). For a head-to-head comparison with Cursor Rules specifically, see [AGENTS.md vs Cursor Rules](/blog/agents-md-vs-cursor-rules/).

---

## FAQ

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Should I write AGENTS.md, CLAUDE.md, or both?","acceptedAnswer":{"@type":"Answer","text":"Start with AGENTS.md. It is the only cross-agent format shipping across Claude Code, Codex, Cursor, Aider, and the other major tools today. Add CLAUDE.md only when you have Claude-Code-specific behavior (custom slash commands, Claude-Code-only workflows) worth separating. Most teams never reach that point."}},{"@type":"Question","name":"Does Claude Code read AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Yes. Claude Code reads AGENTS.md at the repository root at the start of every session. When CLAUDE.md also exists, Claude Code reads CLAUDE.md first and falls back to AGENTS.md for cross-agent context."}},{"@type":"Question","name":"Does Cursor read AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Yes. Cursor reads AGENTS.md at the repository root in addition to .cursorrules and .cursor/rules/*.mdc. Treat AGENTS.md as the canonical cross-tool context and the Cursor-specific files as Cursor-only overrides."}},{"@type":"Question","name":"Does GitHub Copilot read AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"GitHub Copilot's primary instructions file is .github/copilot-instructions.md. The Copilot Coding Agent also follows the AGENTS.md convention when present. Both files can coexist; Copilot-specific guidance belongs in the .github/ file."}},{"@type":"Question","name":"Can I have both AGENTS.md and CLAUDE.md in the same repository?","acceptedAnswer":{"@type":"Answer","text":"Yes. The intended split is: put cross-agent context every coding agent should see in AGENTS.md, and put Claude-Code-specific behavior in CLAUDE.md. Avoid duplicating the same content across both files."}},{"@type":"Question","name":"Where does .cursorrules live?","acceptedAnswer":{"@type":"Answer","text":".cursorrules lives at the repository root and is committed with the code. Newer Cursor projects often use the multi-file .cursor/rules/*.mdc format instead, which supports glob-scoped rules and per-user files that are not committed."}},{"@type":"Question","name":"Is AGENTS.md a standard?","acceptedAnswer":{"@type":"Answer","text":"AGENTS.md is a convention rather than a formal standard. It was introduced by the open-source coding-agent community in 2025 and is now adopted by Claude Code, Codex, Cursor, Aider, Gemini CLI, OpenCode, and others. There is no schema or required section list, which is what makes it portable across tools."}}]}</script>

## Related

- [What Is an Agent-Ready Repository?](/agent-ready-repository/) — the broader picture AGENTS.md fits into
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/) — practical guide
- [AGENTS.md vs Cursor Rules](/blog/agents-md-vs-cursor-rules/) — head-to-head comparison
- [AGENTS.md Template](/agents-md-template/) — copy and adapt for your project
- [`repository-harness` on GitHub](https://github.com/hoangnb24/repository-harness) — the open-source implementation

---

*Every major coding agent now reads repository context the same way: a Markdown file at the root, plain text, no schema. The question is no longer which format to invent — it is which sections to put in the file you already need.*
