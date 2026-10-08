---
repository: "lightpanda-io/browser"
github_id: 598667202
url: "https://github.com/lightpanda-io/browser"
description: "Lightpanda: the headless browser designed for AI and automation"
starred_at: "2026-10-08T20:16:10Z"
language: "Zig"
topics: ["browser", "browser-automation", "cdp", "headless", "lightpanda", "playwright", "puppeteer", "zig"]
homepage: "https://lightpanda.io"
license: "AGPL-3.0"
archived: false
---

# lightpanda-io/browser

Lightpanda: the headless browser designed for AI and automation

**GitHub:** https://github.com/lightpanda-io/browser

## README excerpt

> Lightpanda Browser
>
> The headless browser built from scratch for AI agents and automation.
> Not a Chromium fork. Not a WebKit patch. A new browser, written in Zig.
> 16x lighter and 9x faster than Chromium.
>
> [
> ](https://github.com/lightpanda-io/demo)
> &emsp;
> [
> ](https://github.com/lightpanda-io/demo)
> ## Benchmarks
> Requesting 933 real web pages over the network on a AWS EC2 m5.large instance.
> See [benchmark details](https://github.com/lightpanda-io/demo/blob/main/BENCHMARKS.md#crawler-benchmark).
> | Metric | Lightpanda | Headless Chrome | Difference |
> | :---- | :---- | :---- | :---- |
> | Memory (peak, 100 pages) | 123MB | 2GB | ~16x less |
> | Execution time (100 pages) | 5s | 46s | ~9x faster |
> ## Quick start
> ### Install
> **Package Managers**
> Latest nightly from Homebrew:
> brew install lightpanda-io/browser/lightpanda
> Latest nightly from Arch Linux User Repository:
> yay -S lightpanda-nightly-bin
> **Download from the nightly builds**
> You can download the last binary from the [nightly
> builds](https://github.com/lightpanda-io/browser/releases/tag/nightly) for
> Linux and MacOS for both x86_64 and aarch64.
> *For Linux*
> curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux && \
> chmod a+x ./lightpanda
> Verify the binary before running anything:
> ./lightpanda version
> [Linux aarch64 is also available](https://github.com/lightpanda-io/browser/releases/tag/nightly)
> > **Note:** The Linux release binaries are linked against glibc. On musl-based Linux distributions (Alpine, etc.) the binary fails with `cannot execute: required file not found` because the glibc dynamic linker is missing. Use a glibc-based base image (e.g., `FROM debian:bookworm-slim` or `FROM ubuntu:24.04`) or [build from sources](#build-from-sources).
> >
> > **Android / Termux:** there is no native Android build. The Linux aarch64 binary needs the glibc loader (`/lib/ld-linux-aarch64.so.1`), which Android's Bionic libc does not provide, so it fails with the same `cannot execute: required file not found` error.
> *For MacOS*
> curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-aarch64-macos && \
> chmod a+x ./lightpanda
> [MacOS x86_64 is also available](https://github.com/lightpanda-io/browser/releases/tag/nightly)
> *For Windows + WSL2*
> Lightpanda has no native Windows binary. Install it inside WSL following the Linux steps above.
> WSL not installed? Run `wsl --install` from an administrator shell, restart, then open `wsl`.

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Lightpanda is a headless browser written from scratch in Zig, designed for AI agents and automation. The README reports benchmarks against headless Chrome (about 16x less peak memory and 9x faster on 100 pages) and provides Linux, macOS, and WSL2 binaries.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "fae18bea6b2ea355b9439b103ff86ff64821daa647b4407b9c1a8a1d9d8dbc3b"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "infrastructure",
    "ai-ml"
  ],
  "repository_type": "application",
  "capabilities": [
    "web-scraping",
    "automation",
    "api-integration",
    "testing"
  ],
  "technologies": [
    "Zig",
    "Chrome DevTools Protocol",
    "Playwright",
    "Puppeteer",
    "Homebrew",
    "Docker"
  ],
  "summary": "Lightpanda is a headless browser written from scratch in Zig, designed for AI agents and automation. The README reports benchmarks against headless Chrome (about 16x less peak memory and 9x faster on 100 pages) and provides Linux, macOS, and WSL2 binaries.",
  "use_cases": [
    "Running headless browser automation for AI agents",
    "Crawling and fetching web pages with lower memory use than Chromium",
    "Driving the browser via CDP-compatible tools such as Playwright or Puppeteer"
  ],
  "limitations": [
    "No native Windows binary; Windows users must use WSL2",
    "Linux release binaries require glibc, so musl-based distributions like Alpine fail without a build from source",
    "No native Android build; Termux is not supported"
  ],
  "suggested_terms": [
    "headless browser",
    "browser automation",
    "Zig browser",
    "CDP headless",
    "AI agent browser"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
