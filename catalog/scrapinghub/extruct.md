---
repository: "scrapinghub/extruct"
github_id: 44965223
url: "https://github.com/scrapinghub/extruct"
description: "Extract embedded metadata from HTML markup"
starred_at: "2026-10-09T14:12:02Z"
language: "Python"
topics: ["hacktoberfest", "json-ld", "microdata", "microformats", "opengraph", "rdfa", "semantic-web"]
homepage: ""
license: "BSD-3-Clause"
archived: false
---

# scrapinghub/extruct

Extract embedded metadata from HTML markup

**GitHub:** https://github.com/scrapinghub/extruct

## README excerpt

> =======
> extruct
> =======
> .. image:: https://github.com/scrapinghub/extruct/workflows/build/badge.svg?branch=master
> :target: https://github.com/scrapinghub/extruct/actions
> :alt: Build Status
> .. image:: https://img.shields.io/codecov/c/github/scrapinghub/extruct/master.svg?maxAge=2592000
> :target: https://codecov.io/gh/scrapinghub/extruct
> :alt: Coverage report
> .. image:: https://img.shields.io/pypi/v/extruct.svg
> :target: https://pypi.python.org/pypi/extruct
> :alt: PyPI Version
> *extruct* is a library for extracting embedded metadata from HTML markup.
> Currently, *extruct* supports:
> - `W3C's HTML Microdata`_
> - `embedded JSON-LD`_
> - `Microformat`_ via `mf2py`_
> - `Facebook's Open Graph`_
> - (experimental) `RDFa`_ via `rdflib`_
> - `Dublin Core Metadata (DC-HTML-2003)`_
> .. _W3C's HTML Microdata: http://www.w3.org/TR/microdata/
> .. _embedded JSON-LD: http://www.w3.org/TR/json-ld/#embedding-json-ld-in-html-documents
> .. _RDFa: https://www.w3.org/TR/html-rdfa/
> .. _rdflib: https://pypi.python.org/pypi/rdflib/
> .. _Microformat: http://microformats.org/wiki/Main_Page
> .. _mf2py: https://github.com/microformats/mf2py
> .. _Facebook's Open Graph: http://ogp.me/
> .. _Dublin Core Metadata (DC-HTML-2003): https://www.dublincore.org/specifications/dublin-core/dcq-html/2003-11-30/
> The microdata algorithm is a revisit of `this Scrapinghub blog post`_ showing how to use EXSLT extensions.
> .. _this Scrapinghub blog post: http://blog.scrapinghub.com/2014/06/18/extracting-schema-org-microdata-using-scrapy-selectors-and-xpath/
> Installation
> ------------
> ::
> pip install extruct
> Usage
> -----
> All-in-one extraction
> +++++++++++++++++++++
> The simplest example how to use extruct is to call
> ``extruct.extract(htmlstring, base_url=base_url)``
> with some HTML string and an optional base URL.
> Let's try this on a webpage that uses all the syntaxes supported (RDFa with `ogp`_).
> First fetch the HTML using python-requests and then feed the response body to ``extruct``::
> >>> import extruct
> >>> import requests
> >>> import pprint
> >>> from w3lib.html import get_base_url
> >>>
> >>> pp = pprint.PrettyPrinter(indent=2)
> >>> r = requests.get('https://www.optimizesmart.com/how-to-use-open-graph-protocol/')
> >>> base_url = get_base_url(r.text, r.url)
> >>> data = extruct.extract(r.text, base_url=base_url)
> >>>
> >>> pp.pprint(data)
> { 'dublincore': [ { 'elements': [ { 'URI': 'http://purl.org/dc/elements/1.1/description',
> 'content': 'What is Open Graph Protocol '
> 'and why you need it? Learn to '
> 'implement Open Graph Protocol '
> 'for Faceb

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

extruct is a Python library for extracting embedded metadata from HTML markup. It supports W3C HTML Microdata, embedded JSON-LD, Microformats via mf2py, Facebook Open Graph, Dublin Core, and experimental RDFa via rdflib.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "7c6748f6c35282e47aec37432506903f78a093c8c63d2afb864d0e169d49a995"
  },
  "primary_domain": "data-engineering",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "data-ingestion",
    "data-transformation"
  ],
  "technologies": [
    "Python",
    "HTML",
    "JSON-LD",
    "RDFa",
    "rdflib",
    "mf2py",
    "w3lib"
  ],
  "summary": "extruct is a Python library for extracting embedded metadata from HTML markup. It supports W3C HTML Microdata, embedded JSON-LD, Microformats via mf2py, Facebook Open Graph, Dublin Core, and experimental RDFa via rdflib.",
  "use_cases": [
    "Extracting structured metadata from web pages",
    "Parsing schema.org and Open Graph data for crawlers or scrapers",
    "Converting embedded HTML metadata into Python data structures"
  ],
  "limitations": [
    "RDFa support is marked experimental",
    "Extraction depends on the metadata being present and well-formed in the HTML"
  ],
  "suggested_terms": [
    "html metadata extraction",
    "json-ld parser",
    "microdata python",
    "open graph python",
    "rdfa extraction"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
