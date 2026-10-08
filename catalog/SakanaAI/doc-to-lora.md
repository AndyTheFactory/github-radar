---
repository: "SakanaAI/doc-to-lora"
github_id: 1155266070
url: "https://github.com/SakanaAI/doc-to-lora"
description: "Hypernetworks that update LLMs to remember factual information"
starred_at: "2026-10-08T20:15:18Z"
language: "Python"
topics: ["ai", "ai-agent", "hypernetworks", "llm", "llm-agent", "lora", "machine-learning", "memory"]
homepage: "https://arxiv.org/abs/2602.15902"
license: "MIT"
archived: false
---

# SakanaAI/doc-to-lora

Hypernetworks that update LLMs to remember factual information

**GitHub:** https://github.com/SakanaAI/doc-to-lora

## README excerpt

> Doc-to-LoRA (D2L): Learning to Instantly Internalize Contexts
> :sparkles:Interactive Web |
> :newspaper:X |
> :scroll:Paper |
> :hugs:Hugging Face |
> :octocat:GitHub
> A reference implementation of Doc-to-LoRA (D2L).
> ---
> ## 🛠️ Installation
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ./install.sh
> ## 🤗 Pre-Trained Models
> uv run huggingface-cli login
> uv run huggingface-cli download SakanaAI/doc-to-lora --local-dir trained_d2l --include "*/"
> ## 🚀 Python API Usage
> # caveat: this interface only supports non-batched inputs
> # for batched inference please see `src/ctx_to_lora/modeling/hypernet.py`
> import torch
> from ctx_to_lora.model_loading import get_tokenizer
> from ctx_to_lora.modeling.hypernet import ModulatedPretrainedModel
> # model loading
> checkpoint_path = "trained_d2l/gemma_demo/checkpoint-80000/pytorch_model.bin"
> state_dict = torch.load(checkpoint_path, weights_only=False)
> model = ModulatedPretrainedModel.from_state_dict(
> state_dict, train=False, use_sequence_packing=False
> )
> model.reset()
> tokenizer = get_tokenizer(model.base_model.name_or_path)
> # prepare data
> doc = open("data/sakana_wiki.txt", "r").read()
> chat = [{"role": "user", "content": "Tell me about Sakana AI."}]
> chat_ids = tokenizer.apply_chat_template(
> chat,
> add_special_tokens=False,
> return_attention_mask=False,
> add_generation_prompt=True,
> return_tensors="pt",
> ).to(model.device)
> # calls after internalization will be influenced by internalized info
> model.internalize(doc)
> outputs = model.generate(input_ids=chat_ids, max_new_tokens=512)
> print(tokenizer.decode(outputs[0]))
> # remove internalized info
> # model.reset()
> # without internalized info, the model will halucinate
> # outputs = model.generate(input_ids=chat_ids, max_new_tokens=512)
> # print(tokenizer.decode(outputs[0]))
> ### 🎮 Interactive Demo
> uv run demo/app.py
> Video Demo
>
> ### 🧪 Experimental Scripts
> To run any of the following scripts, use `uv run $PATH_TO_SCRIPT` from the root of this project.
> | Experiment                           | Data prep                             | Training                      | Evaluation                   | Notes                                                                                                                               |
> | ------------------------------------ | ------------------------------------- | ----------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
> | [Main experiment]

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Reference implementation of Doc-to-LoRA (D2L), a hypernetwork approach that internalizes document contexts into LLM weights via LoRA modules. It provides a Python API, an interactive web demo, and experimental training and evaluation scripts.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "790476764612330fd8ea8723cc64393fcf1d5ffeb5271f14b02b1a0683fd5ece"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning",
    "developer-tools"
  ],
  "repository_type": "research",
  "capabilities": [
    "model-training",
    "inference-serving",
    "fine-tuning",
    "question-answering"
  ],
  "technologies": [
    "Python",
    "PyTorch",
    "LoRA",
    "Hugging Face",
    "uv",
    "Gemma"
  ],
  "summary": "Reference implementation of Doc-to-LoRA (D2L), a hypernetwork approach that internalizes document contexts into LLM weights via LoRA modules. It provides a Python API, an interactive web demo, and experimental training and evaluation scripts.",
  "use_cases": [
    "Letting an LLM answer questions about a document without keeping it in the prompt",
    "Experimenting with hypernetwork-based context internalization",
    "Running an interactive demo of document-to-LoRA updates"
  ],
  "limitations": [
    "Python API supports only non-batched inputs per the README",
    "Requires downloading pre-trained checkpoints from Hugging Face",
    "README notes that without internalized info the model may hallucinate"
  ],
  "suggested_terms": [
    "hypernetwork LoRA",
    "doc-to-lora",
    "context internalization",
    "LLM memory",
    "instant fine-tuning"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
