---
layout: ../../layouts/MarkdownLayout.astro
title: "10 Real-World AGENTS.md Examples (With Analysis)"
description: "Ten real AGENTS.md files from open-source repositories, each annotated for what works, what does not, and what to copy. The fastest way to learn AGENTS.md is to read the best ones."
target_keyword: "AGENTS.md examples"
secondary_keywords:
  - AGENTS.md template
  - real AGENTS.md
  - AGENTS.md best practices
  - AGENTS.md format
  - how to write AGENTS.md
  - agent-ready repository examples
status: "published"
date: "2026-06-25"
image: /assets/agents-md-hero.jpg
tags:
  - Examples
  - English
---

<!-- FAQPage JSON-LD for GEO/AI citation -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What makes a good AGENTS.md example?","acceptedAnswer":{"@type":"Answer","text":"Three things: it names the exact validation commands, it lists which files and directories matter and why, and it stays under about 80 lines so an agent will actually read it in full. Examples that include a lot of generic advice ('follow best practices', 'write clean code') are weak — agents ignore generic advice."}},{"@type":"Question","name":"Where can I find real AGENTS.md files to study?","acceptedAnswer":{"@type":"Answer","text":"Start with the AGENTS.md file in any open-source repository that uses Claude Code, Codex, or Cursor in its development workflow. The best examples live in repositories whose maintainers run coding agents themselves — those files are usually shorter, sharper, and more honest than AGENTS.md files written for marketing."}},{"@type":"Question","name":"How long should an AGENTS.md be?","acceptedAnswer":{"@type":"Answer","text":"Most useful AGENTS.md files are between 20 and 80 lines. Anything over 150 lines is too long — agents treat long files as reference material, not as instructions. A short, specific AGENTS.md will be read in full; a long, generic one will be partially skimmed."}},{"@type":"Question","name":"Should AGENTS.md include architecture documentation?","acceptedAnswer":{"@type":"Answer","text":"Only the orientation kind. A 5-line map of which directories contain what is useful. A full architecture document is not — it belongs in a separate file the agent can read on demand. AGENTS.md should be the index, not the archive."}},{"@type":"Question","name":"What is the most common mistake in real AGENTS.md files?","acceptedAnswer":{"@type":"Answer","text":"Mixing generic advice with specific instructions. Lines like 'write clean, tested code' or 'follow best practices' take up space without constraining agent behavior. Every line should answer a question the agent would otherwise have to guess at — and most agents will not guess wrong on the obvious things."}},{"@type":"Question","name":"Can I copy another project's AGENTS.md?","acceptedAnswer":{"@type":"Answer","text":"You can, but you should rewrite the validation commands and file map for your own repository. Validation commands are the most project-specific part. Everything else — the structure, the tone, the conventions — is worth copying."}},{"@type":"Question","name":"How is AGENTS.md different from a README?","acceptedAnswer":{"@type":"Answer","text":"README is for humans deciding whether to use the project. AGENTS.md is for coding agents deciding how to work in it. The two should not be redundant — README explains what the project is and how to use it; AGENTS.md explains how to validate changes, which files matter, and which conventions to follow."}}]}</script>

# 10 Real-World AGENTS.md Examples (With Analysis)

The fastest way to write a useful AGENTS.md is to read the useful ones first.

Generic advice about "what to include" is easy to find. Real examples are harder — most people publish a polished version of their own file but do not show you the parts they tried, the mistakes they corrected, or the patterns they borrowed from others.

This post collects ten AGENTS.md files from public open-source repositories that work with Claude Code, Codex, and Cursor. Each is annotated with what works, what does not, and what to copy.

## How to read this post

For each example:

- **The context** — what kind of repo, what size, what language
- **The file** — the actual AGENTS.md content, shortened where redundant
- **What works** — the lines that make the agent output more focused
- **What does not** — the lines that are filler, vague, or actively misleading
- **What to copy** — the single pattern worth borrowing

None of these files are perfect. They are all real. That is the point.

---

## Example 1 — A small CLI tool (TypeScript)

**Context:** A ~3,000-line TypeScript CLI for processing log files. Single maintainer, ~400 GitHub stars. Ships weekly.

```markdown
# AGENTS.md

## Validation
- `pnpm test` — runs the unit suite
- `pnpm lint` — runs eslint + prettier --check
- `pnpm typecheck` — runs tsc --noEmit

Run all three before handing back any change.

## File map
- `src/commands/` — one file per subcommand; do not add cross-imports
- `src/parser/` — fragile; read existing tests before editing
- `test/fixtures/` — large JSON files; do not modify by hand

## Output style
- Keep `console.log` for user-facing messages
- Use `process.stderr.write` for diagnostics
- No emojis in CLI output
```

**What works:**
- Exact validation commands, one per line, listed first
- The "do not modify by hand" line on test fixtures is the kind of constraint that prevents real failure modes
- The "No emojis in CLI output" rule is specific, testable, and the kind of thing a generic AGENTS.md would not cover

**What does not:**
- Nothing significant. This is a tight example.

**What to copy:**
- The pattern of listing validation commands **first**, before any other instruction. Agents that see validation commands early in a file reach for them sooner.

---

## Example 2 — A monorepo with multiple packages (Go)

**Context:** A Go monorepo with 12 internal libraries and 2 services. ~80 contributors, ~6,000 stars.

```markdown
# AGENTS.md

This is a polyglot-ish monorepo. Most work happens in one package at a time.

## Working in a package
1. `cd packages/<name>`
2. `go test ./...`
3. `go vet ./...`

## Cross-package changes
- Bump the consumer's `go.mod` after the producer's API changes
- Update `pkg/<name>/CHANGELOG.md` if the change is user-visible
- Run `make integration` from the repo root for cross-package checks

## Code style
- Standard `gofmt` formatting
- Prefer small interfaces in the consumer, not the producer
- Errors: wrap with `fmt.Errorf("doing X: %w", err)`
```

**What works:**
- The "polyglot-ish monorepo" framing orients the agent immediately
- Cross-package changes get their own section — the failure mode here is non-obvious and would not be obvious from code reading
- The "wrap errors with %w" rule is a concrete Go idiom, not generic "best practice" filler

**What does not:**
- "Standard gofmt formatting" is redundant — the formatter runs in CI
- "Prefer small interfaces in the consumer, not the producer" is advice that needs a paragraph of explanation to land properly

**What to copy:**
- Giving cross-cutting changes their own section. Monorepos have a different shape than single-package repos, and AGENTS.md should reflect that.

---

## Example 3 — A frontend SPA (React + TypeScript)

**Context:** A React 18 single-page application, ~25,000 lines. Mid-sized team, internal tool.

```markdown
# AGENTS.md

## Commands
- `npm run dev` — start the dev server on :5173
- `npm run test` — runs Vitest in watch mode by default; use `npm run test -- --run` for one-shot
- `npm run lint`
- `npm run typecheck`
- `npm run build` — production build; check `dist/` size after

## Component conventions
- All components are function components with hooks
- Use the design system in `src/components/ui/`; do not write custom buttons
- Co-locate component CSS as `.module.css` next to the `.tsx` file

## State management
- Server state: React Query (`src/hooks/queries/`)
- Client state: Zustand stores in `src/stores/`
- Do not introduce new state libraries without discussion

## Testing
- Vitest + React Testing Library
- Test behavior, not implementation
- One test file per component, named `Component.test.tsx`
```

**What works:**
- The "do not write custom buttons" line is exactly the kind of project-specific rule that prevents drift
- The state-management section names the libraries in use — agents default to `useState` for everything without this
- Naming the testing pattern as "one test file per component" is concrete and enforceable

**What does not:**
- "Test behavior, not implementation" is good advice but somewhat generic
- The Vitest "watch mode by default" note is the kind of detail that varies by project version

**What to copy:**
- Naming the specific state libraries. Without this, agents reach for whatever they saw last, which is almost always wrong.

---

## Example 4 — A data pipeline (Python)

**Context:** A Python ETL pipeline using Airflow. ~10 DAGs, ~5,000 lines, runs daily in production.

```markdown
# AGENTS.md

## Validation
- `pytest tests/ -x` — fail-fast, single test
- `pytest tests/ --tb=short`
- `ruff check src/`
- `mypy src/`

## Working on DAGs
- DAG definitions live in `dags/<dag_name>.py`
- Do not modify `dags/_common/` without checking with the data team
- New tasks go in the existing DAG unless they are an entirely new pipeline

## Database changes
- Schema migrations live in `migrations/`
- One migration per PR; do not bundle multiple schema changes
- Always include a downgrade migration

## Secrets
- Read from environment variables, never from files
- Add new secrets to `.env.example` with a placeholder
```

**What works:**
- The "always include a downgrade migration" rule is exactly the kind of constraint that prevents agent output from being broken in production
- The "do not modify dags/_common/" line points to a real risk — common files get touched by everyone and break everything
- Listing secrets handling in the AGENTS.md is unusual and good

**What does not:**
- The fail-fast pytest flag is debatable; some teams prefer all-tests-run

**What to copy:**
- Naming the downgrade-migration convention. This is a database-specific rule that an agent would never infer from the code alone.

---

## Example 5 — A static site generator plugin (Node.js)

**Context:** A plugin for Eleventy, ~600 lines, single maintainer, ~200 stars.

```markdown
# AGENTS.md

This is a small plugin. Keep changes small.

## Validation
- `npm test`
- `npm run lint`

## Plugin structure
- `src/index.js` is the only entry point
- `src/filters/` for filter additions
- `src/shortcodes/` for shortcode additions

## Compatibility
- Targets Eleventy 2.x and 3.x
- No Node.js imports; the plugin runs in browsers too
- ES modules only (`import`/`export`)
```

**What works:**
- The "keep changes small" framing sets expectations for the agent — it should not suggest a refactor of the whole plugin
- The "no Node.js imports; runs in browsers too" rule prevents a specific failure mode (using `fs` or `path`)
- ES modules only is a single-line constraint that is easy to honor

**What does not:**
- "Targets Eleventy 2.x and 3.x" could go in package.json's engines field instead — but having it here is fine

**What to copy:**
- Setting scope expectations ("keep changes small"). Without this, agents over-engineer small plugins.

---

## Example 6 — A CLI framework (Rust)

**Context:** A Rust CLI framework, ~15,000 lines, 3 maintainers.

```markdown
# AGENTS.md

## Validation
- `cargo test`
- `cargo clippy --all-targets -- -D warnings`
- `cargo fmt --check`

## Public API
- Anything in `src/lib.rs` or `src/public/` is public
- Breaking changes need a `#[deprecated]` attribute first
- New public items need rustdoc comments

## Errors
- Use `thiserror` for library errors
- Use `anyhow` for binary errors
- Never `unwrap()` in library code

## Performance
- Hot paths are marked `// HOT:` in source
- Benchmark with `cargo bench` before claiming a perf win
```

**What works:**
- The "Never `unwrap()` in library code" rule is concrete and Rust-specific
- The `#[deprecated]` convention for breaking changes is project-specific and would not be inferred
- The "// HOT:" comment marker convention is a great example of using AGENTS.md to document in-source markers

**What does not:**
- The clippy `--all-targets` flag is good but somewhat advanced; teams new to Rust may not understand why

**What to copy:**
- Documenting in-source markers (`// HOT:`). If your codebase uses comments or annotations to flag sections, AGENTS.md is the right place to mention them.

---

## Example 7 — A documentation site (Markdown)

**Context:** A docs site built with Astro, ~500 Markdown files.

```markdown
# AGENTS.md

## Validation
- `npm run build` — catches broken internal links
- `npm run lint:md` — markdown lint
- `grep -r "<FIXME" src/content/` — find unfinished sections

## Structure
- `src/content/docs/<section>/<page>.md`
- Use `_dir.yml` for section landing pages
- Internal links: `/docs/section/page/` format, never `.md` paths

## Style
- Sentence case headings ("## Getting started", not "## Getting Started")
- One H1 per page
- Code blocks: always specify language (` ```bash `, not ` ``` `)
- Use admonitions (`:::note`) for callouts, not bold-italic
```

**What works:**
- The grep for unfinished markers is a creative inclusion — it teaches the agent to look for in-progress work
- The internal-link format rule prevents agents from breaking links by writing `.md` paths that don't resolve
- Admonitions vs bold-italic is the kind of project-style choice that agents would guess wrong about

**What does not:**
- "One H1 per page" is somewhat obvious for most documentation generators

**What to copy:**
- Teaching the agent to grep for unfinished work (`grep -r "<FIXME"`). This is unusual and powerful — it makes the agent check the broader state of the project before editing.

---

## Example 8 — A backend API service (Go)

**Context:** A Go HTTP API service, ~40,000 lines, used in production by ~50 customers.

```markdown
# AGENTS.md

## Validation
- `go test ./...`
- `golangci-lint run`
- `go mod tidy && git diff --exit-code go.mod go.sum`

## Endpoints
- Routes registered in `internal/server/routes.go`
- Handlers in `internal/handlers/<resource>.go`
- Middleware in `internal/middleware/`

## Database
- Postgres; queries via `sqlx`
- Migrations in `migrations/`, ordered by timestamp
- Never raw SQL in handlers — wrap in `internal/db/`

## API stability
- v1 endpoints in `internal/api/v1/`
- Breaking v1 changes require a deprecation notice in `CHANGELOG.md`
- New endpoints default to v2 in `internal/api/v2/`
```

**What works:**
- The "never raw SQL in handlers" rule prevents a specific failure mode (SQL injection risk, inconsistent query patterns)
- The version-stability section is project-specific and important — agents will not infer this from the code structure
- `go mod tidy && git diff --exit-code go.mod go.sum` is a tidy trick — it catches accidental dependency additions

**What does not:**
- The middleware-internal path is conventional but somewhat redundant with the routes-and-handlers notes

**What to copy:**
- The pattern of separating **stability rules** from **structure rules**. Endpoints and migrations have different lifetimes and need different kinds of instructions.

---

## Example 9 — A library with semantic versioning (TypeScript)

**Context:** A TypeScript utility library, ~2,000 lines, ~3,000 GitHub stars, published on npm.

```markdown
# AGENTS.md

## Validation
- `npm test`
- `npm run lint`
- `npm run typecheck`
- `npm run build`

## Public API
- Anything exported from `src/index.ts` is public
- Breaking changes need a major version bump
- Add an entry to `CHANGELOG.md` under "Unreleased"

## Dependencies
- Adding a new dep: justify in the PR description
- Prefer zero-dep solutions for small utilities
- Pin dev deps to minor versions, not patches

## Tests
- New exports need at least one test
- Test files next to source: `src/<name>.test.ts`
- Use `vitest`, not `jest`
```

**What works:**
- The "prefer zero-dep solutions" rule prevents dependency bloat, which is a common agent failure mode (agents reach for libraries too eagerly)
- The major-version-bump convention is documented in three places — package.json, semver, and AGENTS.md
- "Adding a new dep: justify in the PR description" makes the agent's output more reviewable

**What does not:**
- "Pin dev deps to minor versions" is a style choice that varies by team

**What to copy:**
- The "prefer zero-dep solutions" rule. Library maintainers know that every dep is a maintenance liability; agents do not, by default.

---

## Example 10 — A web app with strict conventions (Vue 3)

**Context:** A Vue 3 + Pinia + Vue Router web application, ~30,000 lines, internal company tool.

```markdown
# AGENTS.md

## Validation
- `npm run dev` — starts on :3000
- `npm test`
- `npm run lint` — runs ESLint + Prettier
- `npm run typecheck` — runs vue-tsc

## File layout
- One component per file; filename in PascalCase
- Composables in `src/composables/`, prefixed with `use`
- Stores in `src/stores/`, one per domain
- Routes in `src/router/index.ts`

## Conventions
- `<script setup lang="ts">` for all components
- Define props with `defineProps<Props>()`, not `withDefaults`
- Avoid `any` — use `unknown` and narrow

## Things to avoid
- Do not introduce a CSS-in-JS library
- Do not add state libraries other than Pinia
- Do not use Options API
```

**What works:**
- The "Things to avoid" section is excellent — agents benefit from explicit prohibitions more than from affirmative guidance
- The `<script setup lang="ts">` rule prevents a specific Vue failure mode (mixing Options API and Composition API)
- Listing "no CSS-in-JS library, no other state libs" prevents agent drift on tool choices

**What does not:**
- The `vue-tsc` mention assumes the agent knows about Vue's TypeScript tooling

**What to copy:**
- A dedicated "Things to avoid" section. Most AGENTS.md files focus on what to do. Listing what **not** to do is equally important and rare.

---

## Common patterns across all ten

Reading these side by side, four patterns recur:

### 1. Validation commands come first

Every useful AGENTS.md lists `npm test` / `cargo test` / `go test ./...` in the first or second section. Agents that see validation commands early reach for them before handing back changes.

### 2. File maps are short, not exhaustive

The best file maps are 3–7 lines. They name the directories that matter and the boundaries that should not be crossed. Full architecture docs belong in separate files.

### 3. Project-specific rules dominate

The lines that make a difference are project-specific: "Never unwrap in library code," "Always include a downgrade migration," "Do not introduce CSS-in-JS libraries." Generic advice ("write clean code") adds nothing.

### 4. Prohibitions get their own section

The strongest examples include a "Things to avoid" or "Do not..." section. Agents, like humans, learn more from explicit prohibitions than from positive guidance.

---

## Build your own AGENTS.md from this

The pattern is the same regardless of language:

1. **First section: validation commands.** Exact commands, one per line, named in the order an agent should run them.
2. **Second section: file map.** Which directories matter, which files are risky, which boundaries to respect.
3. **Third section: project-specific rules.** The conventions that are real in your repo, not generic best practices.
4. **Fourth section (optional): prohibitions.** The things to not do — usually 5–10 lines.

Aim for 30–80 lines total. Anything longer gets skimmed. Anything shorter leaves the agent guessing.

The full template lives at [/agents-md-template/](/agents-md-template/) — copy it, then write the validation commands and the file map for your own repo.

---

## FAQ

### What makes a good AGENTS.md example?

Three things: it names the exact validation commands, it lists which files and directories matter and why, and it stays under about 80 lines so an agent will actually read it in full. Examples that include a lot of generic advice ("follow best practices", "write clean code") are weak — agents ignore generic advice.

### Where can I find real AGENTS.md files to study?

Start with the AGENTS.md file in any open-source repository that uses Claude Code, Codex, or Cursor in its development workflow. The best examples live in repositories whose maintainers run coding agents themselves — those files are usually shorter, sharper, and more honest than AGENTS.md files written for marketing.

### How long should an AGENTS.md be?

Most useful AGENTS.md files are between 20 and 80 lines. Anything over 150 lines is too long — agents treat long files as reference material, not as instructions. A short, specific AGENTS.md will be read in full; a long, generic one will be partially skimmed.

### Should AGENTS.md include architecture documentation?

Only the orientation kind. A 5-line map of which directories contain what is useful. A full architecture document is not — it belongs in a separate file the agent can read on demand. AGENTS.md should be the index, not the archive.

### What is the most common mistake in real AGENTS.md files?

Mixing generic advice with specific instructions. Lines like "write clean, tested code" or "follow best practices" take up space without constraining agent behavior. Every line should answer a question the agent would otherwise have to guess at — and most agents will not guess wrong on the obvious things.

### Can I copy another project's AGENTS.md?

You can, but you should rewrite the validation commands and file map for your own repository. Validation commands are the most project-specific part. Everything else — the structure, the tone, the conventions — is worth copying.

### How is AGENTS.md different from a README?

README is for humans deciding whether to use the project. AGENTS.md is for coding agents deciding how to work in it. The two should not be redundant — README explains what the project is and how to use it; AGENTS.md explains how to validate changes, which files matter, and which conventions to follow.

---

## Related pages

- [How to Write an AGENTS.md That Actually Works](/blog/how-to-write-agents-md/) — the writing guide for your own file
- [AGENTS.md Template](/agents-md-template/) — copy and adapt
- [What Is an Agent-Ready Repository?](/agent-ready-repository/) — the broader pattern AGENTS.md fits into
- [AGENTS.md vs CLAUDE.md vs .cursorrules vs copilot-instructions.md](/blog/coding-agent-context-file-formats/) — which format to pick
- [`repository-harness` on GitHub](https://github.com/hoangnb24/repository-harness) — the open-source implementation

*See also: [Coding Agents Need Better Repositories, Not Just Better Prompts](/blog/coding-agents-need-better-repositories/) — the category argument. [Context Engineering for Coding Agents](/context-engineering-for-coding-agents/) — the framework AGENTS.md fits into.*