#!/usr/bin/env python3
"""Flag suspicious combinations in the stored catalog; no LLM/network required."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RE = re.compile(r'<!-- github-radar:enrichment:start -->[\s\S]*?```json\s*(\{[\s\S]*?\})\s*```')

REFERENCE_TYPES = {"resource", "collection", "dataset"}
EXECUTABLE_CUES = {"inference-serving", "vulnerability-scanning", "fine-tuning", "question-answering",
                   "classification", "information-extraction", "image-generation", "model-training"}

def audit(root=ROOT):
    findings = []
    for path in sorted((root / "catalog").glob("*/*.md")):
        match = RE.search(path.read_text(encoding="utf-8"))
        if not match:
            continue
        try:
            info = json.loads(match.group(1))
        except json.JSONDecodeError:
            findings.append((path, "invalid enrichment JSON"))
            continue
        caps = set(info.get("capabilities") or [])
        typ = info.get("repository_type")
        suspect = sorted(caps & EXECUTABLE_CUES) if typ in REFERENCE_TYPES else []
        if suspect:
            findings.append((path, f"review {typ} with executable capabilities: {', '.join(suspect)}"))
        summary = (info.get("summary") or "").lower()
        if "browser" in summary and "inference-serving" in caps:
            findings.append((path, "browser tagged inference-serving"))
        if any(t in summary for t in ("worktree", "worktrees")) and "virtualization" in caps:
            findings.append((path, "git worktrees tagged virtualization"))
    return findings

if __name__ == "__main__":
    issues = audit()
    for path, description in issues:
        print(f"{path.relative_to(ROOT)}: {description}")
    print(f"Review candidates: {len(issues)} (advisory only)")
