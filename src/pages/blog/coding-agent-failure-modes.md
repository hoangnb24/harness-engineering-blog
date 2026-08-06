---
layout: ../../layouts/MarkdownLayout.astro
title: "Coding-Agent Failure Modes: A Taxonomy for Diagnosing Repository Context Gaps"
description: "A practical taxonomy of coding-agent failure modes, from wrong-task execution and source-of-truth mistakes to validation gaps, context drift, and unsafe recovery."
target_keyword: "coding agent failure modes"
secondary_keywords:
  - "AI coding agent failures"
  - "coding agent debugging"
  - "repository context failure"
  - "why coding agents make mistakes"
  - "coding agent reliability"
  - "context engineering failure modes"
  - "AGENTS.md failure diagnosis"
status: "published"
date: "2026-08-04"
image: /assets/context-hero.jpg
tags:
  - Context Engineering
  - Coding Agents
  - How-to
  - English
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What are the most common coding-agent failure modes?","acceptedAnswer":{"@type":"Answer","text":"The most common failure modes are wrong-outcome execution, authority confusion, orientation failure, source-of-truth mistakes, scope leakage, context loss, decision-history loss, validation gaps, stale instructions, and unsafe recovery after partial writes."}},{"@type":"Question","name":"Why do coding agents make plausible but wrong changes?","acceptedAnswer":{"@type":"Answer","text":"Coding agents often make plausible but wrong changes when generic model knowledge fills a gap that the repository should have resolved with local instructions, code maps, contracts, decision records, or validation evidence."}},{"@type":"Question","name":"How do I find the root cause of a coding-agent failure?","acceptedAnswer":{"@type":"Answer","text":"Find the first wrong decision, not the final bad diff. Record what the agent believed, which evidence it had, which source should have controlled the decision, and what check could have detected the divergence earlier."}},{"@type":"Question","name":"Should every coding-agent mistake become an AGENTS.md rule?","acceptedAnswer":{"@type":"Answer","text":"No. Task-specific ambiguity belongs in the task, temporary discoveries belong in session state, package rules belong near the package, accepted tradeoffs belong in decision records, and only durable cross-repository operating rules belong in root AGENTS.md."}},{"@type":"Question","name":"How can a repository prevent repeated coding-agent failures?","acceptedAnswer":{"@type":"Answer","text":"Encode the missing constraint in the narrowest authoritative source, route agents to it before the risky decision, pair prose with executable validation where possible, and reproduce the task in a fresh session."}},{"@type":"Question","name":"What is the difference between a model failure and a repository-context failure?","acceptedAnswer":{"@type":"Answer","text":"A model failure persists even when the agent receives clear local evidence and adequate tools. A repository-context failure occurs when controlling information is missing, ambiguous, stale, undiscoverable, or lower-authority than a misleading alternative."}},{"@type":"Question","name":"How should teams measure coding-agent reliability?","acceptedAnswer":{"@type":"Answer","text":"Track first-wrong-decision categories, repeated fresh-session failures, validation escape rate, human correction frequency, unsafe action attempts, recovery success after interruption, and whether repository fixes prevent recurrence."}}]}</script>

# Coding-Agent Failure Modes: A Taxonomy for Diagnosing Repository Context Gaps

A coding-agent failure mode is a repeatable pattern in which an agent makes the wrong decision because the task, repository, tool state, or validation system did not provide an authoritative path to the right one.

The visible symptom may be a broken test, an over-broad diff, a direct edit to generated code, or a confident explanation of the wrong architecture. Those are outcomes. The useful diagnosis starts earlier: **what was the first wrong decision, and what should have prevented it?**

This taxonomy turns “the agent got confused” into a concrete failure class with a repair location and a verification method. It extends the [five layers of coding-agent context](/blog/five-layers-coding-agent-context/) from a context-placement model into an incident-analysis tool.

## The failure chain

Most agent failures follow the same causal chain:

1. **A controlling fact is missing, ambiguous, stale, or undiscoverable.**
2. **The agent fills the gap with an inference.**
3. **The inference determines an action.**
4. **The action produces a plausible but locally wrong change.**
5. **Validation either catches the error late or lets it escape.**
6. **A human corrects the output without fixing the repository condition.**
7. **A fresh session repeats the failure.**

The fifth and sixth steps explain why a team can have good models, strong reviewers, and still pay for the same failure repeatedly. Review catches the symptom. Context engineering repairs the system that generated it.

<figure style="margin:2rem 0;padding:1.25rem;border:1px solid #d8d8d4;border-radius:12px;background:#fbfbfa;overflow-x:auto">
<svg viewBox="0 0 960 430" role="img" aria-labelledby="failure-taxonomy-title failure-taxonomy-desc" style="width:100%;min-width:760px;height:auto">
<title id="failure-taxonomy-title">Coding-agent failure modes organized by decision stage</title>
<desc id="failure-taxonomy-desc">A pipeline from intent to evidence with failure families under each stage: wrong outcome and authority confusion under intent, orientation and source-of-truth failures under discovery, scope and decision-history failures under execution, context loss and unsafe recovery under state, and validation gaps and stale instructions under evidence.</desc>
<defs><marker id="failure-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#787774"/></marker></defs>
<g font-family="ui-sans-serif,system-ui,-apple-system" fill="#37352f">
  <text x="20" y="30" font-size="16" font-weight="700">DECISION PIPELINE</text>
  <g font-size="15" font-weight="700">
    <rect x="20" y="50" width="150" height="54" rx="9" fill="#dbeafe" stroke="#93c5fd"/><text x="70" y="83">INTENT</text>
    <rect x="210" y="50" width="150" height="54" rx="9" fill="#e0f2fe" stroke="#7dd3fc"/><text x="243" y="83">DISCOVERY</text>
    <rect x="400" y="50" width="150" height="54" rx="9" fill="#dcfce7" stroke="#86efac"/><text x="432" y="83">EXECUTION</text>
    <rect x="590" y="50" width="150" height="54" rx="9" fill="#fef3c7" stroke="#fcd34d"/><text x="640" y="83">STATE</text>
    <rect x="780" y="50" width="150" height="54" rx="9" fill="#f3e8ff" stroke="#c4b5fd"/><text x="820" y="83">EVIDENCE</text>
  </g>
  <g stroke="#787774" stroke-width="2" marker-end="url(#failure-arrow)"><line x1="170" y1="77" x2="202" y2="77"/><line x1="360" y1="77" x2="392" y2="77"/><line x1="550" y1="77" x2="582" y2="77"/><line x1="740" y1="77" x2="772" y2="77"/></g>
  <g font-size="14">
    <rect x="20" y="142" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="35" y="171" font-weight="700">Wrong outcome</text><text x="35" y="194">solves a different task</text>
    <rect x="20" y="236" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="35" y="265" font-weight="700">Authority confusion</text><text x="35" y="288">acts without permission</text>
    <rect x="210" y="142" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="225" y="171" font-weight="700">Orientation failure</text><text x="225" y="194">starts in the wrong place</text>
    <rect x="210" y="236" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="225" y="265" font-weight="700">Source-of-truth error</text><text x="225" y="288">edits derived output</text>
    <rect x="400" y="142" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="415" y="171" font-weight="700">Scope leakage</text><text x="415" y="194">expands the diff</text>
    <rect x="400" y="236" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="415" y="265" font-weight="700">Decision-history loss</text><text x="415" y="288">reverses a local choice</text>
    <rect x="590" y="142" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="605" y="171" font-weight="700">Context loss</text><text x="605" y="194">forgets session state</text>
    <rect x="590" y="236" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="605" y="265" font-weight="700">Unsafe recovery</text><text x="605" y="288">replays partial writes</text>
    <rect x="780" y="142" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="795" y="171" font-weight="700">Validation gap</text><text x="795" y="194">reports weak proof</text>
    <rect x="780" y="236" width="150" height="76" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="795" y="265" font-weight="700">Instruction drift</text><text x="795" y="288">follows stale guidance</text>
  </g>
  <text x="20" y="362" font-size="15" font-weight="700">ROOT-CAUSE RULE</text>
  <text x="20" y="392" font-size="14">Fix the earliest failed decision stage. A later test or reviewer may catch the symptom, but it cannot make the missing context discoverable next time.</text>
</g>
</svg>
</figure>

## Ten coding-agent failure modes

### 1. Wrong-outcome execution

**Symptom:** The agent performs technically competent work that does not satisfy the requested outcome. It edits when asked to review, implements when asked to investigate, or optimizes a component when the task was to explain its behavior.

**First wrong decision:** Misclassifying the task type.

**Typical cause:** The task says what topic to inspect but does not state the expected deliverable or mutation authority. The agent treats access to write tools as permission to use them.

**Repair location:** Task context. State the outcome class: answer, investigate, review, plan, bounded change, or durable multi-step work. If the confusion recurs across many tasks, add an outcome-classification rule to the repository workflow.

**Verification:** Repeat a review-only request in a clean worktree. The agent should produce findings while `git status --short` remains empty.

### 2. Authority confusion

**Symptom:** The agent crosses a permission boundary: pushes a branch, edits a generated secret-bearing configuration, posts publicly, deletes an artifact, or changes a migration despite being asked only to prepare a plan.

**First wrong decision:** Treating capability as authorization.

**Typical cause:** Permissions are implicit, scattered, or phrased as general caution rather than explicit stop conditions.

**Repair location:** Put task-specific authority in the request and durable safety boundaries in root or scoped repository instructions. Name which actions are autonomous, which require approval, and what safe artifact to produce when approval is unavailable.

**Verification:** Give the agent a task whose best final step is approval-gated. It should stop at a patch, branch, draft, or command kit instead of crossing the boundary.

### 3. Repository orientation failure

**Symptom:** The agent starts in the wrong package, copies an obsolete example, runs commands from the wrong directory, or spends most of the session rediscovering entry points.

**First wrong decision:** Choosing an exploration path without a reliable repository map.

**Typical cause:** The README describes the product for users but not the codebase for maintainers. Root instructions list rules without routing work by subsystem or change type.

**Repair location:** A concise repository map linked from root `AGENTS.md`: major directories, ownership boundaries, canonical entry points, and where different change types begin.

**Verification:** Ask a fresh agent where it would implement one representative change per subsystem. It should name the correct starting files and validation paths before editing.

### 4. Source-of-truth error

**Symptom:** The agent edits generated code, compiled output, vendored files, copied configuration, or a downstream manifest instead of the source that produces it.

**First wrong decision:** Misidentifying an editable artifact as authoritative.

**Typical cause:** Generated and source files look equally legitimate. The generator, source path, and regeneration command are not colocated or enforced.

**Repair location:** Scoped instructions beside the affected path. Name the authoritative source, the generated outputs, the regeneration command, and the clean-tree or contract check that proves synchronization.

**Verification:** Request a behavior change represented in generated output. The agent should edit the source, run the generator, and report both source and generated diffs.

The [prompt-only context failure guide](/blog/why-coding-agent-prompts-fail/) uses this exact generated-client pattern to show why a reminder in one prompt is not a durable repair.

### 5. Scope leakage

**Symptom:** A one-file fix grows into a broad refactor, dependency upgrade, formatting sweep, or architecture cleanup. The extra work may be reasonable but increases review cost and risk.

**First wrong decision:** Expanding the task boundary without evidence that the requested outcome requires it.

**Typical cause:** The repository rewards cleanliness but does not define how to handle adjacent defects, pre-existing failures, or tempting cleanup.

**Repair location:** Workflow instructions. Require the smallest causal change, separate pre-existing failures from introduced ones, and route unrelated improvements into follow-up notes or issues.

**Verification:** Seed a task next to an obvious unrelated cleanup opportunity. The resulting diff should stay focused and mention the adjacent issue without modifying it.

### 6. Decision-history loss

**Symptom:** The agent removes a compatibility adapter, reintroduces a rejected dependency, changes an intentionally odd data shape, or “simplifies” a boundary that protects an external contract.

**First wrong decision:** Treating an unexplained local pattern as accidental complexity.

**Typical cause:** Code records what exists but not why it exists. The rationale is trapped in a closed pull request, chat, or maintainer memory.

**Repair location:** A short decision record with context, decision, rationale, rejected alternatives, and reopening conditions. Link it from the architecture map or scoped instructions that govern the affected area.

**Verification:** Ask a fresh agent to refactor near the surprising pattern. It should discover the record and preserve the constraint unless the reopening condition is satisfied.

### 7. Session-context loss

**Symptom:** The agent repeats searches, forgets a failed command, contradicts an earlier conclusion, loses a user correction, or resumes a multi-step change from an outdated assumption.

**First wrong decision:** Continuing from incomplete or stale working state.

**Typical cause:** Important discoveries live only in transient chat history. Long work has no durable plan, checkpoint, dependency graph, or evidence log.

**Repair location:** Session state for short work; versioned active plans or checkpoint files for work that must survive context compaction, interruption, or another agent.

**Verification:** Interrupt the workflow after a meaningful discovery. Resume in a fresh session using only repository state. The agent should continue without repeating completed work or reviving disproven hypotheses.

### 8. Unsafe partial-write recovery

**Symptom:** After interruption, the agent reruns a migration, release, installer, or write-capable workflow and duplicates an external action, overwrites valid state, or leaves the system between checkpoints.

**First wrong decision:** Assuming “step not recorded complete” means “step did not happen.”

**Typical cause:** The system journals intentions but cannot distinguish before-write, after-write-before-checkpoint, and fully committed states. Recovery is designed as replay rather than inference plus idempotent continuation.

**Repair location:** The workflow and its persistence model, not just documentation. Record operation identifiers, preconditions, postconditions, and enough state to probe whether the external mutation already happened. Make recovery safe to invoke repeatedly.

**Verification:** Inject failure at every mutation-to-checkpoint boundary. Reload persisted state and run recovery twice. The final state should match one uninterrupted execution with no duplicate side effects.

This failure mode matters most for coding agents because they increasingly operate release automation, migrations, installers, and repository-writing workflows—not only source files.

### 9. Validation-evidence gap

**Symptom:** The agent says “tests pass” after running a narrow unit test, reports a build without checking generated output, or hands back a change with no evidence for the risky behavior it modified.

**First wrong decision:** Selecting proof that does not cover the changed contract.

**Typical cause:** Instructions say “run relevant tests” instead of mapping change types and risk surfaces to exact checks. Passing commands are treated as the goal rather than evidence for a claim.

**Repair location:** A validation matrix that maps change categories to focused tests, integration checks, builds, static analysis, generated-file checks, and human-review gates. Handoffs should name commands run, results, skipped checks, and residual risks.

**Verification:** Compare each implementation claim with the command that supposedly proves it. If the command could pass while the claim is false, the evidence is insufficient.

The [100-point repository agent-readiness audit](/blog/audit-repo-agent-readiness/) includes validation and handoff criteria for detecting this gap before it causes an escape.

### 10. Instruction drift and conflict

**Symptom:** The agent follows a documented command that no longer exists, reads two contradictory setup paths, uses a renamed package, or obeys a broad root rule that conflicts with current scoped instructions.

**First wrong decision:** Trusting a stale or ambiguously authoritative source.

**Typical cause:** Repository guidance is added but not maintained. Commands are copied into several files, owners are unclear, and CI verifies code without verifying operating documentation.

**Repair location:** Consolidate each rule into one authoritative source, link instead of copy, define scope and precedence, assign review triggers, and test critical commands or generated templates in CI.

**Verification:** Run the instructions from a clean checkout. Compare documented paths and commands against repository state. Confirm that scoped rules override general guidance where intended.

The guide to [maintaining AGENTS.md as a repository evolves](/blog/maintain-agents-md/) lists the toolchain, layout, validation, deployment, and ownership changes that should trigger a context review.

## Fast triage matrix

Use the symptom to choose the first place to investigate. Do not start by adding more prose.

| Observed symptom | Likely failure mode | Inspect first | Durable repair |
|---|---|---|---|
| Agent changed code during a review | Wrong outcome or authority confusion | Task wording and mutation permission | Explicit outcome class and approval boundary |
| Agent began in the wrong package | Orientation failure | Root router and repo map | Change-type-to-entry-point map |
| Agent edited compiled or generated output | Source-of-truth error | Scoped path instructions | Source + generator + sync check |
| Small fix became a large refactor | Scope leakage | Workflow and handoff policy | Smallest-causal-change rule |
| Agent removed an intentional adapter | Decision-history loss | ADRs and compatibility docs | Decision record with reopening condition |
| Agent repeated work after interruption | Session-context loss | Plan and checkpoint state | Durable progress/evidence record |
| Retried release created duplicates | Unsafe recovery | Journal and external state probe | Idempotent resume protocol |
| “Tests pass” did not cover the bug | Validation gap | Validation matrix | Claim-to-proof mapping |
| Fresh setup follows obsolete commands | Instruction drift | Duplicated docs and CI | One source, review triggers, executable checks |

## How to analyze a coding-agent incident

### Step 1: Preserve the evidence

Before correcting the agent, capture:

- the exact task or issue text
- repository state and relevant commit
- instructions the agent actually read
- tool calls and command results
- the first unexpected action
- the final diff and validation evidence
- any human correction that changed the path

Do not rely on a summary written after the fix. The agent’s first interpretation is the most useful evidence for locating the gap.

### Step 2: Name the first wrong decision

Avoid broad labels such as “hallucination,” “bad reasoning,” or “ignored instructions.” Write an observable decision:

- classified a review as an implementation task
- selected `dist/client.ts` as the editable source
- assumed the adapter was accidental
- treated a failed checkpoint as proof that the external write did not occur
- used unit tests as evidence for an integration contract

If you cannot name the decision, you are not yet at the root cause.

### Step 3: Identify the missing controller

Ask which source should have controlled that decision:

- task acceptance criteria
- explicit permission boundary
- repository map
- scoped `AGENTS.md`
- architecture contract
- decision record
- active plan or checkpoint
- validation matrix
- live system state

Then ask why it failed: absent, ambiguous, stale, undiscoverable, duplicated, or lower-authority than another source.

### Step 4: Repair the narrowest authoritative layer

A package-local generator rule should not inflate root `AGENTS.md`. A one-ticket constraint should not become permanent architecture. A recovery bug needs state-machine work, not a warning paragraph.

Use this placement rule:

> Put information where it becomes true, changes, and can be verified.

That usually keeps task facts in tasks, local rules near local code, rationale in decision records, and proof requirements in validation infrastructure.

### Step 5: Add the earliest useful detector

Prevention is ideal, but early detection still reduces cost. Examples:

- task classifier before mutation
- generated-file cleanliness check before review
- forbidden-dependency rule at package boundaries
- plan checkpoint before context compaction
- external-state probe before retrying a write
- focused contract test before the full suite
- documentation command check in CI

The detector should fail near the first wrong decision, not after the bad diff has propagated.

### Step 6: Reproduce in a fresh session

A corrected current session proves little because it contains the human explanation. Start clean. Provide the original task, current repository, and normal entry instructions—without the corrective prompt.

The repair is durable only if the fresh agent:

1. finds the controlling source
2. makes the corrected decision before editing
3. runs the appropriate proof
4. reports the evidence and remaining uncertainty

## What not to do

### Do not add every lesson to root AGENTS.md

A root file that accumulates every incident becomes a low-signal documentation warehouse. Agents must scan unrelated history, scoped exceptions become invisible, and stale instructions gain accidental authority.

Use root instructions as a router. Put detail near the decision it controls.

### Do not confuse a caught failure with a prevented failure

A reviewer catching a bad generated-file edit is evidence that review works. It is not evidence that the repository is agent-ready. If the next fresh agent can repeat the same mistake, the context gap remains.

### Do not blame the model before checking local evidence

Model limits are real. But “the model should have known” is weak incident analysis when the answer is repository-specific. First verify that the agent could discover current, unambiguous local evidence and had the tools to act on it.

A likely model failure is one that persists after the repository provides the right source at the right time, the agent reads it, and the task stays within the model’s capabilities.

### Do not make prose carry a mechanical invariant

If duplicate release publication is unacceptable, build idempotency and external-state checks. If generated output must stay synchronized, run the generator in CI. If a dependency boundary matters, test it.

Prose can route and explain. Enforcement should carry invariants when the repository can express them mechanically.

## Build a failure-mode feedback loop

A repository improves when incidents become structured input instead of one-off frustration.

Maintain a lightweight log with:

| Field | Example |
|---|---|
| First wrong decision | Edited generated client directly |
| Failure mode | Source-of-truth error |
| Missing controller | Scoped API instructions |
| Cause | Generator and source path undiscoverable |
| Repair | Added `api/AGENTS.md` and regeneration check |
| Detector | CI fails on dirty generated diff |
| Fresh-session result | Agent edited schema and regenerated client |
| Recurrence | 0 in next 10 matching tasks |

The log should not become a blame ledger. Its purpose is to show which repository surfaces produce repeated failures and whether repairs actually reduce recurrence.

Useful reliability measures include:

- failures per task by taxonomy class
- repeated fresh-session failures
- human corrections before first edit
- scope-expansion rate
- validation escapes found in review or CI
- unsafe action attempts
- successful resume rate after interruption
- recurrence after a repository-context repair

The strongest metric is not “the agent succeeded after correction.” It is “the next agent did not need the correction.”

## A compact incident checklist

After a failed coding-agent session, ask:

- [ ] What was the first wrong decision?
- [ ] Which failure mode best describes it?
- [ ] What evidence did the agent have at that moment?
- [ ] Which source should have controlled the decision?
- [ ] Was that source absent, stale, ambiguous, duplicated, or undiscoverable?
- [ ] Does the repair belong in the task, session state, repository instructions, decision history, workflow state, or validation system?
- [ ] Can a mechanical check detect the failure earlier?
- [ ] Can recovery be invoked twice without duplicating side effects?
- [ ] Does a fresh session find and follow the repair without a corrective prompt?
- [ ] Will the repository delete or update the rule when its underlying condition changes?

## Turn agent mistakes into repository improvements

Coding-agent reliability does not come from eliminating every mistake. It comes from making failures classifiable, their controlling evidence discoverable, and their recurrence testable.

Start with one recent bad session. Find the first wrong decision. Assign a failure mode. Repair the narrowest authoritative source. Add the earliest useful detector. Then rerun the original task without replaying the correction.

[repository-harness](https://github.com/hoangnb24/repository-harness) provides a practical starting point for repository instructions, workflow boundaries, validation maps, durable plans, and evidence-based handoffs across Claude Code, Codex, Cursor, and other coding agents.

## Related pages

- [Repository Harness Patterns](/blog/repository-harness-patterns/) — composable controllers for recurring failure classes
- [The Five Layers of Coding-Agent Context](/blog/five-layers-coding-agent-context/)
- [Why Coding-Agent Prompts Fail When Context Lives Only in Prompts](/blog/why-coding-agent-prompts-fail/)
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/)
- [How to Audit a Repository for Agent-Readiness](/blog/audit-repo-agent-readiness/)
- [Agent-Readiness vs Code Quality](/blog/agent-readiness-vs-code-quality/)
- [How to Maintain AGENTS.md as Your Repository Evolves](/blog/maintain-agents-md/)
- [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness)

---

## FAQ

### What are the most common coding-agent failure modes?

The most common failure modes are wrong-outcome execution, authority confusion, orientation failure, source-of-truth mistakes, scope leakage, context loss, decision-history loss, validation gaps, stale instructions, and unsafe recovery after partial writes.

### Why do coding agents make plausible but wrong changes?

Coding agents often make plausible but wrong changes when generic model knowledge fills a gap that the repository should have resolved with local instructions, code maps, contracts, decision records, or validation evidence.

### How do I find the root cause of a coding-agent failure?

Find the first wrong decision, not the final bad diff. Record what the agent believed, which evidence it had, which source should have controlled the decision, and what check could have detected the divergence earlier.

### Should every coding-agent mistake become an AGENTS.md rule?

No. Task-specific ambiguity belongs in the task, temporary discoveries belong in session state, package rules belong near the package, accepted tradeoffs belong in decision records, and only durable cross-repository operating rules belong in root `AGENTS.md`.

### How can a repository prevent repeated coding-agent failures?

Encode the missing constraint in the narrowest authoritative source, route agents to it before the risky decision, pair prose with executable validation where possible, and reproduce the task in a fresh session.

### What is the difference between a model failure and a repository-context failure?

A model failure persists even when the agent receives clear local evidence and adequate tools. A repository-context failure occurs when controlling information is missing, ambiguous, stale, undiscoverable, or lower-authority than a misleading alternative.

### How should teams measure coding-agent reliability?

Track first-wrong-decision categories, repeated fresh-session failures, validation escape rate, human correction frequency, unsafe action attempts, recovery success after interruption, and whether repository fixes prevent recurrence.
