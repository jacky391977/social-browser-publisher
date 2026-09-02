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
init_profile = load_module("init_profile", "social-browser-publisher/scripts/init_profile.py")
select_profile = load_module("select_profile", "social-browser-publisher/scripts/select_profile.py")
doctor = load_module("doctor", "social-browser-publisher/scripts/doctor.py")


class ConfigTests(unittest.TestCase):
    def test_written_config_is_private_and_valid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "private" / "config.json"
            config = {
                "version": 1,
                "chrome_profile_label": "Codex Social",
                "voice_profile_id": "student-a",
                "instagram": {"expected_account": "@demo"},
                "facebook": {"expected_destination": "Demo Page"},
                "threads": {"expected_account": "@demo"},
            }
            init_config.write_config(config, path)
            self.assertEqual(doctor.check(path), [])
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
            self.assertEqual(stat.S_IMODE(path.parent.stat().st_mode), 0o700)

    def test_per_user_profile_is_private_and_has_no_personal_default_voice(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profiles_root = Path(temp_dir) / "profiles"
            profile_dir, created = init_profile.init_profile("student-a", profiles_root)
            self.assertEqual(
                sorted(created),
                ["brand-profile.md", "content-plan.md", "voice-profile.md"],
            )
            self.assertEqual(stat.S_IMODE(profile_dir.stat().st_mode), 0o700)
            for filename in created:
                path = profile_dir / filename
                self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
                rendered = path.read_text(encoding="utf-8").casefold()
                self.assertNotIn("hao", rendered)
                self.assertNotIn("jacky", rendered)
                self.assertNotIn("yuquan", rendered)
            self.assertIn("Status: untrained", (profile_dir / "voice-profile.md").read_text())

    def test_profile_init_never_overwrites_existing_user_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profiles_root = Path(temp_dir) / "profiles"
            profile_dir, _ = init_profile.init_profile("student-a", profiles_root)
            voice_path = profile_dir / "voice-profile.md"
            voice_path.write_text("USER-CORRECTION", encoding="utf-8")
            _, created = init_profile.init_profile("student-a", profiles_root)
            self.assertEqual(created, [])
            self.assertEqual(voice_path.read_text(encoding="utf-8"), "USER-CORRECTION")

    def test_invalid_profile_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(ValueError):
                init_profile.init_profile("../another-user", Path(temp_dir) / "profiles")

    def test_select_profile_preserves_platform_destinations(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "private" / "config.json"
            profiles_root = config_path.parent / "profiles"
            init_profile.init_profile("student-a", profiles_root)
            init_profile.init_profile("student-b", profiles_root)
            config = {
                "version": 1,
                "chrome_profile_label": "Codex Social",
                "voice_profile_id": "student-a",
                "instagram": {"expected_account": "@demo"},
                "facebook": {"expected_destination": "Demo Page"},
                "threads": {"expected_account": "@demo"},
            }
            init_config.write_config(config, config_path)
            selected = select_profile.select_profile("student-b", config_path, profiles_root)
            self.assertEqual(selected["voice_profile_id"], "student-b")
            self.assertEqual(selected["instagram"]["expected_account"], "@demo")
            self.assertEqual(selected["facebook"]["expected_destination"], "Demo Page")
            self.assertEqual(stat.S_IMODE(config_path.stat().st_mode), 0o600)
            self.assertEqual(doctor.check(config_path), [])

    def test_forbidden_secret_key_fails_without_value(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "private" / "config.json"
            config = {
                "version": 1,
                "chrome_profile_label": "Codex Social",
                "voice_profile_id": "default",
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
                "voice_profile_id": "default",
                "instagram": {},
                "facebook": {},
                "threads": {},
                "unexpected": True,
            }
            init_config.write_config(config, path)
            self.assertTrue(doctor.check(path))

    def test_non_object_config_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "private" / "config.json"
            init_config.write_config(["not", "an", "object"], path)
            self.assertIn("設定檔最外層必須是 JSON object", doctor.check(path))


if __name__ == "__main__":
    unittest.main()
