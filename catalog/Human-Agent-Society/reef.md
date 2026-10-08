---
repository: "Human-Agent-Society/reef"
github_id: 1351879111
url: "https://github.com/Human-Agent-Society/reef"
description: "Infrastructure for continually self‑improving agents"
starred_at: "2026-10-08T20:36:39Z"
language: "Python"
topics: ["agent-infrastructure", "ai-agents", "continual-learning", "inference", "llm", "llm-training", "reinforcement-learning", "self-improving-agents"]
homepage: "https://reefinfra.ai"
license: "Apache-2.0"
archived: false
---

# Human-Agent-Society/reef

Infrastructure for continually self‑improving agents

**GitHub:** https://github.com/Human-Agent-Society/reef

## README excerpt

> Infrastructure for continually self‑improving agents
> English | [中文](README.zh.md)
> Reef is the first open-source infrastructure for continual self-improving agents.
> It connects agent inference, feedback, learning, and versioned delivery. Use it
> to train model weights with Slime and SGLang, or improve an agent's harness, including its prompts, rules, and skills.
> **🚀 [Get started](https://reefinfra.ai/docs/getting-started/quickstart/) |
> 🗺️ [Roadmap](https://github.com/Human-Agent-Society/reef/issues/25) |
> 📣 [Launch post](https://x.com/ao_qu18465/status/2094867930081337730) |
> 💬 [Join Discord](https://discord.gg/5y8e5f937k) |
> 📱 [Join WeChat Group](docs/community/wechat.md)**
> ## 🎯 When to use Reef
> Use Reef when you want your agent to keep improving simply by learning from how you interact with your agent.
> | Your goal | Learning path | What you need |
> |---|---|---|
> | Keep getting stronger model designed for you | Model weight training | A trainable model, a supported GPU stack, and feedback your recipe can use |
> | Get your harness to self-improve | Harness optimization | A model endpoint, representative tasks, and an evaluator; no local training GPUs |
> | Scientific discoveries | Test-time training | An execution environment, a correctness checker, and a measurable objective |
> ## 🧩 How Reef fits your stack
> | Ability | Inference engine (vLLM, SGLang, …) | RL training framework (Slime, veRL, AReaL, …) | **Reef** |
> |---|:---:|:---:|:---:|
> | Serves live traffic | ✅ | ❌ | ✅ |
> | Trains weights | ❌ | ✅ | ✅ |
> | Version management | ❌ | ❌ | ✅ |
> | Stays live through updates | ❌ | ❌ | ✅ |
> | Evolves beyond weights (skills, harness) | ❌ | ❌ | ✅ |
> ## 🔄 How it works
>
>
> Reef processes each learning cycle in four steps. The table also shows which
> modules implement each step.
> | Step | What happens | Where it lives |
> |---|---|---|
> | **1&nbsp;·&nbsp;Serve** | Serve agent requests and record interactions. | [`service/`](reef/service) — agent requests and interaction records[`runtime/`](reef/runtime) — inference and artifact updates |
> | **2&nbsp;·&nbsp;Observe** | Match feedback to recorded interactions. | [`storage/records.py`](reef/storage/records.py) — stored interactions and feedback[`train/processors/`](reef/train/processors) — feedback matching and eligibility |
> | **3&nbsp;·&nbsp;Grow** | Produce an update from eligible records. | [`recipe/`](reef/recipe) — recipe integration[`train/`](reef/train) — batches and update jobs |
> | **4&nbsp;·&nbsp;Commit** | Apply the configured sele

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Reef is an open-source infrastructure for continually self-improving agents. It connects agent inference, feedback, learning, and versioned delivery, and can train model weights or improve an agent's harness, including prompts, rules, and skills. The README excerpt describes this scope; features were not verified against the code.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "edd4dd24c92523c13a4cca7967f88393a7ee820f9049cc8b9f76a9c6123a34c6"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools",
    "research-learning"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "model-training",
    "inference-serving",
    "fine-tuning",
    "workflow-orchestration"
  ],
  "technologies": [
    "Python",
    "SGLang",
    "Slime",
    "vLLM",
    "veRL",
    "AReaL",
    "LLM",
    "reinforcement learning"
  ],
  "summary": "Reef is an open-source infrastructure for continually self-improving agents. It connects agent inference, feedback, learning, and versioned delivery, and can train model weights or improve an agent's harness, including prompts, rules, and skills. The README excerpt describes this scope; features were not verified against the code.",
  "use_cases": [
    "Improving model weights from user interaction feedback",
    "Optimizing an agent's prompts, rules, and skills using an evaluator",
    "Running test-time training against a measurable objective"
  ],
  "limitations": [
    "Model weight training requires a trainable model and a supported GPU stack",
    "Harness optimization requires representative tasks and an evaluator",
    "Details are from a README excerpt that was cut off, so the full feature set is unconfirmed"
  ],
  "suggested_terms": [
    "continual learning agents",
    "self-improving agents",
    "agent harness optimization",
    "LLM reinforcement learning infrastructure",
    "versioned agent delivery"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
