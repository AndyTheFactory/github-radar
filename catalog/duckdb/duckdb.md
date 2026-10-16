---
repository: "duckdb/duckdb"
github_id: 138754790
url: "https://github.com/duckdb/duckdb"
description: "DuckDB is an analytical in-process SQL database management system"
starred_at: "2026-10-16T06:28:54Z"
language: "C++"
topics: ["analytics", "database", "embedded-database", "olap", "sql"]
homepage: "http://www.duckdb.org"
license: "MIT"
archived: false
---

# duckdb/duckdb

DuckDB is an analytical in-process SQL database management system

**GitHub:** https://github.com/duckdb/duckdb

## README excerpt

> ## DuckDB
> DuckDB is a high-performance analytical database system. It is designed to be fast, reliable, portable, and easy to use. DuckDB provides a rich SQL dialect with support far beyond basic SQL. DuckDB supports arbitrary and nested correlated subqueries, window functions, collations, complex types (arrays, structs, maps), and [several extensions designed to make SQL easier to use](https://duckdb.org/docs/current/sql/dialect/friendly_sql.html).
> DuckDB is available as a [standalone CLI application](https://duckdb.org/docs/current/clients/cli/overview) and has clients for [Python](https://duckdb.org/docs/current/clients/python/overview), [R](https://duckdb.org/docs/current/clients/r), [Java](https://duckdb.org/docs/current/clients/java), [Wasm](https://duckdb.org/docs/current/clients/wasm/overview), etc., with deep integrations with packages such as [pandas](https://duckdb.org/docs/guides/python/sql_on_pandas) and [dplyr](https://duckdb.org/docs/current/clients/r#duckplyr-dplyr-api).
> For more information on using DuckDB, please refer to the [DuckDB documentation](https://duckdb.org/docs/current/).
> ## Installation
> If you want to install DuckDB, please see [our installation page](https://duckdb.org/docs/installation/) for instructions.
> ## Data Import
> For CSV files and Parquet files, data import is as simple as referencing the file in the FROM clause:
> SELECT * FROM 'myfile.csv';
> SELECT * FROM 'myfile.parquet';
> Refer to our [Data Import](https://duckdb.org/docs/current/data/overview) section for more information.
> ## SQL Reference
> The documentation contains a [SQL introduction and reference](https://duckdb.org/docs/current/sql/introduction).
> ## Development
> For development, DuckDB requires [CMake](https://cmake.org), Python 3 and a `C++17` compliant compiler. In the root directory, run `make` to compile the sources. For development, use `make debug` to build a non-optimized debug version. You should run `make unit` and `make allunit` to verify that your version works properly after making changes. To test performance, you can run `BUILD_BENCHMARK=1 BUILD_TPCH=1 make` and then perform several standard benchmarks from the root directory by executing `./build/release/benchmark/benchmark_runner`. The details of benchmarks are in our [Benchmark Guide](benchmark/README.md).
> Please also refer to our [Build Guide](https://duckdb.org/docs/current/dev/building/overview) and [Contribution Guide](CONTRIBUTING.md).
> ## Support
> See the [Support Options](https://duckla

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

DuckDB is an in-process analytical SQL database management system written in C++, with clients for Python, R, Java, and Wasm. It supports nested correlated subqueries, window functions, and direct querying of CSV and Parquet files. It is also available as a standalone CLI application.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "0961e3ffdd3666337d39955e6a5701e5d1ed85097dff7000c4f7bad03e23b1dd"
  },
  "primary_domain": "databases",
  "secondary_domains": [
    "data-engineering"
  ],
  "repository_type": "library",
  "capabilities": [
    "database-management",
    "data-transformation",
    "data-ingestion",
    "question-answering"
  ],
  "technologies": [
    "C++",
    "SQL",
    "CMake",
    "Python",
    "R",
    "Java",
    "WebAssembly",
    "Parquet"
  ],
  "summary": "DuckDB is an in-process analytical SQL database management system written in C++, with clients for Python, R, Java, and Wasm. It supports nested correlated subqueries, window functions, and direct querying of CSV and Parquet files. It is also available as a standalone CLI application.",
  "use_cases": [
    "Embedded analytical queries inside applications",
    "Running SQL directly over CSV and Parquet files",
    "Analytics on pandas or dplyr data frames"
  ],
  "limitations": [
    "README excerpt is truncated, so full feature coverage is unverified",
    "Analytical (OLAP) focus rather than high-concurrency transactional workloads"
  ],
  "suggested_terms": [
    "embedded SQL database",
    "OLAP",
    "DuckDB",
    "analytical database",
    "Parquet query"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
