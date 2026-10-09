---
repository: "pydantic/pydantic-ai"
github_id: 818331198
url: "https://github.com/pydantic/pydantic-ai"
description: "How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end."
starred_at: "2026-10-09T14:07:39Z"
language: "Python"
topics: ["agent-framework", "genai", "harness", "harness-engineering", "llm", "pydantic", "python"]
homepage: "https://pydantic.dev/pydantic-ai"
license: "MIT"
archived: false
---

# pydantic/pydantic-ai

How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.

**GitHub:** https://github.com/pydantic/pydantic-ai

## README excerpt

> How Python does AI
>
> Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.
>
> ---
> **Pydantic AI** is the Python AI SDK: a typed, [extensible](https://pydantic.dev/docs/ai/guides/extensibility/) agent loop with [every model](https://pydantic.dev/docs/ai/models/overview/) a string swap away. The same agent [runs everywhere you need it](https://pydantic.dev/docs/ai/overview/interfaces/): behind a [web frontend](https://pydantic.dev/docs/ai/integrations/ui/overview/), in the [terminal](https://pydantic.dev/docs/ai/integrations/cli/), on a [voice call](https://pydantic.dev/docs/ai/realtime/overview/), on a [durable background queue](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/), in [GitHub Actions](https://pydantic.dev/docs/ai/harness/gh-aw/), or as a plain object you call [`run()`](https://pydantic.dev/docs/ai/core-concepts/agent/#running-agents) on. [Image generation](https://pydantic.dev/docs/ai/guides/image-generation/) and [embeddings](https://pydantic.dev/docs/ai/guides/embeddings/) come in the same box; [Pydantic Graph](https://pydantic.dev/docs/ai/graph/graph/) and [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) are separate packages, for typed control flow and for testing agent behavior the way pytest tests code.
> **[Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/)** has everything an agent needs for complex, long-running work, snapped on as [capabilities](https://pydantic.dev/docs/ai/capabilities/overview/), from [memory](https://pydantic.dev/docs/ai/harness/memory/), [guardrails](https://pydantic.dev/docs/ai/harness/guardrails/), and [sub-agents](https://pydantic.dev/docs/ai/harness/subagents/) to [planning](https://pydantic.dev/docs/ai/harness/planning/), [context management](https://pydantic.dev/docs/ai/harness/compaction/), and [persistence](https://pydantic.dev/docs/ai/core-concepts/persistence/), up to a complete [coding agent](https://pydantic.dev/docs/ai/harness/coder/).
> [Pydantic Logfire](https://pydantic.dev/logfire?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai) is the AI observability platform that sees your whole app, not just the LLM calls, and the [Pydantic AI Gateway](https://pydantic.dev/ai-gateway?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai) is one key for every model with real-time cost monitoring and budget control; the Gateway self-hosts if you would rather, and our [instrumentation](https://pydantic.dev/doc

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Pydantic AI is a Python SDK providing a typed agent loop that works across many LLM providers. The README also describes image generation, embeddings, sub-agents, and Pydantic Graph and Pydantic Evals as separate packages for control flow and agent testing.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "35c4e17123bf607c62dbc2dfeacfbb950435e1efd75172499706938b202850bc"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "image-generation",
    "model-evaluation",
    "workflow-orchestration"
  ],
  "technologies": [
    "Python",
    "Pydantic",
    "Pydantic Graph",
    "Pydantic Evals"
  ],
  "summary": "Pydantic AI is a Python SDK providing a typed agent loop that works across many LLM providers. The README also describes image generation, embeddings, sub-agents, and Pydantic Graph and Pydantic Evals as separate packages for control flow and agent testing.",
  "use_cases": [
    "Building typed Python AI agents",
    "Running agents behind web, CLI, or voice interfaces",
    "Testing agent behavior with pytest-style evaluations"
  ],
  "limitations": [
    "Logfire observability and AI Gateway are separate hosted products, not delivered by this repository",
    "Realtime voice and harness features are described in the README but not verified in this record"
  ],
  "suggested_terms": [
    "pydantic-ai agent framework",
    "python llm agent sdk",
    "pydantic evals",
    "pydantic graph",
    "typed llm agents"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
