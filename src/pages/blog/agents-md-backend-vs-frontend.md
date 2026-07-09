---
layout: ../../layouts/MarkdownLayout.astro
title: "AGENTS.md for Backend/API Repos vs Frontend Repos"
description: "Backend and frontend repositories need different AGENTS.md instructions. This guide shows what to include for APIs, services, UI apps, design systems, and full-stack projects."
target_keyword: "AGENTS.md backend frontend"
secondary_keywords:
  - "AGENTS.md for backend repos"
  - "AGENTS.md for frontend repos"
  - "coding agent instructions for API repos"
  - "coding agent instructions for frontend repos"
  - "AI coding agents frontend backend"
  - "repository-harness AGENTS.md"
status: "published"
date: "2026-07-09"
image: /assets/agents-md-hero.jpg
tags:
  - AGENTS.md
  - How-to
  - Coding Agents
  - Context Engineering
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Should backend and frontend repositories use the same AGENTS.md template?","acceptedAnswer":{"@type":"Answer","text":"They can start from the same structure, but the operational details should differ. Backend repos need service boundaries, schema and migration rules, API compatibility, and integration-test commands. Frontend repos need route maps, design-system rules, accessibility checks, visual regression expectations, and build-preview commands."}},{"@type":"Question","name":"What should AGENTS.md include for backend or API repos?","acceptedAnswer":{"@type":"Answer","text":"Backend AGENTS.md files should explain service ownership, API contracts, database migrations, generated clients, queues, background jobs, security-sensitive files, and the exact unit, integration, contract, and migration checks required before handoff."}},{"@type":"Question","name":"What should AGENTS.md include for frontend repos?","acceptedAnswer":{"@type":"Answer","text":"Frontend AGENTS.md files should explain routes, component ownership, design tokens, accessibility requirements, state-management boundaries, screenshot or visual-regression checks, browser support, and when to run local previews or end-to-end tests."}},{"@type":"Question","name":"How should full-stack repos organize AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"Use one root AGENTS.md for universal rules, then point agents to backend and frontend sections or nested AGENTS.md files when the repo is large. Keep shared validation, security, and generated-output rules at the root so agents do not miss them."}},{"@type":"Question","name":"Should AGENTS.md mention database credentials or secrets?","acceptedAnswer":{"@type":"Answer","text":"No. AGENTS.md should never include secrets. It can document safe local setup commands, required environment-variable names, redacted examples, and rules for not printing or modifying credentials."}},{"@type":"Question","name":"How do I keep backend and frontend AGENTS.md instructions from drifting?","acceptedAnswer":{"@type":"Answer","text":"Add AGENTS.md review lines to pull requests, review validation commands on every release, and update instructions whenever API contracts, routes, generated files, migrations, or package scripts change."}},{"@type":"Question","name":"Can repository-harness generate both backend and frontend instructions?","acceptedAnswer":{"@type":"Answer","text":"repository-harness provides reusable templates and patterns you can adapt for either backend/API repos or frontend repos. The important step is tailoring the path map, validation commands, and stop rules to the actual repository."}}]}</script>

# AGENTS.md for Backend/API Repos vs Frontend Repos

A good AGENTS.md is not just a generic “be careful” note for coding agents. It is an operating guide for a specific repository.

That means backend and frontend repositories should not have identical AGENTS.md files.

A backend/API repo needs to protect service boundaries, data migrations, API contracts, generated clients, queues, and integration checks. A frontend repo needs to protect route ownership, design-system rules, accessibility, state boundaries, browser behavior, and visual regressions.

The structure can be shared. The details should be different.

If you are starting from scratch, use the [AGENTS.md template](/agents-md-template/) first. Then adapt the sections below for your stack. If you already have a file, pair this guide with [how to maintain AGENTS.md as your repository evolves](/blog/maintain-agents-md/).

## The one-sentence rule

Use this rule:

> Backend AGENTS.md files should help agents preserve system behavior; frontend AGENTS.md files should help agents preserve user experience.

Both matter. But they fail in different ways.

| Repo type | Most common agent failure | AGENTS.md should emphasize |
|---|---|---|
| Backend/API | Breaks contract, migration, auth, or integration behavior | Service boundaries, schemas, migrations, integration checks |
| Frontend/UI | Breaks layout, route behavior, accessibility, or state flow | Route map, design system, accessibility, previews, E2E checks |
| Full-stack | Changes both sides without validating the seam | Shared contracts, generated clients, local end-to-end flow |

The goal is not to make AGENTS.md long. The goal is to make the highest-risk rules visible before an agent starts editing.

## 1. What backend/API repos need

Backend repos are usually less visual and more contract-heavy. The agent can make a change that looks small in code but breaks a caller, queue worker, migration, or generated client.

A backend AGENTS.md should answer seven questions quickly:

1. What services or modules exist?
2. Which files define public contracts?
3. How are database migrations created and validated?
4. Which generated files must not be edited by hand?
5. Which tests prove API compatibility?
6. Which auth, billing, or data paths are high-risk?
7. What should the agent do when local integration dependencies are unavailable?

A useful backend section might look like this:

```md
## Backend/API rules

Work in:
- src/api/ — HTTP route handlers
- src/domain/ — business logic
- src/db/ — migrations and query helpers
- tests/integration/ — API + database integration tests

Do not manually edit:
- src/generated/**
- openapi/client/**
- migration snapshots unless the migration command generated them

Public contracts:
- openapi.yaml
- proto/**
- src/api/routes.ts

Validation before handoff:
- pnpm test -- --run
- pnpm test:integration -- --run
- pnpm openapi:check
- pnpm migration:check

If Docker or the local database is unavailable, report the blocked command and why.
```

This gives the agent an execution map. It does not need to discover the repo from scratch.

For a broader framework, read [what makes a repository agent-ready](/agent-ready-repository/).

## 2. Backend stop rules should be explicit

Backend stop rules are often more important than backend style rules.

Agents need to know where a normal code change turns into a risky product or security change. Put that in AGENTS.md directly.

Examples:

```md
## Backend stop rules

Ask before changing:
- authentication or authorization checks
- billing, metering, or quota logic
- database migration strategy
- irreversible data writes
- public API response shapes
- encryption, token, or secret-handling code
```

This does not block agents from being useful. It prevents them from silently expanding scope into areas where the cost of being wrong is high.

If your team has repeated agent mistakes around stale commands or old paths, use the checklist in [10 AGENTS.md mistakes that break coding agent sessions](/blog/agents-md-mistakes/).

## 3. Backend validation should include contracts, not only unit tests

A common weak AGENTS.md says:

```md
Run tests before submitting.
```

For backend repos, that is usually not enough. The agent may run unit tests but skip the contract check that catches a broken API response.

Better:

```md
## Backend validation

For pure domain logic:
- pnpm test -- --run src/domain

For API route changes:
- pnpm test:integration -- --run
- pnpm openapi:check
- pnpm test:contract

For database changes:
- pnpm migration:create --check
- pnpm migration:check
- pnpm test:integration -- --run tests/integration/db
```

The principle: validation should follow the blast radius of the change.

## 4. What frontend repos need

Frontend repos fail differently. A change can pass unit tests while breaking layout, focus behavior, mobile spacing, browser compatibility, or a route-level data flow.

A frontend AGENTS.md should answer these questions:

1. Where are routes defined?
2. Which component layer should be edited?
3. Where do design tokens live?
4. Which components are generated or vendored?
5. What accessibility checks are required?
6. How should the agent preview UI changes?
7. Which end-to-end tests cover affected flows?

A useful frontend section might look like this:

```md
## Frontend/UI rules

Work in:
- src/pages/ — route-level pages
- src/components/ — reusable components
- src/features/ — feature-specific UI
- src/styles/tokens.css — design tokens

Prefer:
- existing components before new components
- design tokens before hard-coded colors
- accessible labels and keyboard behavior for interactive elements

Do not manually edit:
- generated route manifests
- built assets in dist/**
- vendored component snapshots

Validation before handoff:
- pnpm typecheck
- pnpm test -- --run
- pnpm lint
- pnpm test:e2e -- --grep "affected flow"
- pnpm build
```

Frontend agents also need permission to use visual evidence. If a route changes, the AGENTS.md should say how to preview it and what to inspect.

## 5. Frontend AGENTS.md should encode design-system boundaries

Many frontend agent failures are not syntax failures. They are consistency failures.

The agent introduces a new button, card, modal, spacing rule, or color because it did not know the existing design system.

Add a short design-system section:

```md
## Design system

Before adding UI:
- check src/components/ui/ for existing primitives
- use tokens from src/styles/tokens.css
- do not add one-off colors unless the task asks for a new visual treatment
- keep focus states visible
- preserve mobile layout at 375px width

Common components:
- Button — src/components/ui/Button.tsx
- Card — src/components/ui/Card.tsx
- Modal — src/components/ui/Modal.tsx
```

This is more useful than telling the agent to “make it look good.”

If the repo uses multiple context-file formats, align this with [AGENTS.md vs CLAUDE.md vs .cursorrules vs copilot-instructions.md](/blog/coding-agent-context-file-formats/) so universal repo rules and editor-specific rules do not fight each other.

## 6. Frontend validation needs previews and accessibility

For frontend work, `npm test` may not prove much. AGENTS.md should tell the agent when to build, preview, run E2E, and check accessibility.

Example:

```md
## Frontend validation

For component-only changes:
- pnpm test -- --run affected-component
- pnpm typecheck

For route or layout changes:
- pnpm build
- pnpm preview
- pnpm test:e2e -- --grep "affected route"

Accessibility checks:
- interactive elements have labels
- keyboard navigation still works
- focus states are visible
- color contrast uses existing tokens
```

If your workflow includes screenshots, Storybook, Playwright, or visual regression snapshots, name the exact command. Agents are much more reliable when the repo gives them a concrete check instead of a vague expectation.

## 7. Full-stack repos need seam rules

Full-stack repos need both backend and frontend instructions, but the most important rules are at the seam between them.

Common seam failures:

- backend response changes without updating frontend types
- frontend assumes a field that is optional in the API
- generated clients are patched by hand
- database migration changes are not reflected in seed data
- E2E tests are skipped because unit tests passed

Add a seam section:

```md
## Full-stack contract rules

When changing API shape:
1. Update the backend schema or route type.
2. Regenerate the frontend client.
3. Update frontend call sites.
4. Run contract tests and the affected E2E flow.

Commands:
- pnpm api:check
- pnpm generate:client
- pnpm test:contract
- pnpm test:e2e -- --grep "affected flow"

Do not manually edit generated API clients.
```

This is where AGENTS.md can save hours. It tells the agent the order of operations before it invents one.

## 8. A compact backend/API template

Use this when the repo is mostly services, APIs, CLIs, workers, or data pipelines:

```md
# AGENTS.md — Backend/API repo

## Project map
- src/api/ — route handlers and request/response mapping
- src/domain/ — business logic
- src/db/ — migrations and persistence
- src/workers/ — background jobs
- tests/ — unit and integration tests

## Public contracts
- openapi.yaml
- proto/**
- src/api/routes.ts

## Do not edit manually
- src/generated/**
- openapi/client/**
- dist/**

## Stop rules
Ask before changing auth, billing, migrations, public response shapes, or secret handling.

## Validation
- pnpm test -- --run
- pnpm test:integration -- --run
- pnpm openapi:check
- pnpm migration:check
```

Keep this short. Link to deeper architecture docs instead of copying them into AGENTS.md.

## 9. A compact frontend template

Use this when the repo is mostly UI, docs, marketing pages, dashboards, design systems, or browser apps:

```md
# AGENTS.md — Frontend repo

## Project map
- src/pages/ — route-level pages
- src/components/ — reusable components
- src/features/ — feature-specific UI
- src/styles/ — tokens and global styles
- tests/e2e/ — browser flows

## UI rules
Use existing components and design tokens first. Keep interactive elements accessible. Preserve mobile behavior.

## Do not edit manually
- dist/**
- generated route manifests
- vendored component snapshots

## Preview and validation
- pnpm typecheck
- pnpm test -- --run
- pnpm lint
- pnpm build
- pnpm test:e2e -- --grep "affected flow"

For route or layout changes, run a local preview and inspect the affected route.
```

This gives agents a realistic frontend operating model: code checks plus visual and accessibility expectations.

## 10. How repository-harness helps

[`repository-harness`](https://github.com/hoangnb24/repository-harness) is an open-source set of templates and patterns for making repositories easier for coding agents to work in.

It helps you create an AGENTS.md that is not just a prompt file, but part of a larger repo harness:

- repo instructions
- feature intake
- story packets
- validation commands
- review checklists
- decision records
- generated-output rules

The templates are intentionally adaptable. A backend API repo, frontend app, CLI, data pipeline, and documentation site should not all expose the same agent contract.

Start here:

- [AGENTS.md template](/agents-md-template/)
- [What is an agent-ready repository?](/agent-ready-repository/)
- [`repository-harness` on GitHub](https://github.com/hoangnb24/repository-harness)

## Backend vs frontend checklist

Use this checklist before merging AGENTS.md changes:

| Check | Backend/API | Frontend/UI |
|---|---|---|
| Path map names real edit locations | ✅ | ✅ |
| Validation commands match package scripts | ✅ | ✅ |
| Generated files are protected | ✅ | ✅ |
| Public contract files are named | ✅ | Sometimes |
| Database/migration rules exist | ✅ | Rarely |
| Design-system rules exist | Rarely | ✅ |
| Accessibility expectations exist | Sometimes | ✅ |
| Preview or E2E flow is documented | Sometimes | ✅ |
| Stop rules cover high-risk changes | ✅ | ✅ |

If one column is empty for your repo type, AGENTS.md is probably too generic.

## FAQ

### Should backend and frontend repositories use the same AGENTS.md template?

They can start from the same structure, but the operational details should differ. Backend repos need service boundaries, schema and migration rules, API compatibility, and integration-test commands. Frontend repos need route maps, design-system rules, accessibility checks, visual regression expectations, and build-preview commands.

### What should AGENTS.md include for backend or API repos?

Backend AGENTS.md files should explain service ownership, API contracts, database migrations, generated clients, queues, background jobs, security-sensitive files, and the exact unit, integration, contract, and migration checks required before handoff.

### What should AGENTS.md include for frontend repos?

Frontend AGENTS.md files should explain routes, component ownership, design tokens, accessibility requirements, state-management boundaries, screenshot or visual-regression checks, browser support, and when to run local previews or end-to-end tests.

### How should full-stack repos organize AGENTS.md?

Use one root AGENTS.md for universal rules, then point agents to backend and frontend sections or nested AGENTS.md files when the repo is large. Keep shared validation, security, and generated-output rules at the root so agents do not miss them.

### Should AGENTS.md mention database credentials or secrets?

No. AGENTS.md should never include secrets. It can document safe local setup commands, required environment-variable names, redacted examples, and rules for not printing or modifying credentials.

### How do I keep backend and frontend AGENTS.md instructions from drifting?

Add AGENTS.md review lines to pull requests, review validation commands on every release, and update instructions whenever API contracts, routes, generated files, migrations, or package scripts change.

### Can repository-harness generate both backend and frontend instructions?

`repository-harness` provides reusable templates and patterns you can adapt for either backend/API repos or frontend repos. The important step is tailoring the path map, validation commands, and stop rules to the actual repository.

## Related pages

- [How to maintain AGENTS.md as your repository evolves](/blog/maintain-agents-md/)
- [10 AGENTS.md mistakes that break coding agent sessions](/blog/agents-md-mistakes/)
- [10 real-world AGENTS.md examples](/blog/agents-md-examples/)
- [AGENTS.md template](/agents-md-template/)
- [What is an agent-ready repository?](/agent-ready-repository/)
- [`repository-harness` on GitHub](https://github.com/hoangnb24/repository-harness)
