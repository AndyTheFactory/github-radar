---
repository: "google/langextract"
github_id: 1016323751
url: "https://github.com/google/langextract"
description: "A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization."
starred_at: "2026-10-08T20:16:43Z"
language: "Python"
topics: ["gemini", "gemini-ai", "gemini-api", "gemini-flash", "gemini-pro", "information-extration", "large-language-models", "llm", "nlp", "python", "structured-data"]
homepage: "https://pypi.org/project/langextract/"
license: "Apache-2.0"
archived: false
---

# google/langextract

A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization.

**GitHub:** https://github.com/google/langextract

## README excerpt

> # LangExtract
> ## Table of Contents
> - [Introduction](#introduction)
> - [Why LangExtract?](#why-langextract)
> - [Quick Start](#quick-start)
> - [Installation](#installation)
> - [API Key Setup for Cloud Models](#api-key-setup-for-cloud-models)
> - [Adding Custom Model Providers](#adding-custom-model-providers)
> - [Using OpenAI Models](#using-openai-models)
> - [Using Local LLMs with Ollama](#using-local-llms-with-ollama)
> - [More Examples](#more-examples)
> - [*Romeo and Juliet* Full Text Extraction](#romeo-and-juliet-full-text-extraction)
> - [Medication Extraction](#medication-extraction)
> - [Radiology Report Structuring: RadExtract](#radiology-report-structuring-radextract)
> - [Community Providers](#community-providers)
> - [Contributing](#contributing)
> - [Testing](#testing)
> - [How to Cite](#how-to-cite)
> - [Disclaimer](#disclaimer)
> ## Introduction
> LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based on user-defined instructions. It processes materials such as clinical notes or reports, identifying and organizing key details while ensuring the extracted data corresponds to the source text.
>
>
>
>
>
> Try the live demo &rarr;
> Run grounded extraction on Romeo and Juliet in your browser, no install required.
>
> ## Why LangExtract?
> 1.  **Precise Source Grounding:** Maps every extraction to its exact location in the source text, enabling visual highlighting for easy traceability and verification.
> 2.  **Reliable Structured Outputs:** Enforces a consistent output schema based on your few-shot examples, leveraging controlled generation in supported models like Gemini to guarantee robust, structured results.
> 3.  **Optimized for Long Documents:** Overcomes the "needle-in-a-haystack" challenge of large document extraction by using an optimized strategy of text chunking, parallel processing, and multiple passes for higher recall.
> 4.  **Interactive Visualization:** Instantly generates a self-contained, interactive HTML file to visualize and review thousands of extracted entities in their original context.
> 5.  **Flexible LLM Support:** Supports your preferred models, from cloud-based LLMs like the Google Gemini family to local open-source models via the built-in Ollama interface.
> 6.  **Adaptable to Any Domain:** Define extraction tasks for any domain using just a few examples. LangExtract adapts to your needs without requiring any model fine-tuning.
> 7.  **Leverages LLM World Knowledge:** Utilize precise prompt wording and few-sho

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

LangExtract is a Python library that uses LLMs to extract structured information from unstructured text based on user-defined instructions and few-shot examples. It maps extractions to their source text locations and generates an interactive HTML visualization for review.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "5f464997c582da69cbba53c8d47078a369bd5c62ccd77d5993d5ad74174916a9"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning"
  ],
  "repository_type": "library",
  "capabilities": [
    "information-extraction",
    "data-transformation",
    "annotation"
  ],
  "technologies": [
    "Python",
    "Gemini",
    "Ollama",
    "OpenAI",
    "Large Language Models",
    "HTML"
  ],
  "summary": "LangExtract is a Python library that uses LLMs to extract structured information from unstructured text based on user-defined instructions and few-shot examples. It maps extractions to their source text locations and generates an interactive HTML visualization for review.",
  "use_cases": [
    "Structuring clinical notes and radiology reports",
    "Extracting entities from long documents",
    "Reviewing extractions against source text"
  ],
  "limitations": [
    "Depends on external LLM providers or local models such as Ollama",
    "Output consistency relies on model support for controlled generation, such as Gemini"
  ],
  "suggested_terms": [
    "llm information extraction",
    "structured data from text",
    "source grounding",
    "few-shot extraction",
    "langextract"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
