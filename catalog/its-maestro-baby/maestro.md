---
repository: "its-maestro-baby/maestro"
github_id: 1129336223
url: "https://github.com/its-maestro-baby/maestro"
description: "The Bloomberg Terminal for CLI Agents, its Maestro Baby! "
starred_at: "2026-10-08T20:40:24Z"
language: "TypeScript"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# its-maestro-baby/maestro

The Bloomberg Terminal for CLI Agents, its Maestro Baby! 

**GitHub:** https://github.com/its-maestro-baby/maestro

## README excerpt

> # Maestro
> **Orchestrate multiple AI coding assistants in parallel**
> A cross-platform desktop application that lets you run 1-6 Claude Code (or other AI CLI) sessions simultaneously, each in its own isolated git worktree.
> **Star us on GitHub — your support motivates us a lot!**
> ---
> ## Table of Contents
> - [Why Maestro?](#why-maestro)
> - [Features](#features)
> - [Keyboard Shortcuts](#keyboard-shortcuts)
> - [Architecture](#architecture)
> - [Installation](#installation)
> - [Usage](#usage)
> - [Configuration](#configuration)
> - [Troubleshooting](#troubleshooting)
> - [Contributing](#contributing)
> - [License](#license)
> - [Acknowledgments](#acknowledgments)
> ---
> ## Why Maestro?
> **The Problem:** AI coding assistants work on one task at a time. While Claude works on Feature A, you wait. Then you start Feature B. Then you wait again. Context switching is expensive, and your development velocity is bottlenecked by serial execution.
> **The Solution:** Run multiple AI sessions in parallel. Each session gets its own:
> - Terminal instance with full shell environment
> - Git worktree for complete code isolation
> - Assigned branch for focused work
> - Port allocation for web development
> ### Core Principles
> | Principle | Description |
> |-----------|-------------|
> | **Parallel Development** | Launch 1-6 AI sessions simultaneously. Work on feature branches, bug fixes, and refactoring all at once. |
> | **True Isolation** | Each session operates in its own git worktree. No merge conflicts, no stepping on each other's changes. |
> | **AI-Native Workflow** | Built specifically for Claude Code, Gemini CLI, OpenAI Codex, and other AI coding assistants. |
> | **Cross-Platform** | Runs on macOS, Windows, and Linux with native performance. |
> ---
> ## Features
> ### Multi-Terminal Session Grid
> - Dynamic grid layout (1x1 to 2x3) that adapts to your session count
> - iTerm2-style split panes within each session (Cmd+D vertical, Cmd+Shift+D horizontal)
> - Real-time status indicators: idle, working, waiting for input, done, error
> - Per-session mode selection (Claude Code, Gemini CLI, OpenAI Codex, Plain Terminal)
> ### Git Worktree Isolation
> - Automatic worktree creation at `~/.claude-maestro/worktrees/`
> - Each session works on its own branch without conflicts
> - Worktrees are pruned on session close
> - Visual branch assignment in the sidebar
> - "Worktree" badge in the terminal header when a session is running in a worktree
> ### MCP Server Integration
> - Built-in MCP server for agent status reporting
> - AI sessions report their

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Maestro is a cross-platform desktop application for running 1-6 AI coding assistant CLI sessions in parallel. Each session runs in its own isolated git worktree with a dedicated branch and terminal. The README also describes an MCP server for agent status reporting.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "08e46574ed35f832f128cd13409df7b2139e8fb6681122fac6ebb8d5976d209d"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "ai-ml",
    "productivity"
  ],
  "repository_type": "application",
  "capabilities": [
    "agent-orchestration",
    "workflow-orchestration",
    "monitoring",
    "automation"
  ],
  "technologies": [
    "TypeScript",
    "Electron",
    "Git",
    "Claude Code",
    "Gemini CLI",
    "OpenAI Codex",
    "MCP"
  ],
  "summary": "Maestro is a cross-platform desktop application for running 1-6 AI coding assistant CLI sessions in parallel. Each session runs in its own isolated git worktree with a dedicated branch and terminal. The README also describes an MCP server for agent status reporting.",
  "use_cases": [
    "Parallel development of multiple features or bug fixes with AI coding assistants",
    "Isolating concurrent AI-driven code changes in separate git worktrees",
    "Monitoring the status of multiple AI coding sessions from one interface"
  ],
  "limitations": [
    "README excerpt is truncated; full feature set and Electron usage are not confirmed from the excerpt",
    "Repository topics are empty and homepage is not set",
    "Relies on external AI CLI tools (Claude Code, Gemini CLI, OpenAI Codex) that must be installed separately"
  ],
  "suggested_terms": [
    "AI coding assistant orchestration",
    "git worktree parallel sessions",
    "Claude Code multi-session",
    "MCP agent status",
    "terminal session grid"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
