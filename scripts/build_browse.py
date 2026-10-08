#!/usr/bin/env python3
"""Deterministically publish a readable browse/ site from catalog Markdown.

No network calls, LLM, or third-party packages. catalog/ remains authoritative.
"""
from collections import defaultdict
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- github-radar:enrichment:start -->"
END = "<!-- github-radar:enrichment:end -->"
JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)


def taxonomy_names(root: Path) -> dict[str, dict[str, str]]:
    names = {"domains": {}, "repository_types": {}}
    section = None
    for line in (root / "taxonomy.yaml").read_text(encoding="utf-8").splitlines():
        if line in ("domains:", "repository_types:"):
            section = line[:-1]
        elif line and not line.startswith((" ", "#")):
            section = None
        elif section and (match := re.fullmatch(r'  ([a-z0-9-]+): "(.*)"', line)):
            names[section][match[1]] = match[2]
    return names


def read_record(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta = {}
    if text.startswith("---\n"):
        front = text.split("---\n", 2)[1]
        for line in front.splitlines():
            if ":" not in line or line.startswith(" "):
                continue
            key, value = line.split(":", 1)
            try:
                meta[key] = json.loads(value.strip())
            except json.JSONDecodeError:
                meta[key] = value.strip()
    enrichment = {}
    if START in text and END in text:
        managed = text.split(START, 1)[1].split(END, 1)[0]
        match = JSON_BLOCK.search(managed)
        if match:
            try:
                enrichment = json.loads(match[1])
            except json.JSONDecodeError:
                pass
    return {
        "name": f"{path.parent.name}/{path.stem}",
        "path": path,
        "url": meta.get("url") or f"https://github.com/{path.parent.name}/{path.stem}",
        "description": meta.get("description") or "",
        "summary": enrichment.get("summary") or meta.get("description") or "No description available.",
        "domain": enrichment.get("primary_domain") or "unclassified",
        "type": enrichment.get("repository_type") or "unclassified",
        "capabilities": enrichment.get("capabilities") or [],
        "technologies": enrichment.get("technologies") or [],
        "enriched": bool(enrichment.get("summary")),
    }


def safe_line(value: object) -> str:
    """Use untrusted upstream text as literal single-line prose."""
    value = re.sub(r"<[^>]*>", "", str(value))
    value = re.sub(r"[\r\n\t]+", " ", value)
    return re.sub(r"\s+", " ", value).strip().replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def item(record: dict, prefix: str = "../") -> str:
    link = f"{prefix}catalog/{record['path'].parent.name}/{record['path'].name}"
    tags = ", ".join(safe_line(x) for x in record["capabilities"][:4])
    detail = safe_line(record["summary"])
    suffix = f" · **Does:** {tags}" if tags else ""
    if not record["enriched"]:
        suffix += " · *Awaiting enrichment*"
    return f"- **[{safe_line(record['name'])}]({link})** — {detail}{suffix}"


def build(root: Path = ROOT) -> None:
    records = [read_record(path) for path in sorted((root / "catalog").glob("*/*.md"))]
    records = [r for r in records if r["path"].parent.name.casefold() != "andythefactory"]
    records.sort(key=lambda r: r["name"].casefold())
    labels = taxonomy_names(root)
    output = root / "browse"
    domain_dir = output / "domains"
    domain_dir.mkdir(parents=True, exist_ok=True)
    domains = defaultdict(list)
    types = defaultdict(list)
    for record in records:
        domains[record["domain"]].append(record)
        types[record["type"]].append(record)

    # Remove only our generated domain pages.
    for stale in domain_dir.glob("*.md"):
        stale.unlink()
    index = [
        "# GitHub Radar — Explore",
        "",
        "A human-readable, automatically generated guide to starred repositories.",
        "All descriptions come from the stored catalog; **no AI calls are made to build these pages**.",
        "",
        f"**{len(records)} repositories** · **{sum(r['enriched'] for r in records)} enriched**"
        f" · **{sum(not r['enriched'] for r in records)} awaiting enrichment**",
        "",
        "## Explore by subject",
        "",
    ]
    for domain, group in sorted(domains.items(), key=lambda pair: labels["domains"].get(pair[0], pair[0]).casefold()):
        title = labels["domains"].get(domain, "Unclassified" if domain == "unclassified" else domain.replace("-", " ").title())
        index.append(f"- [{title}](domains/{domain}.md) — {len(group)} repositories")
        lines = [f"# {title}", "", f"{len(group)} repositories", "", "[← Back to overview](../README.md)", ""]
        lines += [item(r, "../../") for r in group]
        (domain_dir / f"{domain}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    index += ["", "## Explore by repository type", "", "[Browse all types](types.md)", "",
              "## All repositories", "", "[Alphabetical directory](all.md)", "",
              "## How to search", "",
              "Use GitHub Code Search with `repo:AndyTheFactory/github-radar` and keywords.",
              "Entries without Copilot enrichment still appear with their original descriptions.", ""]
    (output / "README.md").write_text("\n".join(index), encoding="utf-8")

    type_lines = ["# Browse by repository type", "", "[← Back to overview](README.md)", ""]
    for type_id, group in sorted(types.items(), key=lambda pair: labels["repository_types"].get(pair[0], pair[0]).casefold()):
        title = labels["repository_types"].get(type_id, "Unclassified" if type_id == "unclassified" else type_id)
        type_lines += [f"## {title} ({len(group)})", ""]
        type_lines += [item(r) for r in group]
        type_lines.append("")
    (output / "types.md").write_text("\n".join(type_lines), encoding="utf-8")

    all_lines = ["# All repositories (A–Z)", "", "[← Back to overview](README.md)", ""]
    all_lines += [item(r) for r in records]
    all_lines.append("")
    (output / "all.md").write_text("\n".join(all_lines), encoding="utf-8")


if __name__ == "__main__":
    build()
