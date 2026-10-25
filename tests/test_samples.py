from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from samples.data_quality import profile_records
from samples.dependency_graph import DependencyCycleError, topological_order
from samples.integrity import build_manifest, verify_manifest


class IntegrityTests(unittest.TestCase):
    def test_manifest_is_stable_and_detects_change(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "a.txt").write_text("alpha", encoding="utf-8")
            (root / "b.txt").write_text("beta", encoding="utf-8")
            manifest = build_manifest(root)

            self.assertEqual(list(manifest), ["a.txt", "b.txt"])
            self.assertEqual(
                verify_manifest(root, manifest),
                {"missing": [], "changed": [], "unexpected": []},
            )

            (root / "a.txt").write_text("changed", encoding="utf-8")
            self.assertEqual(verify_manifest(root, manifest)["changed"], ["a.txt"])


class DataQualityTests(unittest.TestCase):
    def test_profile_reports_missing_and_duplicate_values(self) -> None:
        result = profile_records(
            [
                {"id": "A", "value": 1},
                {"id": "A", "value": None},
                {"id": "B", "value": 3},
            ],
            required_fields=("id", "value"),
            identity_field="id",
        )

        self.assertEqual(result["record_count"], 3)
        self.assertEqual(result["missing_required"], {"id": 0, "value": 1})
        self.assertEqual(result["duplicate_identities"], ["A"])
        self.assertFalse(result["complete"])


class DependencyGraphTests(unittest.TestCase):
    def test_dependencies_appear_before_dependants(self) -> None:
        order = topological_order(
            {
                "report": {"analysis"},
                "analysis": {"capture"},
                "capture": set(),
            }
        )
        self.assertLess(order.index("capture"), order.index("analysis"))
        self.assertLess(order.index("analysis"), order.index("report"))

    def test_cycle_is_rejected(self) -> None:
        with self.assertRaises(DependencyCycleError):
            topological_order({"a": {"b"}, "b": {"a"}})


if __name__ == "__main__":
    unittest.main()

