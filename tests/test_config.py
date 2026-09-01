import importlib.util
import stat
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


init_config = load_module("init_config", "social-browser-publisher/scripts/init_config.py")
doctor = load_module("doctor", "social-browser-publisher/scripts/doctor.py")


class ConfigTests(unittest.TestCase):
    def test_written_config_is_private_and_valid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "private" / "config.json"
            config = {
                "version": 1,
                "chrome_profile_label": "Codex Social",
                "instagram": {"expected_account": "@demo"},
                "facebook": {"expected_destination": "Demo Page"},
                "threads": {"expected_account": "@demo"},
            }
            init_config.write_config(config, path)
            self.assertEqual(doctor.check(path), [])
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
            self.assertEqual(stat.S_IMODE(path.parent.stat().st_mode), 0o700)

    def test_forbidden_secret_key_fails_without_value(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "private" / "config.json"
            config = {
                "version": 1,
                "chrome_profile_label": "Codex Social",
                "instagram": {"expected_account": "@demo", "access_token": "DO-NOT-PRINT"},
                "facebook": {"expected_destination": ""},
                "threads": {"expected_account": ""},
            }
            init_config.write_config(config, path)
            errors = doctor.check(path)
            rendered = "\n".join(errors)
            self.assertIn("instagram.access_token", rendered)
            self.assertNotIn("DO-NOT-PRINT", rendered)

    def test_unknown_top_level_key_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "private" / "config.json"
            config = {
                "version": 1,
                "chrome_profile_label": "Codex Social",
                "instagram": {},
                "facebook": {},
                "threads": {},
                "unexpected": True,
            }
            init_config.write_config(config, path)
            self.assertTrue(doctor.check(path))


if __name__ == "__main__":
    unittest.main()
