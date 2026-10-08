---
repository: "lamm-mit/SwarmWorld"
github_id: 1356949462
url: "https://github.com/lamm-mit/SwarmWorld"
description: ""
starred_at: "2026-10-08T20:18:40Z"
language: "Python"
topics: []
homepage: ""
license: "Apache-2.0"
archived: false
---

# lamm-mit/SwarmWorld

No description provided.

**GitHub:** https://github.com/lamm-mit/SwarmWorld

## README excerpt

> # SwarmWorld
> SwarmWorld is a deterministic research environment for studying how societies of
> language-model agents discover, test, exchange, inherit, and physically embody
> technologies in a shared world. Agents perceive locally, act through a bounded action
> contract, and leave persistent artifacts whose material effects and executable
> programs continue on later simulation ticks.
> This repository is the clean source-code release. The approximately 8.4 GB paper
> dataset - authoritative traces, manifests, seed-level tables, derived analyses, and
> final figures - is released separately at
> [lamm-mit/swarmworld-data](https://huggingface.co/datasets/lamm-mit/swarmworld-data).
> See [DATA.md](DATA.md) for the code/data boundary and download examples.
> The historical Python package and command name is `biofoundry`; it is retained for
> trace, import, and command-line compatibility. The public project and repository are
> named SwarmWorld.
> ## What is included
> - authoritative Python simulator and PettingZoo interface;
> - scripted and OpenAI-compatible LLM policies;
> - exact event traces, deterministic replay, counterfactual replay, and integrity checks;
> - controlled multi-condition study runner and seed-level analysis;
> - artifact programs, program inheritance, causal knowledge records, and held-out
> ecological evaluation;
> - Three.js Observatory, optional Godot client, and human-in-the-swarm client;
> - declarative scenario packages, including the Ashen Realms example;
> - a repository-local agent skill for authoring and validating new scenario packages;
> - core Python and browser tests.
> Generated study data, journal-figure pipelines, reports, movies, caches, and local
> development state are intentionally not bundled.
> ## Install
> SwarmWorld requires Python 3.10 or newer. Python 3.12 is the reference release
> environment.
> git clone https://github.com/lamm-mit/SwarmWorld.git
> cd SwarmWorld
> python -m venv .venv
> source .venv/bin/activate
> python -m pip install --upgrade pip
> python -m pip install -e ".[dev,analysis]"
> biofoundry doctor --config configs/demo.yaml
> Alternatively, create the pinned Conda environment:
> conda env create -f environment.yml
> conda activate biofoundry-world
> biofoundry doctor --config configs/demo.yaml
> No model is downloaded or contacted by `configs/demo.yaml`. API keys are read only
> from the environment variable named by the selected YAML profile.
> ## Run a deterministic no-key simulation
> biofoundry simulate \
> --config configs/demo.yaml \
> --policy scripted \
> --ticks 128 \
> -

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

SwarmWorld is a deterministic research environment for studying how societies of language-model agents discover, test, exchange, and embody technologies in a shared world. The repository provides the simulator, PettingZoo interface, LLM and scripted policies, replay and integrity tooling, study runner, and browser and Godot clients.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "a1f4ca3b69dbd903b54afd765fff5982bab75d922c873f6b8ea50e55d4b1e043"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "scientific-computing",
    "games"
  ],
  "repository_type": "research",
  "capabilities": [
    "simulation",
    "agent-orchestration",
    "model-evaluation",
    "benchmarking",
    "game-development"
  ],
  "technologies": [
    "Python",
    "PettingZoo",
    "Three.js",
    "Godot",
    "Conda",
    "YAML",
    "OpenAI-compatible APIs"
  ],
  "summary": "SwarmWorld is a deterministic research environment for studying how societies of language-model agents discover, test, exchange, and embody technologies in a shared world. The repository provides the simulator, PettingZoo interface, LLM and scripted policies, replay and integrity tooling, study runner, and browser and Godot clients.",
  "use_cases": [
    "Studying emergent multi-agent behavior of language-model agents in simulated worlds",
    "Running deterministic, no-key simulations for reproducible experiments",
    "Authoring and evaluating declarative scenario packages"
  ],
  "limitations": [
    "Generated study data and figures are not bundled; the ~8.4 GB dataset is released separately on Hugging Face",
    "Requires Python 3.10+ and optional API keys for OpenAI-compatible LLM policies",
    "Repository has no description or topics in source metadata"
  ],
  "suggested_terms": [
    "multi-agent simulation",
    "language model agents",
    "PettingZoo environment",
    "deterministic replay",
    "artifact programs"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
