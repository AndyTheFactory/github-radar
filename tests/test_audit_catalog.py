import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_catalog.py"
spec = importlib.util.spec_from_file_location("audit_catalog", SCRIPT)
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)

class AuditCatalogTests(unittest.TestCase):
    def test_flags_discussed_capabilities_without_blocking(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "catalog" / "example"
            folder.mkdir(parents=True)
            bad = {"repository_type": "collection", "summary": "Reading list",
                   "capabilities": ["question-answering"]}
            good = {"repository_type": "library", "summary": "Question answering library",
                    "capabilities": ["question-answering"]}
            for name, data in [("reading", bad), ("software", good)]:
                (folder / f"{name}.md").write_text(
                    "<!-- github-radar:enrichment:start -->\n```json\n"
                    + json.dumps(data) + "\n```\n<!-- github-radar:enrichment:end -->",
                    encoding="utf-8"
                )
            findings = audit_module.audit(root)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0][0].name, "reading.md")
            self.assertIn("question-answering", findings[0][1])

if __name__ == "__main__":
    unittest.main()
