---
repository: "langchain-ai/deepagents"
github_id: 1027384981
url: "https://github.com/langchain-ai/deepagents"
description: "The batteries-included agent harness."
starred_at: "2026-10-08T20:39:54Z"
language: "Python"
topics: ["ai", "deepagents", "harness", "harness-engineering", "langchain", "langgraph", "python", "typescript"]
homepage: "https://docs.langchain.com/deepagents"
license: "MIT"
archived: false
---

# langchain-ai/deepagents

The batteries-included agent harness.

**GitHub:** https://github.com/langchain-ai/deepagents

## README excerpt

> The batteries-included agent harness.
>
> Deep Agents is an open source agent harness — an opinionated agent that runs out of the box. Extend, override, or replace any piece.
> **Principles:**
> - **Opinionated** — defaults tuned for long-horizon, multi-step work
> - **Extensible** — override or replace any piece without forking
> - **Model-agnostic** — works with any LLM that supports tool calling: frontier, open-weight, or local
> - **Production-ready** — built on LangGraph (streaming, persistence, checkpointing) with first-class tracing, evaluation, and deployment via LangSmith
> **Features include:**
> - **Sub-agents** — delegate tasks to agents with isolated context windows
> - **Filesystem** — read, write, edit, or search over pluggable local, sandboxed, or remote backends
> - **Context management** — summarize long threads and offload tool outputs to disk
> - **Shell access** — run commands in your sandbox of choice
> - **Persistent memory** — pluggable state and store backends for cross-session recall
> - **Human-in-the-loop** — approve, edit, or reject tool calls before they run
> - **Skills** — reusable behaviors the agent can load on demand
> - **Tools** — bring your own functions or any MCP server
> Deep Agents is available as a JavaScript/TypeScript library — see [deepagents.js](https://github.com/langchain-ai/deepagentsjs).
> > [!NOTE]
> > **Deep Agents Code** — a pre-built coding agent in your terminal, similar to Claude Code or Cursor, powered by any LLM. Install with `curl -LsSf https://langch.in/dcode | bash`. See the [documentation](https://docs.langchain.com/deepagents-code) for the full feature set.
> ## Quickstart
> uv add deepagents
> from deepagents import create_deep_agent
> agent = create_deep_agent(
> model="openai:gpt-6-astra",
> system_prompt="You are a research assistant.",
> )
> result = agent.invoke({"messages": "Research LangGraph and write a summary"})
> The agent can plan, read/write files, and manage its own context. Add your own tools, swap models, customize prompts, configure sub-agents, and more. See the [documentation](https://docs.langchain.com/oss/python/deepagents/overview) for full details.
> > [!TIP]
> > For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home).
> ## FAQ
> ### How is this different from LangGraph or LangChain?
> LangGraph is the graph runtime. LangChain's `create_agent` is a minimal agent harness on top of it. Deep Agents is a more opinionated harness on top of `create_agent` — same

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Deep Agents is an open source, opinionated agent harness built on LangGraph, offering sub-agents, pluggable filesystem and memory backends, context management, and human-in-the-loop tool approval. It is available as Python and JavaScript/TypeScript libraries and includes a terminal coding agent.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "70a39604807a06e92589a2fb1e29f891b17b986da4eb51f3c1dfe936fc7bfeaf"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "workflow-orchestration",
    "task-management",
    "api-integration",
    "storage"
  ],
  "technologies": [
    "Python",
    "TypeScript",
    "LangGraph",
    "LangChain",
    "LangSmith",
    "MCP"
  ],
  "summary": "Deep Agents is an open source, opinionated agent harness built on LangGraph, offering sub-agents, pluggable filesystem and memory backends, context management, and human-in-the-loop tool approval. It is available as Python and JavaScript/TypeScript libraries and includes a terminal coding agent.",
  "use_cases": [
    "Long-horizon, multi-step agent tasks",
    "Building custom LLM agents with extensible tools and sub-agents",
    "Running a terminal-based coding agent"
  ],
  "limitations": [
    "Requires an LLM that supports tool calling",
    "Depends on the LangGraph/LangChain ecosystem",
    "Some advanced features reference LangSmith for tracing and deployment"
  ],
  "suggested_terms": [
    "agent harness",
    "LangGraph agents",
    "deep agents",
    "sub-agents LLM",
    "human-in-the-loop agents"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
