---
repository: "Brainwires/jevwire"
github_id: 1375075176
url: "https://github.com/Brainwires/jevwire"
description: "Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)"
starred_at: "2026-10-08T20:41:21Z"
language: "TypeScript"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# Brainwires/jevwire

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

**GitHub:** https://github.com/Brainwires/jevwire

## README excerpt

> # jevwire
> **Jev** is TypeSafe AI's [System One](https://docs.typesafe.ai/concepts/system-one) model: a fast,
> calibrated classifier. You give it a state and a map of typed questions — yes/no, pick-one,
> rate-on-a-rubric — and it answers every one in parallel with a probability over the answer space
> *you* defined. It never generates text, so the answer is always inside your schema.
> **jevwire** wires it into a harness. The repository is
> [Brainwires/jevwire](https://github.com/Brainwires/jevwire); the npm package is still published as
> `jevwire` and the Claude Code plugin is `jev`.
> It is three things:
> - **7 MCP tools** — `jev_rank`, `jev_pick`, `jev_verify`, `jev_evaluate`, `jev_gate_action`, `jev_next_step`,
> `jev_list_models`.
> - **An embeddable library** — `JevDecisionModel` plus a pure `run*` function per tool, so mandatory
> checks can live in your harness instead of in a tool an agent may decline to call.
> - **A Claude Code plugin** — hooks that put judgments at the harness boundaries: before a tool
> call, after a fetched result, before the turn ends. Everything they decide is addressed to Claude,
> not to you: a note about a call that already ran, or a single `deny` Claude can answer. As of
> 0.3.0 they never prompt you.
> It is **not** for generation, arithmetic, counting, date comparison, or multi-hop reasoning. It
> answers bounded questions over text you hand it. Anything numeric or ordered should be extracted as
> a choice over enumerated options and compared in code.
> Release 0.4.0 has been exercised against the live TypeSafe API on **2026-09-18**. Every latency,
> token count and cost figure quoted in this README comes from that run or the 0.3.0 one it is compared
> against.
> ## Install
> Node >= 20 for all three routes.
> ### Claude Code plugin
> /plugin marketplace add Brainwires/jevwire
> /plugin install jev@brainwires-jevwire
> Then give it a key, by either route:
> - `/plugin` → jev → **TypeSafe API key**, or
> - `export TYPESAFE_API_KEY=sk-...` in the shell you start Claude Code from.
> Then `/reload-plugins`. Without a key the judgment hooks stay inactive — the deterministic pattern
> checks still run — and the plugin says so once per session.
> There is no build or install step: `plugin/dist/hook.mjs` and `plugin/dist/mcp.mjs` are committed,
> dependency-free, esbuild-bundled single files.
> ### Bare MCP server
> claude mcp add jev -e TYPESAFE_API_KEY=sk-... -- npx -y jevwire
> Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):
> {
> "mcpServers": {
> "j

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

jevwire is a decision layer for AI agents that answers bounded typed questions (yes/no, pick-one, rubric ratings) with probabilities over user-defined answer spaces via the TypeSafe API. It provides seven MCP tools, an embeddable DecisionModel library, and a Claude Code plugin with harness-boundary hooks.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "5581b8e6cbc3922e3a0311bb7a9f0bc99675481d79fdd1792a2b628199276855"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools",
    "security"
  ],
  "repository_type": "library",
  "capabilities": [
    "classification",
    "api-integration",
    "inference-serving",
    "automation",
    "authorization"
  ],
  "technologies": [
    "TypeScript",
    "Node.js",
    "MCP",
    "Claude Code",
    "esbuild",
    "npm"
  ],
  "summary": "jevwire is a decision layer for AI agents that answers bounded typed questions (yes/no, pick-one, rubric ratings) with probabilities over user-defined answer spaces via the TypeSafe API. It provides seven MCP tools, an embeddable DecisionModel library, and a Claude Code plugin with harness-boundary hooks.",
  "use_cases": [
    "Adding calibrated yes/no or pick-one judgments to agent workflows",
    "Gating agent tool calls before execution",
    "Embedding mandatory checks in an agent harness via the library"
  ],
  "limitations": [
    "Not suitable for text generation, arithmetic, counting, date comparison, or multi-hop reasoning",
    "Requires a TypeSafe API key for judgment hooks; without one only deterministic pattern checks run",
    "Depends on the external TypeSafe API service"
  ],
  "suggested_terms": [
    "agent decision layer",
    "MCP server classifier",
    "Claude Code plugin hooks",
    "TypeSafe Jev",
    "calibrated classification agents"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
