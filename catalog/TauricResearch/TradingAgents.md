---
repository: "TauricResearch/TradingAgents"
github_id: 909213664
url: "https://github.com/TauricResearch/TradingAgents"
description: "TradingAgents: Multi-Agents LLM Financial Trading Framework"
starred_at: "2026-10-08T20:17:17Z"
language: "Python"
topics: ["agent", "finance", "llm", "multiagent", "trading"]
homepage: "https://arxiv.org/pdf/2412.20138"
license: "Apache-2.0"
archived: false
---

# TauricResearch/TradingAgents

TradingAgents: Multi-Agents LLM Financial Trading Framework

**GitHub:** https://github.com/TauricResearch/TradingAgents

## README excerpt

> ---
> # TradingAgents: Multi-Agents LLM Financial Trading Framework
> ## News
> - [2026-10] **TradingAgents v0.6.0** released with reports saved as one HTML page, a provider per model tier so the managers and analysts can run on different models, past decisions settled for every ticker while the analysts work, and company news read from Yahoo search while Yahoo's news feed is down.
> - [2026-09] **TradingAgents v0.5.2** released with parallel analysts for a faster analysis, a CLI that runs without prompts from flags such as `--ticker` and `--date`, the run's settings recorded in every report, and backtests that see only data published by each analysis date.
> - [2026-09] **TradingAgents v0.5.1** released with a package layout organised by what each module holds (import paths moved), optional Jev screening of social posts, GPT-6 Sol and Luna as the default models, and fixes to run isolation and SEC EDGAR statements.
> Full release notes are in [CHANGELOG.md](CHANGELOG.md).
>
> Earlier news
> - [2026-09] **TradingAgents v0.5.0** released with point-in-time integrity across every dated path, SEC EDGAR fundamentals served as filed, backtesting over a ticker and date grid, portfolio-aware runs, and current model lineups across every provider.
> - [2026-08] **TradingAgents v0.4.0** released with look-ahead / point-in-time fixes across FRED macro, social sentiment, and the decision-log memory; clearer decision signals; working CLI checkpoint resume; Trader price grounding; and the GPT-5.6 and GLM-5.3 models.
> - [2026-07] **TradingAgents v0.3.1** released with correctness and stability fixes: Alpha Vantage look-ahead filtering, graph-router crash-safety, graph-shape-aware checkpoint resume, working crypto sentiment sources, a configurable LLM retry budget, Bedrock API-key auth, and Claude Sonnet 5 / Fable 5 support.
> - [2026-06] **TradingAgents v0.3.0** released with a verified data-access contract, an expanded provider registry (NVIDIA, Kimi, Groq, Mistral, Bedrock, and any OpenAI-compatible endpoint), FRED and Polymarket data vendors, a current-generation model catalog, and a CI gate.
> - [2026-05] **TradingAgents v0.2.5** released with the grounded Sentiment Analyst, GPT-5.5 etc. model coverage, Qwen/GLM/MiniMax dual-region support, `TRADINGAGENTS_*` env-var configurability with API-key auto-detection, remote Ollama support, non-US alpha benchmarks, and ticker path-traversal hardening.
> - [2026-04] **TradingAgents v0.2.4** released with structured-output agents (Research Manager,

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

TradingAgents is a multi-agent LLM framework for financial trading analysis, with analyst, research, and trader roles. The README describes a CLI, backtesting over ticker and date grids, HTML reports, and support for multiple LLM providers and financial data vendors.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "d26de08210b51607780021a3bde02514187f0568abf221610806b1fc53b68fd5"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "productivity"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "data-ingestion",
    "model-evaluation",
    "reporting",
    "benchmarking"
  ],
  "technologies": [
    "Python",
    "LLM",
    "OpenAI",
    "Anthropic",
    "Ollama",
    "FRED",
    "Alpha Vantage",
    "SEC EDGAR"
  ],
  "summary": "TradingAgents is a multi-agent LLM framework for financial trading analysis, with analyst, research, and trader roles. The README describes a CLI, backtesting over ticker and date grids, HTML reports, and support for multiple LLM providers and financial data vendors.",
  "use_cases": [
    "Running multi-agent LLM analysis of stock tickers",
    "Backtesting LLM-driven trading decisions over date ranges",
    "Comparing LLM providers and models for financial analysis"
  ],
  "limitations": [
    "README describes release notes only; trading performance claims are not verified here",
    "Requires API keys or self-hosted models for LLM and data providers",
    "Some data sources are noted as temporarily unavailable in release notes"
  ],
  "suggested_terms": [
    "multi-agent trading",
    "LLM finance",
    "stock analysis agents",
    "backtesting LLM",
    "financial agents"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
