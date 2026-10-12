---
repository: "microsoft/agent-framework"
github_id: 974445592
url: "https://github.com/microsoft/agent-framework"
description: "A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET."
starred_at: "2026-10-12T08:10:23Z"
language: "Python"
topics: ["agent-framework", "agentic-ai", "agents", "ai", "dotnet", "multi-agent", "orchestration", "python", "sdk", "workflows"]
homepage: "https://aka.ms/agent-framework"
license: "MIT"
archived: false
---

# microsoft/agent-framework

A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.

**GitHub:** https://github.com/microsoft/agent-framework

## README excerpt

> # Welcome to Microsoft Agent Framework!
> Microsoft Agent Framework (MAF) is an open, multi-language framework for building **production-grade AI agents and multi-agent workflows** in **.NET and Python**.
> Microsoft Agent Framework is built for teams taking agents from prototype to production. It provides a consistent foundation for building, orchestrating, and operating agent systems across Python, .NET and Go, while keeping architecture choices open as requirements evolve, and supports a broad ecosystem including Microsoft Foundry, Azure OpenAI, OpenAI, and the GitHub Copilot SDK, with samples and hosting patterns for both local development and cloud deployment.
> > [!NOTE]
> > For the Go SDK, including its documentation, samples, contribution guidance, and issue tracker, visit [microsoft/agent-framework-go](https://github.com/microsoft/agent-framework-go/).
>
> alt="Watch the full Agent Framework introduction (30 min)" width="480">
>
>
> Watch the full Agent Framework introduction (30 min)
>
> ## Is this the right framework for you?
> MAF is a strong fit if you:
> - are building agents and workflows you expect to run in production,
> - need orchestration beyond a single prompt or stateless chat loop,
> - want graph-based patterns such as sequential, concurrent, handoff, and group collaboration,
> - care about durability, restartability, observability, governance, or human-in-the-loop control,
> - need provider flexibility so your architecture can evolve without major rewrites.
> ## Key Features
> Explore new MAF capabilities and real implementation patterns on the [official blog](https://devblogs.microsoft.com/agent-framework/).
> - **Python and C#/.NET Support**: Full framework support for both Python and C#/.NET implementations with consistent APIs
> - [Python packages](./python/packages/) | [.NET source](./dotnet/src/)
> - **Go Support**: For the Go SDK, including its documentation, samples, contribution guidance, and issue tracker, visit [microsoft/agent-framework-go](https://github.com/microsoft/agent-framework-go/).
> - **Multiple Agent Provider Support**: Support for various LLM providers with more being added continuously
> - [Python examples](./python/samples/02-agents/providers/) | [.NET examples](./dotnet/samples/02-agents/AgentProviders/)
> - **Middleware**: Flexible middleware system for request/response processing, exception handling, and custom pipelines
> - [Python middleware](./python/samples/02-agents/middleware/) | [.NET middleware](./dotnet/samples/02-agents/Agents/Agent_Step11_M

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Microsoft Agent Framework is an open, multi-language SDK for building, orchestrating, and deploying AI agents and multi-agent workflows in Python and .NET. It supports graph-based patterns such as sequential, concurrent, handoff, and group collaboration, plus middleware and multiple LLM providers.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "c05fa681edd50445e9f295fbcc25c182e8efa55eb34558edf8a8f58148650c4e"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "agent-orchestration",
    "workflow-orchestration",
    "inference-serving",
    "observability"
  ],
  "technologies": [
    "Python",
    ".NET",
    "C#",
    "Go",
    "Azure OpenAI",
    "OpenAI",
    "Microsoft Foundry",
    "GitHub Copilot SDK"
  ],
  "summary": "Microsoft Agent Framework is an open, multi-language SDK for building, orchestrating, and deploying AI agents and multi-agent workflows in Python and .NET. It supports graph-based patterns such as sequential, concurrent, handoff, and group collaboration, plus middleware and multiple LLM providers.",
  "use_cases": [
    "Building production-grade AI agent systems",
    "Orchestrating multi-agent workflows with handoff and group collaboration",
    "Integrating multiple LLM providers behind a consistent API"
  ],
  "limitations": [
    "Go support is provided by a separate repository, microsoft/agent-framework-go",
    "Provider coverage is described as expanding continuously",
    "Feature details beyond the README excerpt were not verified"
  ],
  "suggested_terms": [
    "agent framework",
    "multi-agent workflows",
    "AI agent orchestration",
    "Python agents",
    ".NET agents"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
