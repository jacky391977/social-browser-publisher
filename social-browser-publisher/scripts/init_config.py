#!/usr/bin/env python3
"""Create a non-secret local configuration for Social Browser Publisher."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


CONFIG_DIR = Path.home() / ".config" / "codex-social-publisher"
CONFIG_PATH = CONFIG_DIR / "config.json"


def prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def build_config(args: argparse.Namespace) -> dict[str, object]:
    interactive = not args.non_interactive
    profile = args.chrome_profile_label
    voice_profile_id = args.voice_profile_id
    instagram = args.instagram
    facebook = args.facebook
    threads = args.threads

    if interactive:
        profile = prompt("Chrome Profile 顯示名稱", profile or "Codex Social")
        voice_profile_id = prompt("使用者語氣設定檔代號", voice_profile_id or "default")
        instagram = prompt("Instagram 預期帳號（可留空）", instagram or "")
        facebook = prompt("Facebook 預期目的地（可留空）", facebook or "")
        threads = prompt("Threads 預期帳號（可留空）", threads or "")

    return {
        "version": 1,
        "chrome_profile_label": profile or "Codex Social",
        "voice_profile_id": voice_profile_id or "default",
        "instagram": {"expected_account": instagram or ""},
        "facebook": {"expected_destination": facebook or ""},
        "threads": {"expected_account": threads or ""},
    }


def write_config(config: dict[str, object], path: Path = CONFIG_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(path.parent, 0o700)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open(path, flags, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(config, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.chmod(path, 0o600)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--non-interactive", action="store_true")
    parser.add_argument("--chrome-profile-label", default="Codex Social")
    parser.add_argument("--voice-profile-id", default="default")
    parser.add_argument("--instagram", default="")
    parser.add_argument("--facebook", default="")
    parser.add_argument("--threads", default="")
    parser.add_argument("--config", type=Path, default=CONFIG_PATH, help=argparse.SUPPRESS)
    args = parser.parse_args()

    write_config(build_config(args), args.config.expanduser())
    print(f"設定已建立：{args.config.expanduser()}")
    print("僅保存非敏感目的地名稱；請勿加入密碼、Token 或 Cookie。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
