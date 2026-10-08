---
repository: "jackwener/OpenCLI"
github_id: 1181982220
url: "https://github.com/jackwener/OpenCLI"
description: "Make Any Website into CLI & Use your logged-in browser by AI agent. "
starred_at: "2026-10-08T20:42:16Z"
language: "JavaScript"
topics: ["ai-agent", "ai-agents", "ai-tools", "browser-automation", "browser-use", "cli", "playwright"]
homepage: "https://opencli.info/"
license: "Apache-2.0"
archived: false
---

# jackwener/OpenCLI

Make Any Website into CLI & Use your logged-in browser by AI agent. 

**GitHub:** https://github.com/jackwener/OpenCLI

## README excerpt

> # OpenCLI
> > **Convert any website into a CLI & run Browser Use on your logged-in Chrome.**
> > Turn websites, browser sessions, Electron apps, and local tools into deterministic interfaces for humans and AI agents.
> > Or run Browser Use against any page — navigate, fill forms, click, extract, automate.
> OpenCLI gives you one surface for three different kinds of automation:
> - **Use built-in adapters** for sites like Bilibili, Zhihu, Xiaohongshu, Reddit, HackerNews, Twitter/X, and [many more](#built-in-commands).
> - **Let AI Agents operate any website** — install the `opencli-browser` skill in your AI agent (Claude Code, Cursor, etc.), and it can navigate, click, type/fill, extract, and inspect any page through your logged-in browser via `opencli browser` primitives.
> - **Write new adapters** end-to-end with `opencli browser` + the `opencli-adapter-author` skill, which guides from first recon through field decoding, code, and `opencli browser verify`.
> It also provides **desktop app adapters** for Electron apps like Cursor, Trae CN, Codex, Antigravity, ChatGPT, and Trae SOLO.
> ## Quick Start
> ### 1. Install OpenCLI
> For desktop use, start with **OpenCLIApp**. It bundles the OpenCLI runtime,
> keeps the managed `opencli` command installed, and gives you a system tray UI
> for setup, diagnostics, updates, browser-login keepalive, and Web → Markdown.
> **Option A — OpenCLIApp (recommended for macOS / Windows):**
> Download the latest app from , install it, then
> open the app once and use the System page to install or repair the `opencli`
> command.
> **Option B — npm global install (CLI-only / CI / servers):**
> OpenCLI requires **Node.js >= 20.18.1** when installed through npm.
> node --version
> npm install -g @jackwener/opencli
> ### 2. Install the Browser Bridge Extension
> OpenCLI connects to Chrome/Chromium through a lightweight Browser Bridge extension plus a small local daemon. The daemon auto-starts when needed.
> **Option A — Chrome Web Store (recommended):**
> Install **OpenCLI** from the [Chrome Web Store](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk).
> **Option B — Manual install:**
> 1. Download the latest `opencli-extension-v{version}.zip` from the GitHub [Releases page](https://github.com/jackwener/opencli/releases).
> 2. Unzip it, open `chrome://extensions`, and enable **Developer mode**.
> 3. Click **Load unpacked** and select the unzipped folder.
> ### 3. Verify the setup
> opencli doctor
> ### 4. Optional: name your Chrome profile
> Each Chrome profile run

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

OpenCLI converts websites into command-line interfaces and lets AI agents operate a user's logged-in Chrome browser via navigate, click, fill, and extract primitives. It provides built-in adapters for sites such as Bilibili, Reddit, and Hacker News, plus adapters for Electron desktop apps.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "538c41bb390c4fee3be6ad613ed9a213325a994445c7b293068ef9ad99bd3bf4"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "productivity",
    "security"
  ],
  "repository_type": "application",
  "capabilities": [
    "api-integration",
    "web-scraping",
    "automation"
  ],
  "technologies": [
    "JavaScript",
    "Node.js",
    "Playwright",
    "Chrome Extension",
    "Electron"
  ],
  "summary": "OpenCLI converts websites into command-line interfaces and lets AI agents operate a user's logged-in Chrome browser via navigate, click, fill, and extract primitives. It provides built-in adapters for sites such as Bilibili, Reddit, and Hacker News, plus adapters for Electron desktop apps.",
  "use_cases": [
    "Exposing websites as deterministic CLI commands for scripts or CI",
    "Letting AI agents navigate and extract data from pages in a logged-in browser",
    "Writing new site adapters with the opencli-adapter-author skill"
  ],
  "limitations": [
    "Requires Node.js >= 20.18.1 for npm installation",
    "Requires the Browser Bridge extension and local daemon for Chrome connectivity",
    "Built-in adapters cover only the listed sites and may break when those sites change"
  ],
  "suggested_terms": [
    "browser automation CLI",
    "AI agent browser use",
    "website to CLI",
    "Playwright Chrome extension",
    "logged-in browser automation"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
