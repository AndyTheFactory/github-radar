# GitHub Radar

A searchable archive of repositories starred by [@AndyTheFactory](https://github.com/AndyTheFactory).

**Capture:** star a repository on GitHub, then close the tab. A twice-daily GitHub Action imports it into this repository.

**Browse:** start with the [human-readable catalog](browse/README.md), or inspect [CATALOG.md](CATALOG.md) and the raw [catalog/](catalog/) entries.

**Search:** use GitHub Code Search with `repo:AndyTheFactory/github-radar` plus terms such as `agent orchestration`, `evaluation`, or `OCR`. Indexing new files may take some time.

## Deterministic browse pages\n\n`python scripts/build_browse.py` generates [browse/README.md](browse/README.md), subject pages under `browse/domains/`, [types](browse/types.md), and an [alphabetical directory](browse/all.md). These pages are rebuilt after each sync and enrichment; they require no model, network calls, or extra dependencies. Repositories awaiting classification appear in Unclassified with their original descriptions. Do not edit generated browse pages manually.\n\n## How it works

- Each starred repository is written once to `catalog/<owner>/<repo>.md`.
- Entries contain metadata and a short, searchable excerpt of the upstream README where available.
- Existing entries are **never overwritten**: manual edits and notes are safe.
- Removing a star does **not** delete an archived entry.
- Repositories owned by **AndyTheFactory** are excluded; any previously imported entries under that owner are removed on the next sync.
- Each run imports up to 50 new repositories, newest first. Repeated runs gradually backfill older stars.
- Sync checks all star pages, so it does not rely on a fragile timestamp checkpoint.
- No LLM key, database, or third-party dependencies are necessary.

## Running it

From [Actions → Sync starred repositories](https://github.com/AndyTheFactory/github-radar/actions/workflows/sync.yml), choose **Run workflow** to begin the initial import. Subsequent imports run at 00:00 and 14:00 fixed EET (UTC+2; GitHub may delay scheduled jobs).

Or run locally (Python 3.11+):

```bash
export GH_TOKEN="$(gh auth token)"
python scripts/sync.py --user AndyTheFactory --max-new 50
python -m unittest discover -s tests -v
```

Local sync writes files but does not commit them. To backfill faster, repeat with a larger `--max-new`.

## Optional GitHub Copilot enrichment

The regular sync imports stars without requiring Copilot. After import, Actions checks for entries without a generated summary. If there are none, the Copilot SDK is **not installed or invoked**.

To enable enrichment:

1. Create a GitHub personal access token with Copilot Requests permission, associated with an account that can use Copilot.
2. Set repository **Actions secret** `COPILOT_TOKEN` under Settings → Secrets and variables → Actions.
3. Set the optional **Actions repository variable** `COPILOT_MODEL` to one of:
   - `cheapest` (default): query the Copilot SDK model API and pick the lowest known premium-request multiplier; where multipliers are unavailable, compare estimated AI-credit token prices. If pricing cannot be queried, **fail without a costly fallback**.
   - `auto`: let Copilot select the model according to your plan and policies; it is **not necessarily cheapest**.
   - An explicit model ID (for example `claude-haiku-4.5`): use that model only; fail if unavailable.

Each scheduled run (00:00 and 14:00 **fixed EET**, UTC+02:00) processes at most **10 unenriched entries**. A manual **Run workflow** exposes an `enrichment_limit` input (default **100**, allowed **1–100**) for backfilling; it never processes more than 100 enrichments in one run. Importing remains functional without the Copilot secret. Individual failed entries stay pending, and successful entries are retained. Nothing triggers Copilot when all records are already enriched. Expect usage of your Copilot entitlement and possible AI-credit charges.

You can preview the pending queue without a token:

```bash
python scripts/enrich.py --dry-run
```

The enrichment output is stored in an explicitly machine-managed block at the bottom of each Markdown entry. Reprocessing an enriched entry is not automatic; manual notes are preserved. The taxonomy is specified in [taxonomy.yaml](taxonomy.yaml) and [CLASSIFICATION.md](CLASSIFICATION.md).

## Data and privacy

This is a **public** catalog of public starred repositories. It may reflect your interests and approximate discovery dates. Don't put internal client details or private notes into public entries.

The catalog is useful without AI-generated summaries. Copilot enrichment is optional, and requires the repository secret described above.
