---
repository: "langchain-ai/langchain"
github_id: 552661142
url: "https://github.com/langchain-ai/langchain"
description: "The agent engineering platform."
starred_at: "2026-03-23T21:15:11Z"
language: "Python"
topics: ["agents", "ai", "ai-agents", "anthropic", "chatgpt", "deepagents", "enterprise", "framework", "gemini", "generative-ai", "langchain", "langgraph", "llm", "multiagent", "open-source", "openai", "pydantic", "python", "rag", "typescript"]
homepage: "https://docs.langchain.com/langchain/"
license: "MIT"
archived: false
---

# langchain-ai/langchain

The agent engineering platform.

**GitHub:** https://github.com/langchain-ai/langchain

## README excerpt

> The agent engineering platform.
>
> LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves.
> > [!TIP]
> > Just getting started? Check out **[Deep Agents](https://docs.langchain.com/oss/python/deepagents/)** — a higher-level package built on LangChain for agents that have built-in capabilities for common usage patterns such as planning, subagents, file system usage, and more.
> ## Quickstart
> uv add langchain
> from langchain.chat_models import init_chat_model
> model = init_chat_model("openai:gpt-5.5")
> result = model.invoke("Hello, world!")
> If you're looking for more advanced customization or agent orchestration, check out [LangGraph](https://github.com/langchain-ai/langgraph), our framework for building controllable agent workflows.
> For an equivalent JS/TS library, check out [LangChain.js](https://github.com/langchain-ai/langchainjs).
> > [!TIP]
> > For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home).
> ## LangChain ecosystem
> While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications.
> - **[Deep Agents](https://docs.langchain.com/oss/python/deepagents/)** — Build agents that can plan, use subagents, and leverage file systems for complex tasks
> - **[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)** — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework
> - **[Integrations](https://docs.langchain.com/oss/python/integrations/providers/overview)** — Chat & embedding models, tools & toolkits, and more
> - **[LangSmith](https://www.langchain.com/langsmith)** — Agent evals, observability, and debugging for LLM apps
> - **[LangSmith Deployment](https://docs.langchain.com/langsmith/deployments)** — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows
> ## Why use LangChain?
> LangChain helps developers build applications powered by LLMs through a standard interface for models, embeddings, vector stores, and more.
> - **Real-time data augmentation** — Easily connect LLMs to diverse data sources and external/internal systems, drawing from LangChain's vast library of integrations

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

LangChain is a framework for building agents and LLM-powered applications, offering standard interfaces for models, embeddings, and vector stores. It provides interoperable components and third-party integrations, and links to related projects such as LangGraph, Deep Agents, and LangSmith.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "7fa9fdb147715f8fdd85fc52b40ea45aacecaa5354c558eed6461e8912837f31"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "api-integration",
    "inference-serving",
    "search-retrieval",
    "workflow-orchestration"
  ],
  "technologies": [
    "Python",
    "TypeScript",
    "Pydantic",
    "LangGraph",
    "OpenAI",
    "Anthropic",
    "Gemini",
    "RAG"
  ],
  "summary": "LangChain is a framework for building agents and LLM-powered applications, offering standard interfaces for models, embeddings, and vector stores. It provides interoperable components and third-party integrations, and links to related projects such as LangGraph, Deep Agents, and LangSmith.",
  "use_cases": [
    "Building LLM-powered applications with chained components",
    "Creating agents with tool and model integrations",
    "Connecting LLMs to external and internal data sources"
  ],
  "limitations": [
    "Observability, evals, and debugging are provided by the separate LangSmith product",
    "Advanced agent orchestration is provided by the separate LangGraph project",
    "Source README claims are not independently verified"
  ],
  "suggested_terms": [
    "llm framework",
    "agent framework",
    "rag",
    "langchain integrations",
    "llm application development"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
