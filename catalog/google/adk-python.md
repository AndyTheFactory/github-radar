---
repository: "google/adk-python"
github_id: 958830659
url: "https://github.com/google/adk-python"
description: "An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control."
starred_at: "2026-10-19T11:29:27Z"
language: "Python"
topics: ["agent", "agentic", "agentic-ai", "agents", "agents-sdk", "ai", "ai-agents", "aiagentframework", "genai", "genai-chatbot", "llm", "llms", "multi-agent", "multi-agent-systems", "multi-agents", "multi-agents-collaboration"]
homepage: "https://google.github.io/adk-docs/"
license: "Apache-2.0"
archived: false
---

# google/adk-python

An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

**GitHub:** https://github.com/google/adk-python

## README excerpt

> # Agent Development Kit (ADK) 2.0
>
>
>
> An open-source, code-first Python framework for building, evaluating, and deploying sophisticated AI agents with flexibility and control.
>
>
> Important Links:
>
>
> ADK in other languages:
>
> Agent Development Kit (ADK) is a flexible and modular framework that applies
> software development principles to AI agent creation. It is designed to
> simplify building, deploying, and orchestrating agent workflows, from simple
> tasks to complex systems. While optimized for Gemini, ADK is model-agnostic,
> deployment-agnostic, and compatible with other frameworks.
> ## ✨ Key Features
> - **Workflow Runtime**: A graph-based execution engine for composing
> deterministic execution flows for agentic apps, with support for routing,
> fan-out/fan-in, loops, retry, state management, dynamic nodes,
> human-in-the-loop, and nested workflows.
> - **Task API**: Structured agent-to-agent delegation with multi-turn task
> mode, single-turn controlled output, mixed delegation patterns,
> human-in-the-loop, and task agents as workflow nodes.
> - **Modular Multi-Agent Systems**: Design scalable applications by composing
> multiple specialized agents into flexible hierarchies.
> - **Rich Tool Ecosystem**: Utilize pre-built tools, custom functions,
> OpenAPI specs, MCP tools or integrate existing tools to give agents diverse
> capabilities, all for tight integration with the Google ecosystem.
> - **Code-First Development**: Define agent logic, tools, and orchestration
> directly in Python for ultimate flexibility, testability, and versioning.
> - **Agent Config**: Build agents without code. Check out the
> [Agent Config](https://adk.dev/agents/config/) feature.
> - **Tool Confirmation**: A [tool confirmation flow (HITL)](https://adk.dev/tools-custom/confirmation/) that can guard tool execution with explicit confirmation and custom input.
> - **Deploy Anywhere**: Easily containerize and deploy agents on Cloud Run or
> scale seamlessly with Vertex AI Agent Engine.
> ## 🚀 Installation
> ### Stable Release (Recommended)
> You can install the latest stable version of ADK using `pip`:
> pip install google-adk
> **Requirements:** Python 3.11+.
> For transitive dependency protection, we recommend installing with our companion
> constraints files (for python 3.11 to 3.15).
> Choose the constraints file matching your Python version:
> # For example, for Python 3.11
> curl -o constraints-3.11.txt https://raw.githubusercontent.com/google/adk-python/main/constraints-3.11.txt
> pip install google-adk -c constraints-3.11.txt
> rm constrai

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A code-first Python framework for building, evaluating, and deploying AI agents, with a workflow runtime, multi-agent composition, and a tool ecosystem. It is model-agnostic while optimized for Gemini, and includes human-in-the-loop tool confirmation.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "9c79764699c96167edf2a2f5cff38849c8ca56f5b519b6bae7152811d025798d"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "workflow-orchestration",
    "api-integration",
    "deployment"
  ],
  "technologies": [
    "Python",
    "pip",
    "Gemini",
    "Vertex AI",
    "Cloud Run",
    "MCP",
    "OpenAPI"
  ],
  "summary": "A code-first Python framework for building, evaluating, and deploying AI agents, with a workflow runtime, multi-agent composition, and a tool ecosystem. It is model-agnostic while optimized for Gemini, and includes human-in-the-loop tool confirmation.",
  "use_cases": [
    "Building multi-agent systems composed of specialized agents",
    "Orchestrating graph-based agent workflows with routing, loops, and retries",
    "Deploying agents to Cloud Run or Vertex AI Agent Engine"
  ],
  "limitations": [
    "Requires Python 3.11+",
    "Optimized for Gemini; other model support depends on integration",
    "Evaluation and deployment capabilities are described in the README excerpt only partially"
  ],
  "suggested_terms": [
    "agent framework python",
    "multi-agent orchestration",
    "agent development kit",
    "llm agents toolkit",
    "agent workflow runtime"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
