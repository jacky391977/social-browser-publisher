---
name: social-browser-publisher
description: Draft, preview, and publish user-approved posts to Instagram, Facebook, and Threads through the user's already signed-in Chrome browser. Use when the user asks Codex to prepare or post social content through browser UI; do not use for API-based or high-volume automation.
---

# Social Browser Publisher

Publish through the user's visible, already signed-in Chrome session. Never ask for, read, store, export, or transmit passwords, one-time codes, cookies, browser profiles, local storage, session data, or access tokens.

## Requirements

- Use the installed Chrome browser-control capability and follow its instructions before browser work.
- If Chrome control is unavailable, stop and explain that the user must install/enable the Codex Chrome extension under **Settings → Computer use**. Do not substitute another browser when the user requested Chrome.
- Before uploading local images or videos, ensure the user has completed the Chrome file-upload permission steps in [references/setup-and-security.md](references/setup-and-security.md). If file upload is unavailable, stop before posting and guide the user through that setup. Never change browser-extension permissions on the user's behalf.
- Use the platform websites only: `instagram.com`, `facebook.com`, and `threads.net`.
- Keep normal human posting frequency. This skill is not for scraping, engagement bots, bulk posting, unsolicited messaging, or bypassing platform safeguards.

## Route the request

Choose one mode from the user's wording:

- **Setup / doctor:** read [references/setup-and-security.md](references/setup-and-security.md), run the local helpers, then inspect the requested platform login state without posting.
- **Draft / preview:** prepare platform-specific content and show the exact destination, text, media order, and any first comment. Do not open a composer unless useful to the requested preview.
- **Dry run:** follow the complete browser flow only up to the final publish/share button. Do not click it.
- **Publish:** read [references/browser-publishing.md](references/browser-publishing.md) and follow the confirmation boundary below.
- **Testing or maintenance:** read [references/test-cases.md](references/test-cases.md).

## Confirmation boundary

Treat publishing as an external side effect requiring fresh, batch-specific authorization.

1. Resolve the requested platforms, destination account/page, exact text, and media files.
2. Present a concise final preview for every platform. Clearly say that nothing has been published yet.
3. Ask for explicit authorization unless the user's current message already clearly authorizes publishing this exact preview. A standalone `發`, `發布`, or `確認發佈` authorizes only the immediately preceding previewed batch.
4. Before each final click, verify from visible page UI that the signed-in account or selected Facebook destination matches the preview. If identity cannot be verified, stop that platform.
5. After authorization, do not silently rewrite the caption, swap media, add platforms, change the destination, or publish a second batch. Material changes require a new preview and authorization.
6. Captcha, two-factor prompts, login forms, suspicious-login checks, consent dialogs, and account switching must be completed by the user. Pause and ask them to finish in Chrome, then tell you when it is ready.

Never interpret scheduling approval, a general preference such as "以後都直接發", or approval for one platform as authorization for another platform or future post.

## Browser execution

- Inspect the visible page and use accessible labels/roles where possible; platform UI and wording change often.
- Upload only user-provided or user-authorized local media. Confirm order when multiple files are present.
- If Chrome reports that file upload is disabled, do not request credentials or work around the restriction. Point the user to the **Chrome file upload permission** section in [references/setup-and-security.md](references/setup-and-security.md), then wait for them to confirm that it is enabled.
- Do not access Chrome's password manager, profile directories, cookies, local storage, developer tools, or network tokens.
- If an upload or publish state is ambiguous, inspect the resulting feed/profile and visible confirmation. Do not click Publish again until duplication is ruled out.
- Stop after one bounded retry per platform. Report the failure instead of repeatedly posting.
- Handle platforms independently: one failure does not imply success or authorization to duplicate posts elsewhere.

## Completion report

Return one status per requested platform: `已發布`, `未發布`, `需登入`, `帳號不符`, or `失敗／狀態不明`. Include the visible destination and a post URL only when it can be obtained from the resulting UI. Never claim success from a button click alone when no visible success state or resulting post was verified.
