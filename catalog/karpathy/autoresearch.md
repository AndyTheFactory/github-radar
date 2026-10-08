---
repository: "karpathy/autoresearch"
github_id: 1174820787
url: "https://github.com/karpathy/autoresearch"
description: "AI agents running research on single-GPU nanochat training automatically"
starred_at: "2026-10-08T20:14:47Z"
language: "Python"
topics: []
homepage: ""
license: null
archived: false
---

# karpathy/autoresearch

AI agents running research on single-GPU nanochat training automatically

**GitHub:** https://github.com/karpathy/autoresearch

## README excerpt

> # autoresearch
> *One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of "group meeting". That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies. The agents claim that we are now in the 10,205th generation of the code base, in any case no one could tell if that's right or wrong as the "code" is now a self-modifying binary that has grown beyond human comprehension. This repo is the story of how it all began. -@karpathy, March 2026*.
> The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. You wake up in the morning to a log of experiments and (hopefully) a better model. The training code here is a simplified single-GPU implementation of [nanochat](https://github.com/karpathy/nanochat). The core idea is that you're not touching any of the Python files like you normally would as a researcher. Instead, you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org. The default `program.md` in this repo is intentionally kept as a bare bones baseline, though it's obvious how one would iterate on it over time to find the "research org code" that achieves the fastest research progress, how you'd add more agents to the mix, etc. A bit more context on this project is here in this [tweet](https://x.com/karpathy/status/2029701092347630069) and [this tweet](https://x.com/karpathy/status/2031135152349524125).
> ## How it works
> The repo is deliberately kept small and only really has three files that matter:
> - **`prepare.py`** — fixed constants, one-time data prep (downloads training data, trains a BPE tokenizer), and runtime utilities (dataloader, evaluation). Not modified.
> - **`train.py`** — the single file the agent edits. Contains the full GPT model, optimizer (Muon + AdamW), and training loop. Everything is fair game: architecture, hyperparameters, optimizer, batch size, etc. **This file is edited and iterated on by the agent**.
> - **`program.md`** — baseline instructions for one agent. Point your agent here and let it go. **This file is edited and iterated on by the human**.
> By design, training runs for a **fixed 5-minu

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

An autonomous research setup where an AI agent edits a single-GPU LLM training script, runs five-minute training experiments, and keeps or discards changes based on results. It is a simplified implementation based on nanochat, with the human-edited program.md providing agent instructions.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "b2ccadfa651ae4d7063686a1b5641a8a70658453655cd231464e07944b76199e"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning"
  ],
  "repository_type": "application",
  "capabilities": [
    "model-training",
    "code-generation",
    "model-evaluation"
  ],
  "technologies": [
    "Python",
    "PyTorch",
    "Markdown"
  ],
  "summary": "An autonomous research setup where an AI agent edits a single-GPU LLM training script, runs five-minute training experiments, and keeps or discards changes based on results. It is a simplified implementation based on nanochat, with the human-edited program.md providing agent instructions.",
  "use_cases": [
    "Running automated overnight LLM training experiments on a single GPU",
    "Studying how agent-driven research loops modify and evaluate training code"
  ],
  "limitations": [
    "Designed for single-GPU training; scale-up is not documented",
    "Topics and license metadata are empty, so licensing terms are unverified",
    "README excerpt is truncated and the full feature set could not be confirmed"
  ],
  "suggested_terms": [
    "autoresearch",
    "nanochat",
    "autonomous agents LLM training",
    "single-GPU training",
    "program.md"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
