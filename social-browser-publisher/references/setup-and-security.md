# Setup and security

Use this guide for first-time setup, account changes, or doctor checks.

## Local configuration

Run:

```bash
python3 scripts/init_config.py
python3 scripts/init_profile.py --profile-id default
python3 scripts/select_profile.py --profile-id default
python3 scripts/doctor.py
```

The configuration helper stores only non-secret preferences at `~/.config/codex-social-publisher/config.json`. The directory is mode `0700` and the file is mode `0600` on POSIX systems.

Allowed fields:

- `chrome_profile_label`: a human-readable label only; it is not a filesystem path.
- `voice_profile_id`: the active private user/brand profile identifier.
- `instagram.expected_account`: expected visible Instagram handle.
- `facebook.expected_destination`: expected visible profile, Page, or group name.
- `threads.expected_account`: expected visible Threads handle.

The configuration is optional. When an expected destination is blank, ask the user to identify the intended account/page before publishing and verify it from visible UI.

## Per-user voice and brand data

Private user-specific files live outside the installed Skill:

```text
~/.config/codex-social-publisher/profiles/<profile-id>/
```

Each profile contains `voice-profile.md`, `brand-profile.md`, and `content-plan.md`. Use a separate profile ID for every person or brand. Do not copy these files into the repository, release ZIP, another profile, or another user's chat.

Use `scripts/select_profile.py --profile-id <id>` before drafting or publishing for a different user. It changes only the active profile ID and preserves platform destination settings. Still verify the visible account before every publish.

These files may contain personal writing patterns and business context. Treat them as private user data even though they must never contain passwords, cookies, tokens, or login data.

## Login setup

1. Recommend a separate Chrome profile named `Codex Social` so social sessions are isolated from personal email, banking, and unrelated work accounts.
2. Open each requested platform in Chrome.
3. If signed out, ask the user to sign in directly in Chrome. Never ask them to paste credentials or verification codes into chat.
4. After the user says login is complete, inspect only visible page UI and compare the displayed account with the configured expectation.

Do not create, copy, rename, inspect, or launch Chrome profile directories. The user controls profiles through Chrome UI.

## Chrome file upload permission

This one-time setting is required when Codex needs to upload a local image or video to Instagram or Facebook. Text-only Threads posts do not require it.

1. In Chrome, open `chrome://extensions/`.
2. Find the ChatGPT browser extension and click **Details** (`詳細資料`).
3. Turn on **Allow access to file URLs** (`允許存取檔案網址`).
4. Close or discard any social composer/file chooser opened before the permission change.
5. Return to Codex, confirm that the setting is enabled, and start a fresh Chrome publishing task with a new composer.

Official setup reference: [Chrome extension file uploads](https://developers.openai.com/codex/app/chrome-extension#upload-files).

Codex must not change this permission automatically. If it is disabled, stop before uploading or publishing and ask the user to enable it in Chrome. After the user confirms, begin a new Chrome task and new composer before retrying. Never ask for account credentials as a workaround.

## Secret handling

Do not place these in the repository, Skill folder, config, logs, screenshots, or chat output:

- passwords or password hints
- cookies or session identifiers
- access/refresh tokens, app secrets, or API keys
- one-time passwords, backup codes, or recovery codes
- copied browser profile data or login databases

Do not publish or package a user's `voice-profile.md`, `brand-profile.md`, or `content-plan.md`. If `doctor.py` reports a forbidden key, stop publishing. Ask the user to remove that field and rotate the exposed credential if it was real.
