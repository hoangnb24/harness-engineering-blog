---
layout: ../../layouts/MarkdownLayout.astro
title: "AGENTS.md Before and After: A Real Repository Case Study"
description: "See how repository-harness evolved AGENTS.md from a 75-line operating manual into a 32-line routing layer with explicit authority, planning, validation, and handoff rules."
target_keyword: "AGENTS.md case study"
secondary_keywords:
  - "AGENTS.md before and after"
  - "real AGENTS.md example"
  - "agent-ready repository case study"
  - "improve AGENTS.md"
  - "repository instructions for coding agents"
  - "repository-harness AGENTS.md"
status: "published"
date: "2026-07-23"
image: /assets/agents-md-hero.jpg
tags:
  - AGENTS.md
  - Case Study
  - Agent-ready repository
  - Coding Agents
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What changed in the repository-harness AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"It changed from a 75-line operating manual that duplicated workflow detail into a 32-line routing layer. The current file classifies read-only outcomes, bounded changes, and durable work; identifies when to pause; requires evidence before completion; and links to deeper repository sources of truth."}},{"@type":"Question","name":"Should AGENTS.md contain the entire development workflow?","acceptedAnswer":{"@type":"Answer","text":"Usually not. AGENTS.md should make the first decisions clear and route agents to authoritative workflow, architecture, validation, and planning documents. Duplicating the whole workflow creates drift and increases the amount of context every session must load."}},{"@type":"Question","name":"Is a shorter AGENTS.md always better?","acceptedAnswer":{"@type":"Answer","text":"No. Shorter is useful only when the removed detail still exists in clear, linked sources of truth. The goal is not the fewest lines; it is the smallest entry point that lets an agent choose the correct workflow without guessing."}},{"@type":"Question","name":"What are authority rules in AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Authority rules tell an agent which requests permit edits, which outcomes must remain read-only, when product intent is still unresolved, and when the agent must pause before an irreversible or weakly validated action. They prevent a plausible implementation from becoming an unauthorized one."}},{"@type":"Question","name":"How should AGENTS.md handle small tasks and multi-session work?","acceptedAnswer":{"@type":"Answer","text":"Use a lightweight path for bounded changes and a durable plan for work that spans sessions, has dependencies, needs coordination, or requires recovery steps. A single heavy workflow for every task creates unnecessary state and slows simple changes."}},{"@type":"Question","name":"How often should AGENTS.md be revised?","acceptedAnswer":{"@type":"Answer","text":"Revise it when the repository's canonical commands, workflow, authority model, validation requirements, planning system, or generated-file boundaries change. Review it during releases and after repeated agent mistakes reveal a missing or misleading rule."}},{"@type":"Question","name":"Can I copy the repository-harness AGENTS.md directly?","acceptedAnswer":{"@type":"Answer","text":"Use it as a pattern, not a drop-in file. Keep the outcome classification, pause conditions, evidence requirement, and routing structure, but replace every linked document and workflow rule with the sources of truth in your own repository."}}]}</script>

# AGENTS.md Before and After: A Real Repository Case Study

A good `AGENTS.md` is not finished when it is first written. It should evolve as the repository learns which instructions agents actually need, which details belong elsewhere, and which mistakes require a stronger boundary.

This case study follows the real `AGENTS.md` history of [repository-harness](https://github.com/hoangnb24/repository-harness), from its first public commit on May 5, 2026 to its current form on July 21, 2026.

The change was not simply “make the file shorter.” The file moved through three distinct roles:

1. a complete operating manual
2. a small pointer file into a growing harness system
3. a decision router that classifies work, identifies authority, and requires evidence

That final role is the useful one to copy.

## The short answer

The original `AGENTS.md` was **75 lines** and described the repository status, reading order, task loop, change policy, and done definition in one place. It was explicit, but it duplicated rules that also lived in repository documentation.

The current file is **32 lines**. It does less documentation and more routing. It tells an agent:

- which requested outcomes must stay read-only
- when a bounded change can use an ephemeral plan
- when work needs a durable plan under `docs/plans/active/`
- when unresolved authority or risk requires a pause
- what evidence is required before claiming completion
- which legacy control-plane features are optional rather than mandatory

The line count fell by 57%, but compression is not the main result. The important change is that the entry point now answers the decisions an agent must make **before** it starts editing.

## Before and after

| Dimension | May 5, 2026: first commit | July 21, 2026: current form |
|---|---|---|
| Length | 75 lines | 32 lines |
| Primary role | Complete operating guide | Decision router and stable entry point |
| Reading behavior | Fixed nine-document reading order | Read `docs/WORKFLOW.md`, then only task-relevant material |
| Task model | One seven-step loop for every task | Separate paths for read-only outcomes, bounded changes, and durable work |
| Planning | Stories and intake for all work | Ephemeral plans for bounded changes; durable plans only when complexity requires them |
| Authority | Human confirmation for five broad policy changes | Identify authority for new observable policy; pause when choices remain open or the request is insufficient |
| Validation | Run commands when they exist | Claim completion only with executable or observable evidence |
| Handoff | Report what changed and what was not attempted | Report outcome, changed surfaces, validation, and unresolved risks |
| State machinery | Repository docs and backlog are part of every loop | SQLite intake, trace, scoring, and audit features are optional compatibility paths |
| Maintenance risk | Rules duplicated across the entry point and deeper docs | Workflow detail lives behind one canonical router |

This is a source-history comparison, not a controlled productivity experiment. The repository history proves how the instructions changed. It does not, by itself, prove a specific percentage improvement in completion time or defect rate.

## What the first version got right

The first public version, commit [`b07d72a`](https://github.com/hoangnb24/repository-harness/commit/b07d72a), was already stronger than a generic instruction file.

It included:

- a repository-status warning: there was no product implementation yet
- an ordered source-of-truth list
- a seven-step task loop
- explicit changes agents could make directly
- explicit changes that needed human confirmation
- a five-part done definition

Those are all useful ingredients. The file recognized that coding agents need more than style preferences. They need operating context, decision boundaries, and proof expectations.

The weakness appeared as the repository grew: the entry point was trying to be both the index and the handbook.

A nine-document reading order is precise, but it also requires every agent to load the same broad context before every task. A full task loop is safe, but it can make a read-only review and a multi-session implementation follow the same machinery. When the same rule exists in `AGENTS.md`, workflow docs, installer assets, and tool guidance, every change creates a synchronization problem.

## The evolution timeline

### May 22: instructions expanded with the control plane

Commit [`7e61551`](https://github.com/hoangnb24/repository-harness/commit/7e61551) added a SQLite durable layer for intake, stories, traces, audits, and proposals. `AGENTS.md` grew to **107 lines**.

The expansion made the new operational model visible, but it also revealed a design pressure: an entry file can grow quickly when every repository capability becomes part of the default agent workflow.

### May 23: the file became a stable shim

Commit [`fd81519`](https://github.com/hoangnb24/repository-harness/commit/fd81519) reduced `AGENTS.md` from 107 lines to **19 lines**.

The file stopped duplicating the whole harness and instead pointed to:

- `README.md`
- `docs/HARNESS.md`
- `docs/FEATURE_INTAKE.md`
- `docs/ARCHITECTURE.md`
- the repository-local Harness CLI

This established an important pattern: `AGENTS.md` should be a stable layer above documents and tools that can evolve independently.

The tradeoff was that the shim became mostly a reading list. It was compact, but it did not yet help the agent classify the requested outcome before invoking the workflow.

### June 13 to July 11: useful pointers accumulated, then were removed

Commit [`b5ba98a`](https://github.com/hoangnb24/repository-harness/commit/b5ba98a) added tool-registry guidance and grew the file to **23 lines**.

Commit [`4fbb260`](https://github.com/hoangnb24/repository-harness/commit/4fbb260) later removed duplicated project-skill and tool-registry guidance, shrinking it to **15 lines**.

That subtraction was not cosmetic. It enforced a separation of concerns:

- `AGENTS.md` chooses the workflow
- repository docs explain the workflow
- tool registries describe available tools
- scripts and tests enforce mechanical contracts

When every useful fact is promoted into the root instruction file, the root file becomes a second README. Removing detail can improve authority when the remaining links are precise.

### July 13: request authority became explicit

Commit [`fad321a`](https://github.com/hoangnb24/repository-harness/commit/fad321a) raised the file to **20 lines** and added a distinction that many repositories miss:

- answers, reviews, diagnoses, plans, and status reports are read-only
- explicit requests to build, fix, change, or write authorize repository mutation

This protects against a common agent failure: treating a request to analyze a problem as permission to fix it.

The same commit added installer tests around the authority contract, moving a critical instruction from prose-only guidance toward an enforceable repository invariant.

### July 20: small work was decoupled from heavy workflow state

Commit [`232e0e3`](https://github.com/hoangnb24/repository-harness/commit/232e0e3) expanded the file to **29 lines**, but simplified the default operating model.

It introduced three paths:

1. **Read-only outcome** — inspect only what is needed; do not mutate state.
2. **Bounded change** — use an ephemeral plan, implement, and run behavior-appropriate validation.
3. **Durable work** — create a plan under `docs/plans/active/` when work spans sessions, has dependencies, needs coordination, or requires recovery steps.

This is a better form of simplicity than forcing every task through one “correct” process. The workflow becomes proportional to the work.

The commit also made SQLite intake, story, trace, scoring, audit, and proposal commands optional compatibility features. Capabilities can remain available without taxing every routine task.

### July 21: policy authority and evidence became first-class

The July 21 sequence—commits [`98ebecc`](https://github.com/hoangnb24/repository-harness/commit/98ebecc), [`f65f415`](https://github.com/hoangnb24/repository-harness/commit/f65f415), and [`63510ac`](https://github.com/hoangnb24/repository-harness/commit/63510ac)—produced the current **32-line** file.

The important addition is the authority check:

> Before editing, identify repository authority for each new externally observable policy. If materially different choices remain open, stop before edits; configurable defaults are not authority.

This prevents an agent from converting an unresolved product decision into code merely because it can invent a reasonable default.

The current file also defines completion in terms of evidence rather than confidence:

- executable or observable proof
- changed surfaces
- validation performed
- unresolved risks

That is the endpoint of the evolution: not a bigger instruction manual, but a smaller set of high-leverage decisions.

## Five design lessons from the history

### 1. Make `AGENTS.md` a router, not a warehouse

The file should contain the minimum context needed to choose the correct path. Detailed architecture, release procedures, test matrices, and tool catalogs should live in their own authoritative documents.

A useful routing instruction says:

```md
Read docs/WORKFLOW.md, then only the product, design,
code, and validation material relevant to the task.
```

A warehouse instruction copies all of those documents into the root file. That increases context load and creates drift.

For a practical starting structure, use the [AGENTS.md template](/agents-md-template/) and keep the root file focused on orientation, boundaries, validation, and handoff.

### 2. Classify outcomes before classifying implementation work

Many instruction files begin with branch names, test commands, and coding conventions. They skip a more basic question: **is this request asking for a repository change at all?**

The repository-harness history converged on outcome-first routing:

| Requested outcome | Default behavior |
|---|---|
| Answer, explanation, review, diagnosis, plan, status | Read-only inspection |
| Bounded build, fix, or change | Ephemeral plan plus relevant validation |
| Multi-session or dependency-heavy work | Durable plan with recovery and handoff |
| Unresolved product policy | Pause before editing |

That one classification prevents unnecessary writes, unnecessary process, and unauthorized defaults.

### 3. Keep process proportional to task size

A heavy control plane can be valuable for long-running work and harmful for a one-file fix.

The current split preserves both:

- fast execution for bounded changes
- durable state for work that actually needs coordination or recovery

The trigger should be complexity, not habit. If a task can be inspected, changed, validated, and handed back in one bounded session, a durable story or database record may add more ceremony than safety.

### 4. Turn critical prose into repository checks

Some instructions are too important to remain advisory.

The request-authority change updated not only `AGENTS.md` but also installer assets, Claude-specific shims, documentation, and tests such as `tests/installer/assert-agent-authority-contract.sh`.

That pattern matters because generated instruction files drift. If the installer can refresh or create `AGENTS.md`, repository tests should verify that the generated block retains the authority and validation rules.

A practical test can assert that installed instructions contain:

- the read-only outcome rule
- the bounded-change path
- the durable-plan trigger
- pause conditions
- evidence-based completion language

### 5. Optimize for fewer wrong decisions, not fewer lines

The shortest version in this history was 15 lines, but the current 32-line version is stronger.

It grew because it added missing decisions:

- read-only versus mutating outcomes
- ephemeral versus durable planning
- authority for externally observable policy
- stop conditions
- evidence requirements

Line count is a maintenance signal, not the objective. A good revision removes duplicated detail and adds decision rules that prevent costly mistakes.

## A before-and-after method for your repository

You can apply the same reasoning without copying repository-harness verbatim.

### Step 1: inspect the current entry point

Mark every line as one of:

- outcome classification
- workflow routing
- repository map
- validation rule
- safety or authority boundary
- handoff requirement
- duplicated documentation
- tool-specific detail

Duplicated documentation and tool-specific detail are the first candidates to move behind links.

### Step 2: find repeated agent mistakes

Review recent coding-agent sessions and pull-request feedback. Look for repeated failures such as:

- editing after a read-only request
- choosing a product default without authority
- loading the entire repository before a small task
- running the wrong validation command
- creating durable state for trivial changes
- skipping a plan for multi-session work
- claiming completion without evidence

Every repeated failure should map to a concise decision rule, a stronger source-of-truth link, or an executable check.

The [agent-readiness audit](/blog/audit-repo-agent-readiness/) provides a 100-point checklist for finding these gaps systematically.

### Step 3: separate stable rules from changing detail

Keep stable decisions in `AGENTS.md`:

- what outcomes permit edits
- when to pause
- how to choose a workflow
- what counts as complete

Move changing detail elsewhere:

- exact architecture maps
- release procedures
- long test matrices
- tool catalogs
- feature-specific plans

Then link to the authoritative source.

### Step 4: test the routing with three tasks

Use a fresh agent session for each:

1. **Read-only:** “Review this module and identify risks.”
2. **Bounded change:** “Fix this parser bug and run the focused tests.”
3. **Durable work:** “Migrate the persistence layer across several packages with a rollback plan.”

Check whether the agent chooses the correct path without extra prompting.

### Step 5: version and maintain the contract

Treat `AGENTS.md` as code:

- review its diff
- link changes to the failure or workflow change that motivated them
- test generated copies or installer blocks
- remove stale pointers
- revisit it when commands, architecture, or authority changes

The guide to [maintaining AGENTS.md as your repository evolves](/blog/maintain-agents-md/) includes a release-based and monthly review cadence.

## A compact target shape

A mature root instruction file often needs only six sections or ideas:

```md
# Agent Instructions

## Start
Read the workflow and only task-relevant sources of truth.

## Outcome classification
Keep analysis and review read-only. Mutate only when explicitly requested.

## Bounded changes
Inspect, implement, and run behavior-appropriate validation.

## Durable work
Create a versioned plan when work spans sessions or needs recovery.

## Authority and safety
Pause for unresolved product choices, irreversible actions, or weakened proof.

## Handoff
Report outcome, changed surfaces, validation, skipped checks, and risks.
```

Your repository map and commands may add a few more lines. The shape matters more than the exact wording.

## What this case study does not prove

Repository history can show:

- which rules changed
- when the file expanded or contracted
- whether rules moved into canonical docs
- whether critical contracts gained tests
- whether the current entry point distinguishes task types

It cannot prove, without controlled measurements, that the new file made agents a specific percentage faster or reduced defects by a specific amount.

Measure those outcomes in your own repository:

- wrong-workflow selections per session
- edits made after read-only requests
- repeated clarifying questions
- validation commands omitted
- review rework caused by hidden conventions
- stale instruction failures
- time spent loading irrelevant context

The right objective is fewer avoidable surprises, not a prettier instruction file.

## Where repository-harness fits

[repository-harness](https://github.com/hoangnb24/repository-harness) packages the patterns behind this evolution for Claude Code, Codex, Cursor, and other coding agents.

Use it to bootstrap an entry point, durable repository context, planning boundaries, validation expectations, and evidence-based handoffs—then adapt those pieces to the actual authority and workflows in your repository.

## Related pages

- [What Is an Agent-Ready Repository?](/agent-ready-repository/)
- [How to Audit a Repository for Agent-Readiness](/blog/audit-repo-agent-readiness/)
- [Agent-Readiness vs Code Quality](/blog/agent-readiness-vs-code-quality/)
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/)
- [How to Maintain AGENTS.md](/blog/maintain-agents-md/)
- [10 Real-World AGENTS.md Examples](/blog/agents-md-examples/)
- [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness)

---

## FAQ

### What changed in the repository-harness AGENTS.md?

It changed from a 75-line operating manual that duplicated workflow detail into a 32-line routing layer. The current file classifies read-only outcomes, bounded changes, and durable work; identifies when to pause; requires evidence before completion; and links to deeper repository sources of truth.

### Should AGENTS.md contain the entire development workflow?

Usually not. `AGENTS.md` should make the first decisions clear and route agents to authoritative workflow, architecture, validation, and planning documents. Duplicating the whole workflow creates drift and increases the amount of context every session must load.

### Is a shorter AGENTS.md always better?

No. Shorter is useful only when the removed detail still exists in clear, linked sources of truth. The goal is not the fewest lines; it is the smallest entry point that lets an agent choose the correct workflow without guessing.

### What are authority rules in AGENTS.md?

Authority rules tell an agent which requests permit edits, which outcomes must remain read-only, when product intent is still unresolved, and when the agent must pause before an irreversible or weakly validated action. They prevent a plausible implementation from becoming an unauthorized one.

### How should AGENTS.md handle small tasks and multi-session work?

Use a lightweight path for bounded changes and a durable plan for work that spans sessions, has dependencies, needs coordination, or requires recovery steps. A single heavy workflow for every task creates unnecessary state and slows simple changes.

### How often should AGENTS.md be revised?

Revise it when the repository's canonical commands, workflow, authority model, validation requirements, planning system, or generated-file boundaries change. Review it during releases and after repeated agent mistakes reveal a missing or misleading rule.

### Can I copy the repository-harness AGENTS.md directly?

Use it as a pattern, not a drop-in file. Keep the outcome classification, pause conditions, evidence requirement, and routing structure, but replace every linked document and workflow rule with the sources of truth in your own repository.
