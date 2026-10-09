---
repository: "morluto/rea"
github_id: 1209966933
url: "https://github.com/morluto/rea"
description: "Reverse engineer anything with agents, from app behavior down to native binaries."
starred_at: "2026-10-09T14:30:59Z"
language: "TypeScript"
topics: ["agent-skills", "ai-agents", "binary-analysis", "claude-code", "cli", "codex", "cordis", "ctf", "decompiler", "developer-tools", "disassembler", "dsh", "dsh-plugin", "ghidra", "hopper", "llm", "mcp", "model-context-protocol", "reverse-engineering", "static-analysis"]
homepage: "https://rea.tools"
license: "MIT"
archived: false
---

# morluto/rea

Reverse engineer anything with agents, from app behavior down to native binaries.

**GitHub:** https://github.com/morluto/rea

## README excerpt

> **English** · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md)
> # REA: Reverse Engineer Anything
> ### One MCP for reverse engineering across binaries, applications, and runtime behavior.
> **See a feature you like. Understand how it works, down to the binary level.**
> **[Website](https://rea.tools/) · [Guides](https://rea.tools/guides/) · [Showcases](https://rea.tools/showcase/)**
> [Quick start](#quick-start) · [How REA works](#how-rea-works) · [What you can analyze](#what-you-can-analyze) · [Showcases](#showcases) · [FAQ](#faq) · [Documentation](#documentation)
> npx rea-agents setup
>
>
>
>
>
> Join the Reverse Engineering Community
> Discord · Q&amp;A · Show and Tell
>
>
>
>
> ---
> See a feature in an app that you want in your own product? Ask your agent to investigate it with REA. It can inspect the app without its source code, explain how the feature works, show the evidence, and build a version for your project.
> REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites. You can also use the same tools from your terminal. Analysis runs locally, and results include the evidence and limitations behind each conclusion.
> Setup registers REA with your agent and installs matching workflow instructions. Native analysis can use an existing Hopper, Ghidra, or IDA installation; setup can optionally install Hopper with approval. Static JavaScript analysis needs no native analysis engine.
> > **[Visit the REA website](https://rea.tools/)** for setup instructions, illustrated guides, and real case studies.
> ## Quick start
> ### Set up your agent
> With Node.js and npm installed, run:
> npx rea-agents setup
> Choose your agents, review the proposed changes, and approve them. Setup adds
> REA's MCP server and matching workflow instructions, with backups of existing
> configuration. Restart your agent afterward.
> Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and
> [other agents](docs/installation.md#supported-agents). See
> [installation and setup](docs/installation.md) for provider configuration and
> manual MCP registration.
> ### Ask your agent
> Understand how search

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

REA is an MCP server and CLI that gives AI agents tools to reverse engineer native binaries, JavaScript/Electron apps, .NET assemblies, and websites. Analysis runs locally and reports evidence and limitations, using existing Hopper, Ghidra, or IDA installations for native binaries.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "a22d655cb5be9664b5cedbd0f3027a42eb9c7d925233558f4f8465f41fe37eb4"
  },
  "primary_domain": "security",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "static-analysis",
    "debugging",
    "profiling"
  ],
  "technologies": [
    "TypeScript",
    "MCP",
    "Ghidra",
    "Hopper",
    "IDA",
    "Node.js",
    "npm",
    "Electron"
  ],
  "summary": "REA is an MCP server and CLI that gives AI agents tools to reverse engineer native binaries, JavaScript/Electron apps, .NET assemblies, and websites. Analysis runs locally and reports evidence and limitations, using existing Hopper, Ghidra, or IDA installations for native binaries.",
  "use_cases": [
    "Inspecting app behavior and native binaries without source code",
    "Analyzing JavaScript, Electron, and .NET applications",
    "Using agent-driven reverse engineering from the terminal"
  ],
  "limitations": [
    "Native analysis requires an existing Hopper, Ghidra, or IDA installation",
    "Static JavaScript analysis needs no native engine, but native analysis does",
    "Results depend on agent behavior and tool evidence"
  ],
  "suggested_terms": [
    "reverse engineering MCP",
    "binary analysis agent",
    "Ghidra MCP",
    "decompiler MCP",
    "Electron reverse engineering"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
