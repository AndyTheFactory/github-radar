---
repository: "kunchenguid/backpass"
github_id: 1342226102
url: "https://github.com/kunchenguid/backpass"
description: "You don't write AGENTS.md. You train it with gradient descent."
starred_at: "2026-10-08T20:36:48Z"
language: "JavaScript"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# kunchenguid/backpass

You don't write AGENTS.md. You train it with gradient descent.

**GitHub:** https://github.com/kunchenguid/backpass

## README excerpt

> backpass
>
> ><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/backpass/ci.yml?style=flat-square&label=ci"
> />
> ><img alt="Release" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/backpass/release-please.yml?style=flat-square&label=release"
> />
> ><img alt="npm" src="https://img.shields.io/npm/v/backpass?style=flat-square"
> />
> ><img alt="Platform" src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square"
> />
> ><img alt="X" src="https://img.shields.io/badge/X-@kunchenguid-black?style=flat-square"
> />
> ><img
> alt="Discord"
> src="https://img.shields.io/discord/1439901831038763092?style=flat-square&label=discord"
> />
>
> Gradient descent for your agent memory.
> [This blog post](https://blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net) explains the why and how.
> `backpass` helps you improve your `AGENTS.md`, `CLAUDE.md` and skills with scientific rigor.
> It finds the agent sessions that actually ran in your repo, reads
> what happened in them, and proposes evidence-backed edits to your memory surface - the
> memory file and project skills - under a token budget, gated by you.
> - **Local-first** - Reads the transcript stores of seven agent harnesses directly from disk,
> locally or over SSH to your own machines. No API, no upload; transcripts never leave your
> machines except into an agent you already authenticated, and obvious secrets are redacted
> before they do.
> - **Evidence-gated** - Every proposed edit carries verbatim quotes from real sessions,
> and every `add`, `rewrite`, or `remove` edit needs evidence from at least two distinct
> sessions. Small, noisy, bounded steps - not a rewrite.
> - **Human in the loop** - Analysis never writes.
> See [Apply - the human gate](#8-apply---the-human-gate) for review and explicit scripted decisions.
> AGENTS.md / CLAUDE.md + skills (the weights)
> → agent session               (forward pass)
> → transcript on disk          (loss signal)
> → backpass: collect samples, distill, calculate loss, aggregate gradients
> → backpass: gradient descent  (diffs + skill extractions)
> → you accept or reject        (the human gate)
> → back to the weights
> One run is one bounded gradient step.
> ## Quick Start
> npm install -g backpass
> # or run it without installing
> npx backpass
> Requires **Node >= 22.5** and [`acpx`](https://github.com/openclaw/acpx) on your PATH.
> backpass has **no API keys of its own**. Every model call goes through acpx to a harness
> you have already authenticated.
> cd your-repo
> ba

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

backpass is a CLI tool that improves AGENTS.md, CLAUDE.md, and project skills by analyzing local agent session transcripts and proposing evidence-backed edits gated by human review. It reads transcripts from seven agent harnesses locally or over SSH and makes no API calls of its own, routing model calls through acpx.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "e65f5e789a0d56fc2d6b26159d4c8a5eedc9f9a472a86ea076f50c2e44974e7a"
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
    "data-ingestion",
    "data-evaluation"
  ],
  "technologies": [
    "JavaScript",
    "Node.js",
    "npm",
    "acpx",
    "GitHub Actions",
    "shields.io"
  ],
  "summary": "backpass is a CLI tool that improves AGENTS.md, CLAUDE.md, and project skills by analyzing local agent session transcripts and proposing evidence-backed edits gated by human review. It reads transcripts from seven agent harnesses locally or over SSH and makes no API calls of its own, routing model calls through acpx.",
  "use_cases": [
    "Refining AGENTS.md or CLAUDE.md memory files from real agent sessions",
    "Proposing project skill extractions from repeated agent behavior",
    "Reviewing and accepting or rejecting agent memory edits before applying them"
  ],
  "limitations": [
    "Requires Node >= 22.5 and acpx on PATH",
    "Supports macOS and Linux only per the README badge",
    "Depends on an already-authenticated agent harness via acpx"
  ],
  "suggested_terms": [
    "agent memory",
    "AGENTS.md",
    "CLAUDE.md",
    "agent sessions",
    "acpx"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
