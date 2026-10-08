---
repository: "browser-use/browser-harness"
github_id: 1213049020
url: "https://github.com/browser-use/browser-harness"
description: "Browser Harness | Self-healing harness that enables LLMs to complete any task."
starred_at: "2026-10-08T20:40:02Z"
language: "Python"
topics: ["ai-agent", "browser-agent", "browser-automation", "browser-use", "browser-use-box", "browser-use-cloud", "cdp", "cloud-browser", "llm", "persistent-browser", "playwright", "telegram-agent", "vps-agent", "web-automation"]
homepage: "https://browser-harness.com"
license: "MIT"
archived: false
---

# browser-use/browser-harness

Browser Harness | Self-healing harness that enables LLMs to complete any task.

**GitHub:** https://github.com/browser-use/browser-harness

## README excerpt

> # Browser Harness ♞
> Connect an LLM directly to your real browser through one editable CDP websocket. The agent writes missing helpers as it works, so the harness improves with every task.
> Try browser-harness in [Browser Use Cloud](https://cloud.browser-use.com/v4?utm_campaign=browser-harness-use-in-cloud&utm_source=github) or paste the setup prompt into your coding agent.
> ● agent: wants to upload a file
> │
> ● agent-workspace/agent_helpers.py → helper missing
> │
> ● agent writes it                         agent_helpers.py
> │                                                       + custom helper
> ✓ file uploaded
> **You will never use the browser again.**
> ## See it work
> **Task:** "Open my X profile, find my latest 20 video posts, and download them."
> ## Setup prompt
> Paste into Claude Code or Codex:
> Install or upgrade browser-harness to the latest stable version with uv using Python 3.12, register the skill from `browser-harness skill`, and connect it to my browser. Ask whether I want local browser recordings enabled; default to no and preserve my existing preference on upgrades. Follow https://github.com/browser-use/browser-harness/blob/main/install.md if setup or connection fails.
> The agent will open `chrome://inspect/#remote-debugging`. On first setup, tick
> the checkbox so the agent can connect to your browser:
> ## How it works
> - [`install.md`](install.md) connects the agent to your browser.
> - [`SKILL.md`](SKILL.md) teaches it the browser workflow.
> - [`src/browser_harness/`](src/browser_harness/) stays protected while the agent writes reusable helpers in its local workspace.
> ## Scale with Browser Use Cloud
> Use your local browser for logged-in, personal work. When you want many browsers in parallel—with live previews, proxies, stealth, CAPTCHA solving, and more—scale with [Browser Use Cloud](https://cloud.browser-use.com/new-api-key).
> ## MCP server
> `browser-harness-mcp` exposes the browser control helpers as MCP tools over
> stdio, so any MCP client (Claude Code, Devin, Cursor, etc.) can drive the
> browser without writing a second CDP layer. See [docs/MCP.md](docs/MCP.md) for
> setup and client configuration.
> ## Contributing
> Bug fixes, documentation improvements, and agent-generated domain skills are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
> ---
> [The Bitter Lesson of Agent Harnesses](https://browser-use.com/posts/bitter-lesson-agent-harnesses) · [Web Agents That Actually Learn](https://browser-use.com/posts/web-agents-that-actually-learn)

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Browser Harness connects an LLM directly to a user's real browser through an editable CDP websocket. The agent writes missing helper functions as it works, and an MCP server exposes the browser control helpers as tools. It is MIT licensed.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "0327a4d018adfadc5301f314b07c6dff7a83d24f8930331926330de8eec52cc3"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "automation",
    "agent-orchestration",
    "api-integration",
    "code-generation",
    "web-scraping"
  ],
  "technologies": [
    "Python",
    "Chrome DevTools Protocol",
    "Playwright",
    "MCP",
    "uv",
    "LLM",
    "Browser Use Cloud",
    "Chrome"
  ],
  "summary": "Browser Harness connects an LLM directly to a user's real browser through an editable CDP websocket. The agent writes missing helper functions as it works, and an MCP server exposes the browser control helpers as tools. It is MIT licensed.",
  "use_cases": [
    "Driving logged-in personal browser sessions with an LLM agent",
    "Automating multi-step web tasks such as downloading posts or uploading files",
    "Giving MCP-compatible clients browser control without a separate CDP layer"
  ],
  "limitations": [
    "Requires enabling remote debugging in the local browser during setup",
    "Parallel, large-scale browser runs are offered through Browser Use Cloud rather than the local harness",
    "Local browser recordings are optional and disabled by default"
  ],
  "suggested_terms": [
    "browser automation LLM",
    "CDP browser agent",
    "MCP browser tools",
    "self-healing agent harness",
    "browser-use"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
