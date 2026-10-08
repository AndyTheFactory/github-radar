---
repository: "serhiileniv/claude-router"
github_id: 1226036561
url: "https://github.com/serhiileniv/claude-router"
description: "Cut your Claude API bill: local proxy that auto-routes every request to right model. Zero code changes."
starred_at: "2026-10-08T20:41:26Z"
language: "TypeScript"
topics: ["ai", "anthropic", "claude", "claude-code", "cost-optimization", "developer-tools", "haiku", "llm", "model-router", "model-routing", "npm-package", "opus", "proxy", "sdk", "sonnet", "typescript"]
homepage: "https://serhii-leniv.github.io/claude-router/"
license: "MIT"
archived: false
---

# serhiileniv/claude-router

Cut your Claude API bill: local proxy that auto-routes every request to right model. Zero code changes.

**GitHub:** https://github.com/serhiileniv/claude-router

## README excerpt

> Auto-route every Claude request to the cheapest model that can handle it.
>
>
>
> ---
> **Cut your Anthropic API bill by routing every request to the cheapest Claude model that can handle it — Haiku, Sonnet, or Opus.** `claude-router` is a self-hosted, drop-in proxy: point any Anthropic-compatible app (Claude Code, Cursor, Cline, or your own SDK code) at it with one environment variable and get automatic, complexity-aware model routing — **zero code changes, no SaaS in your request path, no per-token markup**. Every response reports exactly what you saved.
> [claude-router] → haiku  (heuristic, 0ms) | cost: $0.0010 | saved: $0.0030 vs claude-sonnet-5
> [claude-router] → opus   (hybrid, 48ms)   | cost: $0.0890 | extra: $0.0740 vs claude-sonnet-5
> ## Is this for you?
> **If you pay per token** (Anthropic API, Amazon Bedrock, or Google Vertex) **and your traffic is a mix of easy and hard requests.** The router skims the easy majority down to Haiku/Sonnet and reserves Opus for what actually needs it.
> **Measured, not promised.** One live Claude Code session through the proxy spent $3.34 against a $4.23 all-Opus counterfactual — **21%** ([note](research/2026-07-25-live-session.md)). A 200-turn replay of the published 0.2.2 projected **35%** ([method](research/2026-07-21-end-to-end-savings.md)), an upper bound that assumes token counts do not change when the model does and that comes almost entirely from one rule: mid-loop tool steps go to Sonnet. Direct API (single-turn) traffic is **unmeasured**. See [What is measured vs assumed](#what-is-measured-vs-assumed).
> ## Contents
> - [Quick start](#quick-start) · [How it works](#how-it-works) · [Configuration](#configuration) · [CLI reference](#cli-reference)
> - [Pricing & savings](#pricing--savings) · [Other providers](#other-providers) · [Use as a library](#use-as-a-library) · [Authentication & security](#authentication--security)
> ## Features
> | | |
> |---|---|
> | 🔌 **Zero code changes** | Point any Anthropic app at the proxy via `ANTHROPIC_BASE_URL`, or `import` it as a library. |
> | 🧠 **Evidence-based routing** | Conjunctive gates on request shape, not a keyword score. Sonnet is the default; leaving it needs positive evidence. See [research/](research/) for the measurements behind it. |
> | 🛟 **Quality-safe** | Sonnet floor for tool-using sessions, plus auto-escalation on truncation/refusal and auto-fallback on rate limits. |
> | 📊 **Measurable** | Every call reports exact cents saved vs your baseline, with lifetime `stats` and a live da

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A self-hosted local proxy that routes Anthropic-compatible API requests to Claude Haiku, Sonnet, or Opus based on request complexity, configured via the ANTHROPIC_BASE_URL environment variable. It reports per-call cost and savings versus a baseline model and can also be imported as a TypeScript library.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "b67174529570588f4c71296ad7f2d36544c8e4eb8edb6d59b36a5bd8ad21880c"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "ai-ml",
    "productivity"
  ],
  "repository_type": "library",
  "capabilities": [
    "inference-serving",
    "api-integration",
    "monitoring",
    "reporting",
    "automation"
  ],
  "technologies": [
    "TypeScript",
    "Node.js",
    "npm",
    "Anthropic API",
    "Claude",
    "Amazon Bedrock",
    "Google Vertex"
  ],
  "summary": "A self-hosted local proxy that routes Anthropic-compatible API requests to Claude Haiku, Sonnet, or Opus based on request complexity, configured via the ANTHROPIC_BASE_URL environment variable. It reports per-call cost and savings versus a baseline model and can also be imported as a TypeScript library.",
  "use_cases": [
    "Reducing Anthropic API costs for mixed easy and hard workloads",
    "Routing Claude Code, Cursor, or Cline traffic to cheaper models without code changes",
    "Tracking per-request cost savings against an all-Opus or all-Sonnet baseline"
  ],
  "limitations": [
    "Direct single-turn API traffic savings are unmeasured according to the README",
    "Reported 21% and 35% savings figures come from specific sessions and a replay with assumptions",
    "Savings estimates assume token counts do not change when the model changes"
  ],
  "suggested_terms": [
    "claude model router",
    "anthropic api cost optimization",
    "llm proxy",
    "claude code proxy",
    "model routing"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
