---
repository: "huggingface/transformers"
github_id: 155220641
url: "https://github.com/huggingface/transformers"
description: "🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. "
starred_at: "2020-05-02T22:22:40Z"
language: "Python"
topics: ["audio", "deep-learning", "deepseek", "gemma", "glm", "hacktoberfest", "llm", "machine-learning", "model-hub", "natural-language-processing", "nlp", "pretrained-models", "python", "pytorch", "pytorch-transformers", "qwen", "speech-recognition", "transformer", "vlm"]
homepage: "https://huggingface.co/transformers"
license: "Apache-2.0"
archived: false
---

# huggingface/transformers

🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**GitHub:** https://github.com/huggingface/transformers

## README excerpt

> Copyright 2020 The HuggingFace Team. All rights reserved.
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
> http://www.apache.org/licenses/LICENSE-2.0
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
> -->
>
>
>
>
>
>
>
>
>
>
>
> English |
>
>
>
> State-of-the-art pretrained models for inference and training
>
>
>
> Transformers acts as the model-definition framework for state-of-the-art machine learning with text, computer
> vision, audio, video, and multimodal models, for both inference and training.
> It centralizes the model definition so that this definition is agreed upon across the ecosystem. `transformers` is the
> pivot across frameworks: if a model definition is supported, it will be compatible with the majority of training
> frameworks (Axolotl, Unsloth, DeepSpeed, FSDP, PyTorch-Lightning, ...), inference engines (vLLM, SGLang, TGI, ...),
> and adjacent modeling libraries (llama.cpp, mlx, ...) which leverage the model definition from `transformers`.
> We pledge to help support new state-of-the-art models and democratize their usage by having their model definition be
> simple, customizable, and efficient.
> There are over 1M+ Transformers [model checkpoints](https://huggingface.co/models?library=transformers&sort=trending) on the [Hugging Face Hub](https://huggingface.co/models) you can use.
> Explore the [Hub](https://huggingface.co/) today to find a model and use Transformers to help you get started right away.
> ## Installation
> Transformers works with Python 3.10+, and [PyTorch](https://pytorch.org/get-started/locally/) 2.5+.
> Create and activate a virtual environment with [venv](https://docs.python.org/3/library/venv.html) or [uv](https://docs.astral.sh/uv/), a fast Rust-based Python package and project manager.
> # venv
> python -m venv .my-env
> source .my-env/bin/activate
> # uv
> uv venv .my-env
> source .my-env/bin/activate
> Install Transformers in your virtual environment.
> # pip
> pip install "transformers[torch]"
> # uv
> uv pip install "transformers[torch]"
> Install Transformers from source if you want the latest changes in the library or are interested in contributing. However, the *latest* version may not be stable. Feel free t

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Transformers is a model-definition framework providing state-of-the-art pretrained machine learning models for text, vision, audio, video, and multimodal tasks, supporting both inference and training. The README states it is compatible with training frameworks, inference engines, and adjacent modeling libraries, and that over one million checkpoints are available on the Hugging Face Hub.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "ef18b7e2c9960a90159969d97cc034557bd84a8eb0f1049dff64a40c7d24ac1e"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning",
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "model-training",
    "inference-serving",
    "speech-recognition",
    "image-classification",
    "question-answering"
  ],
  "technologies": [
    "Python",
    "PyTorch",
    "Hugging Face Hub",
    "Transformers",
    "DeepSpeed",
    "vLLM",
    "llama.cpp",
    "uv"
  ],
  "summary": "Transformers is a model-definition framework providing state-of-the-art pretrained machine learning models for text, vision, audio, video, and multimodal tasks, supporting both inference and training. The README states it is compatible with training frameworks, inference engines, and adjacent modeling libraries, and that over one million checkpoints are available on the Hugging Face Hub.",
  "use_cases": [
    "Running pretrained models for inference on text, vision, audio, and multimodal tasks",
    "Fine-tuning or training state-of-the-art models with PyTorch-based frameworks",
    "Finding and loading model checkpoints from the Hugging Face Hub"
  ],
  "limitations": [
    "Requires Python 3.10+ and PyTorch 2.5+ per the README",
    "Source-installed versions on main may not be stable",
    "Model support and performance depend on individual checkpoints"
  ],
  "suggested_terms": [
    "pretrained models",
    "transformers library",
    "Hugging Face",
    "NLP model training",
    "model inference"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
