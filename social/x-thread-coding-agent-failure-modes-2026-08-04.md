# X thread draft — Coding-Agent Failure Modes

**Status:** Drafted, not posted
**Date:** 2026-08-04
**Account:** @TuBaKhuym via `--app growth`
**Article:** https://codeharness.kuckit.dev/blog/coding-agent-failure-modes/
**Repository:** https://github.com/hoangnb24/repository-harness

## Tweet 1 — Hook

Most coding-agent failures get called hallucinations too early.

The useful question is: what was the first wrong decision?

Wrong task, wrong source of truth, scope leakage, context loss, weak validation, and unsafe recovery need different fixes.

**X-weighted count:** 247 / 280

## Tweet 2 — Key takeaway

A reviewer can catch a bad diff. That does not prevent the next agent from making the same mistake.

Diagnose the missing controller, repair the narrowest authoritative source, add the earliest useful check, then rerun without the corrective prompt.

https://codeharness.kuckit.dev/blog/coding-agent-failure-modes/

**X-weighted count:** 274 / 280

## Tweet 3 — Repository CTA

I published a taxonomy of 10 coding-agent failure modes, with symptoms, root causes, repair locations, and fresh-session tests.

The open-source starting point for durable repo context and evidence-based handoffs:
https://github.com/hoangnb24/repository-harness

**X-weighted count:** 237 / 280

## Posting probe

The required one-time discovery/write-availability probe was executed with:

```text
xurl --app growth search 'coding agent context failure' -n 3
```

It failed before any post request was attempted. Exact API response:

```json
{
  "detail": "credits depleted",
  "status": 402,
  "title": "Payment Required",
  "type": "https://api.x.com/2/problems/credits-depleted"
}
```

Per the X distribution runbook, the account-level credit failure makes discovery and posting unavailable for this run. No tweet IDs or public URLs were created. Do not attempt replies until a future one-time probe succeeds.
