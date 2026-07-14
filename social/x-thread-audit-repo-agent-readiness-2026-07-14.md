# X thread draft — agent-readiness audit post

Date: 2026-07-14
Status: drafted, not posted
Reason: X API returned `CreditsDepleted` on the root post request.
Target post: https://codeharness.kuckit.dev/blog/audit-repo-agent-readiness/
Repo CTA: https://github.com/hoangnb24/repository-harness

## Error

```json
{
  "account_id": 1949003093120876544,
  "title": "CreditsDepleted",
  "detail": "Your enrolled account [1949003093120876544] does not have any credits to fulfill this request.",
  "type": "https://api.twitter.com/2/problems/credits"
}
```

## Tweet 1

X weighted: 205 / 280

```text
Most coding-agent failures are repo-context failures.

I published a practical agent-readiness audit: 7 surfaces to score before you trust Claude Code, Codex, Cursor, or any agent with bigger repo changes.
```

## Tweet 2

X weighted: 230 / 280

```text
The audit checks:

1. orientation
2. AGENTS.md quality
3. validation commands
4. safety boundaries
5. durable context
6. handoff quality
7. maintenance loop

A repo with good code can still be bad for agents if these are implicit.
```

## Tweet 3

X weighted: 161 / 280

```text
If you want a copyable baseline, repository-harness has the AGENTS.md template and repo conventions I use for the audit.

github.com/hoangnb24/repository-harness
```
