---
repository: "NVIDIA/SkillSpector"
github_id: 1187630119
url: "https://github.com/NVIDIA/SkillSpector"
description: "Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them."
starred_at: "2026-10-08T20:40:37Z"
language: "Python"
topics: ["agent-security", "agent-skills", "agentic-ai", "ai-security", "claude-code", "mcp", "prompt-injection", "security-scanner", "security-tools", "security-workflow", "supply-chain-security"]
homepage: "https://docs.nvidia.com/skills/scanning-agent-skills"
license: "Apache-2.0"
archived: false
---

# NVIDIA/SkillSpector

Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.

**GitHub:** https://github.com/NVIDIA/SkillSpector

## README excerpt

> # SkillSpector
> **Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installing agent skills.
> ## Overview
> AI agent skills (used by Claude Code, Codex CLI, Gemini CLI, etc.) execute with implicit trust and minimal vetting. In the 31,132-skill analyzed subset of the research dataset, **26.1% of skills contain vulnerabilities** and **5.2% show likely malicious intent**.
> SkillSpector helps you answer: **"Is this skill safe to install?"**
> SkillSpector is part of the [NVIDIA Verified Skills pipeline](https://docs.nvidia.com/skills/), which scans, evaluates, and signs agent skills before publication. Skills that pass are published to the [NVIDIA skills catalog](https://github.com/NVIDIA/skills).
> ## Documentation
> - **[Scan agent skills before installation](https://docs.nvidia.com/skills/scanning-agent-skills)** — Hosted guide: when to scan, how to read a report, and how to gate installs.
> - **[Development guide](docs/DEVELOPMENT.md)** — Architecture, package layout, and how to extend the analyzer pipeline.
> - **[Analysis resource bounds](docs/ANALYSIS_RESOURCE_BOUNDS.md)** — Fail-closed bundle, parser, nested-artifact, ledger, and finding ceilings.
> - **[Pi extension](docs/PI_EXTENSION.md)** — Install SkillSpector as a Pi tool for scanning skills from inside agent sessions.
> - **[OpenCode extension](docs/OPENCODE_EXTENSION.md)** — Install SkillSpector as an OpenCode tool and `/skillspector` command for scanning skills from inside agent sessions.
> ## Features
> - **Multi-format input**: Scan Git repos, URLs, zip files, directories, or single files
> - **71 vulnerability patterns** across 17 categories: prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, output handling, system prompt leakage, memory poisoning, tool misuse, rogue agent, anti-refusal, trigger abuse, dangerous code (AST), taint tracking, YARA signatures, MCP least privilege, and MCP tool poisoning
> - **Two-stage analysis**: Fast static analysis + optional LLM semantic evaluation
> - **Live vulnerability lookups**: SC4 queries [OSV.dev](https://osv.dev) for real-time CVE data with automatic offline fallback
> - **Multiple output formats**: Terminal, JSON, Markdown, and SARIF reports
> - **Risk scoring**: 0-100 score with severity labels and clear recommendations
> - **Baseline / false-positive suppression**: Accept known findings via a glob-rule or fingerprint baseline so re-scans surface only *new* issues ([docs](docs/SUPPR

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

SkillSpector is a security scanner that analyzes AI agent skills for vulnerabilities, prompt injection, data exfiltration, and supply-chain risks before installation. It combines fast static analysis with optional LLM-based semantic evaluation and outputs terminal, JSON, Markdown, or SARIF reports with risk scores.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "f1b70ee90c6c509a9f5f171ef003cab1ce439e382d5c92853e1c6e5c631cc8ba"
  },
  "primary_domain": "security",
  "secondary_domains": [
    "developer-tools",
    "ai-ml"
  ],
  "repository_type": "application",
  "capabilities": [
    "static-analysis",
    "vulnerability-scanning",
    "reporting",
    "web-scraping"
  ],
  "technologies": [
    "Python",
    "YARA",
    "SARIF",
    "OSV.dev",
    "MCP",
    "Claude Code",
    "Codex CLI",
    "OpenCode"
  ],
  "summary": "SkillSpector is a security scanner that analyzes AI agent skills for vulnerabilities, prompt injection, data exfiltration, and supply-chain risks before installation. It combines fast static analysis with optional LLM-based semantic evaluation and outputs terminal, JSON, Markdown, or SARIF reports with risk scores.",
  "use_cases": [
    "Checking whether an AI agent skill is safe to install",
    "Gating agent skill installs in CI or review workflows",
    "Suppressing known findings with a baseline so re-scans report only new issues"
  ],
  "limitations": [
    "LLM semantic evaluation is optional and depends on external model access",
    "Live CVE lookups rely on OSV.dev, with offline fallback data",
    "Scope is limited to the documented pattern categories and input formats"
  ],
  "suggested_terms": [
    "agent skill security",
    "prompt injection scanner",
    "MCP security",
    "supply chain security",
    "SARIF scanner"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
