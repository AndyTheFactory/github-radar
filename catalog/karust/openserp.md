---
repository: "karust/openserp"
github_id: 657380031
url: "https://github.com/karust/openserp"
description: "Self-hosted SERP API for AI, SEO & automation. Browser-rendered Google, Bing, Yandex, Baidu, DuckDuckGo and Ecosia search with page extraction 🎉"
starred_at: "2026-10-19T11:32:10Z"
language: "Go"
topics: ["ai", "api", "baidu", "bing", "cli", "duckduckgo", "ecosia", "google", "llm", "openserp", "opensource", "search", "search-engine", "seo", "serp", "serpapi", "web-scraping", "yandex"]
homepage: "https://openserp.org"
license: "MIT"
archived: false
---

# karust/openserp

Self-hosted SERP API for AI, SEO & automation. Browser-rendered Google, Bing, Yandex, Baidu, DuckDuckGo and Ecosia search with page extraction 🎉

**GitHub:** https://github.com/karust/openserp

## README excerpt

> # OpenSERP
> **OpenSERP** is a free, open-source SERP API and CLI for Google, Yandex, Baidu, Bing, DuckDuckGo, and Ecosia.
> No API keys, no per-search billing: one command gives you live, structured search results on localhost - including engines the paid APIs don't cover. Use it as a search tool for LLMs and agents, or as a backend for SEO rank tracking. If you'd rather not run infrastructure, there is a [hosted version](https://openserp.org/cloud) with the same API.
> ## Features
> - Dedicated endpoints for six engines, same JSON schema across all of them
> - **Megasearch** - one query across several engines at once, merged and deduped
> - **URL extraction** - search results plus clean markdown of the target pages in one call
> - SERP features: AI summaries, answer boxes, people-also-ask, related searches
> - Image search, filters (language, date range, file type, site), **JSON/Markdown/Text/NdJSON** output
> - Proxies, cache, resilient mode, prebuilt Docker images
> ## Quick Start
> ### Docker
> Prebuilt images are published to [docker hub: `karust/openserp`](https://hub.docker.com/r/karust/openserp).
> # Run the API server via prebuilt image
> docker run --rm -p 127.0.0.1:7000:7000 karust/openserp:latest serve -a 0.0.0.0 -p 7000
> # Or
> docker compose up
> ### Go install
> go install github.com/karust/openserp@latest
> openserp search duckduckgo "open source serp api" --format markdown
> ### From Source
> git clone https://github.com/karust/openserp.git
> cd openserp
> go build -o openserp .
> ./openserp serve
> ### First request
> # mode=any returns the first engine that responds
> curl "http://127.0.0.1:7000/mega/search?engines=bing,google&text=golang+vs+rust&extract=1&mode=any"
>
> Example JSON response
> {
> "query": {
> "text": "golang vs rust",
> "engines_requested": ["bing", "google"]
> },
> "meta": {
> "request_id": "019ecdc0-a66d-79a4-9d2b-9e9b480d495e",
> "requested_at": "2026-06-16T00:06:55Z",
> "took_ms": 720,
> "engines_responded": ["bing"],
> "engines_failed": [],
> "version": "2.1"
> },
> "results": [
> {
> "id": "s_5a8273f16b19ab64",
> "rank": 1,
> "type": "organic",
> "title": "The Go Programming Language",
> "url": "https://go.dev/",
> "display_url": "go.dev",
> "snippet": "Get Started Playground Tour Stack Overflow Help Packages Standard Library …",
> "domain": "go.dev",
> "favicon": "https://go.dev/favicon.ico",
> "position": {
> "absolute": 1
> },
> "engine": "bing",
> "domain_info": {
> "tld": "dev",
> "sld": "go",
> "category": ""
> },
> "extracted": {
> "title": "Build simple, secure, scalable systems with Go",
> "format": "markdown",
> "content": "## Bui

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

OpenSERP is a self-hosted Go application that provides a CLI and HTTP API for searching Google, Bing, Yandex, Baidu, DuckDuckGo and Ecosia through a browser-rendered backend. It returns structured search results in a shared JSON schema and can extract markdown content from result pages.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "c07a1960102ff203d1d758ec012253eec235029bb8fbed57b269d7f06cd59b20"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "data-engineering",
    "vision-media"
  ],
  "repository_type": "application",
  "capabilities": [
    "api-integration",
    "web-scraping",
    "search-retrieval",
    "data-transformation",
    "image-generation"
  ],
  "technologies": [
    "Go",
    "Docker",
    "Docker Compose"
  ],
  "summary": "OpenSERP is a self-hosted Go application that provides a CLI and HTTP API for searching Google, Bing, Yandex, Baidu, DuckDuckGo and Ecosia through a browser-rendered backend. It returns structured search results in a shared JSON schema and can extract markdown content from result pages.",
  "use_cases": [
    "Providing live search results to LLMs or agents without per-search API billing",
    "Backing SEO rank tracking across multiple search engines",
    "Running a local multi-engine search endpoint via Docker or Go install"
  ],
  "limitations": [
    "Requires self-hosting infrastructure unless the separate hosted cloud version is used",
    "Results depend on scraping rendered search engine pages, which may change or be rate-limited"
  ],
  "suggested_terms": [
    "serp api",
    "self-hosted search api",
    "multi-engine search",
    "web search scraper",
    "search results extraction"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
