import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_browse.py"
spec = importlib.util.spec_from_file_location("build_browse", SCRIPT)
browse = importlib.util.module_from_spec(spec)
spec.loader.exec_module(browse)


class BrowseTests(unittest.TestCase):
    def test_deterministic_generation_and_fallbacks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "catalog" / "someone").mkdir(parents=True)
            (root / "catalog" / "AndyTheFactory").mkdir()
            (root / "taxonomy.yaml").write_text(
                'domains:\n  developer-tools: "Developer Tools"\n'
                'repository_types:\n  application: "Application"\n', encoding="utf-8"
            )
            info = {
                "primary_domain": "developer-tools", "repository_type": "application",
                "summary": "A useful terminal tool.", "capabilities": ["automation"]
            }
            (root / "catalog" / "someone" / "useful.md").write_text(
                '---\nrepository: "someone/useful"\ndescription: "Original"\n---\n'
                + browse.START + '\n```json\n' + json.dumps(info)
                + '\n```\n' + browse.END, encoding="utf-8"
            )
            (root / "catalog" / "someone" / "plain.md").write_text(
                '---\ndescription: "A simple utility"\n---\n', encoding="utf-8"
            )
            (root / "catalog" / "AndyTheFactory" / "own.md").write_text(
                '---\ndescription: "Should not be indexed"\n---\n', encoding="utf-8"
            )
            browse.build(root)
            output = root / "browse"
            overview = (output / "README.md").read_text()
            self.assertIn("2 repositories", overview)
            self.assertIn("Developer Tools", overview)
            self.assertIn("**[plain](https://github.com/someone/plain)** <sub>someone</sub>", (output / "all.md").read_text())
            self.assertNotIn("AndyTheFactory/own", (output / "all.md").read_text())
            self.assertIn("## P", (output / "all.md").read_text())
            self.assertIn("| Subject | Repositories |", overview)
            self.assertIn("## Apps & command-line tools", (output / "domains" / "developer-tools.md").read_text())
            self.assertIn("[catalog entry](../../catalog/someone/useful.md)", (output / "domains" / "developer-tools.md").read_text())
            self.assertIn("A useful terminal tool.", (output / "domains" / "developer-tools.md").read_text())
            first = {str(p.relative_to(output)): p.read_bytes() for p in output.rglob("*.md")}
            browse.build(root)
            second = {str(p.relative_to(output)): p.read_bytes() for p in output.rglob("*.md")}
            self.assertEqual(first, second)

if __name__ == "__main__":
    unittest.main()
