---
repository: "microsoft/TokenEconomizer"
github_id: 1416442720
url: "https://github.com/microsoft/TokenEconomizer"
description: "Experience-Driven Black-Box Cost Control for Coding Agents"
starred_at: "2026-11-08T21:01:39Z"
language: "Python"
topics: ["agentic-ai", "agentic-coding", "ai-coding", "ai-coding-assistant", "anthropic", "artificial-intelligence", "claude-code", "codex", "coding-agent", "coding-agents", "cost-optimization", "cost-reduction", "developer-tools", "github-copilot", "llm", "open-source", "openai", "productivity", "token-optimization"]
homepage: ""
license: "Apache-2.0"
archived: false
---

# microsoft/TokenEconomizer

Experience-Driven Black-Box Cost Control for Coding Agents

**GitHub:** https://github.com/microsoft/TokenEconomizer

## README excerpt

> # TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents
>
> Aaron J. Li1,
> Weijia Xu2,
> Chandan Singh2,
> Zixiao Chen3,
> Jeevana Priya Inala2,
> Charlotte Siska3,
>
> Acar Tamersoy3,
> Bin Yu1,
> Ion Stoica1,
> Michel Galley2,
> Jianfeng Gao2
>
>
> 1UC Berkeley &nbsp; 2Microsoft Research &nbsp; 3Microsoft Security
>
>
>
>
>
>
> Our measurement on SWE-Bench tasks: 18.4–30.9% lower mean cost across five agent–model
> combinations, cheaper in all 30 repository × combination cells, and Pass@1 up in
> 4 of 5. Results
>
>
>
>
>
> TokenEconomizer makes coding agents cheaper to run in the repositories you work in often,
> without changing the agent itself. It learns from the sessions an agent has already run in a
> repository, and uses that experience to cut waste in the sessions that follow. It has three
> mechanisms:
> - **Micro-skills: remember how the repository works.** Sessions keep rediscovering the same
> facts: a build step that must run first, the spelling of a command that works here
> (`python -m pytest` where `pytest` is missing, `npx tsc` where `tsc` is), an environment
> variable a command needs, where generated files live. Micro-skills learns such facts, in any
> language, from two sources: failures that repeat across sessions, and a model that reviews the
> recent sessions every *k* sessions (*k* = 3) and proposes facts. A fact is stated at the start
> of each session once three sessions have confirmed it, and dropped when later sessions
> contradict it.
> - **Tool pruning: stop loading tools that go unused.** Every loaded tool's definition is sent with
> every request. A tool that goes unused over *p* prompts spread across at least *m* sessions, or
> over *s* sessions of any length (*p* = 10, *m* = 2, *s* = 5), is left out of the next sessions
> through the agent's own settings. One command brings it back.
> - **Failure-loop intervention (the loop guard): step in when a turn is stuck.** When a turn (the
> agent's work on one prompt) keeps hitting the same failures, a judge model checks whether it is
> stuck. If the judge is at least *c* sure (*c* = 0.7), the agent gets a redirect (a short note,
> added to its context, to try another approach), at most *r* times per turn (*r* = 1). If the
> turn is still stuck after that, TokenEconomizer tells you how to stop it; it never stops a turn
> itself.
> TokenEconomizer is a plugin for **Claude Code**, **Codex**, the **GitHub Copilot CLI** and **Pi**,
> with experimental support for **opencode**, **Cursor Agent**, **Grok Build**, **Hermes Agent** and
> the **Antigravity CLI

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

TokenEconomizer is a plugin for coding agents such as Claude Code, Codex, and GitHub Copilot CLI that reduces token cost by learning repository facts, pruning unused tools, and intervening in stuck turns. The README reports 18.4–30.9% lower mean cost on SWE-Bench tasks in the authors' measurements.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "f22e8cb83477d0827b11a18412f1d5553293548cb82686320df545266c0eecb9"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "ai-ml",
    "productivity"
  ],
  "repository_type": "application",
  "capabilities": [
    "automation",
    "monitoring",
    "code-generation"
  ],
  "technologies": [
    "Python",
    "Claude Code",
    "Codex",
    "GitHub Copilot CLI",
    "Pi",
    "opencode",
    "Cursor Agent"
  ],
  "summary": "TokenEconomizer is a plugin for coding agents such as Claude Code, Codex, and GitHub Copilot CLI that reduces token cost by learning repository facts, pruning unused tools, and intervening in stuck turns. The README reports 18.4–30.9% lower mean cost on SWE-Bench tasks in the authors' measurements.",
  "use_cases": [
    "Lowering token costs for coding agents in frequently used repositories",
    "Reducing repeated rediscovery of build and test commands across agent sessions",
    "Detecting and redirecting stuck agent turns in failure loops"
  ],
  "limitations": [
    "Benchmark results are the authors' reported measurements on SWE-Bench, not independently verified",
    "Support for opencode, Cursor Agent, Grok Build, Hermes Agent, and Antigravity CLI is experimental",
    "README excerpt is truncated and may omit further details"
  ],
  "suggested_terms": [
    "coding agent cost",
    "token optimization",
    "Claude Code plugin",
    "agent loop guard",
    "tool pruning"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
