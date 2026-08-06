---
layout: ../../layouts/MarkdownLayout.astro
title: "Repository Harness Patterns: A Pattern Language for Reliable Coding Agents"
description: "Nine reusable repository harness patterns for routing coding agents, bounding work, preserving decisions, validating changes, recovering safely, and producing evidence-based handoffs."
target_keyword: "repository harness patterns"
secondary_keywords:
  - "coding agent harness patterns"
  - "AI coding agent workflow patterns"
  - "repository harness engineering"
  - "agent-ready repository patterns"
  - "coding agent validation workflow"
  - "coding agent handoff pattern"
  - "durable coding agent context"
status: "published"
date: "2026-08-06"
image: /assets/harness-engineering-hero.jpg
tags:
  - Harness Engineering
  - Coding Agents
  - How-to
  - English
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is a repository harness pattern?","acceptedAnswer":{"@type":"Answer","text":"A repository harness pattern is a reusable arrangement of instructions, workflow state, validation, and evidence that helps coding agents make correct local decisions repeatedly. Each pattern names a recurring problem, the forces behind it, a durable repository-level solution, and a way to verify that the solution works in a fresh session."}},{"@type":"Question","name":"How is a repository harness different from AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"AGENTS.md is one surface inside a repository harness. A complete harness also includes task envelopes, authority boundaries, source-of-truth maps, validation contracts, decision records, checkpoints, safe recovery rules, and evidence-based handoffs. AGENTS.md should route agents to those sources rather than contain every detail."}},{"@type":"Question","name":"Which repository harness pattern should a team implement first?","acceptedAnswer":{"@type":"Answer","text":"Start with the smallest pattern that prevents the most frequent costly mistake. For many teams that is the task envelope, which defines outcome, scope, constraints, acceptance criteria, and validation. If agents regularly start in the wrong place, begin with the repository router instead."}},{"@type":"Question","name":"Do repository harness patterns depend on Claude Code, Codex, or Cursor?","acceptedAnswer":{"@type":"Answer","text":"No. The patterns are tool-agnostic because they live in repository files, executable checks, and workflow state. Tool-specific instruction files can act as adapters, while the authoritative maps, contracts, decisions, and validation commands remain shared."}},{"@type":"Question","name":"How do you test whether a coding-agent harness pattern works?","acceptedAnswer":{"@type":"Answer","text":"Reproduce a representative task in a fresh session without replaying the human correction. Verify that the agent discovers the controlling source before the risky decision, stays within scope, runs the required proof, and reports evidence. A current session succeeding after correction is not sufficient."}},{"@type":"Question","name":"Should every coding-agent failure create a new rule?","acceptedAnswer":{"@type":"Answer","text":"No. First classify the failure and repair the narrowest authoritative layer. One-task facts belong in the task envelope, package rules near the package, accepted tradeoffs in decision records, mechanical invariants in executable checks, and only durable cross-repository routing rules in root instructions."}},{"@type":"Question","name":"How should teams measure repository harness quality?","acceptedAnswer":{"@type":"Answer","text":"Track fresh-session success, human corrections before the first edit, scope expansion, validation escapes, repeated failure classes, successful resume after interruption, duplicate side effects during recovery, and whether each handoff contains claim-to-proof evidence."}}]}</script>

# Repository Harness Patterns: A Pattern Language for Reliable Coding Agents

A **repository harness pattern** is a reusable arrangement of instructions, workflow state, validation, and evidence that helps coding agents make correct local decisions repeatedly.

The point is not to produce more documentation. The point is to shape the repository so that the right action becomes discoverable before a risky decision, mechanically checkable after a change, and recoverable when a session stops halfway through.

This pattern language extends the [harness-engineering workflow](/harness-engineering-for-coding-agents/) into nine composable building blocks. Use it when a team knows its agent workflow is unreliable but “write a better prompt” is too vague to guide the repair.

## How to read a harness pattern

Each pattern has five parts:

- **Context:** the situation in which the problem appears
- **Problem:** the repeated failure the pattern addresses
- **Forces:** why the obvious fix is incomplete or creates another problem
- **Pattern:** the durable arrangement to add
- **Evidence:** how to prove it works without relying on the corrected session

Patterns are not templates to install blindly. They are responses to observed pressure. A small repository may need only three. A multi-package system with migrations and release automation may need all nine.

<figure style="margin:2rem 0;padding:1.25rem;border:1px solid #d8d8d4;border-radius:12px;background:#fbfbfa;overflow-x:auto">
<svg viewBox="0 0 1040 500" role="img" aria-labelledby="harness-pattern-title harness-pattern-desc" style="width:100%;min-width:820px;height:auto">
<title id="harness-pattern-title">Nine repository harness patterns arranged across the coding-agent workflow</title>
<desc id="harness-pattern-desc">The workflow moves from orientation through intent, execution, proof, and continuity. Patterns include repository router, task envelope, authority boundary, source-of-truth map, decision memory, validation contract, evidence handoff, durable checkpoint, and safe recovery protocol.</desc>
<defs><marker id="pattern-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#787774"/></marker></defs>
<g font-family="ui-sans-serif,system-ui,-apple-system" fill="#37352f">
  <text x="20" y="30" font-size="16" font-weight="700">CODING-AGENT WORKFLOW</text>
  <g font-size="15" font-weight="700">
    <rect x="20" y="54" width="170" height="54" rx="9" fill="#dbeafe" stroke="#93c5fd"/><text x="61" y="87">ORIENT</text>
    <rect x="225" y="54" width="170" height="54" rx="9" fill="#e0f2fe" stroke="#7dd3fc"/><text x="275" y="87">BOUND</text>
    <rect x="430" y="54" width="170" height="54" rx="9" fill="#dcfce7" stroke="#86efac"/><text x="477" y="87">CHANGE</text>
    <rect x="635" y="54" width="170" height="54" rx="9" fill="#fef3c7" stroke="#fcd34d"/><text x="685" y="87">PROVE</text>
    <rect x="840" y="54" width="170" height="54" rx="9" fill="#f3e8ff" stroke="#c4b5fd"/><text x="875" y="87">CONTINUE</text>
  </g>
  <g stroke="#787774" stroke-width="2" marker-end="url(#pattern-arrow)"><line x1="190" y1="81" x2="217" y2="81"/><line x1="395" y1="81" x2="422" y2="81"/><line x1="600" y1="81" x2="627" y2="81"/><line x1="805" y1="81" x2="832" y2="81"/></g>
  <g font-size="14">
    <rect x="20" y="148" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="34" y="178" font-weight="700">Repository router</text><text x="34" y="201">find the right starting point</text>
    <rect x="20" y="244" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="34" y="274" font-weight="700">Source-of-truth map</text><text x="34" y="297">find what may be edited</text>
    <rect x="225" y="148" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="239" y="178" font-weight="700">Task envelope</text><text x="239" y="201">define outcome and scope</text>
    <rect x="225" y="244" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="239" y="274" font-weight="700">Authority boundary</text><text x="239" y="297">separate access from permission</text>
    <rect x="430" y="148" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="444" y="178" font-weight="700">Decision memory</text><text x="444" y="201">preserve local rationale</text>
    <rect x="635" y="148" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="649" y="178" font-weight="700">Validation contract</text><text x="649" y="201">map claims to proof</text>
    <rect x="635" y="244" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="649" y="274" font-weight="700">Evidence handoff</text><text x="649" y="297">return reviewable results</text>
    <rect x="840" y="148" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="854" y="178" font-weight="700">Durable checkpoint</text><text x="854" y="201">resume from known state</text>
    <rect x="840" y="244" width="170" height="78" rx="9" fill="#fff" stroke="#b8b8b4"/><text x="854" y="274" font-weight="700">Safe recovery protocol</text><text x="854" y="297">continue without duplicate writes</text>
  </g>
  <rect x="20" y="370" width="990" height="88" rx="11" fill="#fff" stroke="#b8b8b4"/>
  <text x="40" y="402" font-size="15" font-weight="700">COMPOSITION RULE</text>
  <text x="40" y="430" font-size="14">Route to the controlling source → bound the change → preserve why → prove the contract → hand off evidence → checkpoint before interruption.</text>
</g>
</svg>
</figure>

## Pattern 1: Repository router

**Context:** A repository has multiple packages, services, generators, or validation paths. A fresh agent sees many plausible entry points.

**Problem:** The agent spends time rediscovering structure or starts in the wrong subsystem.

**Forces:** A full architecture document is too slow to scan before every task. A short root file cannot explain every package. Directory trees become stale when they are copied into several places.

**Pattern:** Make root `AGENTS.md` a router. Map representative change types to authoritative starting points, scoped instructions, and focused validation. Link to deeper maps instead of duplicating them.

```md
## Repository map
- API behavior → `services/api/AGENTS.md` → `make test-api`
- Web UI → `apps/web/AGENTS.md` → `npm run test:web`
- Database schema → `db/README.md` → `make migration-check`
- Generated clients → edit `schema/`, then run `make generate`
```

**Evidence:** Ask a fresh agent where it would begin four representative changes. It should identify the correct package, source file family, and first validation command before editing.

Use the [five layers of coding-agent context](/blog/five-layers-coding-agent-context/) to keep routing facts in the repository layer instead of repeating them in task prompts.

## Pattern 2: Task envelope

**Context:** A human requests a change in natural language.

**Problem:** The agent must infer the outcome type, scope, constraints, acceptance criteria, and proof.

**Forces:** A one-line prompt is fast but ambiguous. A heavyweight specification costs more than a small change deserves. The task must stay readable enough that both agent and reviewer use it.

**Pattern:** Wrap each non-trivial task in a compact envelope:

```md
## Outcome
Add retry visibility to the import job without changing retry policy.

## In scope
- expose attempt count in job status
- add focused API and UI tests

## Out of scope
- changing backoff values
- replacing the queue library

## Acceptance
- attempt count is visible while running and after failure
- existing job-status clients remain compatible

## Proof
- `make test-import-status`
- `npm run test -- job-status`
```

Scale the envelope with risk. A documentation fix may need one sentence and a lint command. A migration needs preconditions, rollback, and explicit human gates.

**Evidence:** Review the resulting diff against the envelope. Unrequested refactors, guessed acceptance criteria, and unexplained skipped checks indicate the boundary was not strong enough.

This is the operational version of the story packet described in the [harness-engineering pillar](/harness-engineering-for-coding-agents/).

## Pattern 3: Authority boundary

**Context:** The agent has tools capable of editing, deleting, pushing, publishing, deploying, or mutating external systems.

**Problem:** Capability is mistaken for permission.

**Forces:** Asking approval for every file edit destroys autonomy. Broad autonomy without named stop conditions creates unacceptable risk. Different tasks need different boundaries.

**Pattern:** Separate actions into three explicit classes:

- **Autonomous:** safe, reversible actions inside the task scope
- **Approval-gated:** irreversible, public, account-sensitive, or high-blast-radius actions
- **Forbidden:** actions the workflow must never perform

For every approval-gated action, define a safe fallback artifact: patch, branch, draft, migration plan, command kit, or deployment preview.

**Evidence:** Give the agent a task whose highest-value final step crosses a gate. It should finish the safe artifact, identify the exact pending action, and stop without repeated permission prompts.

Authority confusion is the second class in the [coding-agent failure-mode taxonomy](/blog/coding-agent-failure-modes/). The durable repair is a boundary, not a generic warning to “be careful.”

## Pattern 4: Source-of-truth map

**Context:** Source, generated output, compiled assets, copied manifests, fixtures, and external configuration coexist.

**Problem:** The agent edits a plausible downstream artifact instead of the source that controls it.

**Forces:** Generated files are useful to inspect and sometimes committed. Their headers may be missing. The generator command may live far from the output. A prose reminder cannot prove synchronization.

**Pattern:** For each derived artifact family, colocate or link four facts:

1. authoritative source
2. derived outputs
3. regeneration command
4. synchronization check

```md
## API client contract
- Edit: `schema/openapi.yaml`
- Generated: `clients/python/`, `clients/typescript/`
- Regenerate: `make generate-clients`
- Verify: `git diff --exit-code -- clients/`
```

Add mechanical checks where possible. The repository should reject a stale generated diff even if an agent misses the prose.

**Evidence:** Request a behavior change visible in generated output. The agent should edit the source, regenerate, and report both source and derived diffs.

## Pattern 5: Decision memory

**Context:** The code contains an unusual adapter, dependency, data shape, compatibility branch, or operational constraint.

**Problem:** A future agent treats intentional complexity as accidental and “simplifies” it away.

**Forces:** Comments explain local mechanics but rarely capture alternatives and reopening conditions. Pull-request discussion is hard to discover. Large architecture documents become archives rather than decision tools.

**Pattern:** Record the smallest decision that future work must preserve:

```md
# Keep the v1 event adapter

Status: accepted
Scope: `events/legacy/`
Decision: keep the adapter until partner traffic reaches zero.
Why: three external consumers still send the v1 envelope.
Rejected: forced migration; dual writes.
Reopen when: 30 days of telemetry shows zero v1 events.
```

Link the record from the scoped instructions or architecture map that governs the affected path.

**Evidence:** Ask a fresh agent to refactor near the surprising code. It should discover the rationale and preserve the constraint unless the reopening condition is met.

## Pattern 6: Validation contract

**Context:** The agent has changed code and must decide what “verified” means.

**Problem:** It runs a convenient command that can pass while the changed contract remains broken.

**Forces:** Full suites may be slow. Focused tests may miss integration behavior. Different changes carry different risk. “Run relevant tests” leaves proof selection implicit.

**Pattern:** Map change categories and claims to required evidence.

| Change category | Focused proof | Broader proof | Extra invariant |
|---|---|---|---|
| API response | contract test | service integration suite | generated clients clean |
| Migration | forward/backward test | database suite | rollback or restore verified |
| UI state | component test | production build | browser behavior checked |
| Release workflow | dry run | workflow test | published version not duplicated |
| Documentation command | command smoke test | link/build audit | clean-checkout compatibility |

Validation commands belong near the code or workflow they validate. Task envelopes select from that map; agents should not invent a proof strategy from scratch every session.

**Evidence:** For each handoff claim, ask whether the cited command could pass while the claim is false. If yes, the contract needs another check.

The [agent-readiness audit](/blog/audit-repo-agent-readiness/) includes validation and handoff criteria for finding this gap systematically.

## Pattern 7: Evidence handoff

**Context:** The agent finishes a task and returns control to a reviewer or another agent.

**Problem:** The handoff says what changed but not why it is correct, what was actually tested, or what remains uncertain.

**Forces:** Raw command logs are noisy. “All tests pass” is too vague. Reviewers need concise evidence without repeating the entire session.

**Pattern:** Return a structured evidence packet:

```md
## Outcome
Attempt count is visible in the API and UI.

## Changed
- API status schema and serializer
- UI job-status component
- focused contract and component tests

## Evidence
- `make test-import-status` — 18 passed
- `npm run test -- job-status` — 12 passed
- `npm run build` — success

## Not run
- full end-to-end suite; unrelated and 45 minutes

## Residual risk
- old mobile client ignores the new optional field; compatibility preserved
```

State exact commands and results. Separate skipped checks from failures. Tie residual risk to the changed contract.

**Evidence:** A reviewer should be able to decide whether proof is sufficient without reconstructing the agent’s terminal history.

## Pattern 8: Durable checkpoint

**Context:** Work spans context compaction, interruption, multiple sessions, or multiple agents.

**Problem:** The next session repeats exploration, revives disproven assumptions, or continues from stale state.

**Forces:** Chat history is transient. Detailed logs become expensive to read. A checkbox alone does not preserve the evidence behind a decision.

**Pattern:** Checkpoint the minimum state required to continue safely:

- intended outcome and current scope
- completed steps with evidence
- current repository and external state
- disproven hypotheses
- unresolved decisions and blockers
- exact next action and its prerequisites

Use versioned plans for durable repository work and workflow state for automation. Do not store secrets or ephemeral noise.

**Evidence:** Interrupt after a meaningful discovery and resume in a fresh session using only the repository and checkpoint. The new session should continue without repeating completed work or discarding a verified conclusion.

## Pattern 9: Safe recovery protocol

**Context:** A workflow can be interrupted between an external mutation and the checkpoint that records success.

**Problem:** Retrying duplicates a release, deployment, migration, payment, notification, or remote write.

**Forces:** “Not marked complete” does not mean “did not happen.” Blind replay is unsafe. Manual recovery does not scale. Documentation cannot make a non-idempotent operation safe.

**Pattern:** Design recovery around observation and idempotency:

1. assign a stable operation identifier
2. record preconditions before mutation
3. probe external state after interruption
4. distinguish not-started, applied-not-checkpointed, and complete states
5. continue from observed state
6. make repeated recovery converge on the same result

**Evidence:** Inject failure at every mutation-to-checkpoint boundary. Reload state and invoke recovery twice. The final system should match one uninterrupted execution with no duplicate side effects.

This is the pattern where prose is least sufficient. If the invariant is mechanical, the harness must enforce it mechanically.

## How the patterns compose

The patterns form a decision path rather than a pile of files:

1. The **repository router** finds the correct local surface.
2. The **task envelope** defines the requested outcome and proof.
3. The **authority boundary** determines which actions may proceed.
4. The **source-of-truth map** identifies what can be changed.
5. **Decision memory** preserves constraints that code alone cannot explain.
6. The **validation contract** selects evidence for the changed behavior.
7. The **evidence handoff** makes review possible without replaying the session.
8. A **durable checkpoint** preserves progress across interruption.
9. The **safe recovery protocol** prevents duplicate external effects.

A single artifact can participate in several patterns. Root `AGENTS.md` may route work and state durable authority boundaries. A story packet can serve as task envelope and select the validation contract. The important property is not the filename; it is that every risky decision has a discoverable controller and every completion claim has evidence.

## Choose patterns from observed failures

Do not begin by installing all nine. Start with a recent costly session and name the first wrong decision.

| Repeated symptom | Start with |
|---|---|
| Agent begins in the wrong package | Repository router |
| Correct topic, wrong deliverable | Task envelope |
| Agent pushes or deploys without permission | Authority boundary |
| Generated output edited directly | Source-of-truth map |
| Intentional adapter removed | Decision memory |
| “Tests pass” but behavior is broken | Validation contract |
| Reviewer reruns everything | Evidence handoff |
| Fresh session repeats exploration | Durable checkpoint |
| Retry duplicates a remote action | Safe recovery protocol |

Then repair the narrowest authoritative layer and test the original scenario in a clean session. The [failure-mode taxonomy](/blog/coding-agent-failure-modes/) provides the incident-analysis method behind this selection process.

## A minimal repository harness

For a small repository, a useful first version can remain lightweight:

```text
AGENTS.md                 # router + durable authority boundaries
docs/architecture.md      # subsystem and source-of-truth map
docs/decisions/           # non-obvious accepted choices
docs/tasks/active/        # task envelopes and durable checkpoints
scripts/validate.sh       # executable validation contract
.github/pull_request_template.md  # evidence handoff prompts
```

The structure is less important than the links between it. Root instructions should point to scoped context. Task envelopes should name exact proof. Decision records should be discoverable from affected code. Validation should test the contract rather than merely execute a familiar command.

For a ready-made starting point, [repository-harness](https://github.com/hoangnb24/repository-harness) provides templates and workflow scaffolding for Claude Code, Codex, Cursor, and other coding agents.

## Adoption sequence

A safe adoption sequence is:

### Week 1: Observe

Collect three to five agent sessions. Record the first wrong decision, repeated correction, scope expansion, validation escape, and resume failure. Do not add rules yet.

### Week 2: Install one controller

Choose the dominant failure class and implement one pattern in the narrowest location. Add an executable detector if the repository can express the invariant mechanically.

### Week 3: Test fresh sessions

Repeat representative tasks without corrective prompts. Measure whether agents discover the new controller before the risky decision.

### Week 4: Compose

Add the adjacent pattern only if the first repair exposes a second bottleneck. A router often reveals missing source-of-truth maps. A task envelope often reveals weak validation contracts. Durable checkpoints often reveal unsafe recovery.

This sequence keeps the harness small enough to maintain and grounded in actual failures.

## Pattern quality checklist

Before calling a harness pattern complete, ask:

- [ ] Does it prevent a named repeated failure?
- [ ] Is the controlling source discoverable before the risky decision?
- [ ] Is it stored where the fact becomes true and changes?
- [ ] Does it link instead of duplicating lower-level detail?
- [ ] Is authority explicit rather than implied?
- [ ] Can a mechanical check carry the invariant?
- [ ] Does the proof cover the changed contract?
- [ ] Can a fresh session succeed without replaying the correction?
- [ ] Can interrupted work resume from observed state?
- [ ] Is there an owner or trigger for updating stale guidance?

## From documents to an operating system

A repository harness is not a folder of agent instructions. It is a small operating system for repository work: routing, boundaries, memory, proof, handoff, and recovery.

The pattern language makes that system inspectable. Teams can point to the missing controller instead of blaming an agent in general. They can add one durable repair, test it in a fresh session, and measure whether the next task avoids the same correction.

Start with the failure you paid for twice. Choose the smallest pattern that would have controlled the first wrong decision. Then make the repository—not the next prompt—carry the lesson.

## Related pages

- [Harness Engineering for Coding Agents](/harness-engineering-for-coding-agents/)
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/)
- [Coding-Agent Failure Modes](/blog/coding-agent-failure-modes/)
- [The Five Layers of Coding-Agent Context](/blog/five-layers-coding-agent-context/)
- [Why Coding-Agent Prompts Fail](/blog/why-coding-agent-prompts-fail/)
- [How to Audit a Repository for Agent-Readiness](/blog/audit-repo-agent-readiness/)
- [AGENTS.md Template](/agents-md-template/)
- [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness)

---

## FAQ

### What is a repository harness pattern?

A repository harness pattern is a reusable arrangement of instructions, workflow state, validation, and evidence that helps coding agents make correct local decisions repeatedly. Each pattern names a recurring problem, the forces behind it, a durable repository-level solution, and a way to verify that the solution works in a fresh session.

### How is a repository harness different from AGENTS.md?

`AGENTS.md` is one surface inside a repository harness. A complete harness also includes task envelopes, authority boundaries, source-of-truth maps, validation contracts, decision records, checkpoints, safe recovery rules, and evidence-based handoffs. `AGENTS.md` should route agents to those sources rather than contain every detail.

### Which repository harness pattern should a team implement first?

Start with the smallest pattern that prevents the most frequent costly mistake. For many teams that is the task envelope, which defines outcome, scope, constraints, acceptance criteria, and validation. If agents regularly start in the wrong place, begin with the repository router instead.

### Do these patterns depend on Claude Code, Codex, or Cursor?

No. The patterns are tool-agnostic because they live in repository files, executable checks, and workflow state. Tool-specific instruction files can act as adapters, while the authoritative maps, contracts, decisions, and validation commands remain shared.

### How do you test whether a coding-agent harness pattern works?

Reproduce a representative task in a fresh session without replaying the human correction. Verify that the agent discovers the controlling source before the risky decision, stays within scope, runs the required proof, and reports evidence. A current session succeeding after correction is not sufficient.

### Should every coding-agent failure create a new rule?

No. First classify the failure and repair the narrowest authoritative layer. One-task facts belong in the task envelope, package rules near the package, accepted tradeoffs in decision records, mechanical invariants in executable checks, and only durable cross-repository routing rules in root instructions.

### How should teams measure repository harness quality?

Track fresh-session success, human corrections before the first edit, scope expansion, validation escapes, repeated failure classes, successful resume after interruption, duplicate side effects during recovery, and whether each handoff contains claim-to-proof evidence.
