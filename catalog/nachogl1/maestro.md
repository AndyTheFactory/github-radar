---
repository: "nachogl1/maestro"
github_id: 1225467236
url: "https://github.com/nachogl1/maestro"
description: "The Bloomberg Terminal for CLI Agents, its Maestro Baby! "
starred_at: "2026-10-08T20:40:30Z"
language: "Rust"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# nachogl1/maestro

The Bloomberg Terminal for CLI Agents, its Maestro Baby! 

**GitHub:** https://github.com/nachogl1/maestro

## README excerpt

> # Maestro
> **Orchestrate multiple AI coding assistants in parallel**
> A cross-platform desktop application that lets you run 1-12 Claude Code (or other AI CLI) sessions simultaneously, each in its own isolated git worktree.
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
> | **Parallel Development** | Launch 1-12 AI sessions simultaneously. Work on feature branches, bug fixes, and refactoring all at once. |
> | **True Isolation** | Each session operates in its own git worktree. No merge conflicts, no stepping on each other's changes. |
> | **AI-Native Workflow** | Built specifically for Claude Code, Gemini CLI, OpenAI Codex, and other AI coding assistants. |
> | **Cross-Platform** | Runs on macOS, Windows, and Linux with native performance. |
> ---
> ## Features
> ### Multi-Terminal Session Grid
> - Dynamic grid layout (1x1 to 2x3) that adapts to your session count
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
> - AI sessions report their state (idle, working, needs input, finished, error)
> - Real-time status updates display

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Maestro is a cross-platform desktop application for running 1-12 AI coding CLI sessions (such as Claude Code, Gemini CLI, or OpenAI Codex) in parallel. Each session runs in its own isolated git worktree and branch, with real-time status indicators and a built-in MCP server for status reporting.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "3e3976bbf8ff9b4f5aca9980f10b44a047d2dd688e03a603737fc2521b0efcf5"
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
    "monitoring"
  ],
  "technologies": [
    "Rust",
    "Claude Code",
    "Gemini CLI",
    "OpenAI Codex",
    "Git",
    "MCP"
  ],
  "summary": "Maestro is a cross-platform desktop application for running 1-12 AI coding CLI sessions (such as Claude Code, Gemini CLI, or OpenAI Codex) in parallel. Each session runs in its own isolated git worktree and branch, with real-time status indicators and a built-in MCP server for status reporting.",
  "use_cases": [
    "Running multiple AI coding assistant tasks on separate feature branches in parallel",
    "Isolating concurrent AI-driven code changes in separate git worktrees",
    "Monitoring the working, idle, or waiting state of several AI coding sessions"
  ],
  "limitations": [
    "Documented features only; installation, stability, and real-world performance were not verified",
    "Depends on external AI CLI tools being installed and available",
    "Feature list and platform support are based on the README excerpt only"
  ],
  "suggested_terms": [
    "multi-agent coding",
    "git worktree orchestration",
    "parallel Claude Code sessions",
    "AI CLI terminal manager",
    "MCP agent status"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
