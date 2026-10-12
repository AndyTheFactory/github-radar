---
repository: "google-research/rrsi"
github_id: 1372530077
url: "https://github.com/google-research/rrsi"
description: ""
starred_at: "2026-10-12T14:17:04Z"
language: "Python"
topics: []
homepage: ""
license: "Apache-2.0"
archived: false
---

# google-research/rrsi

No description provided.

**GitHub:** https://github.com/google-research/rrsi

## README excerpt

> # RRSI: Regularized Recursive Self-Improvement of Agent Harnesses
> Check out our [paper](https://arxiv.org/abs/2609.24972) and [project page](https://regularized-rsi.com/) for more details.
> ## 🔥 Updates
> - [09/21/2026] Our [paper](https://arxiv.org/abs/2609.24972) is out! Check it out! [[project page]](https://regularized-rsi.com/)
> ## 🧬 Overview
>
>
> An LLM agent's capability is largely set by its harness: the prompts, control
> flow, tools, memory and context management around a frozen model. Evolving the
> harness against a fixed evolve set is effective but overfits: the harness
> memorizes the training tasks, and large in-distribution gains shrink or vanish
> out of distribution. RRSI keeps the harness edit space open and regularizes the
> search trajectory through it instead.
> On the proposal side, an annealed budget caps how many independent edits one
> candidate may bundle, the proposer is conditioned on the full edit history so a
> falsified hypothesis is not redrawn, and a stalled run is redirected toward
> components it has never exercised. On the selection side, a critic screens
> every candidate for suite-specific logic before it is evaluated, a
> noise-adjusted floor blocks gains within evaluation variance, a cost rule
> requires added inference tokens to be paid for by measured gain, and
> components that stop helping are pruned.
> ### ✨ Key features
> * **Open edit space, regularized search.** Prompts, control flow, configuration, context management, tools, skills, memory and sub-agents may all be modified; the constraints act on how the search moves, not on what the harness may contain.
> * **One method, three instances.** The same loop drives a terminal agent (Terminal-Bench 2.1), a document-work agent (Harvey LAB) and an engineering-design agent (EngDesign); each instance is a `Domain` adapter plus its starting harness.
> * **Candidates in git worktrees.** Every candidate harness is drafted, screened and evaluated in its own worktree on a branch off `evolve/`; accepting one fast-forwards the branch, so the incumbent is always a commit.
> * **Evidence you can audit.** The edit history records, per edit, the component, the hypothesis, the measured score and cost change and the verdict; the prompts the proposer, analyst and critic receive are plain files in `domains//`.
> ## 🧩 Method to code
> | Paper | Code |
> |---|---|
> | Empirical score and cost estimate | `rrsi/evaluate.py: aggregate` (weighted per-trial rewards; a missing trial counts 0 with the full denominator) |
> | Annealed edit b

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Research code for RRSI, a method that iteratively self-improves LLM agent harnesses (prompts, control flow, tools, memory) using regularized search with git worktrees. It includes Domain adapters for terminal, document-work, and engineering-design agent benchmarks, per the README excerpt.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "67ab8abaa201c029d080b44ee8e9e42d908aa5d47e902f0bf1f2001dd3718346"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "developer-tools",
    "research-learning"
  ],
  "repository_type": "research",
  "capabilities": [
    "agent-orchestration",
    "benchmarking",
    "model-evaluation"
  ],
  "technologies": [
    "Python",
    "git"
  ],
  "summary": "Research code for RRSI, a method that iteratively self-improves LLM agent harnesses (prompts, control flow, tools, memory) using regularized search with git worktrees. It includes Domain adapters for terminal, document-work, and engineering-design agent benchmarks, per the README excerpt.",
  "use_cases": [
    "Reproducing the RRSI paper's harness self-improvement experiments",
    "Studying regularized search over LLM agent harness edits",
    "Auditing per-edit histories of harness changes"
  ],
  "limitations": [
    "Description is empty and README is excerpted; full functionality not verified",
    "Depends on external benchmarks (Terminal-Bench 2.1, Harvey LAB, EngDesign)",
    "Repository has no topics"
  ],
  "suggested_terms": [
    "recursive self-improvement",
    "agent harness",
    "LLM agents",
    "regularized search",
    "Terminal-Bench"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
