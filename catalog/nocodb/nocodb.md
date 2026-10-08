---
repository: "nocodb/nocodb"
github_id: 108761645
url: "https://github.com/nocodb/nocodb"
description: "🔥 🔥 🔥 A Free & Self-hostable Airtable Alternative"
starred_at: "2024-01-16T14:54:51Z"
language: "TypeScript"
topics: ["airtable", "airtable-alternative", "automatic-api", "hacktoberfest", "low-code", "no-code", "no-code-database", "no-code-platform", "postgresql", "rest-api", "restful-api", "spreadsheet", "sqlite", "swagger"]
homepage: "https://nocodb.com"
license: "NOASSERTION"
archived: false
---

# nocodb/nocodb

🔥 🔥 🔥 A Free & Self-hostable Airtable Alternative

**GitHub:** https://github.com/nocodb/nocodb

## README excerpt

> NocoDB is the fastest and easiest way to build databases online.
>
>
>
> [](markdown/readme/languages/chinese.md)
> [](markdown/readme/languages/french.md)
> [](markdown/readme/languages/german.md)
> [](markdown/readme/languages/spanish.md)
> [](markdown/readme/languages/portuguese.md)
> [](markdown/readme/languages/italian.md)
> [](markdown/readme/languages/japanese.md)
> [](markdown/readme/languages/korean.md)
> [](markdown/readme/languages/russian.md)
> [](markdown/readme/languages/bengali.md)
> See other languages »
> # Join Our Community
> # Installation
> ## Docker with SQLite
> docker run -d \
> --name noco \
> -v "$(pwd)"/nocodb:/usr/app/data/ \
> -p 8080:8080 \
> nocodb/nocodb:latest
> ## Docker with PG
> docker run -d \
> --name noco \
> -v "$(pwd)"/nocodb:/usr/app/data/ \
> -p 8080:8080 \
> -e NC_DB="pg://host.docker.internal:5432?u=root&p=password&d=d1" \
> -e NC_AUTH_JWT_SECRET="569a1821-0a93-45e8-87ab-eb857f20a010" \
> nocodb/nocodb:latest
> ## Auto-upstall
> Auto-upstall is a single command that sets up NocoDB on a server for production usage.
> Behind the scenes it auto-generates docker-compose for you.
> bash <(curl -sSL http://install.nocodb.com/noco.sh) <(mktemp)
> Auto-upstall does the following: 🕊
> - 🐳 Automatically installs all pre-requisites like docker, docker-compose
> - 🚀 Automatically installs NocoDB with PostgreSQL, Redis, Traefik gateway using Docker Compose. 🐘 🗄️ 🌐
> - 🔄 Automatically upgrades NocoDB to the latest version when you run the command again.
> - 🔒 Automatically setups SSL and also renews it. Needs a domain or subdomain as input while installation.
> > install.nocodb.com/noco.sh script can be found [here in our github](https://raw.githubusercontent.com/nocodb/nocodb/develop/docker-compose/1_Auto_Upstall/noco.sh)
> ## Other Methods
> > Binaries are only for quick testing locally.
> | Install Method                | Command to install                                                                                                                                                                                                                                                                                                                                                         |
> |-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

NocoDB is a self-hostable, spreadsheet-style interface that turns databases into online, no-code databases, positioned as an Airtable alternative. The README describes Docker-based installation with SQLite or PostgreSQL and an automated production setup script. Repository topics also reference an automatic REST API and Swagger documentation.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "7ae47344fbd8893da7d0896da49c0160079d295303a0724a1a798501863148ea"
  },
  "primary_domain": "databases",
  "secondary_domains": [
    "applications",
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "database-management",
    "api-integration",
    "storage",
    "authentication",
    "deployment"
  ],
  "technologies": [
    "TypeScript",
    "Docker",
    "PostgreSQL",
    "SQLite",
    "REST API",
    "Swagger",
    "Redis",
    "Traefik"
  ],
  "summary": "NocoDB is a self-hostable, spreadsheet-style interface that turns databases into online, no-code databases, positioned as an Airtable alternative. The README describes Docker-based installation with SQLite or PostgreSQL and an automated production setup script. Repository topics also reference an automatic REST API and Swagger documentation.",
  "use_cases": [
    "Building no-code databases and spreadsheet-style apps",
    "Self-hosting an Airtable alternative",
    "Exposing database tables through an automatic REST API"
  ],
  "limitations": [
    "License is listed as NOASSERTION in the metadata, so terms should be verified",
    "Auto-upstall script requires a domain for SSL setup",
    "Binary installation is documented only for quick local testing"
  ],
  "suggested_terms": [
    "airtable alternative",
    "no-code database",
    "self-hosted spreadsheet database",
    "automatic REST API",
    "low-code platform"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
