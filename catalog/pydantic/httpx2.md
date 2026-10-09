---
repository: "pydantic/httpx2"
github_id: 1235232619
url: "https://github.com/pydantic/httpx2"
description: "A next generation HTTP client for Python. 🦋"
starred_at: "2026-10-09T14:12:09Z"
language: "Python"
topics: []
homepage: "https://pydantic.dev/docs/httpx2/"
license: "BSD-3-Clause"
archived: false
---

# pydantic/httpx2

A next generation HTTP client for Python. 🦋

**GitHub:** https://github.com/pydantic/httpx2

## README excerpt

> HTTPX2
> A next-generation HTTP client for Python.
>
>
> HTTPX2 is a fully featured HTTP client library for Python. It includes **an integrated command line client**, has support for both **HTTP/1.1 and HTTP/2**, and provides both **sync and async APIs**.
> > [!NOTE]
> > HTTPX2 is a continuation of the wonderful work started by [@lovelydinosaur](https://github.com/lovelydinosaur) and the broader HTTPX community. We're enormously grateful for everything that has gone into HTTPX over the years - it has been a foundational piece of the modern Python ecosystem, and this project would not exist without it.
> >
> > With HTTPX itself seeing limited activity recently, Pydantic is picking up stewardship under the HTTPX2 name so that users have a reliably maintained path forward - including timely security updates for a library that sits in the critical path of so many production systems. Our aim is to honour the original project's design, keep it stable for everyone relying on it, and continue evolving it carefully. Thank you to [@lovelydinosaur](https://github.com/lovelydinosaur) and every past contributor for laying such a strong foundation. 💙
> ---
> Install HTTPX2 using pip:
> pip install httpx2
> Now, let's get started:
> >>> import httpx2
> >>> r = httpx2.get('https://www.example.org/')
> >>> r
>
> >>> r.status_code
> 200
> >>> r.headers['content-type']
> 'text/html; charset=UTF-8'
> >>> r.text
> '\n\n\nExample Domain...'
> Or, using the command-line client.
> pip install 'httpx2[cli]'  # The command line client is an optional dependency.
> Which now allows us to use HTTPX2 directly from the command-line:
> httpx2 --help
> ## Features
> HTTPX2 builds on the well-established usability of `requests`, and gives you:
> * A broadly [requests-compatible API](https://pydantic.dev/docs/httpx2/guides/compatibility/).
> * An integrated command-line client.
> * HTTP/1.1 [and HTTP/2 support](https://pydantic.dev/docs/httpx2/guides/http2/).
> * Standard synchronous interface, but with [async support if you need it](https://pydantic.dev/docs/httpx2/guides/async/).
> * Ability to make requests directly to [WSGI applications](https://pydantic.dev/docs/httpx2/advanced/transports/#wsgi-transport) or [ASGI applications](https://pydantic.dev/docs/httpx2/advanced/transports/#asgi-transport).
> * Strict timeouts everywhere.
> * Fully type annotated.
> * 100% test coverage.
> Plus all the standard features of `requests`...
> * International Domains and URLs
> * Keep-Alive & Connection Pooling
> * Sessions with Cookie Persistence
> * Browser-style SSL Verifica

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

HTTPX2 is a Python HTTP client library offering sync and async APIs, HTTP/1.1 and HTTP/2 support, and an optional integrated command-line client. The README describes it as a requests-compatible successor to HTTPX maintained by Pydantic.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "6ec5246ed0543756b92a8a4b39180750a98b283af52962bc5aaab09b61b97d09"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "infrastructure"
  ],
  "repository_type": "library",
  "capabilities": [
    "api-integration",
    "networking"
  ],
  "technologies": [
    "Python",
    "HTTP/1.1",
    "HTTP/2",
    "ASGI",
    "WSGI"
  ],
  "summary": "HTTPX2 is a Python HTTP client library offering sync and async APIs, HTTP/1.1 and HTTP/2 support, and an optional integrated command-line client. The README describes it as a requests-compatible successor to HTTPX maintained by Pydantic.",
  "use_cases": [
    "Making HTTP requests from Python applications with sync or async code",
    "Sending requests directly to WSGI or ASGI applications for testing",
    "Issuing HTTP requests from the command line via the optional CLI extra"
  ],
  "limitations": [
    "Requests-compatibility is described as broad, not complete",
    "Command-line client is an optional install (httpx2[cli])",
    "Documentation and feature claims are taken from the README excerpt and were not verified"
  ],
  "suggested_terms": [
    "python http client",
    "http2 python",
    "async http library",
    "requests alternative",
    "httpx"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
