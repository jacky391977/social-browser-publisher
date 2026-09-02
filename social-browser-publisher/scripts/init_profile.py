#!/usr/bin/env python3
"""Create private, per-user social voice/profile files without personal defaults."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


PROFILES_ROOT = Path.home() / ".config" / "codex-social-publisher" / "profiles"
PROFILE_ID_PATTERN = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}\Z")

TEMPLATES = {
    "voice-profile.md": """# Voice profile

Status: untrained
Owner label:
Source:
Sample count: 0
Last updated:
Confidence: low

## One-sentence voice

## Sentence and paragraph rhythm

## Punctuation and formatting

## Openings and endings

## Emoji and hashtags

## Topics and calls to action

## Avoid

## Platform differences

## User corrections
""",
    "brand-profile.md": """# Brand profile

Status: unconfigured
Owner label:

## Audience

## Goals

## Approved facts and offers

## Colors, fonts, logo, and visual direction

## Privacy and topic boundaries
""",
    "content-plan.md": """# Content plan

Status: not planned

## Goals and frequency

## Current plan

| Date/slot | Platform | Purpose | Topic | Format/media | Status | Result notes |
|---|---|---|---|---|---|---|

## Review notes
""",
}


def validate_profile_id(profile_id: str) -> str:
    if not PROFILE_ID_PATTERN.fullmatch(profile_id):
        raise ValueError(
            "profile-id 只能使用小寫英文字母、數字、底線或連字號，且需以字母或數字開頭（最長 64 字元）"
        )
    return profile_id


def write_private_new(path: Path, content: str) -> bool:
    """Create a private file without overwriting an existing profile file."""
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return False
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(content)
    os.chmod(path, 0o600)
    return True


def init_profile(profile_id: str, profiles_root: Path = PROFILES_ROOT) -> tuple[Path, list[str]]:
    profile_id = validate_profile_id(profile_id)
    profiles_root = profiles_root.expanduser()
    profiles_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    if profiles_root.is_symlink():
        raise ValueError("profiles 目錄不可為符號連結")
    os.chmod(profiles_root, 0o700)

    profile_dir = profiles_root / profile_id
    profile_dir.mkdir(mode=0o700, exist_ok=True)
    if profile_dir.is_symlink():
        raise ValueError("profile 目錄不可為符號連結")
    os.chmod(profile_dir, 0o700)

    created: list[str] = []
    for filename, content in TEMPLATES.items():
        if write_private_new(profile_dir / filename, content):
            created.append(filename)
    return profile_dir, created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-id", default="default")
    parser.add_argument("--profiles-root", type=Path, default=PROFILES_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()

    try:
        profile_dir, created = init_profile(args.profile_id, args.profiles_root)
    except (OSError, ValueError) as error:
        print(f"建立失敗：{error}")
        return 1

    print(f"私人使用者設定檔：{profile_dir}")
    if created:
        print("已建立：" + ", ".join(created))
    else:
        print("現有檔案均已保留，沒有覆寫。")
    print("請用這位使用者自己提供或授權讀取的貼文訓練語氣；不要放入帳密、Token 或 Cookie。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

