import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync.py"
spec = importlib.util.spec_from_file_location("radar_sync", SCRIPT)
radar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(radar)


class SyncTests(unittest.TestCase):
    def test_safe_paths(self):
        self.assertEqual(radar.catalog_path("some-owner/cool.repo"), radar.CATALOG / "some-owner" / "cool.md")
        for name in ("../escape", "one", "one/two/three", "one/../evil"):
            with self.assertRaises(ValueError):
                radar.catalog_path(name)

    def test_render_searchable(self):
        repo = {"id": 123, "full_name": "owner/tool", "description": "Agent orchestration", "topics": ["agents"]}
        result = radar.render(repo, "2026-10-08T12:00:00Z", "# Tool\nMulti-agent delegation tools")
        self.assertIn("Agent orchestration", result)
        self.assertIn("Multi-agent delegation", result)
        self.assertIn("## Personal notes", result)
        self.assertIn("github_id: 123", result)

    def test_idempotent_archive(self):
        repo = {"id": 1, "full_name": "owner/tool", "description": "Useful tool"}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(radar, "CATALOG", root / "catalog"), patch.object(radar, "INDEX", root / "CATALOG.md"):
                with patch.object(radar, "iter_stars", return_value=iter([(repo, None)])), patch.object(radar, "api_get", return_value="# Readme"):
                    first = radar.sync("tester", "", max_new=50)
                self.assertEqual(first, (1, 1))
                path = radar.catalog_path("owner/tool")
                path.write_text(path.read_text() + "\nMy notes stay here.\n")
                with patch.object(radar, "iter_stars", return_value=iter([(repo, None)])), patch.object(radar, "api_get") as api:
                    second = radar.sync("tester", "", max_new=50)
                self.assertEqual(second, (0, 1))
                api.assert_not_called()
                self.assertIn("My notes stay here.", path.read_text())
                self.assertIn("owner/tool", (root / "CATALOG.md").read_text())


if __name__ == "__main__":
    unittest.main()
