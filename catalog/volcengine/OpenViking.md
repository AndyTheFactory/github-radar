---
repository: "volcengine/OpenViking"
github_id: 1128123594
url: "https://github.com/volcengine/OpenViking"
description: "Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills."
starred_at: "2026-10-19T11:01:11Z"
language: "Python"
topics: ["agent-context", "agent-memory", "agent-plugins", "agentic-rag", "context-database", "dsh-plugin", "knowledge-base", "memory", "memory-management", "self-evolving", "vector-database"]
homepage: "https://openviking.ai"
license: "AGPL-3.0"
archived: false
---

# volcengine/OpenViking

Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills.

**GitHub:** https://github.com/volcengine/OpenViking

## README excerpt

> ### The Context Database for AI Agents
> English / [中文](docs/repository/README_CN.md) / [日本語](docs/repository/README_JA.md)
>
>
>
>
>
>
> ***
> ## What is OpenViking
> OpenViking is an open-source context database for AI agents — one filesystem for everything an agent knows: knowledge, memory, and skills.
> Most agent memory is a black box: text goes in, embeddings come out, and nobody can see what was actually stored. OpenViking organizes context as a virtual filesystem under `viking://` instead. Agents navigate it like files — `ls`, `tree`, `read`, `write`, `grep` — and you can open any directory to inspect and edit what your agent knows. Every directory carries a generated summary, so agents can scan summaries first and decide what to read.
>
>
> [Try OpenViking Studio](https://studio.openviking.ai) in your browser, no installation required. [Self-host Web Studio](web-studio/README.md).
> ## Why OpenViking
> - **One filesystem for knowledge, memory, and skills.** Resources hold documents and code; memories retain user preferences and experience; skills define how to perform tasks — not just extracted facts, but the full context, each with a `viking://` URI for browsing and retrieval. → [Viking URI](https://docs.openviking.ai/en/concepts/04-viking-uri) · [Context types](https://docs.openviking.ai/en/concepts/02-context-types)
> - **Search a directory, not the whole index.** Scope semantic search to a project or memory subtree instead of scanning a flat vector pool. `find` runs a query directly; `search` plans retrieval from session context. → [Retrieval](https://docs.openviking.ai/en/concepts/07-retrieval)
> - **Read the summary before the source.** Generated directory abstracts (L0) and overviews (L1) let agents judge relevance before opening full content (L2). → [Context layers](https://docs.openviking.ai/en/concepts/03-context-layers)
> - **Sessions become files you can read.** Committing a session archives the conversation and extracts memories as Markdown you can inspect, edit, and merge. With VikingBot enabled, `ov compile` organizes source material into a wiki, knowledge graph, or report. → [Sessions](https://docs.openviking.ai/en/concepts/08-session) · [Context compilation](https://docs.openviking.ai/en/context-compilation/01-overview)
> [Architecture](https://docs.openviking.ai/en/concepts/01-architecture) · [Design rationale](https://blog.openviking.ai/post/openviking-context-database/)
> viking://
> ├── resources/              # Resources: project docs, repos, web pages, etc.

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

OpenViking is an open-source context database for AI agents that organizes knowledge, memory, and skills as a virtual filesystem under viking:// URIs. It provides directory-scoped semantic search and generated summaries so agents can inspect and edit stored context.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "a75dc71862f680c25171b9b6b0ec5909f5d4f25b588d5c85a6e3a41541d29b16"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools",
    "databases"
  ],
  "repository_type": "library",
  "capabilities": [
    "indexing",
    "search-retrieval",
    "knowledge-management",
    "storage",
    "data-ingestion"
  ],
  "technologies": [
    "Python",
    "Vector database",
    "Markdown",
    "Agent frameworks"
  ],
  "summary": "OpenViking is an open-source context database for AI agents that organizes knowledge, memory, and skills as a virtual filesystem under viking:// URIs. It provides directory-scoped semantic search and generated summaries so agents can inspect and edit stored context.",
  "use_cases": [
    "Storing and browsing agent memory as readable files",
    "Scoping semantic retrieval to project or memory subtrees",
    "Converting agent sessions into editable Markdown memories"
  ],
  "limitations": [
    "README excerpt does not document installation or API details",
    "Context compilation features require VikingBot to be enabled",
    "Licensed under AGPL-3.0"
  ],
  "suggested_terms": [
    "agent memory",
    "context database",
    "agentic RAG",
    "vector database",
    "agent skills"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
