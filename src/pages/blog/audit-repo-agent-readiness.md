---
layout: ../../layouts/MarkdownLayout.astro
title: "How to Audit a Repository for Agent-Readiness"
description: "A practical audit checklist for finding the gaps that make Claude Code, Codex, Cursor, and other coding agents fail inside a repository."
target_keyword: "agent readiness audit"
secondary_keywords:
  - "audit repository for coding agents"
  - "agent-ready repository checklist"
  - "AI coding agent repo audit"
  - "AGENTS.md audit checklist"
  - "repository-harness audit"
  - "prepare repo for coding agents"
status: "published"
date: "2026-07-14"
image: /assets/agents-md-hero.jpg
tags:
  - Agent-ready repository
  - How-to
  - Coding Agents
  - Context Engineering
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is an agent-readiness audit?","acceptedAnswer":{"@type":"Answer","text":"An agent-readiness audit checks whether a repository gives AI coding agents enough durable context, validation commands, safety boundaries, and handoff expectations to make useful, reviewable changes without rediscovering the project from scratch."}},{"@type":"Question","name":"How is an agent-readiness audit different from a code quality audit?","acceptedAnswer":{"@type":"Answer","text":"A code quality audit asks whether the code is maintainable. An agent-readiness audit asks whether an AI coding agent can safely understand, change, validate, and explain the code. A repo can have good code quality but still be hard for agents if conventions, tests, and risk boundaries are implicit."}},{"@type":"Question","name":"What should I audit first?","acceptedAnswer":{"@type":"Answer","text":"Start with the entry points: README, AGENTS.md, setup commands, test commands, project structure, and contribution or review expectations. These determine whether an agent can orient itself before editing files."}},{"@type":"Question","name":"Does every repository need AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Any repository that expects repeat coding-agent work benefits from AGENTS.md. Small repos can use a short file. Larger repos need more explicit path maps, validation commands, generated-file rules, and stop rules."}},{"@type":"Question","name":"How often should I repeat the audit?","acceptedAnswer":{"@type":"Answer","text":"Repeat the audit after major architecture changes, new test tooling, new generated code, new deployment paths, or every month during active development. Agent instructions drift when the repository changes faster than its documentation."}},{"@type":"Question","name":"What is a passing score for an agent-ready repository?","acceptedAnswer":{"@type":"Answer","text":"A practical passing score is 80 out of 100 with no critical gaps in setup, validation, safety boundaries, or handoff. Repositories under 60 usually need a focused cleanup before relying on agents for non-trivial changes."}},{"@type":"Question","name":"Can repository-harness help with the audit?","acceptedAnswer":{"@type":"Answer","text":"Yes. repository-harness provides copyable templates and conventions for AGENTS.md, validation expectations, and cross-agent repository context. Use it as a baseline for turning audit findings into concrete repo files."}}]}</script>

# How to Audit a Repository for Agent-Readiness

Most teams ask the wrong question after a bad coding-agent session.

They ask: “Was the model good enough?”

A better question is: “Could the repository explain itself well enough?”

Claude Code, Codex, Cursor, and other coding agents can only work with the context they can discover. If setup commands are buried in chat history, validation rules live in one maintainer's head, generated files look editable, and risky paths have no stop signs, agents will improvise.

An agent-readiness audit finds those gaps before they turn into broken pull requests.

Use this guide as a practical scoring checklist. If you want a baseline template while you audit, start with the [AGENTS.md template](/agents-md-template/) and the [agent-ready repository definition](/agent-ready-repository/).

## The short version

A repository is agent-ready when a coding agent can answer five questions before it edits code:

1. **Where am I?** The repo structure, ownership boundaries, and important paths are obvious.
2. **How do I work here?** Setup, build, test, lint, and preview commands are explicit.
3. **What should I not touch?** Generated files, secrets, migrations, and high-risk product areas are labeled.
4. **How do I know I am done?** Validation and handoff expectations are concrete.
5. **What context should persist?** Architecture, conventions, and decisions live in files, not prompts.

If any of those answers require asking a maintainer, the repo is not fully agent-ready yet.

## Score the repo across seven surfaces

Use a 100-point score. The exact number matters less than the gaps it reveals.

| Surface | Points | What to inspect |
|---|---:|---|
| Orientation | 15 | README, repo map, package/workspace structure, ownership boundaries |
| Agent instructions | 20 | AGENTS.md, tool-specific files, coding conventions, stop rules |
| Validation | 20 | setup, test, lint, typecheck, integration, preview, and failure reporting commands |
| Safety boundaries | 15 | secrets, generated files, migrations, auth, billing, data writes, production paths |
| Context durability | 10 | architecture notes, decisions, examples, fixtures, API contracts |
| Handoff quality | 10 | PR template, change summary expectations, screenshots, test evidence |
| Maintenance loop | 10 | owner, review cadence, drift triggers, stale-command cleanup |

Interpret the score like this:

| Score | Meaning | Action |
|---:|---|---|
| 85–100 | Strong agent-ready baseline | Improve examples and edge-case instructions |
| 70–84 | Usable but leaky | Fix the lowest scoring surface before broad agent use |
| 50–69 | Agent sessions will be inconsistent | Add AGENTS.md, validation commands, and safety boundaries first |
| 0–49 | Agents must rediscover the repo every run | Treat agent work as experimental until the repository is documented |

The highest-leverage fixes are usually small: a real test command, a path map, a generated-file warning, or a stop rule for risky code.

## 1. Audit orientation

An agent should understand the repository shape within the first minute.

Check whether the README or AGENTS.md answers:

- What kind of project is this?
- Which package manager or build tool is canonical?
- Where are app code, tests, scripts, docs, generated files, and examples?
- Which directories are stable interfaces vs internal implementation?
- Which subprojects or packages are independent?
- Which docs explain architecture or deployment?

A minimal orientation section looks like this:

```md
## Repository map

- apps/web/ — customer-facing web app
- apps/api/ — HTTP API and background jobs
- packages/ui/ — shared design system components
- packages/db/ — schema, migrations, query helpers
- docs/architecture/ — durable design notes and decisions
- scripts/ — local maintenance and validation commands
```

This is boring documentation for humans. For agents, it is a search-space reducer.

For the broader category, read [what is an agent-ready repository](/agent-ready-repository/).

## 2. Audit AGENTS.md

AGENTS.md is the agent's operating manual. It should not be a motivational poster.

Check whether it contains:

- the repository purpose in one paragraph
- canonical setup commands
- canonical validation commands
- path-specific editing rules
- generated-file warnings
- naming, style, and architecture conventions
- stop rules for sensitive areas
- handoff expectations before the agent says “done”

A weak AGENTS.md says:

```md
Write clean code and run tests.
```

A useful AGENTS.md says:

```md
Before handoff, run:
- npm run lint
- npm run typecheck
- npm test -- --run

Do not manually edit:
- src/generated/**
- package-lock.json unless npm install changed dependencies
- migrations already applied in production

Ask before changing:
- auth/session logic
- billing or quota checks
- irreversible data writes
```

If the repo has multiple agents in use, also inspect tool-specific context files. The comparison guide [AGENTS.md vs CLAUDE.md vs .cursorrules vs copilot-instructions.md](/blog/coding-agent-context-file-formats/) explains how those files differ.

## 3. Audit validation commands

Agents do not just need advice. They need executable checks.

Look for commands that prove a change is safe:

| Change type | Validation command examples |
|---|---|
| JS/TS code | `npm run lint`, `npm run typecheck`, `npm test -- --run` |
| Python code | `ruff check .`, `pytest`, `mypy .` |
| API contracts | OpenAPI/protobuf compatibility checks, contract tests |
| Database changes | migration generation + migration validation |
| Frontend changes | build, preview, unit tests, accessibility, E2E, screenshots |
| Docs/content | build, link check, public-content hygiene check |

The audit question is not “do tests exist?”

The audit question is “would a first-time agent know exactly which command to run for this kind of change?”

If the answer is no, add a validation table to AGENTS.md.

For tool-specific setup, see [how to prepare your repository for Claude Code](/blog/prepare-repo-for-claude-code/) and [how to prepare your repository for Codex](/blog/prepare-repo-for-codex/).

## 4. Audit safety boundaries

Coding agents need explicit boundaries because the risky paths in a repository often look ordinary.

Search for these categories:

- authentication and authorization
- billing, metering, quotas, payments
- secrets and token handling
- database migrations and destructive data writes
- production deployment scripts
- generated code and vendored code
- public API contracts
- compliance, privacy, and security-sensitive code

Then ask whether the repo tells agents what to do around them.

A good stop-rule block is short:

```md
## Stop rules

Ask before changing:
- auth/session code
- billing, quota, or payment paths
- database migration strategy
- production deployment scripts
- public API response shapes

Never commit secrets. Use redacted examples only.
```

This does not make the agent timid. It keeps the handoff reviewable.

## 5. Audit durable context

Prompts disappear. Repository files persist.

A good agent-ready repo stores durable context in places agents can read every run:

- architecture docs
- decision records
- package or workspace maps
- API contracts
- examples and fixtures
- test data explanations
- migration notes
- design-system documentation

If a maintainer keeps explaining the same rule in chat, that rule belongs in the repo.

This is the practical side of [context engineering for coding agents](/context-engineering-for-coding-agents/): move repeat context out of prompts and into versioned project files.

## 6. Audit handoff quality

Agent work fails at the handoff when the final message is too vague.

Check whether the repo defines what an acceptable handoff includes:

- summary of changed files
- tests run and exact output
- tests not run and why
- screenshots or preview links for UI changes
- migration notes for data changes
- follow-up risks or review focus areas

A useful PR template or AGENTS.md handoff section might say:

```md
## Handoff checklist

Before marking work complete, include:
- what changed and why
- commands run, with pass/fail result
- commands skipped, with reason
- screenshots for UI changes
- risky files touched
- follow-up recommendations
```

This turns agent output into reviewer-ready evidence instead of a generic “done.”

## 7. Audit the maintenance loop

Agent-readiness decays.

A repo can have a great AGENTS.md on Monday and a stale one by Friday if the team changes the build tool, test runner, directory layout, or deployment path.

Check whether someone owns updates after:

- a new package manager or framework version
- a new workspace/package
- a new generated-code path
- a new test or CI command
- a new deployment or migration flow
- recurring agent mistakes in the same area

If no owner exists, add a lightweight monthly drift review. The maintenance guide [how to maintain AGENTS.md as your repository evolves](/blog/maintain-agents-md/) gives a practical cadence.

## A copyable audit worksheet

Use this in an issue, PR, or internal doc:

```md
# Agent-readiness audit

Repository:
Date:
Auditor:

## Score
- Orientation: __ / 15
- Agent instructions: __ / 20
- Validation: __ / 20
- Safety boundaries: __ / 15
- Durable context: __ / 10
- Handoff quality: __ / 10
- Maintenance loop: __ / 10
- Total: __ / 100

## Critical gaps
1.
2.
3.

## Fast fixes this week
- [ ] Add or update AGENTS.md
- [ ] Add validation command table
- [ ] Label generated files and high-risk paths
- [ ] Add handoff checklist
- [ ] Link architecture and decision docs

## Follow-up
- Owner:
- Review date:
- Metric to watch:
```

Do not try to fix every gap in one pass. Fix the gaps that make the next agent session unsafe or unreproducible.

## What to fix first

If the audit finds too much, use this order:

1. **Validation commands** — agents need proof before handoff.
2. **Stop rules** — prevent risky autonomous edits.
3. **Repository map** — reduce discovery cost.
4. **Generated-file rules** — prevent noisy diffs.
5. **Handoff checklist** — improve review quality.
6. **Durable architecture context** — compound across future sessions.
7. **Maintenance owner** — keep the system from drifting again.

This order is intentionally practical. It makes the next coding-agent run safer even before the entire repo is perfect.

## Where repository-harness fits

[repository-harness](https://github.com/hoangnb24/repository-harness) is the working template for this audit.

Use it when you want to turn findings into concrete repo files:

- copy an AGENTS.md baseline
- define validation expectations
- keep context portable across Claude Code, Codex, Cursor, and other coding agents
- make handoffs easier to review
- document the repo as a durable operating environment, not just a code dump

The goal is not to make agents autonomous at all costs. The goal is to make their work legible, bounded, and reviewable.

## Related pages

- [What Is an Agent-Ready Repository?](/agent-ready-repository/)
- [AGENTS.md Template](/agents-md-template/)
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/)
- [How to Maintain AGENTS.md as Your Repository Evolves](/blog/maintain-agents-md/)
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/)
- [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness)

---

## FAQ

### What is an agent-readiness audit?

An agent-readiness audit checks whether a repository gives AI coding agents enough durable context, validation commands, safety boundaries, and handoff expectations to make useful, reviewable changes without rediscovering the project from scratch.

### How is an agent-readiness audit different from a code quality audit?

A code quality audit asks whether the code is maintainable. An agent-readiness audit asks whether an AI coding agent can safely understand, change, validate, and explain the code. A repo can have good code quality but still be hard for agents if conventions, tests, and risk boundaries are implicit.

### What should I audit first?

Start with the entry points: README, AGENTS.md, setup commands, test commands, project structure, and contribution or review expectations. These determine whether an agent can orient itself before editing files.

### Does every repository need AGENTS.md?

Any repository that expects repeat coding-agent work benefits from AGENTS.md. Small repos can use a short file. Larger repos need more explicit path maps, validation commands, generated-file rules, and stop rules.

### How often should I repeat the audit?

Repeat the audit after major architecture changes, new test tooling, new generated code, new deployment paths, or every month during active development. Agent instructions drift when the repository changes faster than its documentation.

### What is a passing score for an agent-ready repository?

A practical passing score is 80 out of 100 with no critical gaps in setup, validation, safety boundaries, or handoff. Repositories under 60 usually need a focused cleanup before relying on agents for non-trivial changes.

### Can repository-harness help with the audit?

Yes. repository-harness provides copyable templates and conventions for AGENTS.md, validation expectations, and cross-agent repository context. Use it as a baseline for turning audit findings into concrete repo files.
