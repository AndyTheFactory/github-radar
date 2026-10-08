---
repository: "MemPalace/mempalace"
github_id: 1201656210
url: "https://github.com/MemPalace/mempalace"
description: "The best-benchmarked open-source AI memory system. And it's free."
starred_at: "2026-10-08T20:18:46Z"
language: "Python"
topics: ["ai", "chromadb", "llm", "mcp", "memory", "python"]
homepage: "http://mempalaceofficial.com/"
license: "MIT"
archived: false
---

# MemPalace/mempalace

The best-benchmarked open-source AI memory system. And it's free.

**GitHub:** https://github.com/MemPalace/mempalace

## README excerpt

> # MemPalace
> Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.
> > [!CAUTION]
> > **Beware of impostor sites.** MemPalace has no other official websites. The **only** official sources are this **[GitHub repository](https://github.com/MemPalace/mempalace)**, the **[PyPI package](https://pypi.org/project/mempalace/)**, and the docs at **[mempalaceofficial.com](https://mempalaceofficial.com)**. Any other domain (including `.tech`, `.net`, or other `.com` variants) is an impostor and may distribute malware. Details and timeline: [docs/HISTORY.md](docs/HISTORY.md).
> > [!IMPORTANT]
> > **Claude Code sessions expire in 30 days without auto-save hooks wired.** [Read this →](https://github.com/MemPalace/mempalace/discussions/1388)
> >
> > Need the shortest recovery/setup path? Use the [Claude Code retention setup checklist](https://mempalaceofficial.com/guide/claude-code-retention.html).
> ---
> ## What it is
> MemPalace stores your conversation history as verbatim text and retrieves
> it with semantic search. It does not summarize, extract, or paraphrase.
> The index is structured — people and projects become *wings*, topics
> become *rooms*, and original content lives in *drawers* — so searches
> can be scoped rather than run against a flat corpus.
> The retrieval layer is pluggable. The current default is ChromaDB; the
> interface is defined in [`mempalace/backends/base.py`](mempalace/backends/base.py)
> and alternative backends can be dropped in without touching the rest of
> the system.
> Nothing leaves your machine unless you opt in.
> Architecture, concepts, and mining flows:
> [mempalaceofficial.com/concepts/the-palace](https://mempalaceofficial.com/concepts/the-palace.html).
> ---
> ## Install
> ### Agent-guided setup
> Install the MemPalace skills first, then ask your coding agent to set up
> MemPalace. The setup skill detects your system, installs the Python package,
> configures MCP, and asks whether you want a private local palace, a shared-brain
> hub, or a client connected to an existing hub:
> npx skills add MemPalace/mempalace
> The repository exposes three skills: `mempalace` for guided installation and
> operations, `mempalace-recall` for search-before-answer recall, and
> `mempalace-task` for logstream delegation. Installing a skill does not by
> itself install the MemPalace CLI or MCP server; the setup skill guides the
> agent through those system changes and verifies the live connection.
> During guided setup the agent can offer weekly stable-release che

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

MemPalace is a local-first AI memory system that stores conversation history as verbatim text and retrieves it via semantic search. It organizes content into wings, rooms, and drawers, with a pluggable retrieval backend whose default is ChromaDB.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "d5a6392daa4b27053d6fb7e97e991e37ee4a5d2808b1d38e4db97c978377e9e6"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools",
    "databases"
  ],
  "repository_type": "library",
  "capabilities": [
    "search-retrieval",
    "indexing",
    "knowledge-management",
    "storage",
    "api-integration"
  ],
  "technologies": [
    "Python",
    "ChromaDB",
    "MCP",
    "LLM"
  ],
  "summary": "MemPalace is a local-first AI memory system that stores conversation history as verbatim text and retrieves it via semantic search. It organizes content into wings, rooms, and drawers, with a pluggable retrieval backend whose default is ChromaDB.",
  "use_cases": [
    "Giving coding agents persistent memory of past conversations",
    "Scoped semantic search over personal conversation history",
    "Running a private local memory store without external API calls"
  ],
  "limitations": [
    "Claude Code sessions expire after 30 days unless auto-save hooks are configured, per the README",
    "Official sources are limited to the GitHub repo, PyPI package, and mempalaceofficial.com; other domains are flagged as impostors"
  ],
  "suggested_terms": [
    "AI memory system",
    "semantic search memory",
    "MCP memory server",
    "ChromaDB retrieval",
    "local-first LLM memory"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
