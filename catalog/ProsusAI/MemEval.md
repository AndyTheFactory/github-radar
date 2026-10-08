---
repository: "ProsusAI/MemEval"
github_id: 1165602722
url: "https://github.com/ProsusAI/MemEval"
description: "Benchmark suite for evaluating agent and LLM memory systems"
starred_at: "2026-10-08T20:35:16Z"
language: "Python"
topics: []
homepage: ""
license: "Apache-2.0"
archived: false
---

# ProsusAI/MemEval

Benchmark suite for evaluating agent and LLM memory systems

**GitHub:** https://github.com/ProsusAI/MemEval

## README excerpt

> Fair evaluation framework for agent memory
>
>
>
>
> Agent memory systems are hard to compare fairly. They are typically evaluated with different LLMs, embedding models, and metrics. MemEval standardizes the setup: same LLM, same embeddings, same scoring pipeline, and end-to-end token cost tracking across ingestion, retrieval, and answer generation. Cost reporting matters because LLM calls often differ by an order of magnitude across architectures.
> Evaluation combines token F1 with LLM-as-judge scores, with per-category breakdowns to show where each system actually wins. The framework ships with 9 memory systems and 2 benchmarks ([LoCoMo](https://arxiv.org/abs/2402.17753) and [LongMemEval](https://arxiv.org/abs/2410.10813)), and adding new systems or datasets is straightforward.
> We also introduce **PropMem**, which provides the strongest measured quality-to-cost tradeoff in our runs. It extracts atomic facts, tags them by entity, and filters retrieval by entity at query time. See [PROPMEM.md](PROPMEM.md) for the design.
> ## Results
> ### LoCoMo
> | Rank | System | F1 | Judge | Tokens |
> |:----:|:------:|:--:|:-----:|:------:|
> | 1 | **PropMem** | **0.605** | **0.823** | 5.9M |
> | 2 | OpenClaw | 0.557 | 0.725 | 16.4M |
> | 3 | Full Context | 0.542 | 0.709 | 37.5M |
> | 4 | Hindsight | 0.489 | 0.676 | 24.2M |
> | 5 | Graphiti | 0.416 | 0.573 | 5.1M |
> | 6 | Memory-R1 | 0.389 | 0.569 | 3.4M |
> | 7 | SimpleMem | 0.358 | 0.478 | 11.4M |
> | 8 | Mem0 | 0.344 | 0.497 | **3.0M** |
> | 9 | MemU | 0.299 | 0.399 | 6.7M |
> `Tokens` = total system LLM prompt + completion tokens across ingestion, retrieval, and answering; excludes embedding and judge calls.
>
>
>
> Per-category F1 (table)
> | System | Factual | Temporal | Multi-hop | Inferential | Adversarial |
> |:------:|:-------:|:--------:|:---------:|:-----------:|:-----------:|
> | PropMem | 0.431 | **0.615** | 0.599 | **0.289** | 0.794 |
> | OpenClaw | 0.464 | 0.482 | 0.670 | 0.213 | 0.528 |
> | Full Context | **0.517** | 0.369 | **0.674** | 0.197 | 0.509 |
> | Hindsight | 0.431 | 0.306 | 0.526 | 0.206 | 0.647 |
> | Graphiti | 0.296 | 0.151 | 0.349 | 0.120 | **0.873** |
> | Memory-R1 | 0.370 | 0.116 | 0.460 | 0.193 | 0.504 |
> | SimpleMem | 0.245 | 0.320 | 0.237 | 0.136 | 0.734 |
> | Mem0 | 0.267 | 0.104 | 0.330 | 0.174 | 0.629 |
> | MemU | 0.190 | 0.068 | 0.233 | 0.076 | 0.704 |
>
> 10 conversations, 1,986 QA pairs. LLM: gpt-4.1-mini. Embeddings: text-embedding-3-small. Judge: gpt-5.2 (avg of relevance, completeness, accuracy).
> ### LongMemEval
> | Rank | System | F1 |

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

MemEval is a benchmark suite for fairly evaluating agent and LLM memory systems under a standardized setup (same LLM, embeddings, and scoring). It reports token F1, LLM-as-judge scores, per-category breakdowns, and end-to-end token cost, and ships with 9 memory systems and 2 benchmarks (LoCoMo and LongMemEval). It also introduces PropMem, an entity-tagged atomic-fact memory approach.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "0b213c2d74d53a6340c3f69daa98dbb7841293017e456d68fb906a4575ecbd12"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning",
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "benchmarking",
    "model-evaluation",
    "data-evaluation"
  ],
  "technologies": [
    "Python"
  ],
  "summary": "MemEval is a benchmark suite for fairly evaluating agent and LLM memory systems under a standardized setup (same LLM, embeddings, and scoring). It reports token F1, LLM-as-judge scores, per-category breakdowns, and end-to-end token cost, and ships with 9 memory systems and 2 benchmarks (LoCoMo and LongMemEval). It also introduces PropMem, an entity-tagged atomic-fact memory approach.",
  "use_cases": [
    "Comparing agent memory systems under identical LLM and embedding settings",
    "Measuring token cost alongside answer quality for memory architectures",
    "Adding new memory systems or datasets to a standardized evaluation pipeline"
  ],
  "limitations": [
    "Embedding and judge LLM call costs are excluded from the reported token totals",
    "Results are reported for specific models (gpt-4.1-mini, text-embedding-3-small, gpt-5.2 judge) and a limited set of conversations",
    "LongMemEval results section is incomplete in the README excerpt"
  ],
  "suggested_terms": [
    "agent memory benchmark",
    "LLM memory evaluation",
    "LoCoMo",
    "LongMemEval",
    "PropMem"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
