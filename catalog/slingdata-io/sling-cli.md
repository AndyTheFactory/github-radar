---
repository: "slingdata-io/sling-cli"
github_id: 304285216
url: "https://github.com/slingdata-io/sling-cli"
description: "Sling is a CLI tool that extracts data from a source storage/database and loads it in a target storage/database."
starred_at: "2026-10-16T06:26:59Z"
language: "Go"
topics: ["elt", "etl", "extract", "load"]
homepage: "https://docs.slingdata.io"
license: "GPL-3.0"
archived: false
---

# slingdata-io/sling-cli

Sling is a CLI tool that extracts data from a source storage/database and loads it in a target storage/database.

**GitHub:** https://github.com/slingdata-io/sling-cli

## README excerpt

> Slings from a data source to a data target.
> See docs.slingdata.io for more details.
>
>
> Sling is a passion project turned into a free CLI Product which offers an easy solution to create and maintain small to medium volume data pipelines using the Extract & Load (EL) approach. It focuses on data movement between:
> * Database to Database
> * File System to Database
> * Database to File System
> * API to Database
> * API to File System
> https://github.com/slingdata-io/sling-cli/assets/7671010/e10ee716-1de8-4d53-8eb2-95c6d9d7f9f0
> Some key features:
> - Single Binary deployment (built with Go). See [installation](https://docs.slingdata.io/sling-cli/getting-started) page.
> - Use Custom SQL as a stream: `--src-stream='select * from my_table where col1 > 10'`
> - Manage / View / Test / Discover your connections with the [`sling conns`](https://docs.slingdata.io/sling-cli/environment#managing-connections) sub-command
> - Use Environment Variable as connections if you prefer (`export MY_PG='postgres//...`)'
> - Provide YAML or JSON configurations (perfect for git version control).
> - Powerful [Replication](https://docs.slingdata.io/sling-cli/run/configuration/replication) logic, to replication many tables with a wildcard (`my_schema.*`).
> - Reads your existing [DBT connections](https://docs.slingdata.io/sling-cli/environment#dbt-profiles-dbt-profiles.yml)
> - Use your environment variable in your YAML / JSON config (`select * from my_table where date = '{date}'`)
> - Convenient [Transformations](https://docs.slingdata.io/sling-cli/run/configuration/transformations), such as the `flatten` option, which auto-creates columns from your nested fields.
> - Run Pre & Post SQL commands.
> - many more!
> ---
> Example [Replication](https://docs.slingdata.io/sling-cli/run/configuration/replication):
>
> ---
> Available Connectors:
> - **Databases**: [`adbc`](https://docs.slingdata.io/connections/database-connections/adbc) [`azuredwh`](https://docs.slingdata.io/connections/database-connections/azuredwh) [`azuresql`](https://docs.slingdata.io/connections/database-connections/azuresql) [`azuretable`](https://docs.slingdata.io/connections/database-connections/azuretable) [`bigquery`](https://docs.slingdata.io/connections/database-connections/bigquery) [`bigtable`](https://docs.slingdata.io/connections/database-connections/bigtable) [`clickhouse`](https://docs.slingdata.io/connections/database-connections/clickhouse) [`d1`](https://docs.slingdata.io/connections/database-connections/d1) [`databricks`](https://docs.slingda

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Sling is a Go-based CLI tool for extract-and-load (EL) data pipelines, moving data between databases, file systems, and APIs. It supports YAML/JSON configuration, replication with wildcards, custom SQL streams, and connection management.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "934d134c0d2fc27da5ed361efbfa27bbddc4bb8e0647bfb450ca0f20f489267c"
  },
  "primary_domain": "data-engineering",
  "secondary_domains": [
    "databases",
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "data-ingestion",
    "data-transformation",
    "storage",
    "api-integration",
    "workflow-orchestration"
  ],
  "technologies": [
    "Go",
    "YAML",
    "JSON",
    "SQL",
    "ADBC",
    "BigQuery",
    "ClickHouse",
    "Databricks"
  ],
  "summary": "Sling is a Go-based CLI tool for extract-and-load (EL) data pipelines, moving data between databases, file systems, and APIs. It supports YAML/JSON configuration, replication with wildcards, custom SQL streams, and connection management.",
  "use_cases": [
    "Replicating tables between databases on a schedule",
    "Loading file or API data into a database",
    "Exporting database tables to files"
  ],
  "limitations": [
    "Described as suited to small to medium volume pipelines",
    "Focuses on extract and load rather than full transformation",
    "Licensed GPL-3.0"
  ],
  "suggested_terms": [
    "sling cli",
    "elt tool",
    "database replication cli",
    "data pipeline go",
    "etl command line"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
