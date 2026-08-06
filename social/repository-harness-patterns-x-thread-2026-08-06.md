# X thread draft — Repository Harness Patterns

**Date:** 2026-08-06
**Status:** Drafted, not posted
**Reason:** X API write returned HTTP 402 `credits depleted`.
**Canonical article:** https://codeharness.kuckit.dev/blog/repository-harness-patterns/
**Repository CTA:** https://github.com/hoangnb24/repository-harness

## Tweet 1 — hook

**X-weighted count:** 257 / 280

Most “AI coding agent problems” are not one problem. They are missing controllers in the repository: no router, no task boundary, no source-of-truth map, no proof contract, no safe recovery.

I turned those recurring gaps into 9 repository harness patterns.

## Tweet 2 — key takeaway

**X-weighted count:** 254 / 280

The patterns follow the work. First orient with a Repository Router. Bound the task and authority. Map sources of truth and preserve decisions. Match claims to validation evidence. Then checkpoint progress and recover without duplicating external writes.

## Tweet 3 — repository CTA

**X-weighted count:** 270 / 280

A good harness does not make agents “smarter.” It makes the next correct decision discoverable and the completion claim provable.

repository-harness gives Claude Code, Codex, Cursor, and other agents that operating layer:
https://github.com/hoangnb24/repository-harness

## Exact API error

```json
{
  "detail": "credits depleted",
  "status": 402,
  "title": "Payment Required",
  "type": "https://api.x.com/2/problems/credits-depleted"
}
```

The root tweet failed, so no replies were attempted and no public X URLs exist.
