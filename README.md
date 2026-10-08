# GitHub Radar

A searchable archive of repositories starred by [@AndyTheFactory](https://github.com/AndyTheFactory).

**Capture:** star a repository on GitHub, then close the tab. An hourly GitHub Action imports it into this repository.

**Browse:** open [CATALOG.md](CATALOG.md) or the [catalog/](catalog/) directory.

**Search:** use GitHub Code Search with `repo:AndyTheFactory/github-radar` plus terms such as `agent orchestration`, `evaluation`, or `OCR`. Indexing new files may take some time.

## How it works

- Each starred repository is written once to `catalog/<owner>/<repo>.md`.
- Entries contain metadata and a short, searchable excerpt of the upstream README where available.
- Existing entries are **never overwritten**: manual edits and notes are safe.
- Removing a star does **not** delete an archived entry.
- Each run imports up to 50 new repositories, newest first. Repeated runs gradually backfill older stars.
- Sync checks all star pages, so it does not rely on a fragile timestamp checkpoint.
- No LLM key, database, or third-party dependencies are necessary.

## Running it

From [Actions → Sync starred repositories](https://github.com/AndyTheFactory/github-radar/actions/workflows/sync.yml), choose **Run workflow** to begin the initial import. Subsequent imports run hourly (GitHub may delay scheduled jobs).

Or run locally (Python 3.11+):

```bash
export GH_TOKEN="$(gh auth token)"
python scripts/sync.py --user AndyTheFactory --max-new 50
python -m unittest discover -s tests -v
```

Local sync writes files but does not commit them. To backfill faster, repeat with a larger `--max-new`.

## Data and privacy

This is a **public** catalog of public starred repositories. It may reflect your interests and approximate discovery dates. Don't put internal client details or private notes into public entries.

The catalog is useful without AI-generated summaries. A future optional enrichment step could add concise capability descriptions to new entries without modifying personal notes.
