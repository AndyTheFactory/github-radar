---
repository: "datalab-to/surya"
github_id: 741297064
url: "https://github.com/datalab-to/surya"
description: "OCR, layout analysis, reading order, table recognition in 90+ languages"
starred_at: "2026-10-26T15:06:23Z"
language: "Python"
topics: []
homepage: "https://www.datalab.to"
license: "Apache-2.0"
archived: false
---

# datalab-to/surya

OCR, layout analysis, reading order, table recognition in 90+ languages

**GitHub:** https://github.com/datalab-to/surya

## README excerpt

> Datalab
>
> State of the Art models for Document Intelligence
>
>
>
>
>
>
> # Surya
> Surya is a 650M param OCR model with these features:
> - Accuracy - scores 83.3% on [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench) (top under 3B params)
> - Speed - throughput of 5 pages/s on an RTX 5090
> - Multilingual - scores 87.2% on an internal benchmark set of 91 languages (more [here](#multilingual))
> - Layout analysis (table, image, header, etc.) with reading order
> - Table recognition (rows + columns)
> We also ship smaller models for line-level text detection and ocr error detection.  It works on a range of documents (see [usage](#usage) and [benchmarks](#benchmarks)).
> ## Try Datalab's Managed Platform
> Our managed platform uses Surya, our highest accuracy model [Chandra](https://github.com/datalab-to/chandra), and other models.
> The Datalab API turns documents into verifiable knowledge your agents act on. Every result traces back to its page and position, and one API can parse, extract, fill and edit documents.
> Get started with **about 5,000 free convert pages every month** (work email) — [sign up](https://www.datalab.to/?utm_source=gh-surya) (takes under 30 seconds) or try our free [public playground](https://www.datalab.to/playground?utm_source=gh-surya).
> ## Model Information
> |                            Detection                             |                                   OCR                                   |
> |:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
> |    |   |
> |                               Layout                               |                       Table Recognition                       |
> |:------------------------------------------------------------------:|:-------------------------------------------------------------:|
> |  |  |
> Surya is named for the [Hindu sun god](https://en.wikipedia.org/wiki/Surya), who has universal vision.
> ## Examples
> Each row links to five annotated views of the same page: text-line detection, OCR, layout, reading order, and (when present) table recognition.
> | Name              |              Detection              |                                       OCR |                                       Layout |                                          Order |                                       Table Rec |
> |-------------------|:-----------------------------------:|------------------------------------------:|-------------------

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Surya is a Python OCR toolkit built around a 650M-parameter model that provides text detection, OCR, layout analysis with reading order, and table recognition across 90+ languages. The README also describes smaller models for line-level text detection and OCR error detection.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "c8421266c78fa9ab67a8018c45596ce642fc22f609fc69b9ae5779affb16bc0c"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "vision-media",
    "productivity"
  ],
  "repository_type": "library",
  "capabilities": [
    "ocr",
    "object-detection",
    "information-extraction",
    "data-transformation",
    "inference-serving"
  ],
  "technologies": [
    "Python"
  ],
  "summary": "Surya is a Python OCR toolkit built around a 650M-parameter model that provides text detection, OCR, layout analysis with reading order, and table recognition across 90+ languages. The README also describes smaller models for line-level text detection and OCR error detection.",
  "use_cases": [
    "Converting scanned documents and PDFs into machine-readable text",
    "Recovering document layout and reading order",
    "Extracting table rows and columns from documents"
  ],
  "limitations": [
    "Accuracy and throughput figures are self-reported benchmarks",
    "Requires a GPU for the stated throughput numbers (RTX 5090 example)",
    "Highest-accuracy model and managed API are offered via Datalab's commercial platform"
  ],
  "suggested_terms": [
    "OCR",
    "layout analysis",
    "table recognition",
    "document intelligence",
    "reading order"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
