---
repository: "pydantic/pydantic"
github_id: 90194616
url: "https://github.com/pydantic/pydantic"
description: "Data validation using Python type hints"
starred_at: "2026-10-09T14:07:48Z"
language: "Python"
topics: ["hints", "json-schema", "parsing", "pydantic", "python", "python310", "python311", "python312", "python313", "python39", "validation"]
homepage: "https://pydantic.dev/docs/validation"
license: "MIT"
archived: false
---

# pydantic/pydantic

Data validation using Python type hints

**GitHub:** https://github.com/pydantic/pydantic

## README excerpt

> # Pydantic Validation
> Data validation using Python type hints.
> Fast and extensible, Pydantic plays nicely with your linters/IDE/brain.
> Define how data should be in pure, canonical Python 3.10+; validate it with Pydantic.
> ## Pydantic Logfire :fire:
> We've launched Pydantic Logfire to help you monitor your applications.
> [Learn more](https://pydantic.dev/logfire/?utm_source=pydantic_validation)
> ## Pydantic V1.10 vs. V2
> Pydantic V2 is a ground-up rewrite that offers many new features, performance improvements, and some breaking changes compared to Pydantic V1.
> If you're using Pydantic V1 you may want to look at the
> [pydantic V1.10 Documentation](https://pydantic.dev/docs/validation/1.10/overview/) or,
> [`1.10.X-fixes` git branch](https://github.com/pydantic/pydantic/tree/1.10.X-fixes). Pydantic V2 also ships with the latest version of Pydantic V1 built in so that you can incrementally upgrade your code base and projects: `from pydantic import v1 as pydantic_v1`.
> ## Help
> See [documentation](https://pydantic.dev/docs/validation/latest/get-started/) for more details.
> ## Installation
> Install using `pip install -U pydantic` or `conda install pydantic -c conda-forge`.
> For more installation options to make Pydantic even faster,
> see the [Install](https://pydantic.dev/docs/validation/latest/get-started/install/) section in the documentation.
> ## A Simple Example
> from datetime import datetime
> from typing import Optional
> from pydantic import BaseModel
> class User(BaseModel):
> id: int
> name: str = 'John Doe'
> signup_ts: Optional[datetime] = None
> friends: list[int] = []
> external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
> user = User(**external_data)
> print(user)
> #> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
> print(user.id)
> #> 123
> ## Contributing
> For guidance on setting up a development environment and how to make a
> contribution to Pydantic, see
> [Contributing to Pydantic](https://pydantic.dev/docs/validation/latest/get-started/contributing/).
> ## Reporting a Security Vulnerability
> See our [security policy](https://github.com/pydantic/pydantic/security/policy).

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Pydantic is a Python library for data validation and parsing using type hints, with a V2 rewrite and a bundled V1.10 compatibility module. The README describes a BaseModel-based example that coerces external data into typed Python objects.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "c7611c880e191457ed1f8d6eedaf1d90cfd0afa05d9a1a2df93863e500bab853"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "data-engineering"
  ],
  "repository_type": "library",
  "capabilities": [
    "data-validation",
    "data-transformation"
  ],
  "technologies": [
    "Python",
    "JSON Schema"
  ],
  "summary": "Pydantic is a Python library for data validation and parsing using type hints, with a V2 rewrite and a bundled V1.10 compatibility module. The README describes a BaseModel-based example that coerces external data into typed Python objects.",
  "use_cases": [
    "Validating and parsing external data such as API payloads or configuration into typed Python models",
    "Generating JSON Schema from Python type definitions"
  ],
  "limitations": [
    "Pydantic V1 is legacy; V2 contains breaking changes relative to V1",
    "Requires Python 3.10+ according to the README"
  ],
  "suggested_terms": [
    "pydantic",
    "python data validation",
    "type hints parsing",
    "json schema python",
    "BaseModel"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
