---
layout: ../../layouts/MarkdownLayout.astro
title: "The Five Layers of Coding-Agent Context: A Diagnostic Framework"
description: "Learn the five context layers coding agents rely on, how context failures appear, and where task, session, repository, decision, and model knowledge belong."
target_keyword: "coding agent context layers"
secondary_keywords:
  - "AI coding agent context"
  - "context engineering layers"
  - "repository context for coding agents"
  - "coding agent context hierarchy"
  - "AGENTS.md context architecture"
  - "coding agent context failure"
  - "durable context vs session context"
status: "published"
date: "2026-07-28"
image: /assets/context-hero.jpg
tags:
  - Context Engineering
  - Coding Agents
  - How-to
  - English
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What are the five layers of coding-agent context?","acceptedAnswer":{"@type":"Answer","text":"The five layers are task context, session context, repository instructions, decision history, and model knowledge. They differ in lifetime, local authority, and how reliably a team can control them."}},{"@type":"Question","name":"Which context belongs in AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"AGENTS.md should contain or route to durable repository-level operating context: repository orientation, authority and safety boundaries, canonical workflows, validation commands, and handoff expectations. Task-specific acceptance criteria and temporary session notes do not belong there."}},{"@type":"Question","name":"What is the difference between task context and repository context?","acceptedAnswer":{"@type":"Answer","text":"Task context defines the requested outcome for one piece of work. Repository context defines the durable local rules for how work should be performed and validated across many tasks and sessions."}},{"@type":"Question","name":"How is session context preserved across coding-agent runs?","acceptedAnswer":{"@type":"Answer","text":"Preserve only the session state that future work truly needs by writing a durable plan, decision, checkpoint, or recovery note into the repository. Do not turn every observation from a temporary session into permanent documentation."}},{"@type":"Question","name":"Why should model knowledge have the lowest local authority?","acceptedAnswer":{"@type":"Answer","text":"Model knowledge contains useful general patterns but cannot prove how a specific repository works. Local code, tests, instructions, and recorded decisions should override generic conventions whenever they disagree."}},{"@type":"Question","name":"Can too much repository context make an agent worse?","acceptedAnswer":{"@type":"Answer","text":"Yes. Duplicated, stale, conflicting, or indiscriminate context makes authority harder to identify and consumes attention. Keep the root instructions concise, link to authoritative detail, and remove context that no longer changes agent decisions."}},{"@type":"Question","name":"How do I know which context layer caused a failure?","acceptedAnswer":{"@type":"Answer","text":"Capture the first wrong decision, then ask where the missing or ambiguous information should have been available. A one-ticket misunderstanding points to task context; a mid-run loop points to session context; a repeated fresh-session mistake points to repository instructions; a reversed architectural choice points to decision history; and an imported generic convention points to model knowledge."}}]}</script>

# The Five Layers of Coding-Agent Context: A Diagnostic Framework

A coding agent operates across five context layers—**task, session, repository instructions, decision history, and model knowledge**—and reliable behavior comes from moving durable constraints out of temporary or unpredictable layers into versioned repository sources of truth.

That is the diagnostic version of [context engineering for coding agents](/context-engineering-for-coding-agents/). When an agent makes a plausible but wrong change, “write a better prompt” is not automatically the fix. First identify which layer failed. Then put the missing information in the narrowest authoritative location that will prevent the failure from recurring.

## Diagnose the symptom before adding more context

Different failures point to different layers. This table is a fast starting point.

| Symptom | Likely failed layer | First place to inspect |
|---|---|---|
| The agent misunderstood this ticket | Task | Issue, request, acceptance criteria |
| The agent forgot discoveries or repeated work mid-run | Session | Current plan, notes, tool state, handoff |
| Every fresh session repeats the same mistake | Repository instructions | `AGENTS.md`, workflow docs, validation map |
| The agent reopens a settled architecture choice | Decision history | ADRs, compatibility contracts, resolved issue rationale |
| The agent applies a familiar convention that is wrong here | Model knowledge overriding local evidence | Local code, tests, explicit sources of truth |

The point is not to classify blame. The point is to locate the earliest place where correct information was absent, ambiguous, or lower-authority than a misleading alternative.

## The five-layer map

Each layer differs across four properties: what it contains, how long it lives, how much local authority it should carry, and what failure looks like.

<figure style="margin:2rem 0;padding:1.25rem;border:1px solid #d8d8d4;border-radius:12px;background:#fbfbfa;overflow-x:auto">
<svg viewBox="0 0 860 490" role="img" aria-labelledby="context-layers-title context-layers-desc" style="width:100%;min-width:680px;height:auto">
<title id="context-layers-title">Five coding-agent context layers by lifetime, scope, and local authority</title>
<desc id="context-layers-desc">A five-row diagram showing task context, session context, repository instructions, decision history, and model knowledge. Task and repository evidence have high local authority. Decision history has the longest durable lifetime. Model knowledge is broad but has the lowest local authority.</desc>
<defs>
  <linearGradient id="authority" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e9e9e7"/><stop offset="1" stop-color="#2383e2"/></linearGradient>
  <linearGradient id="lifetime" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9e9e7"/><stop offset="1" stop-color="#0f7b6c"/></linearGradient>
</defs>
<text x="18" y="34" font-size="15" font-weight="700" fill="#37352f">LOCAL AUTHORITY</text>
<rect x="30" y="56" width="10" height="350" rx="5" fill="url(#authority)"/>
<path d="M35 46 L27 61 H43 Z" fill="#2383e2"/>
<text x="52" y="71" font-size="13" fill="#55534e">increases toward explicit task and repository evidence</text>
<g font-family="ui-sans-serif,system-ui,-apple-system" fill="#37352f">
  <rect x="165" y="55" width="430" height="58" rx="10" fill="#dbeafe" stroke="#93c5fd"/><text x="185" y="81" font-size="17" font-weight="700">1. Task context</text><text x="185" y="101" font-size="13">narrow scope · one requested outcome · high explicit authority</text>
  <rect x="185" y="126" width="450" height="58" rx="10" fill="#e0f2fe" stroke="#7dd3fc"/><text x="205" y="152" font-size="17" font-weight="700">2. Session context</text><text x="205" y="172" font-size="13">current run · discoveries and working state · temporary</text>
  <rect x="205" y="197" width="490" height="58" rx="10" fill="#dcfce7" stroke="#86efac"/><text x="225" y="223" font-size="17" font-weight="700">3. Repository instructions</text><text x="225" y="243" font-size="13">project-wide · versioned · durable operating authority</text>
  <rect x="225" y="268" width="530" height="58" rx="10" fill="#fef3c7" stroke="#fcd34d"/><text x="245" y="294" font-size="17" font-weight="700">4. Decision history</text><text x="245" y="314" font-size="13">long-lived rationale · accepted tradeoffs · reopening conditions</text>
  <rect x="245" y="339" width="570" height="58" rx="10" fill="#f3f4f6" stroke="#c7c8ca"/><text x="265" y="365" font-size="17" font-weight="700">5. Model knowledge</text><text x="265" y="385" font-size="13">broadest scope · generic patterns · lowest local authority</text>
</g>
<text x="165" y="438" font-size="15" font-weight="700" fill="#37352f">LIFETIME AND DURABILITY</text>
<rect x="165" y="450" width="650" height="10" rx="5" fill="url(#lifetime)"/>
<path d="M826 455 L811 447 V463 Z" fill="#0f7b6c"/>
<text x="165" y="481" font-size="13" fill="#55534e">short-lived task/session state</text><text x="635" y="481" font-size="13" fill="#55534e">versioned, long-lived context</text>
</svg>
<figcaption style="margin-top:.75rem;color:#66645f;font-size:.95rem">Breadth is not authority. Model knowledge covers more domains, but explicit task authority and versioned local evidence should control repository work.</figcaption>
</figure>

These layers are an operational model, not five required files and not a universal description of every agent runtime. Use them to decide where context belongs and which source should win when two sources disagree.

### Layer 1 — Task context

**What it contains:** the requested outcome, acceptance criteria, scope, constraints, and explicit permissions for the current task.

**Lifetime:** one request or work item.

**Authority:** high for the desired outcome. A direct request to review is not permission to edit. A request to fix is not permission to redesign unrelated behavior.

**Failure signal:** the implementation may be competent, but it solves the wrong problem. An agent asked to assess a migration begins changing code. An agent asked for a focused fix performs a broad cleanup because the task boundary was vague.

Task context should stay task-specific. Do not put one ticket’s acceptance criteria into root `AGENTS.md`; clarify the ticket or create a task packet instead.

### Layer 2 — Session context

**What it contains:** files read, hypotheses tested, command results, errors observed, partial decisions, current plan, and unfinished work.

**Lifetime:** the current run unless deliberately externalized.

**Authority:** useful evidence, but provisional. A hypothesis discovered during exploration should not become permanent architecture guidance before it is verified.

**Failure signal:** loops, contradictory edits, repeated searches, forgotten command failures, or a handoff that forces the next session to rediscover everything.

Preserve session state only when the work must survive the session. A bounded one-file fix may need no durable plan. A cross-package migration with dependencies and rollback steps probably does.

### Layer 3 — Repository instructions

**What it contains:** durable operating rules: entry points, repository maps, workflow boundaries, canonical commands, generated-file rules, safety limits, and handoff expectations.

**Lifetime:** versioned across tasks, sessions, humans, and tools.

**Authority:** high for how work must proceed locally. This is where a repository says “regenerate this file; do not edit it,” “run this focused test for this path,” or “pause before changing a public contract.”

**Failure signal:** fresh agents repeatedly rediscover setup, edit the same wrong surface, choose inconsistent examples, skip required proof, or ask the same questions.

`AGENTS.md` should route to this operating context rather than duplicate all of it. The guide to [writing an AGENTS.md that actually works](/blog/how-to-write-agents-md/) shows how to keep the root file short without making it vague.

### Layer 4 — Decision history

**What it contains:** why a local constraint exists, alternatives that were rejected, compatibility promises, evidence behind a tradeoff, and the conditions that would reopen the decision.

**Lifetime:** long-lived rationale, updated when the decision changes.

**Authority:** high when it records an accepted local choice. Code shows what exists; decision history often explains why the obvious alternative was rejected.

**Failure signal:** an agent “improves” a design by undoing a deliberate compatibility choice, replacing a local adapter with a standard abstraction, or reopening a settled debate without new evidence.

A useful decision record is short: context, decision, rationale, rejected alternatives, and reopening conditions. It does not need to narrate every meeting.

### Layer 5 — Model knowledge

**What it contains:** general programming patterns, framework conventions, public APIs, common architectures, and learned expectations from outside the repository.

**Lifetime:** determined before the session and mostly outside the team’s control.

**Authority:** lowest for local facts. Model knowledge is a source of hypotheses, not proof of repository behavior.

**Failure signal:** an agent applies a popular convention despite local tests or documentation that establish a different rule. The answer looks familiar and reasonable but is wrong for this codebase.

Model knowledge is valuable precisely because it is broad. The mistake is allowing breadth to masquerade as local authority.

## The authority rule

When context sources disagree, use this practical precedence model:

1. **Explicit task authority** defines the requested outcome and whether mutation is authorized.
2. **Repository constraints** define how work may proceed safely and how it must be validated.
3. **Recorded decisions** explain why local choices differ from generic conventions and when they may change.
4. **Session inference** fills only the gaps that remain after reading local evidence.
5. **Model knowledge** proposes possibilities but never proves local behavior.

This is not a simple top-to-bottom override list. Task context cannot authorize violating a safety boundary that requires human review, and an old decision record should not overrule current code and tests after an intentional migration. Authority must be current, explicit, and relevant to the decision being made.

The durable rule is simpler: **generic inference must not overrule clear local evidence**.

## Context placement matrix

Use this matrix when deciding whether a new instruction belongs in the task, a plan, `AGENTS.md`, a deeper document, or nowhere permanent.

| Information | Correct layer | Recommended location | Avoid |
|---|---|---|---|
| Acceptance criteria for one issue | Task | Issue, story packet, request | Root `AGENTS.md` |
| Current failed command and hypothesis | Session | Current plan or checkpoint | Permanent docs before verification |
| Canonical build and test commands | Repository instructions | `AGENTS.md` router plus validation doc | Repeating them in every prompt |
| Generated-file edit rule | Repository instructions | Root or scoped instruction file plus a check | Relying on code shape alone |
| Why a public API cannot change | Decision history | ADR or compatibility contract | An unlinked comment with no authority |
| Generic framework pattern | Model knowledge | Verify against local code and docs | Treating it as repository fact |
| A migration that spans several sessions | Session promoted to durable state | Versioned active plan with recovery steps | Leaving the only state in chat history |
| A one-time release deadline | Task | Release issue or project tracker | Permanent architecture guidance |

The placement test has two useful questions:

- If the information changes per task, why would every future session need it?
- If every fresh session needs it, why is it still trapped in chat history or maintainer memory?

## Three failure walkthroughs

### Case A — Correct code, wrong task

A developer asks an agent to “review this migration plan and identify risks.” The agent reads the plan, then begins changing the migration scripts.

The code may even be correct. The failure happened before implementation: the agent treated a read-only outcome as mutation authority.

**Failed layer:** task context.

**Repair:** make the requested outcome explicit in the task, then encode a durable outcome-classification rule in repository instructions if the same confusion recurs. The real [repository-harness `AGENTS.md` before-and-after case study](/blog/agents-md-before-after-case-study/) shows how a root instruction file can distinguish answers, reviews, bounded changes, and durable work before an agent edits.

**Verification:** start a fresh session with a review-only request and confirm that the agent returns analysis without modifying repository state.

### Case B — The same mistake every fresh session

A generated API client lives beside handwritten source. Agents repeatedly edit the generated file directly because nothing identifies the generator or the source schema.

Correcting the prompt fixes one run. The next fresh session makes the same mistake.

**Failed layer:** repository instructions.

**Repair:** add a scoped rule that names the generated path, source file, regeneration command, and validation check. Link to it from the root router. Add a mechanical test when the boundary is important enough to enforce.

This is one reason [agent-readiness differs from code quality](/blog/agent-readiness-vs-code-quality/): clean generated code does not reveal whether it is an editable source of truth.

**Verification:** ask a fresh agent to change behavior represented in the client. Confirm that it edits the schema, regenerates the output, and reports the generated diff.

### Case C — The agent reopens a settled choice

A repository uses a small local adapter around a framework API. An agent sees the indirection, calls it unnecessary, and replaces it with the framework abstraction used in most public examples.

The adapter actually protects a compatibility promise and isolates a dependency version boundary. That rationale exists only in an old pull-request discussion.

**Failed layer:** decision history. Model knowledge filled the gap with a reasonable generic pattern.

**Repair:** record the accepted choice, its compatibility rationale, the rejected direct-framework option, and the conditions that would justify revisiting it. Link the record from the architecture map or relevant scoped instructions.

**Verification:** give a fresh agent a refactoring task near the adapter. Confirm that it finds the decision record and preserves the boundary unless the reopening condition is met.

## Repair workflow: diagnose before adding context

When an agent makes a wrong decision, do not immediately add a paragraph to `AGENTS.md`. Use this five-step loop.

### 1. Capture the first wrong decision

“Agent performed badly” is not actionable. Record the earliest concrete divergence:

- selected the wrong outcome type
- chose the wrong source file
- treated a generated artifact as editable
- skipped a required check
- reversed an accepted decision
- inferred a local convention from generic knowledge

Later errors may all be consequences of that first miss.

### 2. Identify the earliest failed layer

Ask where the correct information should have been available at the moment of the decision. If the ticket itself was ambiguous, fix the task. If the information was discovered and forgotten mid-run, fix session state. If every session needs the rule, make it durable. If the “why” is missing, write a decision record.

### 3. Put the fix in the narrowest authoritative location

A package-specific generated-file rule belongs near that package, not necessarily in the root file. A one-ticket deadline belongs in the issue, not an architecture document. A cross-repository safety boundary may belong in root instructions.

Narrow placement reduces irrelevant context and conflicting copies.

### 4. Link instead of duplicating

The root `AGENTS.md` should route an agent to the authoritative source at the moment it matters. It should not copy long architecture explanations, test matrices, release procedures, and decision histories into one file.

### 5. Reproduce in a fresh session

The repair is not complete because the prose sounds clear. Run a new task that exercises the same decision. Verify the agent discovers the right source, selects the right action, and produces the required evidence.

The [100-point repository agent-readiness audit](/blog/audit-repo-agent-readiness/) provides a broader checklist when failures span several layers.

## A minimum viable context architecture

The filenames are examples, not requirements. What matters is that authority is discoverable and each document has a clear job.

```text
AGENTS.md                 # router: authority, workflow, boundaries, validation links
docs/WORKFLOW.md          # task-sized execution and handoff rules
docs/ARCHITECTURE.md      # repository map and dependency boundaries
docs/decisions/           # accepted decisions and reopening conditions
docs/VALIDATION.md        # change type -> proof command
docs/plans/active/        # only work that must survive sessions
```

A small repository may combine several of these concerns. A large monorepo may add scoped `AGENTS.md` files or package-level validation docs. Do not measure maturity by file count. Measure whether a fresh agent can find the controlling information before it makes an expensive decision.

## Context-layer audit checklist

Use this compact audit against a real task:

- [ ] Can the agent distinguish analysis from permission to edit?
- [ ] Can it find acceptance criteria without inferring the desired outcome?
- [ ] Can a fresh session find the canonical setup and validation commands?
- [ ] Are generated, risky, vendored, or irreversible surfaces explicit?
- [ ] Can the agent find why a surprising local pattern exists?
- [ ] Does multi-session work have durable state, checkpoints, and recovery steps?
- [ ] Does root `AGENTS.md` route rather than duplicate deep documentation?
- [ ] Do local code and tests clearly outrank generic model assumptions?
- [ ] Can a repository test detect drift in critical installed instructions?
- [ ] Does the handoff name commands run, commands skipped, and unresolved risks?

A good context system does not eliminate agent mistakes. It makes the source of a mistake diagnosable and gives the repository a durable way to improve.

## Try the framework on your repository

Pick one repeated coding-agent failure. Identify the first wrong decision and the layer that should have prevented it. Move the missing information to the narrowest durable source of truth, link it from the right entry point, and rerun the task in a fresh session.

[repository-harness](https://github.com/hoangnb24/repository-harness) provides a practical starting system for repository instructions, context routing, validation, and evidence-based handoffs across Claude Code, Codex, Cursor, and other coding agents.

## Related pages

- [Why Coding-Agent Prompts Fail When Context Lives Only in Prompts](/blog/why-coding-agent-prompts-fail/)
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/)
- [AGENTS.md Before and After: A Real Repository Case Study](/blog/agents-md-before-after-case-study/)
- [Agent-Readiness vs Code Quality](/blog/agent-readiness-vs-code-quality/)
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/)
- [How to Audit a Repository for Agent-Readiness](/blog/audit-repo-agent-readiness/)
- [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness)

---

## FAQ

### What are the five layers of coding-agent context?

The five layers are task context, session context, repository instructions, decision history, and model knowledge. They differ in lifetime, local authority, and how reliably a team can control them.

### Which context belongs in AGENTS.md?

`AGENTS.md` should contain or route to durable repository-level operating context: repository orientation, authority and safety boundaries, canonical workflows, validation commands, and handoff expectations. Task-specific acceptance criteria and temporary session notes do not belong there.

### What is the difference between task context and repository context?

Task context defines the requested outcome for one piece of work. Repository context defines the durable local rules for how work should be performed and validated across many tasks and sessions.

### How is session context preserved across coding-agent runs?

Preserve only the session state that future work truly needs by writing a durable plan, decision, checkpoint, or recovery note into the repository. Do not turn every observation from a temporary session into permanent documentation.

### Why should model knowledge have the lowest local authority?

Model knowledge contains useful general patterns but cannot prove how a specific repository works. Local code, tests, instructions, and recorded decisions should override generic conventions whenever they disagree.

### Can too much repository context make an agent worse?

Yes. Duplicated, stale, conflicting, or indiscriminate context makes authority harder to identify and consumes attention. Keep the root instructions concise, link to authoritative detail, and remove context that no longer changes agent decisions.

### How do I know which context layer caused a failure?

Capture the first wrong decision, then ask where the missing or ambiguous information should have been available. A one-ticket misunderstanding points to task context; a mid-run loop points to session context; a repeated fresh-session mistake points to repository instructions; a reversed architectural choice points to decision history; and an imported generic convention points to model knowledge.
