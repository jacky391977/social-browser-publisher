# Browser publishing workflow

Read this only for a real publish or dry run. The exact UI can change; rely on current visible labels and page state rather than fixed CSS selectors.

## Shared preflight

1. Confirm requested platforms and whether the destination is a personal profile, Page, or other supported surface.
2. Confirm caption, links, hashtags, mentions, accessibility text if requested, media files, media order, and platform-specific differences.
3. Confirm local media paths exist before opening composers.
4. Show the exact final preview and obtain authorization as defined in `SKILL.md`.
5. Open the user's Chrome and inspect login/account state from visible UI.

For a dry run, execute the same flow but stop with the final publish/share button visible and report `未發布（dry run）`.

## Instagram

Use Instagram's create-post flow. Verify the visible active account before upload. Upload the authorized image(s) or video, preserve requested order/crop, enter the Instagram caption, and stop before the final Share button if authorization is absent or this is a dry run.

After sharing, verify a visible success confirmation or open the resulting post/profile and confirm the new post. Capture the post URL when available.

## Facebook

Before composing, verify the selected publishing identity and destination. Facebook may default to a personal profile even when a Page was intended. Select the exact configured Page/profile/group from visible UI, then enter the Facebook-specific text and media.

Stop before the final Post button if authorization is absent or this is a dry run. After posting, verify the resulting post in the destination feed and capture its URL when available.

## Threads

Verify the visible Threads account, open the new-thread composer, enter the Threads-specific text and authorized media, and stop before the final Post button if authorization is absent or this is a dry run.

After posting, verify the resulting thread in the profile/feed and capture its URL when available.

## Ambiguous outcomes

If the browser times out, navigates unexpectedly, or shows no clear success state after the final click:

1. Inspect the current composer and destination profile/feed.
2. Search only the user's visible recent posts for the exact text/media.
3. If still unclear, report `失敗／狀態不明` and do not retry automatically.
