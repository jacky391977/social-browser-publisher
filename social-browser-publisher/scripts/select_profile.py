#!/usr/bin/env python3
"""Select an existing private user voice profile without changing destinations."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any


CONFIG_PATH = Path.home() / ".config" / "codex-social-publisher" / "config.json"
PROFILES_ROOT = CONFIG_PATH.parent / "profiles"
PROFILE_ID_PATTERN = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}\Z")


def select_profile(
    profile_id: str,
    config_path: Path = CONFIG_PATH,
    profiles_root: Path = PROFILES_ROOT,
) -> dict[str, Any]:
    if not PROFILE_ID_PATTERN.fullmatch(profile_id):
        raise ValueError("profile-id 格式不合法")

    config_path = config_path.expanduser()
    profiles_root = profiles_root.expanduser()
    profile_dir = profiles_root / profile_id
    if profile_dir.is_symlink() or not profile_dir.is_dir():
        raise ValueError("找不到安全的 profile 目錄；請先執行 init_profile.py")
    if not config_path.is_file() or config_path.is_symlink():
        raise ValueError("找不到安全的 config.json；請先執行 init_config.py")

    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError("config.json 無法讀取或不是有效 JSON") from error
    if not isinstance(config, dict):
        raise ValueError("config.json 最外層必須是 JSON object")

    config["voice_profile_id"] = profile_id
    config_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(config_path.parent, 0o700)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=config_path.parent,
        prefix=".config.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        json.dump(config, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temp_path = Path(handle.name)
    os.chmod(temp_path, 0o600)
    os.replace(temp_path, config_path)
    os.chmod(config_path, 0o600)
    return config


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-id", required=True)
    parser.add_argument("--config", type=Path, default=CONFIG_PATH, help=argparse.SUPPRESS)
    parser.add_argument("--profiles-root", type=Path, default=PROFILES_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()

    try:
        select_profile(args.profile_id, args.config, args.profiles_root)
    except (OSError, ValueError) as error:
        print(f"切換失敗：{error}")
        return 1
    print(f"目前使用者語氣設定檔：{args.profile_id}")
    print("其他平台目的地設定均已保留。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
