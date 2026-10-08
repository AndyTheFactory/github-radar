#!/usr/bin/env python3
"""Create browsable indexes from validated catalog enrichment blocks."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "categories"

def build(root=ROOT):
    entries = {}
    for file in sorted((root / "catalog").glob("*/*.md")):
        text = file.read_text(encoding="utf-8")
        match = re.search(r'<!-- github-radar:enrichment:start -->.*?\x60\x60\x60json\s*(\{.*?\})\s*\x60\x60\x60', text, re.S)
        if not match:
            continue
        try:
            info = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        for domain in [info.get("primary_domain"), *(info.get("secondary_domains") or [])]:
            if not domain:
                continue
            entries.setdefault(domain, []).append((f"{file.parent.name}/{file.stem}", file))
    output = root / "categories"
    output.mkdir(exist_ok=True)
    for stale in output.glob("*.md"):
        stale.unlink()
    lines = ["# Browse by domain", "", "Generated from Copilot-enriched catalog entries.", ""]
    for domain, repos in sorted(entries.items()):
        path = output / f"{domain}.md"
        path.write_text("# " + domain.replace("-", " ").title() + "\n\n" +
                        "\n".join(f"- [{name}](../catalog/{p.parent.name}/{p.name})" for name,p in sorted(repos)) +
                        "\n", encoding="utf-8")
        lines.append(f"- [{domain.replace('-', ' ').title()}](categories/{domain}.md) ({len(repos)})")
    (root / "CATEGORIES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    build()
