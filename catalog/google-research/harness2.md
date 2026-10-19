---
repository: "google-research/harness2"
github_id: 1407951147
url: "https://github.com/google-research/harness2"
description: ""
starred_at: "2026-10-19T11:06:33Z"
language: "Python"
topics: []
homepage: ""
license: "Apache-2.0"
archived: false
---

# google-research/harness2

No description provided.

**GitHub:** https://github.com/google-research/harness2

## README excerpt

> Recursive Agent Harnessing for an Open World
>
>
>
>
>
> A **harness** is the system around a model that enables it to act as an agent:
> prompts, tools, memory, skills, orchestration, and more. **Harnessing** is the
> process of optimizing that system.
> Harness² is a plug-and-play framework for **recursive agent harnessing** in an
> open world, where agents encounter tasks unseen during harness design. It
> connects two levels of recursion while keeping model weights fixed:
> * **Task-level recursion** refines the execution harness for the current task
> through a contrastive **Propose–Probe–Compose** step: propose edits, probe
> their effects on the same task, and compose a refined harness from behavioral
> contrasts between executions, without ground-truth feedback.
> * **Harnessing-level recursion** updates a persistent *improvement harness*
> with adopted harnesses and evidence-supported lessons from each task to guide
> future refinement.
>
>
> Across three professional benchmarks and four model–harness configurations, a
> single Harness² step improves GLM-5 and Gemini 3.5 Flash over their base
> harnesses, with gains of up to 11.5 points on WorkBuddy-Bench, 4.5 points on
> JobBench, and 11.8 percentage points on LAB's partial pass rate. Increasing the
> task-level recursion budget brings further gains.
> The release supports **parallel and sequential recursion**, **OpenCode and
> Codex executors**, and **JobBench, LAB, and WorkBuddy-Bench**.
> ## Video overview
> https://github.com/user-attachments/assets/76b10548-b14b-4c8f-9aa5-a93662df4d56
> ## Contents
> - [Video overview](#video-overview)
> - [Harness components](#harness-components)
> - [Install](#install)
> - [Run a benchmark](#run-a-benchmark)
> - [Experiments](#experiments)
> - [Web access](#web-access)
> - [Results and resume](#results-and-resume)
> - [Citation](#citation)
> - [Contributing](#contributing)
> - [License](#license)
> - [Disclaimer](#disclaimer)
> ## Harness components
> Harness² exposes eight editable components around the model: **system prompt,
> guardrails, memory, tool guidance, subagents, skills, scripts, and plugins**.
> They control context construction, the tool interface, delegation, and behavior
> inside the tool loop.
>
>
> ## Install
> Use **Linux, Python 3.12, and [uv](https://docs.astral.sh/uv/getting-started/installation/)**.
> From the repository root:
> uv venv --python 3.12 .venv
> source .venv/bin/activate
> uv pip install -e '.[render]'
> harness2-demo --output runs/demo --k 2
> The local demo runs both recursion modes with deterministic editors and real

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Harness² is a research framework for recursive agent harnessing that refines the prompts, tools, memory, and orchestration around fixed-weight models. It includes a local demo and supports JobBench, LAB, and WorkBuddy-Bench benchmarks with OpenCode and Codex executors. The README reports benchmark gains for GLM-5 and Gemini 3.5 Flash.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "f99c02e9eb2bf219129e300c3819d0f85913620d9be0251d11acfe03fbcad30f"
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
    "model-evaluation",
    "workflow-orchestration"
  ],
  "technologies": [
    "Python",
    "uv",
    "OpenCode",
    "Codex"
  ],
  "summary": "Harness² is a research framework for recursive agent harnessing that refines the prompts, tools, memory, and orchestration around fixed-weight models. It includes a local demo and supports JobBench, LAB, and WorkBuddy-Bench benchmarks with OpenCode and Codex executors. The README reports benchmark gains for GLM-5 and Gemini 3.5 Flash.",
  "use_cases": [
    "Evaluating agent harness designs on professional benchmarks",
    "Running parallel or sequential recursive harness refinement experiments",
    "Reproducing reported Harness² benchmark results"
  ],
  "limitations": [
    "Requires Linux, Python 3.12, and uv per the install instructions",
    "Local demo uses deterministic editors rather than live model edits",
    "Benchmark results are author-reported and not independently verified here"
  ],
  "suggested_terms": [
    "agent harness",
    "recursive agent harnessing",
    "LLM agent benchmark",
    "JobBench",
    "WorkBuddy-Bench"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
