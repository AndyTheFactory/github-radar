#!/usr/bin/env python3
"""Build readable GitHub Markdown browse pages deterministically from catalog/.

The generated browse/ folder is disposable. No API, LLM, or dependencies.
"""
from collections import defaultdict
import json
from pathlib import Path
import re
import textwrap
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- github-radar:enrichment:start -->"
END = "<!-- github-radar:enrichment:end -->"
JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)

TYPE_GROUPS = (
    ("Libraries & frameworks", "code you import", ("library",)),
    ("Apps & command-line tools", "things you run", ("application", "service")),
    ("Curated lists & collections", "reading lists, datasets, notebooks", ("collection", "dataset")),
    ("Guides & tutorials", "documentation and walkthroughs", ("resource", "template")),
    ("Research code", "paper implementations and experiments", ("research",)),
    ("Games", "playable games", ("game",)),
    ("Hardware & firmware", "physical and embedded projects", ("hardware",)),
    ("Other projects", "other or not yet classified", ("other", "unclassified")),
)
TYPE_LABELS = {type_id: (heading, explanation)
               for heading, explanation, ids in TYPE_GROUPS for type_id in ids}


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
        "summary": enrichment.get("summary") or meta.get("description") or "No description available.",
        "domain": enrichment.get("primary_domain") or "unclassified",
        "type": enrichment.get("repository_type") or "unclassified",
        "capabilities": enrichment.get("capabilities") or [],
        "enriched": bool(enrichment.get("summary")),
    }


def safe_text(value: object) -> str:
    """Render untrusted metadata as literal one-line Markdown text."""
    value = re.sub(r"<[^>]*>", "", str(value))
    value = re.sub(r"[\r\n\t]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    for character in ("\\", "`", "*", "_", "[", "]", "<", ">", "|"):
        value = value.replace(character, "\\" + character)
    return value


def excerpt(value: str, width: int = 145) -> str:
    """Prefer the opening sentence, but cap long descriptions without inventing text."""
    normalized = re.sub(r"\s+", " ", str(value)).strip()
    sentence = re.split(r"(?<=[.!?])\s+(?=[A-Z])", normalized, maxsplit=1)[0]
    selected = sentence if len(sentence) <= width else normalized
    if len(selected) > width:
        selected = textwrap.shorten(selected, width=width, placeholder="…")
    return safe_text(selected)


def sort_key(record: dict):
    owner, name = record["name"].split("/", 1)
    return (name.casefold(), owner.casefold())


def upstream_link(record: dict) -> str:
    # Catalog entries from GitHub have a canonical owner/repository identity.
    # Avoid injecting an arbitrary upstream URL from untrusted metadata.
    owner, name = record["name"].split("/", 1)
    return f"https://github.com/{quote(owner)}/{quote(name)}"


def compact_item(record: dict) -> str:
    owner, name = record["name"].split("/", 1)
    return f"- **[{safe_text(name)}]({upstream_link(record)})** <sub>{safe_text(owner)}</sub> — {excerpt(record['summary'])}"


def detailed_item(record: dict, catalog_prefix: str) -> str:
    owner, name = record["name"].split("/", 1)
    url = f"{catalog_prefix}catalog/{quote(owner)}/{quote(name)}.md"
    tags = " ".join(f"`{safe_text(tag)}`" for tag in record["capabilities"][:3])
    note = f"{tags} · " if tags else ""
    if not record["enriched"]:
        note += "*Awaiting enrichment* · "
    return (
        f"- **[{safe_text(name)}]({upstream_link(record)})** <sub>{safe_text(owner)}</sub><br>\n"
        f"  {excerpt(record['summary'])}<br>\n"
        f"  <sub>{note}[catalog entry]({url})</sub>"
    )


def grouped_types(records: list[dict]):
    grouped = defaultdict(list)
    for record in records:
        group, _ = TYPE_LABELS.get(record["type"], TYPE_LABELS["other"])
        grouped[group].append(record)
    return [(name, description, sorted(grouped[name], key=sort_key))
            for name, description, _ in TYPE_GROUPS if grouped[name]]


def type_sections(records: list[dict], prefix: str) -> list[str]:
    groups = grouped_types(records)
    lines = ["**Jump to** " + " · ".join(
        f"[{name}](#{slug(name)}) ({len(group)})" for name, _, group in groups), ""]
    for name, explanation, group in groups:
        lines += [f"## {name}", "", f"<sub>{len(group)} repositories · {explanation}</sub>", ""]
        lines += [detailed_item(record, prefix) for record in group]
        lines.append("")
    return lines


def slug(value: str) -> str:
    # GitHub heading anchor conventions; remove punctuation, retain words and hyphens.
    return re.sub(r"[^a-z0-9 -]", "", value.casefold()).replace(" ", "-")


def build(root: Path = ROOT) -> None:
    records = [read_record(p) for p in (root / "catalog").glob("*/*.md")
               if p.parent.name.casefold() != "andythefactory"]
    records.sort(key=sort_key)
    labels = taxonomy_names(root)
    output = root / "browse"
    domains_dir = output / "domains"
    domains_dir.mkdir(parents=True, exist_ok=True)
    domains = defaultdict(list)
    for record in records:
        domains[record["domain"]].append(record)

    for stale in domains_dir.glob("*.md"):
        stale.unlink()

    sorted_domains = sorted(domains.items(), key=lambda pair: (
        -len(pair[1]), labels["domains"].get(pair[0], pair[0]).casefold()
    ))
    index = [
        "# GitHub Radar", "",
        "Repositories starred by [@AndyTheFactory](https://github.com/AndyTheFactory), "
        "sorted by subject. Rebuilt automatically after every sync.", "",
        f"**{len(records)} repositories** · {len(domains)} subjects · "
        + ("all summarised" if all(r["enriched"] for r in records) else
           f"{sum(r['enriched'] for r in records)} summarised · "
           f"{sum(not r['enriched'] for r in records)} awaiting enrichment"),
        "", "## Browse by subject", "",
        "| Subject | Repositories |", "|:--|--:|",
    ]
    for domain, group in sorted_domains:
        title = labels["domains"].get(domain, "Unknown / Unclassified"
                                      if domain == "unclassified" else domain.replace("-", " ").title())
        index.append(f"| [{safe_text(title)}](domains/{domain}.md) | {len(group)} |")
        lines = [
            f"<sub>[GitHub Radar](../README.md) / {safe_text(title)}</sub>", "",
            f"# {safe_text(title)}", "",
            f"{len(group)} repositories, grouped by what kind of thing they are.", "",
        ]
        lines += type_sections(group, "../../")
        lines += ["<sub>[↑ Back to top](#"+slug(title)+") · "
                  "[All subjects](../README.md) · [A–Z directory](../all.md)</sub>", ""]
        (domains_dir / f"{domain}.md").write_text("\n".join(lines), encoding="utf-8")

    search = "https://github.com/search?q=repo%3AAndyTheFactory%2Fgithub-radar&type=code"
    index += ["", "## Other ways in", "",
              "- **[By kind](types.md)** — libraries, apps, curated lists, guides, research code",
              "- **[A–Z directory](all.md)** — every repository on one page, by name",
              f"- **[Search]({search})** — GitHub code search across every catalog entry",
              "", "<sub>Generated by `scripts/build_browse.py` — do not edit by hand.</sub>", ""]
    (output / "README.md").write_text("\n".join(index), encoding="utf-8")

    types = ["<sub>[GitHub Radar](README.md) / By kind</sub>", "",
             "# Browse by kind", "",
             f"All {len(records)} repositories, grouped by repository type.", ""]
    types += type_sections(records, "../")
    types += ["<sub>[↑ Back to top](#browse-by-kind) · [All subjects](README.md)</sub>", ""]
    (output / "types.md").write_text("\n".join(types), encoding="utf-8")

    letters = defaultdict(list)
    for record in records:
        name = record["name"].split("/", 1)[1]
        letter = name[0].upper() if name and name[0].isalpha() else "#"
        letters[letter].append(record)
    nav = " · ".join(f"[{letter}](#{'other' if letter == '#' else letter.casefold()})"
                     for letter in sorted(letters))
    all_lines = ["<sub>[GitHub Radar](README.md) / A–Z</sub>", "",
                 "# A–Z directory", "", f"All {len(records)} repositories, sorted by repository name.",
                 "", f"**{nav}**", ""]
    for letter in sorted(letters):
        all_lines += [f"## {'Other' if letter == '#' else letter}", ""]
        all_lines += [compact_item(r) for r in letters[letter]]
        all_lines.append("")
    all_lines += ["<sub>[↑ Back to top](#az-directory) · [All subjects](README.md)</sub>", ""]
    (output / "all.md").write_text("\n".join(all_lines), encoding="utf-8")


if __name__ == "__main__":
    build()
