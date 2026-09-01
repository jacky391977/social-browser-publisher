# Setup and security

Use this guide for first-time setup, account changes, or doctor checks.

## Local configuration

Run:

```bash
python3 scripts/init_config.py
python3 scripts/doctor.py
```

The helper stores only non-secret preferences at `~/.config/codex-social-publisher/config.json`. The directory is mode `0700` and the file is mode `0600` on POSIX systems.

Allowed fields:

- `chrome_profile_label`: a human-readable label only; it is not a filesystem path.
- `instagram.expected_account`: expected visible Instagram handle.
- `facebook.expected_destination`: expected visible profile, Page, or group name.
- `threads.expected_account`: expected visible Threads handle.

The configuration is optional. When an expected destination is blank, ask the user to identify the intended account/page before publishing and verify it from visible UI.

## Login setup

1. Recommend a separate Chrome profile named `Codex Social` so social sessions are isolated from personal email, banking, and unrelated work accounts.
2. Open each requested platform in Chrome.
3. If signed out, ask the user to sign in directly in Chrome. Never ask them to paste credentials or verification codes into chat.
4. After the user says login is complete, inspect only visible page UI and compare the displayed account with the configured expectation.

Do not create, copy, rename, inspect, or launch Chrome profile directories. The user controls profiles through Chrome UI.

## Secret handling

Do not place these in the repository, Skill folder, config, logs, screenshots, or chat output:

- passwords or password hints
- cookies or session identifiers
- access/refresh tokens, app secrets, or API keys
- one-time passwords, backup codes, or recovery codes
- copied browser profile data or login databases

If `doctor.py` reports a forbidden key, stop all publishing. Ask the user to remove that field and rotate the exposed credential if it was real.
