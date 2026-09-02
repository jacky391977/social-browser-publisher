#!/usr/bin/env python3
"""Validate Social Browser Publisher's local non-secret configuration."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
from pathlib import Path
from typing import Any


DEFAULT_CONFIG = Path.home() / ".config" / "codex-social-publisher" / "config.json"
FORBIDDEN_PARTS = {
    "password",
    "passwd",
    "secret",
    "token",
    "cookie",
    "session",
    "otp",
    "2fa",
    "recovery",
    "api_key",
    "apikey",
    "authorization",
}
ALLOWED_TOP_LEVEL = {
    "version",
    "chrome_profile_label",
    "voice_profile_id",
    "instagram",
    "facebook",
    "threads",
}
PROFILE_ID_PATTERN = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}\Z")


def normalized_key(key: str) -> str:
    return key.casefold().replace("-", "_").replace(" ", "_")


def find_forbidden_keys(value: Any, trail: tuple[str, ...] = ()) -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for raw_key, child in value.items():
            key = str(raw_key)
            normalized = normalized_key(key)
            if any(part in normalized for part in FORBIDDEN_PARTS):
                findings.append(".".join((*trail, key)))
            findings.extend(find_forbidden_keys(child, (*trail, key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(find_forbidden_keys(child, (*trail, str(index))))
    return findings


def validate_shape(config: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(config, dict):
        return ["設定檔最外層必須是 JSON object"]
    unknown = sorted(set(config) - ALLOWED_TOP_LEVEL)
    if unknown:
        errors.append("含有不允許的最外層欄位：" + ", ".join(unknown))
    if config.get("version") != 1:
        errors.append("version 必須為 1")
    profile_id = config.get("voice_profile_id", "default")
    if not isinstance(profile_id, str) or not PROFILE_ID_PATTERN.fullmatch(profile_id):
        errors.append("voice_profile_id 格式不合法")
    for platform in ("instagram", "facebook", "threads"):
        if not isinstance(config.get(platform), dict):
            errors.append(f"{platform} 必須是 JSON object")
    return errors


def permission_errors(path: Path) -> list[str]:
    if os.name != "posix":
        return []
    errors: list[str] = []
    file_mode = stat.S_IMODE(path.stat().st_mode)
    dir_mode = stat.S_IMODE(path.parent.stat().st_mode)
    if file_mode & 0o077:
        errors.append(f"設定檔權限過寬（目前 {file_mode:04o}，需要 0600）")
    if dir_mode & 0o077:
        errors.append(f"設定目錄權限過寬（目前 {dir_mode:04o}，需要 0700）")
    return errors


def profile_permission_errors(config: Any, config_path: Path) -> list[str]:
    if os.name != "posix":
        return []
    if not isinstance(config, dict):
        return []
    profile_id = config.get("voice_profile_id", "default")
    if not isinstance(profile_id, str) or not PROFILE_ID_PATTERN.fullmatch(profile_id):
        return []
    profile_dir = config_path.parent / "profiles" / profile_id
    if not profile_dir.exists():
        return []
    if profile_dir.is_symlink() or not profile_dir.is_dir():
        return ["使用者語氣設定檔目錄不可為符號連結，且必須是目錄"]

    errors: list[str] = []
    dir_mode = stat.S_IMODE(profile_dir.stat().st_mode)
    if dir_mode & 0o077:
        errors.append(f"使用者語氣設定檔目錄權限過寬（目前 {dir_mode:04o}，需要 0700）")
    for filename in ("voice-profile.md", "brand-profile.md", "content-plan.md", "trend-log.md"):
        file_path = profile_dir / filename
        if not file_path.exists():
            continue
        if file_path.is_symlink() or not file_path.is_file():
            errors.append(f"{filename} 不可為符號連結，且必須是一般檔案")
            continue
        file_mode = stat.S_IMODE(file_path.stat().st_mode)
        if file_mode & 0o077:
            errors.append(f"{filename} 權限過寬（目前 {file_mode:04o}，需要 0600）")
    return errors


def check(path: Path) -> list[str]:
    if not path.is_file():
        return ["找不到設定檔；請先執行 scripts/init_config.py"]
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ["設定檔無法讀取或不是有效 JSON"]

    errors = permission_errors(path)
    errors.extend(validate_shape(config))
    errors.extend(profile_permission_errors(config, path))
    forbidden = find_forbidden_keys(config)
    if forbidden:
        errors.append("偵測到敏感欄位名稱（不顯示內容）：" + ", ".join(forbidden))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()
    path = args.config.expanduser()
    errors = check(path)
    if errors:
        print("Doctor：未通過")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Doctor：通過")
    print(f"- 設定檔：{path}")
    print("- 未偵測到敏感欄位")
    print("- 使用者語氣資料僅檢查路徑與權限，不輸出內容")
    print("- 提醒：網站登入狀態仍須從 Chrome 可見畫面確認")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
