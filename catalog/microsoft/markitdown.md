---
repository: "microsoft/markitdown"
github_id: 888092115
url: "https://github.com/microsoft/markitdown"
description: "Python tool for converting files and office documents to Markdown."
starred_at: "2026-10-08T20:16:54Z"
language: "Python"
topics: ["autogen", "autogen-extension", "langchain", "markdown", "microsoft-office", "openai", "pdf"]
homepage: ""
license: "MIT"
archived: false
---

# microsoft/markitdown

Python tool for converting files and office documents to Markdown.

**GitHub:** https://github.com/microsoft/markitdown

## README excerpt

> # MarkItDown
> > [!IMPORTANT]
> > MarkItDown performs I/O with the privileges of the current process. Like open() or requests.get(), it will access resources that the process itself can access. Sanitize your inputs in untrusted environments, and call the narrowest `convert_*` function needed for your use case (e.g., `convert_stream()`, or `convert_local()`). See the [Security Considerations](#security-considerations) section of the documentation for more information.
> MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines. To this end, it is most comparable to [textract](https://github.com/deanmalmgren/textract), but with a focus on preserving important document structure and content as Markdown (including: headings, lists, tables, links, etc.) While the output is often reasonably presentable and human-friendly, it is meant to be consumed by text analysis tools -- and may not be the best option for high-fidelity document conversions for human consumption.
> MarkItDown currently supports the conversion from:
> - PDF
> - PowerPoint
> - Word
> - Excel
> - Images (EXIF metadata and OCR)
> - Audio (EXIF metadata and speech transcription)
> - HTML
> - Text-based formats (CSV, JSON, XML)
> - ZIP files (iterates over contents)
> - YouTube URLs
> - EPubs
> - ... and more!
> ## Why Markdown?
> Markdown is extremely close to plain text, with minimal markup or formatting, but still
> provides a way to represent important document structure. Mainstream LLMs, such as
> OpenAI's GPT-4o, natively "_speak_" Markdown, and often incorporate Markdown into their
> responses unprompted. This suggests that they have been trained on vast amounts of
> Markdown-formatted text, and understand it well. As a side benefit, Markdown conventions
> are also highly token-efficient.
> ## Prerequisites
> MarkItDown requires Python 3.10 through 3.14. It is recommended to use a virtual environment to avoid dependency conflicts.
> With the standard Python installation, you can create and activate a virtual environment using the following commands:
> python -m venv .venv
> source .venv/bin/activate
> If using `uv`, you can create a virtual environment with:
> uv venv --python=3.12 .venv
> source .venv/bin/activate
> # NOTE: Be sure to use 'uv pip install' rather than just 'pip install' to install packages in this virtual environment
> If you are using Anaconda, you can create a virtual environment with:
> conda create -n markitdown python=3.12
> conda activate markitdown
> ## Install

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

MarkItDown is a Python utility that converts files such as PDF, Office documents, HTML, images, audio, ZIP archives, and YouTube URLs into Markdown. It is intended for LLM and text analysis pipelines, preserving structure like headings, lists, tables, and links. The README warns that it performs I/O with the current process's privileges and recommends sanitizing inputs in untrusted environments.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "c560bb1cd0b9fb52e5fd048e1b9aaeed9b55426ad6659c8c39d64f41241bd6d8"
  },
  "primary_domain": "data-engineering",
  "secondary_domains": [
    "data-engineering",
    "ai-ml"
  ],
  "repository_type": "library",
  "capabilities": [
    "data-transformation",
    "document-processing",
    "information-extraction",
    "ocr",
    "speech-recognition"
  ],
  "technologies": [
    "Python",
    "PDF",
    "Microsoft Office",
    "OpenAI",
    "AutoGen",
    "LangChain",
    "uv",
    "Anaconda"
  ],
  "summary": "MarkItDown is a Python utility that converts files such as PDF, Office documents, HTML, images, audio, ZIP archives, and YouTube URLs into Markdown. It is intended for LLM and text analysis pipelines, preserving structure like headings, lists, tables, and links. The README warns that it performs I/O with the current process's privileges and recommends sanitizing inputs in untrusted environments.",
  "use_cases": [
    "Preparing document content as Markdown for LLM ingestion",
    "Converting Office files and PDFs into token-efficient text for analysis",
    "Extracting text and metadata from images, audio, and web content"
  ],
  "limitations": [
    "Output may not suit high-fidelity conversions for human consumption",
    "Performs I/O with the privileges of the current process, requiring input sanitization in untrusted environments",
    "Requires Python 3.10 through 3.14"
  ],
  "suggested_terms": [
    "markdown conversion",
    "pdf to markdown",
    "office document conversion",
    "document to text llm",
    "markitdown"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
