# X thread draft — AGENTS.md before-and-after case study

Date: 2026-07-23
Status: drafted, not posted
Reason: X API returned `credits depleted` with HTTP status `402` on the root post request.
Target post: https://codeharness.kuckit.dev/blog/agents-md-before-after-case-study/
Repo CTA: https://github.com/hoangnb24/repository-harness

## Exact API error

```json
{
  "detail": "credits depleted",
  "status": 402,
  "title": "Payment Required",
  "type": "https://api.x.com/2/problems/credits-depleted"
}
```

## Tweet 1

X weighted: 249 / 280

```text
A good AGENTS.md is not finished when it is first written.

I traced repository-harness from its first 75-line operating manual to today's 32-line decision router. The lesson wasn't “shorter is better.” It was: keep the decisions, move the handbook.
```

## Tweet 2

X weighted: 232 / 280

```text
The evolution added 5 high-leverage rules:

• read-only vs mutating outcomes
• bounded vs durable work
• explicit product authority
• pause conditions
• evidence before completion

The root file became a router, not a second README.
```

## Tweet 3

X weighted: 220 / 280

```text
The full case study follows 8 real commits and separates evidence from claims:

https://codeharness.kuckit.dev/blog/agents-md-before-after-case-study/

Pattern + templates: https://github.com/hoangnb24/repository-harness
```
