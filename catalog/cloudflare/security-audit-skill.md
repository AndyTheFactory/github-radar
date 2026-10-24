---
repository: "cloudflare/security-audit-skill"
github_id: 1273427276
url: "https://github.com/cloudflare/security-audit-skill"
description: "A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings"
starred_at: "2026-10-24T21:40:47Z"
language: "JavaScript"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# cloudflare/security-audit-skill

A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings

**GitHub:** https://github.com/cloudflare/security-audit-skill

## README excerpt

> # security-audit
> A coding-agent skill that turns your agent into a security auditor. It orchestrates isolated agents through reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting.
> This is the skill that seeded Cloudflare's vulnerability discovery harness, described in [Build your own vulnerability harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness). The harness grew into a multi-stage, fleet-wide system; this skill is the single-repo starting point it evolved from.
> ## What it does
> The skill runs a structured audit in six phases:
> 1. **Reconnaissance** -- map architecture, trust boundaries, input surfaces, prior evidence, and deterministic coverage in `architecture.md` and `coverage-ledger.json`.
> 2. **Coverage-led hunting** -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps.
> 3. **Candidate validation** -- give every unique candidate to a fresh verifier that tries to disprove it.
> 4. **Structured output** -- write `confirmed`, `needs_validation`, and `rejected` records to `findings.json` and validate them against `report-schema.json`.
> 5. **Independent record verification** -- fresh agents verify final source claims. Material replacements receive another independent verifier.
> 6. **Target-neutral reporting** -- derive `REPORT.md`, `FINDINGS-DETAIL.md`, and `NEEDS-VALIDATION.md` from the verified records and coverage ledger.
> The parent runs `validate-coverage-ledger.cjs` after creating the ledger and after each later ledger update. It runs `validate-findings.cjs` in Phase 4 and again after every Phase 5 replacement.
> The verdicts are distinct: `confirmed` has a complete source trace and bounded observed result, `needs_validation` has an exact unresolved fact and no severity, and `rejected` records a disproved candidate.
> Multiple runs against the same repo are additive. The skill uses prior ledgers and findings to target gaps, revalidate changed source, and carry forward current-source evidence without treating stale or unresolved work as covered.
> ## Files
> | File | Purpose |
> |------|---------|
> | `SKILL.md` | Setup, core principles, platform terminology, workflow overview, and audit anti-patterns |
> | `RECONNAISSANCE.md` | Phase 1 reconnaissance prompts and synthesis instructions |
> | `HUNTING.md` | Phase 2 orchestration, hunting methodology, and validation rules |
> | `ATTACK-CLASSES.md` | Core, wildcard, an

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A coding-agent skill that orchestrates isolated agents through a six-phase security audit, including reconnaissance, hunting, candidate validation, and reporting. It produces machine-readable findings (confirmed, needs_validation, rejected) validated against a JSON schema. Multiple runs against the same repository are additive.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "02195c89fabb5c1c9d464947edd17d9ca7de814f00b1ac4ba4ebd1e85e7416c8"
  },
  "primary_domain": "security",
  "secondary_domains": [
    "developer-tools",
    "ai-ml"
  ],
  "repository_type": "template",
  "capabilities": [
    "vulnerability-scanning",
    "reporting",
    "agent-orchestration",
    "static-analysis"
  ],
  "technologies": [
    "JavaScript",
    "Markdown",
    "JSON Schema",
    "Node.js"
  ],
  "summary": "A coding-agent skill that orchestrates isolated agents through a six-phase security audit, including reconnaissance, hunting, candidate validation, and reporting. It produces machine-readable findings (confirmed, needs_validation, rejected) validated against a JSON schema. Multiple runs against the same repository are additive.",
  "use_cases": [
    "Running structured security audits of a codebase with a coding agent",
    "Producing machine-readable, schema-validated vulnerability findings",
    "Tracking audit coverage across repeated runs"
  ],
  "limitations": [
    "Described as a starting point; the README notes the production harness grew beyond this single-repo skill",
    "Requires a coding agent platform capable of running the skill",
    "Repository topics are empty; capabilities are inferred from the README description only"
  ],
  "suggested_terms": [
    "security audit agent",
    "vulnerability discovery skill",
    "coding agent security",
    "findings schema validation",
    "coverage ledger"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
