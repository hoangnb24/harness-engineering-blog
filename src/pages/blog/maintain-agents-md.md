---
layout: ../../layouts/MarkdownLayout.astro
title: "How to Maintain AGENTS.md as Your Repository Evolves"
description: "AGENTS.md is not a one-time setup file. This guide shows when to update it, what to review, and how to keep coding-agent instructions aligned with tests, architecture, tools, and releases."
target_keyword: "maintain AGENTS.md"
secondary_keywords:
  - "update AGENTS.md"
  - "AGENTS.md maintenance"
  - "coding agent instructions"
  - "agent-ready repository checklist"
  - "AI coding agent context"
  - "repository context drift"
status: "published"
date: "2026-07-07"
image: /assets/agents-md-hero.jpg
tags:
  - AGENTS.md
  - How-to
  - Coding Agents
  - Context Engineering
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How often should AGENTS.md be updated?","acceptedAnswer":{"@type":"Answer","text":"Update AGENTS.md whenever commands, repo structure, generated files, test strategy, deployment steps, or major coding conventions change. For active projects, review it at least once per release."}},{"@type":"Question","name":"What is AGENTS.md drift?","acceptedAnswer":{"@type":"Answer","text":"AGENTS.md drift happens when the instructions describe an older version of the repository. The file may point agents to deleted commands, old directories, stale architecture, or validation steps that no longer prove success."}},{"@type":"Question","name":"Who should own AGENTS.md maintenance?","acceptedAnswer":{"@type":"Answer","text":"Treat AGENTS.md like CI configuration or contributor docs. The person changing test commands, repo structure, generated files, or agent workflow should update AGENTS.md in the same pull request."}},{"@type":"Question","name":"Can AGENTS.md be checked automatically?","acceptedAnswer":{"@type":"Answer","text":"Yes. Add lightweight checks for referenced commands, important paths, old package-manager commands, stale repo names, and generated-output warnings. Automation will not judge quality, but it catches many drift failures."}},{"@type":"Question","name":"Should AGENTS.md include release notes?","acceptedAnswer":{"@type":"Answer","text":"No. Put release history in CHANGELOG or GitHub Releases. AGENTS.md should contain current operating instructions: where to work, commands to run, files not to edit, and validation expectations."}},{"@type":"Question","name":"What is the best format for AGENTS.md changes?","acceptedAnswer":{"@type":"Answer","text":"Keep changes small and operational. Prefer short sections, command blocks, path lists, and explicit stop rules over long prose. Link to deeper docs instead of duplicating them."}},{"@type":"Question","name":"How do I know AGENTS.md is working?","acceptedAnswer":{"@type":"Answer","text":"A working AGENTS.md causes agents to choose the right files, run the right checks, avoid generated outputs, and report evidence. If agents repeatedly miss the same step, the file needs a maintenance update."}}]}</script>

# How to Maintain AGENTS.md as Your Repository Evolves

AGENTS.md is easy to treat as a setup task: write it once, commit it, and move on. That is exactly how it becomes dangerous.

A stale AGENTS.md is worse than no AGENTS.md. It gives Claude Code, Codex, Cursor, and other coding agents confidence about commands, directories, and conventions that may no longer be true. The agent follows the file, but the file has drifted away from the repository.

AGENTS.md maintenance is the habit of keeping the repo's coding-agent contract aligned with the current codebase: commands, file boundaries, validation rules, architecture notes, generated outputs, and release workflow.

If you are still creating your first file, start with the [AGENTS.md template](/agents-md-template/) and the full guide on [how to write an AGENTS.md that actually works](/blog/how-to-write-agents-md/). If you already have a file, this article is the operating rhythm that keeps it useful.

## The maintenance rule

Use this rule:

> If a human reviewer would need to know this change before trusting an agent's next edit, update AGENTS.md in the same pull request.

That sounds broad, but in practice it means seven trigger events.

| Trigger | What to check in AGENTS.md |
|---|---|
| Test/build command changed | Validation section |
| Package manager changed | Setup and command examples |
| Repo structure changed | "Where to work" and path map |
| Generated files changed | "Do not edit" and regeneration rules |
| Architecture boundary changed | Module ownership and layering notes |
| New agent/tool adopted | Cross-agent context-file guidance |
| Release process changed | Required checks before handoff |

A good AGENTS.md is not a museum. It is a current execution contract.

## 1. Review validation commands on every release

The validation section is usually the highest-value part of AGENTS.md. It tells an agent how to prove work before returning it.

That also makes it the section most likely to become stale.

Bad maintenance pattern:

```md
## Validation
Run npm test before submitting.
```

Six months later, the repo uses `pnpm`, the main suite moved to `vitest`, the typecheck is separate, and end-to-end tests only run in CI. The agent still sees `npm test` and does exactly what the repo told it to do.

Better pattern:

```md
## Validation
Before handing back code changes, run the narrowest relevant checks first:
- pnpm test -- --run
- pnpm typecheck
- pnpm lint

For UI or route changes, also run:
- pnpm test:e2e -- --grep "affected route or flow"

If a check cannot run locally, report the exact command you would have run and the blocker.
```

Review this section whenever package scripts, test runners, CI jobs, or supported Node/Python versions change.

For the broader repo-preparation workflow, pair this with [what makes a repository agent-ready](/agent-ready-repository/).

## 2. Keep the path map small and current

Agents do not need a full architecture essay. They need a map that prevents blind search.

Useful path maps look like this:

```md
## Where to work
- src/core/ — domain logic and orchestration
- src/cli/ — command-line entry points
- tests/ — unit and integration tests
- docs/ — user-facing documentation

## Do not edit without explicit task scope
- dist/**
- generated/**
- vendor/**
- lockfiles, unless dependency changes are requested
```

Maintenance means deleting old paths as aggressively as you add new ones. A path map with dead directories teaches agents to search the wrong places.

A simple review checklist:

- Does every path still exist?
- Are the most common edit locations listed?
- Are generated or vendor outputs clearly protected?
- Are docs, tests, examples, and fixtures easy to find?
- Does the file distinguish source files from built artifacts?

If your AGENTS.md is full of obsolete folders, read [10 AGENTS.md mistakes that break coding agent sessions](/blog/agents-md-mistakes/) and fix the file before adding more instructions.

## 3. Update generated-output rules before agents touch artifacts

Generated files are where AGENTS.md drift becomes expensive. Agents can edit built files, snapshots, generated clients, schema outputs, or lockfiles because they look like ordinary text.

Make the rule explicit:

```md
## Generated outputs
Do not manually edit:
- dist/**
- src/generated/**
- openapi/client/**

To update generated files, change the source schema and run:
- pnpm generate:client
- pnpm test:contract
```

The maintenance trigger is not just "we added a generated folder." It is also:

- the generator command changed
- the source-of-truth file moved
- snapshots are now reviewed differently
- lockfiles are managed by a different package manager
- generated assets moved from committed to ignored, or vice versa

When this section is current, agents learn to make source changes and regenerate artifacts instead of patching outputs by hand.

## 4. Separate durable repo rules from tool-specific rules

As teams adopt multiple agents, AGENTS.md often becomes a junk drawer:

- Claude-specific prompt advice
- Cursor editor preferences
- Codex validation expectations
- Copilot instructions
- team onboarding prose
- architecture docs

That creates drift because each tool has its own context mechanism and precedence rules. The durable repo contract belongs in AGENTS.md. Tool-specific behavior belongs in the tool-specific file.

Use this split:

| Content | Best home |
|---|---|
| Repo overview, commands, paths, validation | AGENTS.md |
| Claude Code behavior or tone | CLAUDE.md |
| Cursor editor/project rules | .cursorrules or .cursor/rules |
| GitHub Copilot repo instructions | .github/copilot-instructions.md |
| Long architecture rationale | docs/architecture.md |

The comparison guide [AGENTS.md vs CLAUDE.md vs .cursorrules vs copilot-instructions.md](/blog/coding-agent-context-file-formats/) covers the format differences in detail.

Maintenance rule: when you add or change a tool-specific file, check whether any universal repo rule was duplicated there. Shared rules should live once.

## 5. Add an AGENTS.md review line to pull requests

The easiest maintenance system is a small PR checklist entry:

```md
- [ ] If commands, paths, generated files, or repo conventions changed, AGENTS.md was updated.
```

This avoids a separate documentation chore. The person making the change has the most context and can update the agent contract while the change is fresh.

For bigger repositories, make the checklist more specific:

```md
Agent-readiness check:
- [ ] Validation commands still match package scripts / CI
- [ ] New generated files are documented as generated
- [ ] New top-level directories are reflected in AGENTS.md if agents should use them
- [ ] New architecture boundaries are linked from AGENTS.md or docs
```

This turns AGENTS.md from a static file into part of the repository's operating system.

## 6. Run a lightweight drift audit monthly

A monthly audit does not need to be complex. You can catch most drift with a small checklist.

Manual audit:

1. Open AGENTS.md.
2. Run every command listed in the validation section, or confirm why it is intentionally CI-only.
3. Check every path mentioned in the file.
4. Search for old package-manager commands (`npm`, `yarn`, `pnpm`, `uv`, `poetry`) that no longer apply.
5. Search for old repo names, old release names, or old deployment targets.
6. Ask: "If an agent followed only this file, what would it get wrong?"

Automation can help with the first five. The sixth is still a human or maintainer judgment.

A minimal script can check path and command references, but do not confuse passing a script with having a good AGENTS.md. The file still needs to be short, ranked, and operational.

## 7. Treat repeated agent mistakes as maintenance signals

If an agent repeatedly edits the wrong directory, skips a test, breaks generated files, or expands scope into a refactor, do not only correct the agent in chat. Update AGENTS.md so the next session starts with better context.

A simple pattern:

```md
## Lessons from agent sessions
- When changing CLI output, update tests/cli/snapshots by running pnpm test:cli -- --updateSnapshot. Do not edit snapshots manually.
- For database migrations, add a rollback note in docs/migrations.md and run pnpm test:migrations.
- Avoid broad formatting-only changes unless the task explicitly requests them.
```

Keep this section short. If it grows beyond a handful of lessons, promote the durable rules into the main sections and move detailed history into docs.

The goal is not to document every failure forever. The goal is to convert repeated failure into better defaults.

## Maintenance checklist

Use this checklist before a release or after any repo-structure change:

- [ ] Validation commands still run or clearly name their blockers.
- [ ] Setup commands match the current package manager and runtime version.
- [ ] Path map lists current directories and removes dead ones.
- [ ] Generated files are clearly marked as generated.
- [ ] Regeneration commands are listed next to generated-output rules.
- [ ] Tool-specific context files do not duplicate universal repo rules.
- [ ] AGENTS.md links to deeper docs instead of copying them.
- [ ] Stop conditions are clear: when to run checks, when to report blockers, when not to expand scope.
- [ ] Repeated agent mistakes from the last month have been converted into durable rules.

If you want a working baseline instead of a blank file, copy the [AGENTS.md template](/agents-md-template/) and adapt it. If your repo does not yet have the surrounding harness, use [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness) as the reference implementation.

## FAQ

### How often should AGENTS.md be updated?

Update it whenever commands, repo structure, generated files, test strategy, deployment steps, or major coding conventions change. For active projects, review it at least once per release.

### What is AGENTS.md drift?

AGENTS.md drift happens when the instructions describe an older version of the repository. The file may point agents to deleted commands, old directories, stale architecture, or validation steps that no longer prove success.

### Who should own AGENTS.md maintenance?

Treat AGENTS.md like CI configuration or contributor docs. The person changing test commands, repo structure, generated files, or agent workflow should update AGENTS.md in the same pull request.

### Can AGENTS.md be checked automatically?

Yes. Add lightweight checks for referenced commands, important paths, old package-manager commands, stale repo names, and generated-output warnings. Automation will not judge quality, but it catches many drift failures.

### Should AGENTS.md include release notes?

No. Put release history in CHANGELOG or GitHub Releases. AGENTS.md should contain current operating instructions: where to work, commands to run, files not to edit, and validation expectations.

### What is the best format for AGENTS.md changes?

Keep changes small and operational. Prefer short sections, command blocks, path lists, and explicit stop rules over long prose. Link to deeper docs instead of duplicating them.

### How do I know AGENTS.md is working?

A working AGENTS.md causes agents to choose the right files, run the right checks, avoid generated outputs, and report evidence. If agents repeatedly miss the same step, the file needs a maintenance update.
