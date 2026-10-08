---
repository: "OpenAPITools/openapi-diff"
github_id: 113924383
url: "https://github.com/OpenAPITools/openapi-diff"
description: "Utility for comparing two OpenAPI specifications."
starred_at: "2026-10-08T20:16:50Z"
language: "Java"
topics: ["api", "diff", "openapi", "openapi-diff", "openapi-specification", "openapi3", "swagger"]
homepage: ""
license: "Apache-2.0"
archived: false
---

# OpenAPITools/openapi-diff

Utility for comparing two OpenAPI specifications.

**GitHub:** https://github.com/OpenAPITools/openapi-diff

## README excerpt

> # OpenAPI-diff
> Compare two OpenAPI specifications (3.x) and render the difference to HTML plain text, Markdown files, or JSON files.
> # Requirements
> * Java 8
> # Feature
> * Supports OpenAPI spec v3.0.
> * In-depth comparison of parameters, responses, endpoint, http method (GET,POST,PUT,DELETE...)
> * Supports swagger api Authorization
> * Render difference of property with Expression Language
> * HTML, Markdown, Asciidoc & JSON render
> # Maven
> Available on [Maven Central](https://search.maven.org/artifact/org.openapitools.openapidiff/openapi-diff-core)
>
> org.openapitools.openapidiff
> openapi-diff-core
> ${openapi-diff-version}
>
> # Homebrew
> Available for Mac users on [brew](https://formulae.brew.sh/formula/openapi-diff)
> brew install openapi-diff
> Usage instructions in [Usage -> Command line](#command-line)
> # Docker
> Available on [Docker Hub](https://hub.docker.com/r/openapitools/openapi-diff/) as `openapitools/openapi-diff`.
> # docker run openapitools/openapi-diff:latest
> usage: openapi-diff
> --asciidoc            export diff as asciidoc in given file
> --debug                     Print debugging information
> --error                     Print error information
> --fail-on-changed           Fail if API changed but is backward
> compatible
> --fail-on-incompatible      Fail only if API changes broke backward
> compatibility
> --config-file               Config file to override default behavior. Supported file formats: .yaml
> --config-prop               Config property to override default behavior with key:value format (e.g. my.prop:true)
> -h,--help                      print this message
> --header    use given header for authorisation
> --html                export diff as html in given file
> --info                      Print additional information
> --json                export diff as json in given file
> -l,--log                use given level for log (TRACE, DEBUG,
> INFO, WARN, ERROR, OFF). Default: ERROR
> --markdown            export diff as markdown in given file
> --off                       No information printed
> --query     use query param for authorisation
> --state                     Only output diff state: no_changes,
> incompatible, compatible
> --text                export diff as text in given file
> --trace                     be extra verbose
> --version                   print the version information and exit
> --warn                      Print warning information
> ## Build the image
> This is only required if you want to try new changes in the Dockerfile of this project.
> docker build -t local-openapi-di

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Utility for comparing two OpenAPI specifications (3.x) and rendering the differences as HTML, Markdown, AsciiDoc, text, or JSON. It supports comparison of parameters, responses, endpoints, and HTTP methods, and can be run as a Maven library, CLI, or Docker image.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "59c289189a53b74a0e7fb4e50b8333067f7a019d0969f1db7b620afb25c944c1"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "applications"
  ],
  "repository_type": "application",
  "capabilities": [
    "api-integration",
    "static-analysis",
    "reporting",
    "data-evaluation"
  ],
  "technologies": [
    "Java",
    "Maven",
    "Docker",
    "OpenAPI",
    "Swagger",
    "Homebrew"
  ],
  "summary": "Utility for comparing two OpenAPI specifications (3.x) and rendering the differences as HTML, Markdown, AsciiDoc, text, or JSON. It supports comparison of parameters, responses, endpoints, and HTTP methods, and can be run as a Maven library, CLI, or Docker image.",
  "use_cases": [
    "Detecting breaking changes between API spec versions",
    "Generating HTML or Markdown change reports for API reviews",
    "Gating CI pipelines on backward compatibility with --fail-on-incompatible"
  ],
  "limitations": [
    "Supports only OpenAPI 3.x (README states spec v3.0 support)",
    "Requires Java 8 or later for library/CLI use",
    "Documented feature list does not describe behavior for Swagger 2.0 specs"
  ],
  "suggested_terms": [
    "openapi diff",
    "api breaking changes",
    "openapi compatibility check",
    "swagger diff",
    "api spec comparison"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
