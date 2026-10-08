---
repository: "CloakHQ/CloakBrowser"
github_id: 1163834030
url: "https://github.com/CloakHQ/CloakBrowser"
description: "Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed."
starred_at: "2026-10-08T20:15:26Z"
language: "Python"
topics: ["ai-agents", "anti-detect", "antidetect-browser", "bot-detection", "browser-automation", "captcha-bypass", "chromium", "cloudflare", "cloudflare-bypass", "fingerprint", "headless-browser", "playwright", "puppeteer", "python", "recaptcha", "selenium", "stealth-browser", "undetected", "web-scraping", "webscraping"]
homepage: "https://cloakbrowser.dev/"
license: "MIT"
archived: false
---

# CloakHQ/CloakBrowser

Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.

**GitHub:** https://github.com/CloakHQ/CloakBrowser

## README excerpt

> Stealth Chromium that passes every bot detection test.
>
> Not a patched config. Not a JS injection. A real Chromium binary with fingerprints modified at the C++ source level. Antibot systems score it as a normal browser — because it is a normal browser.
>
>
>
> Cloudflare Turnstile — 3 live tests passing (headed mode, macOS)
>
>
>
> Drop-in Playwright/Puppeteer replacement for Python and JavaScript.
> Same API, same code — just swap the import. 3 lines of code, 30 seconds to unblock.
>
> - **87 source-level C++ patches** — canvas, WebGL, audio, fonts, GPU, screen, WebRTC, network timing, automation signals, CDP input behavior
> - **`humanize=True`** — human-like mouse curves, keyboard timing, and scroll patterns. One flag, behavioral detection passes
> - **Pro: 0.9 reCAPTCHA v3 score** — human-level, server-verified
> - **Passes Cloudflare Turnstile**, FingerprintJS, BrowserScan — tested against 30+ detection sites
> - **Auto-downloads the right binary** — free or Pro based on your license
> - **`pip install cloakbrowser`** or **`npm install cloakbrowser`** — binary auto-downloads, zero config
> - **Latest binary, free to try** — [sign in with GitHub](https://cloakbrowser.dev/free), point the newest build at your hardest target, scale to thousands of sessions on Pro
> **Try it now** — no install needed:
> docker run --rm cloakhq/cloakbrowser cloaktest
> **Python:**
> from cloakbrowser import launch
> browser = launch()
> page = browser.new_page()
> page.goto("https://example.com")
> browser.close()
> **JavaScript (Playwright):**
> import { launch } from 'cloakbrowser';
> const browser = await launch();
> const page = await browser.newPage();
> await page.goto('https://example.com');
> await browser.close();
> Also works with Puppeteer: `import { launch } from 'cloakbrowser/puppeteer'` ([details](#puppeteer))
> **For sites with anti-bot protection**, add a residential proxy and these flags:
> browser = launch(
> proxy="http://user:pass@residential-proxy:port",  # residential IP, not datacenter
> geoip=True,       # match timezone + locale to proxy IP
> headless=False,    # some sites detect headless even with C++ patches
> humanize=True,     # human-like mouse, keyboard, scroll
> )
> const browser = await launch({
> proxy: 'http://user:pass@residential-proxy:port',
> geoip: true,
> headless: false,
> humanize: true,
> });
> See [Troubleshooting](#troubleshooting) for site-specific issues (FingerprintJS, Kasada, reCAPTCHA).
> ## Install
> **Python:**
> pip install cloakbrowser
> **JavaScript / Node.js:**
> # With Playwright
> npm install cloakbrowse

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A Chromium-based browser automation library offered as a drop-in replacement for Playwright and Puppeteer in Python and JavaScript. The README documents source-level C++ fingerprint patches, optional humanized input, proxy and geoip options, and automatic binary download; its bot-detection pass claims are not independently verified here.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "ebe41e2476d7e6db16e2228334c5e33408b02f062b94b9ed334bce5262bf4d09"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "security"
  ],
  "repository_type": "library",
  "capabilities": [
    "automation",
    "web-scraping",
    "api-integration",
    "containerization"
  ],
  "technologies": [
    "Python",
    "JavaScript",
    "Node.js",
    "Chromium",
    "Playwright",
    "Puppeteer",
    "Docker",
    "C++"
  ],
  "summary": "A Chromium-based browser automation library offered as a drop-in replacement for Playwright and Puppeteer in Python and JavaScript. The README documents source-level C++ fingerprint patches, optional humanized input, proxy and geoip options, and automatic binary download; its bot-detection pass claims are not independently verified here.",
  "use_cases": [
    "Automating browser sessions for web scraping",
    "Running Playwright or Puppeteer scripts against sites with anti-bot protection",
    "Launching a prebuilt headless Chromium environment via Docker"
  ],
  "limitations": [
    "README bot-detection and reCAPTCHA score claims are vendor-reported and unverified",
    "Some sites detect headless mode, so the README recommends headed mode for them",
    "Pro tier features and scaling require a paid license"
  ],
  "suggested_terms": [
    "stealth browser",
    "playwright alternative",
    "browser fingerprint",
    "headless chromium automation",
    "anti-bot browser"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
