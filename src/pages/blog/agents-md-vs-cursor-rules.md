---
layout: ../../layouts/MarkdownLayout.astro
title: "AGENTS.md vs Cursor Rules: Which One Does Your Repository Actually Need?"
description: "AGENTS.md and Cursor Rules both aim to give coding agents better context. They work differently, live in different places, and serve different scopes. Here is how to choose."
target_keyword: "Cursor rules vs AGENTS.md"
secondary_keywords:
  - Cursor rules vs AGENTS.md
  - AGENTS.md vs Cursor rules
  - Cursor rules
  - AGENTS.md
  - coding agent context files
  - repo-level agent instructions
  - agent-ready repository
status: "published"
date: "2026-05-29"
image: /assets/comparison-hero.jpg
tags:
  - Comparison
  - English
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Should I use AGENTS.md or Cursor Rules?","acceptedAnswer":{"@type":"Answer","text":"Use AGENTS.md for repository-level context that every coding agent should know. Use Cursor Rules for personal IDE preferences that should not be committed. For most teams with more than one person or more than one tool, start with AGENTS.md."}},{"@type":"Question","name":"Can AGENTS.md and Cursor Rules coexist?","acceptedAnswer":{"@type":"Answer","text":"Yes. They are not mutually exclusive. Put repo-wide rules in AGENTS.md at the repository root, and use Cursor Rules for personal IDE workflows, formatting preferences, and tool-specific overrides that should not be shared."}},{"@type":"Question","name":"Does Claude Code read AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Yes. Claude Code reads AGENTS.md at the repository root at the start of every session. It does not read .cursor/rules/ because that is a Cursor-only feature."}},{"@type":"Question","name":"Does Cursor read AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Yes. Cursor reads AGENTS.md at the repository root in addition to .cursor/rules/. Treat AGENTS.md as the canonical cross-tool context and .cursor/rules/ as Cursor-specific overrides."}},{"@type":"Question","name":"Where do AGENTS.md and Cursor Rules live?","acceptedAnswer":{"@type":"Answer","text":"AGENTS.md lives at the repository root: ./AGENTS.md. It travels with the code in version control. Cursor Rules live in .cursor/rules/ inside the user's local checkout and are not committed unless exported and added manually."}},{"@type":"Question","name":"Is AGENTS.md better than Cursor Rules for open source?","acceptedAnswer":{"@type":"Answer","text":"Yes, for open source repositories. External contributors will arrive with different IDEs and tools. AGENTS.md ensures every contributor — and every coding agent they bring with them — gets the same context. Cursor Rules only help if the contributor happens to use Cursor."}},{"@type":"Question","name":"Do I need both for a small personal project?","acceptedAnswer":{"@type":"Answer","text":"For a 200-line personal project, AGENTS.md is enough. Cursor Rules add value when you want personal IDE behavior that should not leak into the repo. If you only use Cursor and never expect collaborators, Cursor Rules alone are fine, but you will lose the context if you switch tools."}}]}</script>

# AGENTS.md vs Cursor Rules: Which One Does Your Repository Actually Need?

Both AGENTS.md and Cursor Rules are attempts to solve the same problem: **coding agents do not know what they need to know when they enter a repository.**

The difference is where they live, how they work, and what scope they cover.

---

## What AGENTS.md Is

AGENTS.md is a file you place at the root of your repository. It becomes part of the repository itself.

Any coding agent that enters the repo — Claude Code, Codex, Aider, anything that reads files — sees it automatically. The context travels with the code.

```markdown
# AGENTS.md — My Project

## Project overview
[2–4 sentences on what this repo does]

## Before you start
- Read README.md and docs/architecture.md first
- Preferred change size: small and reviewable

## Commands
| Command | What it does |
|---|---|
| npm install | Install dependencies |
| npm test | Run full test suite |

## Architecture
- `src/` — main source
- `tests/` — test files
```

AGENTS.md works because it is **repo-level by design**. The context belongs to the repository and stays in sync with it.

---

## What Cursor Rules Are

Cursor is an AI-first IDE. Its Rules feature lets you define instructions that the IDE applies to every agent session.

Rules are stored in your local Cursor settings, not in the repository. They are IDE-wide, not repo-specific.

Cursor Rules look similar to AGENTS.md content on the surface:

```markdown
# My Project Rules

- This is a Node.js REST API
- Always use the validation script before committing
- Do not touch the legacy `src/legacy/` directory
```

The problem: **these rules stay on your machine.** If someone else clones the repo, they get none of this context.

---

## The Core Difference

| | AGENTS.md | Cursor Rules |
|---|---|---|
| **Location** | Repository root | Local IDE settings |
| **Who sees it** | Any agent in any tool | Only Cursor users |
| **Syncs with repo** | Yes — lives with the code | No — local to each developer |
| **Version control** | Yes | No (unless you export/import manually) |
| **Scope** | Repository context | Developer preference + project rules |

AGENTS.md is about **the repository**. Cursor Rules are about **the IDE session**.

---

## When AGENTS.md Wins

AGENTS.md is the right choice when:

- You want the context to survive team changes and new contributors
- Multiple people work on the repo with different IDEs
- You want the context to be versioned alongside the code
- The repo is open source and you want external contributors to get the same context
- You are writing for tools that are not Cursor (Claude Code, Codex, Aider, etc.)

```bash
# AGENTS.md travels with every clone
git clone https://github.com/owner/repo
cd repo
claude code  # reads AGENTS.md automatically
```

If you use multiple coding agents across different projects or editors, AGENTS.md is the portable option.

---

## When Cursor Rules Win

Cursor Rules are useful when:

- You want personal shortcuts and IDE-specific behaviors that only apply to your setup
- You want rules that apply only in Cursor and should not be imposed on other tool users
- You are doing rapid prototyping and want quick local overrides without committing to the repo
- You want per-file or per-project rules that are more granular than AGENTS.md

Cursor Rules can also **complement** AGENTS.md — use AGENTS.md for repo-level context, Cursor Rules for personal workflow preferences.

---

## Can You Use Both?

Yes. The two systems do not conflict.

Use AGENTS.md for repository-level context that every agent should know. Use Cursor Rules for your personal IDE preferences and tool-specific behaviors that only make sense in Cursor.

A team where everyone uses Cursor might still want AGENTS.md so the context is documented in the repo and survives beyond individual setups.

---

## The Practical Choice for Most Teams

If your repository is used by more than one person, more than one tool, or will outlast any single IDE's dominance: **start with AGENTS.md.**

If you are a solo developer who lives entirely in Cursor and want quick local overrides: **Cursor Rules are convenient, but document them somewhere permanent.**

The key insight: **context that only lives in your IDE is context that disappears when you change tools.**

---

## Frequently Asked Questions

### Should I use AGENTS.md or Cursor Rules?

Use AGENTS.md for repository-level context that every coding agent should know. Use Cursor Rules for personal IDE preferences that should not be committed. For most teams with more than one person or more than one tool, start with AGENTS.md.

### Can AGENTS.md and Cursor Rules coexist?

Yes. They are not mutually exclusive. Put repo-wide rules in AGENTS.md at the repository root, and use Cursor Rules for personal IDE workflows, formatting preferences, and tool-specific overrides that should not be shared.

### Does Claude Code read AGENTS.md?

Yes. Claude Code reads AGENTS.md at the repository root at the start of every session. It does not read `.cursor/rules/` because that is a Cursor-only feature.

### Does Cursor read AGENTS.md?

Yes. Cursor reads AGENTS.md at the repository root in addition to `.cursor/rules/`. Treat AGENTS.md as the canonical cross-tool context and `.cursor/rules/` as Cursor-specific overrides.

### Where do AGENTS.md and Cursor Rules live?

AGENTS.md lives at the repository root: `./AGENTS.md`. It travels with the code in version control. Cursor Rules live in `.cursor/rules/` inside the user's local checkout and are not committed unless exported and added manually.

### Is AGENTS.md better than Cursor Rules for open source?

Yes, for open source repositories. External contributors will arrive with different IDEs and tools. AGENTS.md ensures every contributor — and every coding agent they bring with them — gets the same context. Cursor Rules only help if the contributor happens to use Cursor.

### Do I need both for a small personal project?

For a 200-line personal project, AGENTS.md is enough. Cursor Rules add value when you want personal IDE behavior that should not leak into the repo. If you only use Cursor and never expect collaborators, Cursor Rules alone are fine, but you will lose the context if you switch tools.

---

## Related

- [What Is an Agent-Ready Repository?](/agent-ready-repository/) — the broader picture AGENTS.md fits into
- [AGENTS.md Template](/agents-md-template/) — copy and adapt for your project
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/) — practical guide

---

## Related pages

- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/) — practical guide
- [AGENTS.md Template](/agents-md-template/) — copy and adapt for your project
- [`repository-harness` on GitHub](https://github.com/hoangnb24/repository-harness) — the open-source implementation

---

*Both approaches reflect the same underlying insight: coding agents work better when the repository tells them what they need to know. The question is just where you put that information, and who you want it to serve.*