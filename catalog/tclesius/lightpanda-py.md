---
repository: "tclesius/lightpanda-py"
github_id: 1131394699
url: "https://github.com/tclesius/lightpanda-py"
description: "Embedded Lightpanda for Python - a lightweight browser with CDP support"
starred_at: "2026-10-08T20:16:01Z"
language: "Python"
topics: []
homepage: ""
license: null
archived: false
---

# tclesius/lightpanda-py

Embedded Lightpanda for Python - a lightweight browser with CDP support

**GitHub:** https://github.com/tclesius/lightpanda-py

## README excerpt

> # lightpanda-py
> Embedded [Lightpanda](https://github.com/lightpanda-io/browser) for Python, a fast headless browser for AI agents and web automation.
> ## Installation
> pip install lightpanda-py
> # or
> uv add lightpanda-py
> No extra setup - the Lightpanda binary is bundled in the package.
> ## Usage
> ### Fetch
> Spin up an ephemeral browser to fetch a page:
> import lightpanda
> response = lightpanda.fetch("https://example.com")
> print(response.text)
> # JSON APIs
> response = lightpanda.fetch("https://httpbin.org/ip")
> data = response.json()
> # Markdown output
> response = lightpanda.fetch("https://example.com", dump="markdown")
> # Strip JS/CSS from output
> response = lightpanda.fetch("https://example.com", strip_mode="js,css")
> # Wait for network idle before dump
> response = lightpanda.fetch("https://example.com", wait_until="networkidle")
> ### CDP Server
> Start a CDP server to use with Playwright, Puppeteer, or any CDP client:
> import lightpanda
> proc = lightpanda.serve(host="127.0.0.1", port=9222)
> # 🐼 Running Lightpanda's CDP server... { pid: 12345 }
> # Connect with your favorite CDP client...
> proc.kill()
> Write browser logs to files:
> import lightpanda
> stdout = open("lightpanda.out.log", "w")
> stderr = open("lightpanda.err.log", "w")
> proc = lightpanda.serve(stdout=stdout, stderr=stderr)
> proc.kill()
> With Playwright:
> import lightpanda
> from playwright.sync_api import sync_playwright
> proc = lightpanda.serve()
> with sync_playwright() as p:
> browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
> page = browser.new_page()
> page.goto("https://example.com")
> print(page.content())
> browser.close()
> proc.kill()
> ### MCP Server
> Start a [Model Context Protocol](https://modelcontextprotocol.io) server over stdio:
> import lightpanda, json
> proc = lightpanda.mcp()
> proc.stdin.write(b'{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}\n')
> proc.stdin.flush()
> print(json.loads(proc.stdout.readline()))  # list of available tools
> proc.kill()
> ### Version
> import lightpanda
> print(lightpanda.version())
> ## Development
> The bundled Lightpanda browser version is pinned in `.browser-version`.
> Download the pinned browser for local development:
> scripts/get-browser
> By default this downloads the macOS arm64 binary. To use another asset or browser version:
> scripts/get-browser lightpanda-x86_64-linux
> scripts/get-browser lightpanda-aarch64-macos 0.2.9
> Available raw browser assets:
> - `lightpanda-aarch64-macos` - macOS arm64
> - `lightpanda-x86_64-macos` - macOS x86_64
> - `lightpanda-aarch64-linux` - Linux arm64
> - `lightpa

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A Python package that bundles the Lightpanda headless browser, exposing fetch, CDP server, and MCP server helpers. It supports page fetching with Markdown or JSON output and integration with Playwright and Puppeteer.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "cf79307eefa487d98e3adacfd8adab06b348750acf4c499ee04534515ed90265"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "applications",
    "infrastructure"
  ],
  "repository_type": "library",
  "capabilities": [
    "web-scraping",
    "api-integration",
    "inference-serving",
    "automation",
    "deployment"
  ],
  "technologies": [
    "Python",
    "Lightpanda",
    "Playwright",
    "Chrome DevTools Protocol",
    "Model Context Protocol",
    "uv",
    "pip"
  ],
  "summary": "A Python package that bundles the Lightpanda headless browser, exposing fetch, CDP server, and MCP server helpers. It supports page fetching with Markdown or JSON output and integration with Playwright and Puppeteer.",
  "use_cases": [
    "Fetching and extracting web page content for AI agents",
    "Running a CDP server for Playwright or Puppeteer automation",
    "Exposing a headless browser to MCP-compatible clients"
  ],
  "limitations": [
    "Depends on the bundled Lightpanda binary and its supported platform assets",
    "README excerpt is truncated; full feature and platform coverage is not verified",
    "No license specified in metadata"
  ],
  "suggested_terms": [
    "headless browser python",
    "lightpanda",
    "CDP server",
    "web scraping python",
    "MCP browser server"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
