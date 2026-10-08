---
repository: "aiming-lab/AutoResearchClaw"
github_id: 1182108611
url: "https://github.com/aiming-lab/AutoResearchClaw"
description: "Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞"
starred_at: "2026-10-08T20:17:12Z"
language: "Python"
topics: ["autonomous-research", "citation-verification", "llm-agents", "metaclaw", "multi-agent-debate", "openclaw", "paper-generation", "scientific-discovery", "self-evolving"]
homepage: ""
license: "MIT"
archived: false
---

# aiming-lab/AutoResearchClaw

Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞

**GitHub:** https://github.com/aiming-lab/AutoResearchClaw

## README excerpt

> Chat an Idea. Get a Paper. Autonomous, Collaborative & Self-Evolving.
>
> Just chat with OpenClaw: "Research X" → done.
>
>
> 📄 Our paper is on arXiv — come read it! AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration
>
>
>
>
>
>
>
>
>
> ---
>
>
>
>
>
> 🏆 Generated Paper Showcase
> 8 papers across 8 domains — math, statistics, biology, computing, NLP, RL, vision, robustness — generated fully autonomously or with Human-in-the-Loop co-pilot guidance.
>
>
>
> ---
> > **🧪 We're looking for testers!** Try the pipeline with your own research idea — from any field — and [tell us what you think](docs/TESTER_GUIDE.md). Your feedback directly shapes the next version. **[→ Testing Guide](docs/TESTER_GUIDE.md)** | **[→ 中文测试指南](docs/TESTER_GUIDE_CN.md)** | **[→ 日本語テストガイド](docs/TESTER_GUIDE_JA.md)**
> ---
> ## 🔥 News
> - **[05/19/2026]** **v0.5.0** — **Multi-Domain Experiment Agents + ARC-Bench** — Two headline updates. **(1) Domain-specialist execution agents:** the experiment stage (Stages 10–13) now routes beyond the default ML sandbox to specialist agents per field — **high-energy physics** (ColliderAgent: Lagrangian → FeynRules → MadGraph5 → Delphes via the Magnus cloud), **biology** (COBRApy genome-scale metabolic modelling), and **statistics** (simulation-study agent), with a generic Docker executor covering chemistry/materials. The pipeline auto-selects the right executor from the research domain. **(2) ARC-Bench:** a **55-topic** open-ended autonomous-research benchmark spanning **ML (25), HEP (10), quantum (10), biology (7), and statistics (3)** — each topic ships a manifest (research question + conditions + metrics + datasets) and a rubric for graded scoring, all under [`experiments/arc_bench/`](experiments/arc_bench/), and also released on [🤗 Hugging Face](https://huggingface.co/datasets/AIMING-Lab-UNC/ARC-Bench). **[→ Domain Integration Guide](docs/DOMAIN_INTEGRATION_GUIDE.md)**
> - **[04/01/2026]** **v0.4.0** — **Human-in-the-Loop Co-Pilot System** — AutoResearchClaw is no longer purely autonomous. New HITL system adds 6 intervention modes (`full-auto`, `gate-only`, `checkpoint`, `step-by-step`, `co-pilot`, `custom`), per-stage policies, and deep human-AI collaboration. Includes: Idea Workshop for hypothesis co-creation, Baseline Navigator for experiment design review, Paper Co-Writer for collaborative drafting, SmartPause (confidence-driven dynamic intervention), ALHF intervention learning, anti-hallucination claim verification, cost budget guardrails, pipeline br

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

An autonomous research pipeline that takes a research idea and runs multi-stage processes to produce a paper, with optional human-in-the-loop intervention modes. The README also describes domain-specialist experiment agents and the ARC-Bench benchmark of 55 research topics.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "f0440eebc078706968b952e984b4b29207860e38e3ae4f889d4cc98c18076f5b"
  },
  "primary_domain": "research-learning",
  "secondary_domains": [
    "ai-ml",
    "productivity"
  ],
  "repository_type": "application",
  "capabilities": [
    "agent-orchestration",
    "workflow-orchestration",
    "code-generation",
    "document-processing",
    "question-answering"
  ],
  "technologies": [
    "Python",
    "Docker",
    "MadGraph5",
    "FeynRules",
    "COBRApy",
    "Hugging Face"
  ],
  "summary": "An autonomous research pipeline that takes a research idea and runs multi-stage processes to produce a paper, with optional human-in-the-loop intervention modes. The README also describes domain-specialist experiment agents and the ARC-Bench benchmark of 55 research topics.",
  "use_cases": [
    "Generating research papers from a research idea",
    "Running human-in-the-loop co-pilot research workflows",
    "Evaluating autonomous research agents with ARC-Bench"
  ],
  "limitations": [
    "Excerpt is from the README only; capabilities are not independently verified",
    "Generated papers require human review, as the project itself positions itself as in testing"
  ],
  "suggested_terms": [
    "autonomous research agent",
    "paper generation",
    "multi-agent research pipeline",
    "ARC-Bench",
    "human-in-the-loop research"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
