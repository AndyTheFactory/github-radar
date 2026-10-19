---
repository: "JayPokale/Chisle"
github_id: 1284692613
url: "https://github.com/JayPokale/Chisle"
description: "Cut your AI coding agent's token bill on three axes: terse prose, YAGNI-first code, and tool-output compression. Claude Code, Pi, Cursor, Codex, Gemini + 4 more. Zero deps, published benchmarks including the runs it loses."
starred_at: "2026-10-19T11:40:08Z"
language: "JavaScript"
topics: ["agent-skills", "anthropic", "caveman", "caveman-alternative", "claude", "claude-ai", "claude-code", "claude-code-skill", "claude-code-skills", "claude-plugin", "claude-skills", "codex", "cursor", "developer-tools", "gemini-cli", "gemini-cli-extension", "github-copilot", "hacktoberfest", "ponytail", "token-optimization"]
homepage: "https://chisle.jaypokale.me"
license: "MIT"
archived: false
---

# JayPokale/Chisle

Cut your AI coding agent's token bill on three axes: terse prose, YAGNI-first code, and tool-output compression. Claude Code, Pi, Cursor, Codex, Gemini + 4 more. Zero deps, published benchmarks including the runs it loses.

**GitHub:** https://github.com/JayPokale/Chisle

## README excerpt

> Chisle
>
> Your AI talks less, builds less, reads less, and says more. Like a senior dev who bills by the syllable.
>
>
> The only tool in this class that publishes the runs where it lost. Here's why.
>
>
>
>
> Built for Claude Code: answers about half as long, shorter than caveman and ponytail &middot; 13 agents &middot; zero dependencies &middot; one command
>
> Chisle is a Claude Code plugin that makes Claude cheaper to run without making it dumber. It cuts what Claude writes: no filler, no hedging, no speculative abstractions, just the smallest code that works. It also cuts what Claude reads: a `PostToolUse` hook trims oversized tool output by ~46% before it re-enters the context window, where it would be re-billed on every later request. In agent-loop tests Claude with Chisle passes the same tasks as Claude without it. One `npx chisle` installs it, and the same ruleset ships to Pi, Cursor, Codex, Gemini, Copilot, OpenCode, Antigravity and four more agents. Every number here comes from committed raw transcripts, including the runs where it lost.
>
>
> Pi 0.85.1 + GPT-5.5, 6 tasks: answer length vs the same model with no ruleset. Lower is leaner. More below.
> ---
> "Implement an order state machine covering created, paid, shipped, delivered, cancelled and refunded, with the legal transitions enforced and invalid ones rejected." Same model, same prompt, one difference: the injected ruleset. Both answers are the **verbatim committed output** from [`raw-oct-notools/large-s2`](benchmarks/results/raw-oct-notools/large-s2/):
>
> bare model: 125 lines, 1,342 answer tokensChisle: 54 lines, 450 answer tokens
>
> An `Enum` of states, a custom exception class, type hints and docstrings on every method, a file write, then a test harness:
> class OrderState(Enum):
> CREATED = "created"
> PAID = "paid"
> # … four more
> class InvalidTransition(Exception):
> """Raised when attempting an invalid state transition."""
> pass
> class Order:
> VALID_TRANSITIONS = { … }
> def transition_to(self, next_state: OrderState) -> None:
> """Transition to next state if valid, …"""
> …plus usage, tests and a summary.
>
> One dict of legal transitions, one method that enforces it:
> class OrderStateMachine:
> TRANSITIONS = {
> 'created': {'paid', 'cancelled'},
> 'paid': {'shipped', 'refunded'},
> 'shipped': {'delivered', 'cancelled'},
> 'delivered': {'refunded'},
> 'cancelled': set(),
> 'refunded': set(),
> }
> def transition(self, new_state):
> if new_state not in self.TRANSITIONS[self.state]:
> raise ValueError(f"Invalid transition: …")
> self.state = new_state

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Chisle is a Claude Code plugin and multi-agent ruleset that aims to reduce token usage by enforcing terse prose, YAGNI-first code, and a PostToolUse hook that trims oversized tool output. It is installed via a single npx command and ships the same ruleset to several other AI coding agents. The README states that published benchmarks include runs where it performed worse.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "b86e61a66288649bdae74faac1d376c9b82fbc5b44375384d4dad30ee790001b"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "ai-ml"
  ],
  "repository_type": "application",
  "capabilities": [
    "code-generation",
    "automation"
  ],
  "technologies": [
    "JavaScript",
    "Node.js",
    "Claude Code",
    "npm",
    "Markdown"
  ],
  "summary": "Chisle is a Claude Code plugin and multi-agent ruleset that aims to reduce token usage by enforcing terse prose, YAGNI-first code, and a PostToolUse hook that trims oversized tool output. It is installed via a single npx command and ships the same ruleset to several other AI coding agents. The README states that published benchmarks include runs where it performed worse.",
  "use_cases": [
    "Reducing token costs when running AI coding agents",
    "Shortening AI agent responses and code output",
    "Compressing large tool output before it re-enters the agent context"
  ],
  "limitations": [
    "Benchmark results are the author's published claims and have not been independently verified",
    "README claims benchmarks show a mix of wins and losses; the scope of tasks tested is limited to the listed benchmarks",
    "Effectiveness depends on the specific agent, model, and task"
  ],
  "suggested_terms": [
    "token optimization",
    "Claude Code plugin",
    "AI agent ruleset",
    "tool output compression",
    "coding agent cost"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
