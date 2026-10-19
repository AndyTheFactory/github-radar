---
repository: "okf-memory/okf-agent-memory"
github_id: 1358571386
url: "https://github.com/okf-memory/okf-agent-memory"
description: "Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with zero external databases or dependencies. Built in pure Go."
starred_at: "2026-10-19T11:42:07Z"
language: "Go"
topics: ["agent-memory", "ai-agents", "bm25", "coding-agents", "developer-tools", "git-native", "go", "golang", "knowledge-base", "knowledge-graph", "llm-memory", "markdown", "mcp", "mcp-server", "model-context-protocol", "okf", "open-knowledge-format", "persistent-memory"]
homepage: "https://okf-memory.dev"
license: "MIT"
archived: false
---

# okf-memory/okf-agent-memory

Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with zero external databases or dependencies. Built in pure Go.

**GitHub:** https://github.com/okf-memory/okf-agent-memory

## README excerpt

> # OKF Agent Memory
> > **A Domain-Neutral, Git-Native Persistent Project Memory for AI Agents based on the Open Knowledge Format (OKF) v0.2.**
> ---
> ## 🌟 Overview
> Conversations with AI agents reset when context windows close. Valuable architectural decisions, domain discoveries, and operational facts are lost unless stored persistently.
> Traditional approaches suffer from two fatal failure modes:
> 1. **The Prompt Monolith**: Stuffing all domain knowledge and rules into `AGENTS.md` or `CLAUDE.md` creates massive context bloat and causes **attention drift** (agents ignore critical instructions).
> 2. **The RAG Blindspot**: Dumping behavioral rules into vector databases fails because agents never semantically search for operational constraints (e.g. formatting or security rules) during general tasks.
> **OKF Agent Memory** resolves this dilemma with the **Dual-Memory Agent Architecture (DMAA)**:
> flowchart TD
> subgraph PUSH["1. Normative Working Memory (Push Layer)"]
> direction TB
> C1["Canonical AGENTS.md (capped at 400 tokens)"]
> C2["Domain Codex (Invariants, Ethics, Tone)"]
> C3["OKF Memory Bridge (Deterministic Triggers)"]
> C4["Agent Action Grammar (AAG) Micro-Syntax"]
> end
> subgraph PULL["2. Semantic Domain Memory (Pull Layer)"]
> direction TB
> O1["OKF v0.2 Knowledge Bundle (knowledge/)"]
> O2["0 Tokens baseline in system prompt"]
> O3["Selective Retrieval via okf_search / okf_show"]
> O4["Persistent Graph of Decisions, Facts & Runbooks"]
> end
> INPUT["User Request"] --> PUSH
> PUSH -->|Enforces Domain Codex & Triggers| AGENT["AI Agent (LLM)"]
> AGENT -->|Selective Retrieval| PULL
> PULL -->|Context & Facts| AGENT
> AGENT --> OUTPUT["Deterministic Response"]
> ### The Universal Composition Model
> In DMAA, every agent configuration is structured by a universal composition:
> $$\text{AGENTS.md} = \underbrace{\text{Domain Codex (AAG)}}_{\text{Project Invariants, Tone, Guardrails}} + \underbrace{\text{OKF Memory Bridge}}_{\text{Standardized Triggers: Search-Before-Write}}$$
> * **Layer 1: Normative Working Memory (Push Layer)**: A permanent, ultra-compact behavioral codex (capped at 400 tokens) expressed in [**Agent Action Grammar (AAG)**](docs/spec/AGENT_ACTION_GRAMMAR_RFC.md). Loaded at session start, enforcing zero-tolerance invariants.
> * **Layer 2: Semantic Domain Memory (Pull Layer)**: An [**OKF v0.2**](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) knowledge bundle (`knowledge/`) that consumes **0 tokens at baseline** and is queried on-demand in microseconds.
> flowcha

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
