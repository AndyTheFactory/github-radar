---
repository: "gargpratyush/jev-router"
github_id: 1373617155
url: "https://github.com/gargpratyush/jev-router"
description: "Route to the cheapest model in claude code for your task using jev-router"
starred_at: "2026-10-08T20:41:16Z"
language: "JavaScript"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# gargpratyush/jev-router

Route to the cheapest model in claude code for your task using jev-router

**GitHub:** https://github.com/gargpratyush/jev-router

## README excerpt

> # jev-router
> Automatic per-turn model routing for Claude Code and OpenAI Codex. Jev sends simple work to
> the fast tier and difficult work to the strong tier, while preserving each CLI's native
> interface, tools, sessions, permissions, and authentication.
> | Command | Interface | Authentication | Routing decision |
> | --- | --- | --- | --- |
> | `jev-claude` | Claude Code | Existing `claude login` | Status line |
> | `jev-codex` | OpenAI Codex | Existing `codex login` | Commentary line |
> Both commands launch the real upstream CLI. Jev only chooses the model for a fresh user turn.
> ## Quick start
> Requires Node.js 20.12+ and at least one supported CLI:
> [Claude Code](https://code.claude.com/docs/en/setup) or
> [OpenAI Codex](https://developers.openai.com/codex/cli).
> ### 1. npm package
> npm install -g jev-router
> echo "JEV_API_KEY=..." > ~/.jev-router.env
> ### 2. Local repository
> git clone https://github.com/gargpratyush/jev-router.git
> cd jev-router
> npm install
> npm link
> echo "JEV_API_KEY=..." > ~/.jev-router.env
> On Windows PowerShell:
> Set-Content "$HOME\.jev-router.env" "JEV_API_KEY=..."
> Get a key from [TypeSafe](https://docs.typesafe.ai). Then launch either interface from any
> repository:
> jev-claude
> jev-codex
> No Anthropic or OpenAI API key is required when the corresponding CLI is already logged in
> with a subscription. Every CLI argument is forwarded:
> jev-claude --resume
> jev-claude -p "fix the failing test"
> jev-codex resume --last
> jev-codex exec "fix the failing test"
> For a local checkout, `npm link` installs both commands. Without it, run
> `node bin/jev-claude.mjs` or `node bin/jev-codex.mjs`.
> ## Claude Code interface
> `jev-claude` launches Claude Code with **Jev Router** selected in `/model`. Selecting another
> model pauses routing; selecting **Jev Router** resumes it.
> The injected status line shows the model used for the last turn:
> ⚡ haiku p=0.98 · my-project · 8% context
> ⏸ manual Opus 4.6 · my-project · 21% context
> Claude Code otherwise remains unchanged, including its keybindings, tools, permission prompts,
> `/compact`, `/resume`, and session handling. An existing custom `statusLine` is preserved;
> set `JEV_NO_STATUSLINE=1` to disable Jev's status line.
> The explanation skill is bundled with the npm package and loaded automatically: run
> `/jev-explain` in `jev-claude`, or `$jev-explain` in `jev-codex`, to see the factors behind
> the last routing decision:
> ┌─────────────────────────────────┐
> │ Jev Router                      │
> │                                 │
> │ Jev request

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

jev-router is a CLI wrapper that automatically routes each fresh user turn to a fast or strong model tier for Claude Code and OpenAI Codex. It launches the upstream CLIs while preserving their native interfaces, tools, sessions, permissions, and authentication. A JEV_API_KEY from TypeSafe is required for routing.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "125a1353911f02bc923193c8cba610aaa777ebb4ac6e8e8e78db558ed9a4588b"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "ai-ml"
  ],
  "repository_type": "application",
  "capabilities": [
    "api-integration",
    "code-generation",
    "workflow-orchestration"
  ],
  "technologies": [
    "JavaScript",
    "Node.js",
    "Claude Code",
    "OpenAI Codex",
    "npm"
  ],
  "summary": "jev-router is a CLI wrapper that automatically routes each fresh user turn to a fast or strong model tier for Claude Code and OpenAI Codex. It launches the upstream CLIs while preserving their native interfaces, tools, sessions, permissions, and authentication. A JEV_API_KEY from TypeSafe is required for routing.",
  "use_cases": [
    "Reducing cost by sending simple coding tasks to a fast model tier",
    "Sending difficult coding tasks to a stronger model tier in Claude Code or Codex",
    "Inspecting the reasons behind routing decisions via the bundled /jev-explain skill"
  ],
  "limitations": [
    "Requires Node.js 20.12+ and an installed, supported CLI (Claude Code or OpenAI Codex)",
    "Requires a JEV_API_KEY from TypeSafe for routing",
    "Routing applies only to fresh user turns; selecting another model in Claude Code pauses routing"
  ],
  "suggested_terms": [
    "model routing",
    "Claude Code",
    "OpenAI Codex",
    "cost optimization",
    "LLM router"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
