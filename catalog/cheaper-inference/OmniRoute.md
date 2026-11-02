---
repository: "cheaper-inference/OmniRoute"
github_id: 1157102282
url: "https://github.com/cheaper-inference/OmniRoute"
description: "Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors"
starred_at: "2026-11-02T19:10:46Z"
language: "TypeScript"
topics: ["a2a", "ai-agents", "ai-gateway", "anthropic", "claude", "claude-code", "cline", "codex", "copilot", "cursor", "deepseek", "free-ai", "gemini", "kimi", "llm-gateway", "mcp", "openai", "openai-proxy", "qwen", "token-saver"]
homepage: "https://omniroute.online"
license: "MIT"
archived: false
---

# cheaper-inference/OmniRoute

Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors

**GitHub:** https://github.com/cheaper-inference/OmniRoute

## README excerpt

> # 🚀 OmniRoute — The Free AI Gateway
> ## 💰 ~1.62B Tokens / Month Across Third-Party Free Tiers
> > **Bring your own provider accounts.** This is an estimated aggregate across separately eligible third-party free tiers, not a token grant from OmniRoute. Sign up, obtain credentials where required, and connect the providers you can use; each provider controls its limits, availability, and terms.
> >
> > Stacking free tiers by hand is painful — dozens of SDKs, dozens of rate limits, and no idea how much you actually have. OmniRoute catalogs **485 free-tier entries across 34 recurring pool keys** and computes the token headline from the **17 pools with a published positive monthly budget plus five per-model Groq caps**, deduplicated by shared pool. Quotas that only open after a regional identity check (today: ModelScope) are shown apart, +~6M behind regional identity verification, and never summed into the headline. The result stays visible on the dashboard (`/dashboard/free-tiers`).
> > Animated summary of the live `/dashboard/free-tiers` page. Full methodology (pool dedupe, credit tiers, provider terms): **[docs/reference/FREE_TIERS.md](docs/reference/FREE_TIERS.md)**.
> >
> > These figures are re-audited every two weeks against the live catalog and **move both ways** — a provider ends a free tier and the number drops; a new one lands and it climbs. We publish what the catalog actually computes, never a rounded-up best case.
>
>
> ⭐ Star the repo if OMNIROUTE helped you save money and make your work easier.
>
> ### 💬 Join the community
> **👋 Follow the maintainer — get new providers, releases & tips first:**
> **Questions, provider tips, roadmap & support → [Discord](https://discord.gg/U47eFqAXCn) · [Telegram](https://t.me/omnirouteOficial) · WhatsApp [🌍 Global](https://chat.whatsapp.com/FvuCbrpZmQ6I85n2vW5QIC?s=cl&p=a&mlu=4) / [🇧🇷 Brasil](https://chat.whatsapp.com/KWgatljAjmbELQory59Oti?s=cl&p=a&mlu=4) / [Portal](https://portal.sthub.com.br/communities/groups/st-hub/channels/Omniroute-World-8kRjmK)**
>
> ## 📈 The Gateway Keeps Growing
> |                           |          v3.8.50          | **v3.8.51** |      `v3.8.53+`       |
> | ------------------------- | :-----------------------: | :---------: | :-------------------: |
> | 🌐 Providers              |            352            |   **358**   |          380          |
> | 🧠 Unique chat model IDs  |           1320            |  **1374**   |         1475          |
> | 🖼️ Modality Bridge        | 🆕 vision + audio + video |      ✓      |

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

OmniRoute is described as an MIT-licensed AI gateway that exposes one endpoint routing to many third-party LLM providers, with quota-aware fallback, token compression, and MCP/A2A support. The README states users must bring their own provider accounts and credentials, and that free-tier figures are third-party estimates.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "a11060106f5ad10bf541679eef093e596e61a8587bb953898225e2a5dff06170"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools",
    "infrastructure"
  ],
  "repository_type": "service",
  "capabilities": [
    "api-integration",
    "inference-serving",
    "agent-orchestration",
    "automation",
    "authorization"
  ],
  "technologies": [
    "TypeScript",
    "MCP",
    "A2A",
    "OpenAI-compatible API",
    "Anthropic API",
    "Docker"
  ],
  "summary": "OmniRoute is described as an MIT-licensed AI gateway that exposes one endpoint routing to many third-party LLM providers, with quota-aware fallback, token compression, and MCP/A2A support. The README states users must bring their own provider accounts and credentials, and that free-tier figures are third-party estimates.",
  "use_cases": [
    "Routing coding-assistant tools such as Claude Code, Cursor, or Cline through a single gateway endpoint",
    "Falling back to alternate providers when a quota is exhausted",
    "Comparing and tracking free-tier availability across providers"
  ],
  "limitations": [
    "Relies on third-party provider accounts, credentials, limits, and terms that OmniRoute does not control",
    "Free-tier token totals are estimates that change as providers change their offerings",
    "README figures (provider and model counts) are source claims that were not independently verified"
  ],
  "suggested_terms": [
    "llm gateway",
    "ai proxy",
    "openai compatible",
    "mcp server",
    "llm fallback"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
