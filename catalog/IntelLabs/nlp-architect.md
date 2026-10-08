---
repository: "IntelLabs/nlp-architect"
github_id: 133867923
url: "https://github.com/IntelLabs/nlp-architect"
description: "A model library for exploring state-of-the-art deep learning topologies and techniques for optimizing Natural Language Processing neural networks"
starred_at: "2021-02-14T21:21:06Z"
language: "Python"
topics: ["bert", "deep-learning", "deeplearning", "dynet", "nlp", "nlu", "pytorch", "quantization", "tensorflow", "transformers"]
homepage: "https://intellabs.github.io/nlp-architect"
license: "Apache-2.0"
archived: true
---

# IntelLabs/nlp-architect

A model library for exploring state-of-the-art deep learning topologies and techniques for optimizing Natural Language Processing neural networks

**GitHub:** https://github.com/IntelLabs/nlp-architect

## README excerpt

> > :warning: **DISCONTINUATION OF PROJECT** - *This project will no longer be maintained by Intel.  This project has been identified as having known security escapes.  Intel has ceased development and contributions including, but not limited to, maintenance, bug fixes, new releases, or updates, to this project.* **Intel no longer accepts patches to this project.**
>
>
>
>
>
> A Deep Learning NLP/NLU library by Intel® AI Lab
>
>
>
>
>
> NLP Architect is an open source Python library for exploring state-of-the-art
> deep learning topologies and techniques for optimizing Natural Language Processing and
> Natural Language Understanding Neural Networks.
> ## Overview
> NLP Architect is an NLP library designed to be flexible, easy to extend, allow for easy and rapid integration of NLP models in applications and to showcase optimized models.
> Features:
> * Core NLP models used in many NLP tasks and useful in many NLP applications
> * Novel NLU models showcasing novel topologies and techniques
> * Optimized NLP/NLU models showcasing different optimization algorithms on neural NLP/NLU models
> * Model-oriented design:
> * Train and run models from command-line.
> * API for using models for inference in python.
> * Procedures to define custom processes for training,    inference or anything related to processing.
> * CLI sub-system for running procedures
> * Based on optimized Deep Learning frameworks:
> * [TensorFlow]
> * [PyTorch]
> * [Dynet]
> * Essential utilities for working with NLP models - Text/String pre-processing, IO, data-manipulation, metrics, embeddings.
> ## Installing NLP Architect
> We recommend to install NLP Architect in a new python environment, to use python 3.6+ with up-to-date `pip`, `setuptools` and `h5py`.
> ### Install using `pip`
> Install core library only
> pip install nlp-architect
> ### Install from source (Github)
> Includes core library, examples, solutions and tutorials:
> git clone https://github.com/IntelLabs/nlp-architect.git
> cd nlp-architect
> pip install -e .  # install in developer mode
> ### Running Examples and Solutions
> To run provided examples and solutions please install the library with `[all]` flag which will install extra packages required. (requires installation from source)
> pip install .[all]
> ## Models
> NLP models that provide best (or near) in class performance:
> * [Word chunking](https://intellabs.github.io/nlp-architect/tagging/sequence_tagging.html#word-chunker)
> * [Named Entity Recognition](https://intellabs.github.io/nlp-architect/tagging/sequence_tagging.html#named-entity-recogniti

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

NLP Architect is a Python library for exploring deep learning topologies and optimization techniques for Natural Language Processing and Understanding models. It provides core NLP models, trainable command-line tools, and a Python inference API. The repository is archived and Intel has discontinued maintenance due to known security issues.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "0935b18dc63c7a5d730fffb0e0585758cf08b6b2d7f866a31de7d6d6dcc63a2a"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning"
  ],
  "repository_type": "library",
  "capabilities": [
    "model-training",
    "inference-serving",
    "benchmarking"
  ],
  "technologies": [
    "Python",
    "TensorFlow",
    "PyTorch",
    "DyNet"
  ],
  "summary": "NLP Architect is a Python library for exploring deep learning topologies and optimization techniques for Natural Language Processing and Understanding models. It provides core NLP models, trainable command-line tools, and a Python inference API. The repository is archived and Intel has discontinued maintenance due to known security issues.",
  "use_cases": [
    "Training and running NLP models from the command line",
    "Using pre-built NLP models for inference in Python",
    "Exploring optimized NLP/NLU model techniques"
  ],
  "limitations": [
    "Archived and no longer maintained by Intel",
    "Known security escapes reported; no patches accepted",
    "Requires Python 3.6+ and specific framework dependencies"
  ],
  "suggested_terms": [
    "nlp library",
    "named entity recognition",
    "quantization nlp",
    "nlu models",
    "dynet pytorch tensorflow"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
