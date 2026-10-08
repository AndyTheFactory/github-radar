import importlib.util
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "enrich.py"
spec = importlib.util.spec_from_file_location("radar_enrich", SCRIPT)
radar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(radar)

def model(name, multiplier=None, prices=None):
    billing = None if multiplier is None and prices is None else SimpleNamespace(multiplier=multiplier, token_prices=prices)
    return SimpleNamespace(id=name, billing=billing)

class EnrichTests(unittest.TestCase):
    def test_no_model_lookup_for_auto(self):
        self.assertEqual(radar.select_model([], "auto")[0], "auto")

    def test_choose_lowest_multiplier_from_live_models(self):
        models = [model("auto"), model("expensive", 2), model("cheap", 0.25), model("medium", 0.5)]
        self.assertEqual(radar.select_model(models, "cheapest")[0], "cheap")

    def test_no_implicit_fallback(self):
        with self.assertRaises(RuntimeError):
            radar.select_model([model("unpriced")], "cheapest")
        with self.assertRaises(ValueError):
            radar.select_model([model("named", 1)], "nonexistent")

    def test_token_price_fallback(self):
        prices_a = SimpleNamespace(batch_size=1000, input_price=1, output_price=2)
        prices_b = SimpleNamespace(batch_size=1000, input_price=2, output_price=3)
        self.assertEqual(radar.select_model([model("b", prices=prices_b), model("a", prices=prices_a)], "cheapest")[0], "a")

    def test_unknown_capabilities_are_dropped_before_validation(self):
        allowed = {"domains": {"developer-tools"}, "repository_types": {"application"}, "capabilities": {"testing"}}
        original = {"primary_domain": "developer-tools", "repository_type": "application",
                    "secondary_domains": [], "capabilities": ["testing", "made-up", "testing"],
                    "technologies": [], "summary": "A test tool.", "use_cases": [],
                    "limitations": [], "suggested_terms": [], "confidence": "medium"}
        cleaned = radar.clean_capabilities(original, allowed)
        self.assertEqual(cleaned["capabilities"], ["testing"])
        self.assertEqual(original["capabilities"], ["testing", "made-up", "testing"])
        radar.validate(cleaned, allowed)

    def test_validation_and_preserve_notes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "catalog" / "other").mkdir(parents=True)
            entry = root / "catalog" / "other" / "interesting.md"
            entry.write_text("# Repo\n\n## Personal notes\nKeep this.\n", encoding="utf-8")
            self.assertEqual(radar.pending(root), [entry])
            allowed = {"domains": {"developer-tools", "other"}, "repository_types": {"application"}, "capabilities": {"testing"}}
            data = {"primary_domain": "developer-tools", "repository_type": "application", "secondary_domains": [],
                    "capabilities": ["testing"], "technologies": ["python"], "summary": "A test runner.",
                    "use_cases": [], "limitations": [], "suggested_terms": [], "confidence": "high"}
            radar.validate(data, allowed)
            self.assertTrue(radar.apply(entry, data, "cheap"))
            self.assertFalse(radar.apply(entry, data, "cheap"))
            self.assertIn("Keep this.", entry.read_text())
            self.assertEqual(radar.pending(root), [])
            data["capabilities"] = ["unapproved"]
            with self.assertRaises(ValueError):
                radar.validate(data, allowed)

if __name__ == "__main__":
    unittest.main()
