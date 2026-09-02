---
name: social-browser-publisher
description: Research current social trends with dated sources, learn each user's own writing voice from authorized samples, plan and draft readable platform-specific content, create optional image cards, and safely preview or publish through the user's signed-in Chrome to Instagram, Facebook, and Threads. Use for trend/topic discovery, social style learning, post drafting, content calendars, image-card posts, dry runs, publishing, and performance reviews; not for bulk engagement automation or API-based mass posting.
---

# Social Browser Publisher

Provide one end-to-end social workflow: find timely topics from current evidence, learn the current user's voice, create readable platform-specific content and visuals, preview the exact result, then publish only the approved batch through the user's visible signed-in Chrome session.

Never ask for, read, store, export, or transmit passwords, one-time codes, cookies, browser profiles, local storage, session data, or access tokens.

## Non-negotiable identity rule

There is no built-in author voice. Never imitate this Skill's developer, instructor, examples, or another user.

- Learn only from posts that the current user supplies or explicitly authorizes Codex to read from a specified account.
- Keep every user's voice profile separate under `~/.config/codex-social-publisher/profiles/<profile-id>/`.
- Do not copy a profile, samples, content plan, brand data, or results into the Skill folder, repository, release ZIP, chat with another user, or another profile.
- If no trained profile exists, write a neutral draft and say that voice matching has not been trained. Do not invent a personal style.

For learning or changing a voice, read [references/voice-profile.md](references/voice-profile.md).

## Route the request

Choose only the references needed for the current mode:

- **Setup / doctor:** read [references/setup-and-security.md](references/setup-and-security.md), run the local helpers, and inspect requested platform login state without posting.
- **Learn / refresh voice:** read [references/voice-profile.md](references/voice-profile.md). Obtain source authorization before browser reading.
- **Trend / hot-topic research:** read [references/trend-research.md](references/trend-research.md). Current or "recent" claims require live web or explicitly authorized visible-platform research.
- **Content calendar / strategy:** read [references/content-strategy.md](references/content-strategy.md). Use the active user's goals and results, not universal viral formulas.
- **Draft / rewrite / preview:** read the active private voice profile and [references/platform-writing.md](references/platform-writing.md). Produce a distinct version for each requested platform.
- **Image card / visual post:** also read [references/visual-cards.md](references/visual-cards.md). Preview the actual image before upload.
- **Dry run / publish:** read [references/browser-publishing.md](references/browser-publishing.md) and follow the confirmation boundary below.
- **Performance review:** read [references/content-strategy.md](references/content-strategy.md) and compare against that user's own baseline.
- **Testing or release:** read [references/test-cases.md](references/test-cases.md).

Tell the user which mode is running in one short sentence when it changes what data or browser access is needed.

## Requirements

- For Chrome work, use the installed Chrome browser-control capability and follow its current instructions.
- If Chrome control is unavailable, stop and explain that the user must install or enable the ChatGPT Chrome extension under **Settings → Computer use**. Do not substitute another browser when the user requested Chrome.
- Before uploading local images or videos, require the one-time Chrome file-upload setup in [references/setup-and-security.md](references/setup-and-security.md).
- Use only the requested platform websites: `instagram.com`, `facebook.com`, and `threads.com`/`threads.net`.
- Keep normal human posting frequency. Do not scrape at scale, auto-like, auto-follow, bulk comment, send unsolicited messages, or bypass platform safeguards.
- Never claim a topic is currently trending from model memory alone. Record dated sources and uncertainty, then let the user select the angle before drafting.

## Confirmation boundary

Treat every publish as a bounded external side effect.

1. Resolve the requested platforms, visible destination account/page, exact text including paragraph breaks, media files and order, crop, accessibility text if requested, and all cross-post toggles.
2. Show a concise final preview per platform and clearly state that nothing has been published yet.
3. Obtain explicit batch-specific authorization unless the current message already clearly authorizes that exact preview. A standalone `發`, `發布`, or `確認發佈` applies only to the immediately preceding previewed batch.
4. Before every final click, verify the visible signed-in identity and ensure unrequested Threads/Facebook/Instagram cross-post toggles are off.
5. Do not silently rewrite text, swap media, add destinations, change crop, enable a cross-post, or publish another batch after approval. Material changes require a new preview and authorization.
6. Captcha, two-factor prompts, login forms, suspicious-login checks, consent dialogs, and account switching are user actions. Pause and ask the user to complete them directly in Chrome.

Scheduling approval, a standing preference such as "以後都直接發", or approval for one platform never authorizes another platform or future batch.

## Browser execution invariants

- Inspect the current visible page and use current accessible labels/roles; social UIs change often.
- Upload only user-provided or user-approved media from an exact local path.
- Do not access Chrome's password manager, profile directories, cookies, local storage, developer tokens, or browsing history.
- After entering a caption, re-read the composer value and compare both wording and blank lines with the approved preview before the final click.
- A successful button click is not proof of publication. Require a visible success state and verify the resulting profile/post when possible.
- If an outcome is ambiguous, inspect the destination once and do not click Publish again until duplication is ruled out.
- Stop after one bounded retry per platform. Report partial results independently.

## Completion report

Return one status per requested platform: `已發布`, `未發布`, `需登入`, `帳號不符`, or `失敗／狀態不明`. Include the visible destination and a resulting post URL only after verification. State whether any cross-post destinations were intentionally left off.
