---
repository: "mksglu/context-mode"
github_id: 1164477708
url: "https://github.com/mksglu/context-mode"
description: "Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and   enforces routing across 17 platforms via MCP + hooks."
starred_at: "2026-10-19T11:27:08Z"
language: "TypeScript"
topics: ["antigravity", "claude", "claude-code", "claude-code-hooks", "claude-code-plugins", "claude-code-skill", "codex", "codex-cli", "context-mode", "copilot", "cursor-plugin", "kiro", "mcp", "mcp-server", "mcp-tools", "openclaw", "opencode", "pi-agent", "skills", "zed-extension"]
homepage: "https://context-mode.com"
license: "NOASSERTION"
archived: false
---

# mksglu/context-mode

Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and   enforces routing across 17 platforms via MCP + hooks.

**GitHub:** https://github.com/mksglu/context-mode

## README excerpt

> # Context Mode
> **The other half of the context problem.**
>
> Used across teams at
>
>
> ## The Problem
> Every MCP tool call dumps raw data into your context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone. And when the agent compacts the conversation to free space, it forgets which files it was editing, what tasks are in progress, and what you last asked for. On top of that, the agent wastes output tokens on filler, pleasantries, and verbose explanations — burning context from both sides.
> ### How Context Mode Solves It
> Context Mode is an MCP server that solves all four sides of this problem:
> 1. **Context Saving** — Sandbox tools keep raw data out of the context window. 315 KB becomes 5.4 KB. 98% reduction.
> 2. **Session Continuity** — Every file edit, git operation, task, error, and user decision is tracked in SQLite. When the conversation compacts, context-mode doesn't dump this data back into context — it indexes events into FTS5 and retrieves only what's relevant via BM25 search. The model picks up exactly where you left off. If you don't `--continue`, previous session data is deleted immediately — a fresh session means a clean slate.
> 3. **Think in Code** — The LLM should program the analysis, not compute it. Instead of reading 50 files into context to count functions, the agent writes a script that does the counting and `console.log()`s only the result. One script replaces ten tool calls and saves 100x context. This is a mandatory paradigm across all 17 supported clients, plus the OpenClaw gateway integration: stop treating the LLM as a data processor, treat it as a code generator.
> // Before: 47 × Read() = 700 KB.  After: 1 × ctx_execute() = 3.6 KB.
> ctx_execute("javascript", `
> const files = fs.readdirSync('src').filter(f => f.endsWith('.ts'));
> files.forEach(f => console.log(f + ': ' + fs.readFileSync('src/'+f,'utf8').split('\\n').length + ' lines'));
> `);
> 4. **No prose-style enforcement** — context-mode keeps raw data out of context but never dictates how the model writes its final answer. Brevity, completeness, formatting — your model's call (or yours via your own `CLAUDE.md` / `AGENTS.md`). Aggressive brevity prompts have been shown to degrade coding/reasoning benchmarks ([Moonshot AI on `kimi-k2.5`](https://github.com/anomalyco/opencode/issues/20258)) — the routing block stays focused on *where data goes*, not on *how the model talks*.
>
>
> ## Install
> Platforms are

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Context Mode is an MCP server that sandboxes tool output to reduce AI coding agent context usage and persists session data in SQLite with FTS5/BM25 retrieval. It integrates via MCP and hooks across multiple AI coding platforms, according to its README excerpt.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "75e3db2c743672d914853cdbeaebd97d8752f14993a4e5eb43bf1fdfd0d1bc6f"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "ai-ml",
    "productivity"
  ],
  "repository_type": "library",
  "capabilities": [
    "api-integration",
    "indexing",
    "search-retrieval",
    "storage",
    "automation"
  ],
  "technologies": [
    "TypeScript",
    "MCP",
    "SQLite",
    "FTS5",
    "BM25"
  ],
  "summary": "Context Mode is an MCP server that sandboxes tool output to reduce AI coding agent context usage and persists session data in SQLite with FTS5/BM25 retrieval. It integrates via MCP and hooks across multiple AI coding platforms, according to its README excerpt.",
  "use_cases": [
    "Reducing context window consumption from MCP tool output in AI coding agents",
    "Restoring relevant session state after conversation compaction"
  ],
  "limitations": [
    "README claims (e.g., 98% reduction) are unverified source metadata",
    "License is listed as NOASSERTION in metadata"
  ],
  "suggested_terms": [
    "MCP server",
    "context window optimization",
    "Claude Code plugin",
    "session memory",
    "FTS5 search"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
