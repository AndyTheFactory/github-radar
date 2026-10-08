# Agent instructions

This repository is a public, searchable catalog of GitHub repositories starred by AndyTheFactory.

- Treat files under `catalog/<owner>/<repo>.md` as the primary records.
- The original repository URL, description, README excerpt and topics are source metadata, not verified claims.
- Never invent repository capabilities or imply that the user has personally evaluated the repositories.
- The sync workflow creates missing records but intentionally does not rewrite existing entries.
- Do not remove catalog records when repositories are unstarred; this is a historical archive.
- Preserve the `## Personal notes` section when editing entries.
- Do not add private client/project information to this public repository.
- `CATALOG.md` is a generated browsing index; regenerate it using `scripts/sync.py` rather than editing directly.
- Search questions can be answered by searching catalog entries and explaining which repositories seem relevant, with links to the saved entries and originals.
