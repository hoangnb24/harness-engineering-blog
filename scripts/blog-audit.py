#!/usr/bin/env python3
"""Audit CodeHarness static blog conversion, internal links, schema, and feed tag CSS.

Run from the Astro project root after `npm run build`:
    python3 scripts/blog-audit.py --owner hoangnb24

Exits non-zero when a public source page fails the minimum growth checklist.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(Path.cwd()))
    except ValueError:
        return str(p)


def route_for_source(path: Path) -> str:
    relp = path.relative_to(Path("src/pages"))
    if relp.name == "index.astro" or relp.name == "index.md":
        parts = relp.parts[:-1]
    else:
        parts = relp.with_suffix("").parts
    return "/" + "/".join(parts) + ("/" if parts else "")


def dist_html_for_route(route: str) -> Path:
    if route == "/":
        return Path("dist/index.html")
    return Path("dist") / route.strip("/") / "index.html"


def markdown_links(content: str) -> list[str]:
    raw = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    return [url.strip() for _, url in raw]


def astro_links(content: str) -> list[str]:
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    # Capture simple object-array links used by feeds, e.g. link: '/blog/foo/'
    feed_links = re.findall(r"link:\s*[\"']([^\"']+)[\"']", content)
    return [u.strip() for u in hrefs + feed_links]


def is_internal(url: str) -> bool:
    return url.startswith("/") and not url.startswith("//") and not url.startswith("/#") and url != "/"


def has_faq_section(content: str) -> bool:
    return bool(re.search(r"^##\s+(FAQ|Frequently Asked)", content, flags=re.I | re.M))


def iter_jsonld(html: str) -> Iterable[object]:
    scripts = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, flags=re.S | re.I)
    for raw in scripts:
        text = raw.strip()
        if not text:
            continue
        # Empty placeholder scripts are ignored, but literal Astro directives are a failure elsewhere.
        try:
            yield json.loads(text)
        except Exception:
            yield {"__invalid_jsonld__": text[:120]}


def jsonld_types(doc: object) -> set[str]:
    out: set[str] = set()
    if isinstance(doc, dict):
        t = doc.get("@type")
        if isinstance(t, str):
            out.add(t)
        graph = doc.get("@graph")
        if isinstance(graph, list):
            for item in graph:
                out |= jsonld_types(item)
    elif isinstance(doc, list):
        for item in doc:
            out |= jsonld_types(item)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--owner", default="hoangnb24", help="GitHub owner expected in repo CTAs")
    ap.add_argument("--repo", default="repository-harness", help="GitHub repo expected in CTAs")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    src_root = Path("src/pages")
    layout = Path("src/layouts/BaseLayout.astro")
    failures: list[str] = []
    rows: list[str] = []

    if not src_root.exists():
        print("FAIL: run from the Astro project root; src/pages does not exist", file=sys.stderr)
        return 2

    expected_repo = f"github.com/{args.owner}/{args.repo}"

    for p in sorted(list(src_root.glob("**/*.md")) + list(src_root.glob("**/*.astro"))):
        content = p.read_text(errors="ignore")
        if p.suffix == ".md":
            links = markdown_links(content)
        else:
            links = astro_links(content)
        internal = [u for u in links if is_internal(u)]
        repo_links = [u for u in links if expected_repo in u]
        route = route_for_source(p)
        html_path = dist_html_for_route(route)
        html = html_path.read_text(errors="ignore") if html_path.exists() else ""
        docs = list(iter_jsonld(html))
        types: set[str] = set()
        invalid_jsonld = False
        for d in docs:
            if isinstance(d, dict) and "__invalid_jsonld__" in d:
                invalid_jsonld = True
            types |= jsonld_types(d)

        problems: list[str] = []
        if len(internal) < 2:
            problems.append(f"only {len(internal)} internal links")
        if len(repo_links) < 1:
            problems.append("missing repository-harness GitHub CTA")
        if p.suffix == ".md" and "Article" not in types:
            problems.append("missing valid Article JSON-LD in dist")
        if has_faq_section(content) and "FAQPage" not in types:
            problems.append("FAQ section without valid FAQPage JSON-LD in dist")
        if invalid_jsonld:
            problems.append("invalid JSON-LD script in dist")
        if "harness-experimental" in content:
            problems.append("public source still references old repo name harness-experimental")
        if "TODO" in html or "Distribution snippets" in html or "Internal link targets" in html or "Suggested structured data" in html:
            problems.append("public dist appears to contain planning/TODO text")

        status = "FAIL" if problems else "OK"
        rows.append(f"{status:4} {rel(p)} route={route} internal={len(internal)} repo_cta={len(repo_links)} schema={','.join(sorted(types)) or '-'}")
        if problems:
            failures.extend(f"{rel(p)}: {problem}" for problem in problems)

    # Feed tag CSS coverage: every tag-* class used in source feeds should be defined in BaseLayout.
    used_tags: set[str] = set()
    for p in [Path("src/pages/index.astro"), Path("src/pages/blog/index.astro")]:
        if p.exists():
            used_tags.update(re.findall(r"[\"'](tag-[a-z0-9-]+)[\"']", p.read_text(errors="ignore")))
    css_tags: set[str] = set(re.findall(r"\.((?:tag-[a-z0-9-]+))\b", layout.read_text(errors="ignore") if layout.exists() else ""))
    missing_css = sorted(used_tags - css_tags)
    if missing_css:
        failures.append("missing tag CSS classes: " + ", ".join(missing_css))

    if not args.quiet:
        print("CodeHarness blog audit")
        print("======================")
        for row in rows:
            print(row)
        print()
        print(f"Feed tag classes used: {', '.join(sorted(used_tags)) or '-'}")
        print(f"Feed tag classes defined: {', '.join(sorted(css_tags)) or '-'}")
        print()

    if failures:
        print("FAILURES:")
        for f in failures:
            print("- " + f)
        return 1
    print("PASS: all public source pages meet the minimum link/schema/conversion checklist.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
