---
layout: ../../layouts/MarkdownLayout.astro
title: "Why Coding-Agent Prompts Fail When Context Lives Only in Prompts"
description: "A coding-agent prompt can guide one task, but it cannot maintain repository knowledge. Learn why prompt-only context fails and how to move durable rules into versioned repo sources."
target_keyword: "why coding agent prompts fail"
secondary_keywords:
  - "coding agent prompt failure"
  - "prompt engineering vs context engineering"
  - "repository context for coding agents"
  - "durable context for AI coding agents"
  - "AI coding agent instructions"
  - "AGENTS.md vs prompts"
status: "published"
date: "2026-07-30"
image: /assets/context-hero.jpg
tags:
  - Context Engineering
  - Coding Agents
  - How-to
  - English
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Why do coding-agent prompts fail?","acceptedAnswer":{"@type":"Answer","text":"Coding-agent prompts fail when they are expected to carry durable repository knowledge. Prompts are good at defining one task, but repeated local rules, validation commands, architecture boundaries, and decision history need versioned sources that every fresh session can discover."}},{"@type":"Question","name":"Is context engineering better than prompt engineering?","acceptedAnswer":{"@type":"Answer","text":"They solve different problems. Prompt engineering defines the outcome and constraints of the current task. Context engineering makes durable repository knowledge discoverable and authoritative across tasks, sessions, people, and coding-agent tools."}},{"@type":"Question","name":"What belongs in a coding-agent prompt?","acceptedAnswer":{"@type":"Answer","text":"A coding-agent prompt should contain the requested outcome, acceptance criteria, task-specific constraints, mutation authority, and any temporary facts unique to that work item."}},{"@type":"Question","name":"What context should move out of prompts and into the repository?","acceptedAnswer":{"@type":"Answer","text":"Move repeated setup and validation commands, repository maps, generated-file rules, safety boundaries, architecture contracts, accepted decisions, and handoff expectations into versioned repository files."}},{"@type":"Question","name":"Should all repository context go into AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"No. Root AGENTS.md should be a concise router that states controlling rules and points to deeper authoritative documentation. Package-specific rules, architecture detail, decision records, and long validation matrices should live near the scope they govern."}},{"@type":"Question","name":"How do I know whether a prompt-only fix is durable?","acceptedAnswer":{"@type":"Answer","text":"Repeat the task in a fresh session without pasting the corrective prompt. If the agent cannot discover the rule and reproduce the correct behavior from repository evidence, the fix is not durable."}},{"@type":"Question","name":"Can too much repository context also hurt coding agents?","acceptedAnswer":{"@type":"Answer","text":"Yes. Duplicated, stale, conflicting, or irrelevant instructions make authority harder to identify. Durable context should be scoped, linked, versioned, testable, and removed when it no longer changes decisions."}}]}</script>

# Why Coding-Agent Prompts Fail When Context Lives Only in Prompts

Coding-agent prompts fail when they are asked to carry knowledge that should survive the current task. A prompt is the right place for **what must happen now**; it is the wrong place for repository structure, recurring validation rules, architecture boundaries, generated-file warnings, and decisions that every future session must rediscover.

This is not an argument against prompt engineering. A clear task still matters. The problem begins when a team uses a better prompt to repair a repository-context failure. The correction works once, disappears with the session, and has to be paid for again.

The durable fix is to move repeated local knowledge into versioned, discoverable sources and let the prompt reference them. That is [context engineering for coding agents](/context-engineering-for-coding-agents/) at repository scale.

## The prompt-only failure loop

A common workflow looks like this:

1. An agent edits the wrong file, skips a required check, or crosses a local boundary.
2. A maintainer writes a more detailed prompt explaining the rule.
3. The corrected session succeeds.
4. A new session, teammate, or coding-agent tool repeats the original mistake.
5. The prompt grows again.

The team appears to be improving its prompts, but the repository is not learning. The correction lives in private working memory instead of the shared system where future work happens.

<figure style="margin:2rem 0;padding:1.25rem;border:1px solid #d8d8d4;border-radius:12px;background:#fbfbfa;overflow-x:auto">
<svg viewBox="0 0 920 360" role="img" aria-labelledby="prompt-loop-title prompt-loop-desc" style="width:100%;min-width:720px;height:auto">
<title id="prompt-loop-title">Prompt-only correction loop compared with durable repository context</title>
<desc id="prompt-loop-desc">The top path shows a mistake followed by a larger prompt, one successful session, and the same mistake in a fresh session. The lower path records the rule in a versioned repository source, routes agents to it, validates the behavior, and improves future sessions.</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#787774"/></marker></defs>
<text x="20" y="34" font-size="17" font-weight="700" fill="#b42318">PROMPT-ONLY LOOP</text>
<g font-family="ui-sans-serif,system-ui,-apple-system" font-size="14" fill="#37352f">
  <rect x="20" y="54" width="150" height="64" rx="10" fill="#fee4e2" stroke="#fda29b"/><text x="43" y="82" font-weight="700">Repeated mistake</text><text x="37" y="103">local rule was hidden</text>
  <rect x="220" y="54" width="150" height="64" rx="10" fill="#fff3d6" stroke="#f5c451"/><text x="247" y="82" font-weight="700">Larger prompt</text><text x="242" y="103">rule pasted manually</text>
  <rect x="420" y="54" width="150" height="64" rx="10" fill="#e7f6ec" stroke="#7fc999"/><text x="448" y="82" font-weight="700">One success</text><text x="438" y="103">current task passes</text>
  <rect x="620" y="54" width="260" height="64" rx="10" fill="#fee4e2" stroke="#fda29b"/><text x="663" y="82" font-weight="700">Fresh session forgets</text><text x="652" y="103">cost and failure repeat again</text>
  <line x1="170" y1="86" x2="214" y2="86" stroke="#787774" stroke-width="2" marker-end="url(#arrow)"/><line x1="370" y1="86" x2="414" y2="86" stroke="#787774" stroke-width="2" marker-end="url(#arrow)"/><line x1="570" y1="86" x2="614" y2="86" stroke="#787774" stroke-width="2" marker-end="url(#arrow)"/>
</g>
<text x="20" y="184" font-size="17" font-weight="700" fill="#087c5b">DURABLE CONTEXT LOOP</text>
<g font-family="ui-sans-serif,system-ui,-apple-system" font-size="14" fill="#37352f">
  <rect x="20" y="204" width="150" height="74" rx="10" fill="#eaf2fb" stroke="#90b8e8"/><text x="42" y="234" font-weight="700">Diagnose layer</text><text x="32" y="256">find first wrong decision</text>
  <rect x="220" y="204" width="170" height="74" rx="10" fill="#e7f6ec" stroke="#7fc999"/><text x="247" y="234" font-weight="700">Version the rule</text><text x="241" y="256">narrow source of truth</text>
  <rect x="440" y="204" width="170" height="74" rx="10" fill="#e7f6ec" stroke="#7fc999"/><text x="469" y="234" font-weight="700">Route + validate</text><text x="459" y="256">make discovery testable</text>
  <rect x="660" y="204" width="220" height="74" rx="10" fill="#dcfce7" stroke="#65b883"/><text x="695" y="234" font-weight="700">Future sessions improve</text><text x="685" y="256">shared context compounds</text>
  <line x1="170" y1="241" x2="214" y2="241" stroke="#787774" stroke-width="2" marker-end="url(#arrow)"/><line x1="390" y1="241" x2="434" y2="241" stroke="#787774" stroke-width="2" marker-end="url(#arrow)"/><line x1="610" y1="241" x2="654" y2="241" stroke="#787774" stroke-width="2" marker-end="url(#arrow)"/>
</g>
<text x="20" y="326" font-size="14" fill="#55534e">A correction becomes infrastructure only when a fresh session can discover and verify it without private prompt history.</text>
</svg>
</figure>

## Five reasons prompt-only context breaks

### 1. Prompts expire with the task

Task prompts are disposable by design. They describe one outcome under one set of constraints. A canonical test command or generated-file rule has a different lifetime: it must remain true across issues, sessions, contributors, and tools.

When durable information lives only in a prompt, every new session starts from an incomplete repository. The agent may have a large context window, but the missing rule is not in that window unless someone remembers to paste it.

### 2. Prompt copies drift apart

Suppose a team keeps a “good coding-agent prompt” in a personal note, an issue template, and a chat snippet. The repository later switches from `npm test` to `pnpm test --filter ./packages/api`. Which copy changes?

Usually one does. The others become plausible, detailed, wrong instructions. Versioned repository context reduces this split-brain problem because the command changes beside the code and can be reviewed in the same pull request.

The maintenance guide for [keeping AGENTS.md aligned with a changing repository](/blog/maintain-agents-md/) covers the drift triggers worth checking after toolchain, layout, validation, and deployment changes.

### 3. Prompts hide authority

A long prompt often mixes several kinds of information:

- the requested outcome
- permanent repository conventions
- temporary debugging discoveries
- copied architecture notes
- safety boundaries
- guesses about how the code works

When those statements conflict, the agent has to infer which one controls. A versioned decision record should not have the same status as a temporary hypothesis. A generated-file prohibition should not look like optional style advice.

The [five layers of coding-agent context](/blog/five-layers-coding-agent-context/) provide a diagnostic model for separating task, session, repository-instruction, decision-history, and model-knowledge context before they collapse into one prompt.

### 4. Prompt text is hard to validate mechanically

Repositories can test files. CI can verify that documented commands still exist, generated outputs are clean, links resolve, and installed templates match their sources. A private prompt pasted into a session rarely gets the same review or automation.

This matters because prose is not proof. “Run the relevant tests” sounds responsible but does not tell an agent which command proves a database migration, API change, or UI update safe. A repository can map change types to commands and check that the map stays current.

### 5. Prompt-only fixes do not compound

A corrected prompt helps one operator in one moment. A corrected repository source can help every contributor, agent, and workflow that enters later. It can be reviewed, blamed, compared, reverted, and improved after new evidence.

That compounding effect is the practical difference between a clever instruction and operating infrastructure.

## Prompt engineering and context engineering have different jobs

The useful comparison is not “prompts or context.” It is deciding what each layer should own.

| Question | Prompt engineering | Repository context engineering |
|---|---|---|
| Primary job | Define the current outcome | Define how work happens here |
| Lifetime | One task or work item | Many tasks and sessions |
| Typical contents | Acceptance criteria, scope, deadline, mutation authority | Repo map, commands, boundaries, contracts, decisions |
| Change frequency | Often | When the repository or policy changes |
| Review surface | Task discussion | Version-controlled diff |
| Verification | Did this task satisfy its criteria? | Can a fresh session discover and follow the rule? |
| Failure signal | Agent solves the wrong task | Fresh agents repeat the same local mistake |

Use the prompt to say **what success means now**. Use the repository to explain **how this project works repeatedly**.

A strong task can then be short:

```text
Add CSV export to the reports endpoint.

Acceptance criteria:
- preserve the existing JSON response
- stream large exports instead of buffering them
- add contract tests for authorization and content type

Follow the repository instructions and validation map.
```

The prompt does not need to restate the package map, generated-client workflow, security stop rules, or exact test commands if those are already authoritative and discoverable in the repository.

## What belongs where

Use this placement guide when a prompt keeps growing.

| Information | Best home | Why |
|---|---|---|
| Requested feature or bug outcome | Issue or task prompt | Unique to this work item |
| Acceptance criteria | Issue or task prompt | Defines task completion |
| Read-only vs edit authority | Task prompt | Must be explicit for this interaction |
| Canonical setup and validation commands | `AGENTS.md` or linked validation doc | Reused across tasks |
| Repository and package map | Architecture/workflow doc routed from `AGENTS.md` | Durable orientation |
| Generated or vendored file rules | Scoped instructions near the affected path | Local and repeatedly safety-critical |
| Why a surprising design exists | Decision record | Preserves rationale and reopening conditions |
| Current failed command and working hypothesis | Session plan or checkpoint | Useful now, not necessarily permanent |
| Cross-session migration state | Versioned active plan | Must survive context loss |
| Generic framework convention | Model knowledge, verified against local code | Useful hypothesis, not local proof |

Do not move everything into root `AGENTS.md`. A giant instruction file recreates the prompt problem inside the repository: mixed scope, hidden authority, duplication, and attention waste. Root instructions should route to the narrowest source that governs the decision.

## Before and after: generated client change

Imagine an API client under `src/generated/` that must be regenerated from `api/openapi.yaml`.

### Prompt-only repair

After an agent edits the generated TypeScript directly, a maintainer adds this to the next prompt:

```text
Do not edit files under src/generated. Change api/openapi.yaml,
run pnpm generate:client, then run pnpm test:contracts.
```

That session succeeds. The next issue is opened by another maintainer without the warning, and the mistake returns.

### Durable repair

The team instead adds a scoped instruction:

```md
# api/AGENTS.md

Changes represented in `src/generated/**` must start in `api/openapi.yaml`.
Regenerate with `pnpm generate:client`.
Validate with `pnpm test:contracts`.
A clean handoff includes the schema diff and generated diff.
```

The root `AGENTS.md` links to the API instructions when work touches the schema or client. CI runs the generator and fails if committed output is stale.

Now the repository carries the correction. The task prompt only needs to request the API change and its acceptance criteria.

This is also why an [agent-ready repository is not the same as a clean codebase](/blog/agent-readiness-vs-code-quality/). The generated client can be beautifully formatted while its source-of-truth rule remains invisible.

## A six-step migration from prompt memory to repository memory

### 1. Collect repeated prompt fragments

Look at recent agent tasks, issue comments, review corrections, and saved prompt templates. Mark instructions that appear more than once or that prevent an expensive class of mistake.

Repeated text is a signal, not automatic documentation. Some repeated instructions are still task-specific. The next steps decide which ones deserve durable status.

### 2. Name the decision the instruction changes

Convert vague advice into an observable decision:

- “Be careful with generated files” becomes “edit the schema, not generated output.”
- “Test your changes” becomes “run the API contract suite for response-shape changes.”
- “Understand the architecture” becomes “do not import infrastructure adapters from domain packages.”

If the instruction does not change a decision, it may be noise.

### 3. Choose the narrowest scope

A global safety boundary belongs near the root. A package command belongs with that package. An accepted tradeoff belongs in a decision record. A one-off deadline stays in the task.

Narrow scope makes relevant context easier to retrieve and conflicting copies easier to avoid.

### 4. Make the rule executable where possible

Pair prose with evidence:

- a command that validates the change
- a test that protects the contract
- a generator cleanliness check
- a link check for documentation
- a linter or policy check for a forbidden dependency

Not every rule can be automated, but every critical rule should define what evidence a handoff must report.

### 5. Route agents to the source

A correct document that no agent discovers is operationally missing. Link scoped instructions, architecture maps, validation tables, and decision records from the entry points an agent reads before making the relevant decision.

The guide to [writing an AGENTS.md that actually works](/blog/how-to-write-agents-md/) shows how to use the root file as a decision router rather than a documentation warehouse.

### 6. Test with a fresh session

Do not reuse the corrective prompt. Start a clean session with a realistic task that exercises the rule. Check whether the agent:

1. finds the controlling source
2. identifies the correct editable surface
3. respects the boundary without a reminder
4. runs the required proof command
5. reports the evidence at handoff

If it cannot, improve discovery, wording, scope, or enforcement. The [100-point agent-readiness audit](/blog/audit-repo-agent-readiness/) can expose broader orientation and validation gaps.

## When a longer prompt is still the right fix

Not every failure belongs in repository documentation. Keep information in the task when it is:

- unique to the requested outcome
- temporary or deadline-specific
- an acceptance criterion rather than a reusable workflow
- sensitive and inappropriate to commit
- an explicit authorization boundary for this interaction
- an unverified hypothesis that may be discarded

For example, “keep the legacy endpoint until the mobile release reaches 95% adoption” may belong in a release task if it is temporary. The durable compatibility rationale and removal criteria may belong in a decision record if future work needs them.

The test is not whether information is important. The test is whether future sessions need it, whether it is stable enough to version, and which source should be authoritative.

## Avoid the opposite failure: context dumping

Moving text out of prompts does not justify filling the repository with instructions. Too much context creates its own failures:

- duplicated commands disagree
- global rules obscure package-specific exceptions
- stale documents look authoritative
- agents spend attention on irrelevant history
- long root files become difficult to scan before a decision

Use four controls:

1. **Scope:** place rules near the paths and decisions they govern.
2. **Routing:** keep entry-point files concise and link to detail.
3. **Ownership:** name when and why each source must be reviewed.
4. **Deletion:** remove instructions that no longer affect behavior.

Good context engineering reduces uncertainty at the moment of action. It does not maximize token count.

## A prompt-to-repository audit checklist

Pick three recent coding-agent prompts and ask:

- [ ] Which lines define only the current outcome?
- [ ] Which lines repeat across tasks?
- [ ] Which repeated lines prevent a concrete wrong decision?
- [ ] Does an authoritative repository source already contain them?
- [ ] Are there conflicting copies of the same command or rule?
- [ ] Is the rule placed at the narrowest relevant scope?
- [ ] Can the repository validate the rule mechanically?
- [ ] Can a fresh session discover it before editing?
- [ ] Does the handoff require evidence that the rule was followed?
- [ ] Can any stale or redundant instruction be deleted?

Then migrate one repeated, high-cost rule. Do not rewrite the entire documentation system at once. Measure whether the next fresh session avoids the original mistake.

## Make the repository carry the lesson

A better prompt can rescue a task. A better repository can improve every task that follows.

Use prompts for the current outcome, constraints, and authority. Put durable operating knowledge in versioned sources with clear scope, discovery paths, and validation. Test the result without replaying private prompt history.

[repository-harness](https://github.com/hoangnb24/repository-harness) is an open-source starting point for turning repeated prompt corrections into repository instructions, validation maps, plans, and evidence-based handoffs that work across Claude Code, Codex, Cursor, and other coding agents.

## Related pages

- [Coding-Agent Failure Modes: A Diagnostic Taxonomy](/blog/coding-agent-failure-modes/)
- [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/)
- [The Five Layers of Coding-Agent Context](/blog/five-layers-coding-agent-context/)
- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/)
- [How to Audit a Repository for Agent-Readiness](/blog/audit-repo-agent-readiness/)
- [Agent-Readiness vs Code Quality](/blog/agent-readiness-vs-code-quality/)
- [repository-harness on GitHub](https://github.com/hoangnb24/repository-harness)

---

## FAQ

### Why do coding-agent prompts fail?

Coding-agent prompts fail when they are expected to carry durable repository knowledge. Prompts are good at defining one task, but repeated local rules, validation commands, architecture boundaries, and decision history need versioned sources that every fresh session can discover.

### Is context engineering better than prompt engineering?

They solve different problems. Prompt engineering defines the outcome and constraints of the current task. Context engineering makes durable repository knowledge discoverable and authoritative across tasks, sessions, people, and coding-agent tools.

### What belongs in a coding-agent prompt?

A coding-agent prompt should contain the requested outcome, acceptance criteria, task-specific constraints, mutation authority, and any temporary facts unique to that work item.

### What context should move out of prompts and into the repository?

Move repeated setup and validation commands, repository maps, generated-file rules, safety boundaries, architecture contracts, accepted decisions, and handoff expectations into versioned repository files.

### Should all repository context go into AGENTS.md?

No. Root `AGENTS.md` should be a concise router that states controlling rules and points to deeper authoritative documentation. Package-specific rules, architecture detail, decision records, and long validation matrices should live near the scope they govern.

### How do I know whether a prompt-only fix is durable?

Repeat the task in a fresh session without pasting the corrective prompt. If the agent cannot discover the rule and reproduce the correct behavior from repository evidence, the fix is not durable.

### Can too much repository context also hurt coding agents?

Yes. Duplicated, stale, conflicting, or irrelevant instructions make authority harder to identify. Durable context should be scoped, linked, versioned, testable, and removed when it no longer changes decisions.
