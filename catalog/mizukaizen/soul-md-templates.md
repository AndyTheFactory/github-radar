---
repository: "mizukaizen/soul-md-templates"
github_id: 1177330300
url: "https://github.com/mizukaizen/soul-md-templates"
description: "5 free SOUL.md identity templates for AI agents. Define your agent's culture, domain, voice, and boundaries."
starred_at: "2026-10-26T15:06:17Z"
language: null
topics: []
homepage: ""
license: null
archived: false
---

# mizukaizen/soul-md-templates

5 free SOUL.md identity templates for AI agents. Define your agent's culture, domain, voice, and boundaries.

**GitHub:** https://github.com/mizukaizen/soul-md-templates

## README excerpt

> # SOUL.md Templates
> > 5 free SOUL.md identity templates for AI agents. Define your agent's culture, domain, voice, and boundaries.
> > By Melisia Archimedes.
> ## What is a SOUL.md?
> A SOUL.md is a constitutional identity document for an AI agent. It defines who the agent is — not just what it does, but how it thinks, speaks, and makes decisions. It's the difference between an agent that follows instructions and one that has character.
> The SOUL.md standard was created as part of [The Hive Doctrine](https://hivedoctrine.com) — a thesis on polytheistic AI safety.
> ## Templates
> | Template | Archetype | Best For |
> |----------|-----------|----------|
> | [Strategist](templates/strategist.md) | Strategic thinker | Planning, decision-making, trade-off analysis |
> | [Engineer](templates/engineer.md) | Technical builder | Code review, architecture, debugging |
> | [Creative](templates/creative.md) | Creative producer | Writing, design, content, ideation |
> | [Analyst](templates/analyst.md) | Data interpreter | Research, analysis, pattern recognition |
> | [Coordinator](templates/coordinator.md) | Operations manager | Task routing, scheduling, team coordination |
> ## Usage
> 1. Copy the template that matches your agent's role
> 2. Replace all `[PLACEHOLDER]` values with your specifics
> 3. Save as `SOUL.md` in your agent's configuration directory
> 4. Reference it in your agent's system prompt or configuration
> ### Claude Code
> cp templates/strategist.md .claude/SOUL.md
> ### Any Agent Framework
> with open("SOUL.md") as f:
> soul = f.read()
> system_prompt = f"You are governed by this constitution:\n\n{soul}"
> ## Full Collection
> These 5 templates cover the most common archetypes. For industry-specific templates (healthcare, legal, finance, education, and more), see the [Industry Persona Kit](https://hive-doctrine-mcp.vercel.app/mcp) — 10 vertical SOUL.md templates built for production deployment.
> ### Connect via MCP
> claude mcp add --transport http hive-doctrine https://hive-doctrine-mcp.vercel.app/mcp
> ## The Hive Doctrine
> *"Every agent carries a constitution defining its culture, domain, voice, and boundaries."*
> — Alignment Principle 1: Constitutional Identity
> Read the full thesis at [hivedoctrine.com](https://hivedoctrine.com).
> ## License
> Templates: MIT License
> Content © 2026 Melisia Archimedes.

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A collection of five free Markdown SOUL.md identity templates for defining AI agent culture, domain, voice, and boundaries. The templates cover strategist, engineer, creative, analyst, and coordinator archetypes and are copied into an agent's configuration or system prompt.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "afe7b4f24cc26537565f9051c8813abead2a0b89600dc9050d52a5a096d79b01"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "productivity"
  ],
  "repository_type": "template",
  "capabilities": [],
  "technologies": [
    "Markdown"
  ],
  "summary": "A collection of five free Markdown SOUL.md identity templates for defining AI agent culture, domain, voice, and boundaries. The templates cover strategist, engineer, creative, analyst, and coordinator archetypes and are copied into an agent's configuration or system prompt.",
  "use_cases": [
    "Defining a role-specific identity for an AI agent",
    "Starting from a template and replacing placeholder values for a custom agent",
    "Loading a SOUL.md file into an agent's system prompt"
  ],
  "limitations": [
    "Provides text templates only; no executable code or tooling is included",
    "Requires manual placeholder replacement before use",
    "Industry-specific templates are referenced as a separate, external paid offering"
  ],
  "suggested_terms": [
    "SOUL.md",
    "AI agent identity",
    "system prompt template",
    "agent persona",
    "agent constitution"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
