#!/usr/bin/env python3
"""Import GitHub stars into an append-only Markdown catalog (stdlib only)."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

API = "https://api.github.com"
ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"
INDEX = ROOT / "CATALOG.md"
USER_AGENT = "github-radar/1.0"
MAX_EXCERPT = 2500


def api_get(path: str, token: str, *, raw: bool = False) -> object:
    headers = {
        "Accept": "application/vnd.github.raw+json" if raw else "application/vnd.github.star+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(API + path, headers=headers)
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                data = response.read()
                return data.decode("utf-8") if raw else json.loads(data)
        except HTTPError as exc:
            if exc.code in (403, 429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("GitHub API request failed")


def iter_stars(username: str, token: str):
    page = 1
    while True:
        payload = api_get(
            f"/users/{quote(username)}/starred?sort=created&direction=desc&per_page=100&page={page}",
            token,
        )
        if not isinstance(payload, list):
            raise ValueError("Unexpected GitHub starred repositories response")
        for item in payload:
            if isinstance(item, dict) and isinstance(item.get("repo"), dict):
                yield item["repo"], item.get("starred_at")
            elif isinstance(item, dict) and "full_name" in item:
                yield item, None
        if len(payload) < 100:
            break
        page += 1


def catalog_path(full_name: str) -> Path:
    components = full_name.split("/")
    if len(components) != 2 or any(
        not re.fullmatch(r"[A-Za-z0-9_.-]+", component) or component in (".", "..")
        for component in components
    ):
        raise ValueError(f"Unsafe repository name: {full_name!r}")
    return CATALOG / components[0] / (components[1] + ".md")


def clean_readme(value: str) -> str:
    lines = []
    for line in value.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("![", "<img", "<picture", "<svg", "<!--")):
            continue
        if stripped.startswith(("[![", "<div", "</div", "<a ", "</a")):
            continue
        if stripped.startswith("```"):
            continue
        lines.append(re.sub(r"<[^>]+>", "", line).strip())
        if sum(len(x) for x in lines) >= MAX_EXCERPT:
            break
    text = "\n".join(lines)
    return text[:MAX_EXCERPT].strip()


def yaml_scalar(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def render(repo: dict, starred_at: str | None, readme: str) -> str:
    name = repo["full_name"]
    topics = repo.get("topics") or []
    fields = {
        "repository": name,
        "github_id": repo.get("id"),
        "url": repo.get("html_url") or f"https://github.com/{name}",
        "description": repo.get("description") or "",
        "starred_at": starred_at,
        "language": repo.get("language"),
        "topics": topics,
        "homepage": repo.get("homepage") or "",
        "license": (repo.get("license") or {}).get("spdx_id"),
        "archived": bool(repo.get("archived")),
    }
    frontmatter = "\n".join(f"{key}: {yaml_scalar(value)}" for key, value in fields.items())
    description = (repo.get("description") or "No description provided.").replace("\n", " ")
    excerpt = clean_readme(readme)
    quoted = "\n".join(f"> {line}" if line else ">" for line in excerpt.splitlines())
    section = f"## README excerpt\n\n{quoted}\n\n" if quoted else ""
    return (
        f"---\n{frontmatter}\n---\n\n# {name}\n\n"
        f"{description}\n\n"
        f"**GitHub:** {fields['url']}\n\n"
        f"{section}"
        "## Personal notes\n\n"
        "<!-- Optional. Manual notes are never overwritten by sync. -->\n"
    )


def build_index() -> None:
    paths = sorted(CATALOG.glob("*/*.md"), key=lambda p: str(p).casefold())
    lines = [
        "# Catalog",
        "",
        f"**{len(paths)} repositories archived.**",
        "",
        "Search the repository using GitHub Code Search or browse entries below.",
        "",
    ]
    for path in paths:
        full_name = f"{path.parent.name}/{path.stem}"
        lines.append(f"- [{full_name}]({path.as_posix().removeprefix(str(ROOT) + '/') if path.is_absolute() else path.as_posix()})")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sync(username: str, token: str, max_new: int = 50) -> tuple[int, int]:
    if max_new < 1:
        raise ValueError("--max-new must be at least 1")
    new = 0
    checked = 0
    CATALOG.mkdir(parents=True, exist_ok=True)
    for repo, starred_at in iter_stars(username, token):
        checked += 1
        path = catalog_path(repo["full_name"])
        if path.exists():
            continue
        try:
            readme = api_get(
                f"/repos/{quote(repo['full_name'], safe='/')}/readme", token, raw=True
            )
        except HTTPError as exc:
            if exc.code != 404:
                print(f"Warning: README unavailable for {repo['full_name']}: {exc}", file=sys.stderr)
            readme = ""
        except (URLError, TimeoutError) as exc:
            print(f"Warning: README unavailable for {repo['full_name']}: {exc}", file=sys.stderr)
            readme = ""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(repo, starred_at, str(readme)), encoding="utf-8")
        print(f"Added {repo['full_name']}")
        new += 1
        if new >= max_new:
            break
    build_index()
    return new, checked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", default="AndyTheFactory")
    parser.add_argument("--max-new", type=int, default=50)
    args = parser.parse_args()
    try:
        new, checked = sync(args.user, os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or "", args.max_new)
    except (ValueError, HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"Sync failed: {exc}", file=sys.stderr)
        return 1
    print(f"Done: {new} new entries, {checked} stars checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
