# Browser publishing workflow

Read this only for a real publish or dry run. Social UIs change; use current visible labels and the selected Chrome capability's documentation rather than copied CSS selectors.

## Shared preflight

1. Confirm platforms and whether each destination is a personal profile, Page, group, or other supported surface.
2. Confirm exact text, links, hashtags, mentions, media paths/order, crop, accessibility text if requested, and cross-post behavior.
3. Confirm every local media path exists and show the actual visual when newly generated.
4. Show the exact final preview and obtain authorization as defined in `SKILL.md`.
5. Inspect login/account state from visible Chrome UI. Never infer identity only from the URL.

For a dry run, execute the flow only until the final publish/share button is visible and report `未發布（dry run）`.

## Chrome local-file upload prerequisite

The ChatGPT Chrome extension must have **Allow access to file URLs** enabled. If the user changes that permission while a composer or file chooser is already open:

1. Close or discard that pre-permission composer without publishing.
2. Start a fresh Chrome publishing flow.
3. Open a new composer and a new file chooser.

Do not reuse the old chooser. Do not change extension permissions for the user.

For upload, start the chooser wait before clicking the visible upload control:

```javascript
const chooserPromise = tab.playwright.waitForEvent("filechooser", { timeoutMs: 10000 });
await tab.playwright.getByRole("button", { name: "從電腦選擇", exact: true }).click();
const chooser = await chooserPromise;
await chooser.setFiles(["/absolute/approved/file.png"]);
```

Use the current localized label when it differs. Never upload a guessed path.

## Instagram — verified feed-post sequence

1. Verify the visible account handle before opening the composer.
2. Open a **new feed post** composer. Do not reuse a composer opened before file-upload permission changed.
3. Upload the exact approved media through the file chooser flow above.
4. Wait for a visible crop/edit state such as `裁切` or `下一步`. After `setFiles` returns, the DOM may briefly still show the original chooser. Wait and inspect the current state or screenshot before declaring failure or opening another chooser. Do not upload a second time until the first upload is ruled out.
5. Choose the intended crop. For a 1080 × 1350 portrait card, explicitly select **4:5** and visually verify the headline, image, and footer are all present.
6. Continue to edit/filter and preserve **Original/原始** unless the preview specified a filter.
7. On the caption page, verify the visible Instagram handle again and enter the exact approved caption.
8. Inspect every cross-post switch. Instagram may default Facebook sharing on. Turn off every unrequested destination. If disabling Facebook opens `停止分享到 Facebook？`, choose **不要分享此貼文**; do not choose the global **停止分享所有貼文** unless the user explicitly requests a persistent setting change.
9. Re-read the exact caption and confirm all unrequested Threads/Facebook switches are off.
10. For a dry run or absent authorization, stop with **分享** visible. Otherwise click **分享** once.
11. Wait for a visible success state such as `已分享貼文` and `已分享你的貼文。`.
12. Open the visible destination profile, confirm the new image and caption, then open the post and capture its permalink. A successful click alone is not completion.

If the outcome remains ambiguous, inspect the profile once for the exact caption/media and do not click Share again.

## Facebook

1. Verify the visible publishing identity and exact profile/Page/group destination.
2. Open the current post composer and enter the Facebook-specific text and approved media.
3. Preserve the existing audience unless the user explicitly requests a change.
4. Inspect any Instagram/Threads/group cross-post options and leave unrequested destinations off.
5. Stop before the final Post/Publish button for dry run or absent authorization.
6. After one authorized click, verify a visible success state and the resulting destination post. Capture a permalink when available.

Facebook may insert an intermediate settings/review screen. Treat the last button that creates or schedules the post as the final side effect; do not assume the first `Continue` is publication.

## Threads

1. Verify the visible Threads account; do not assume it matches the active Instagram account.
2. Open the new-thread composer and enter the Threads-specific approved text and media.
3. For a multi-post thread, preview and approve each segment and order before browser entry.
4. Stop before the final Post button for dry run or absent authorization.
5. After one authorized click, verify the resulting thread in the visible profile/feed and capture its permalink.

## Ambiguous or partial outcomes

Handle platforms independently. If one platform fails after another succeeded, report the successful result and stop the failed platform at its bounded retry limit. Never repost a successful platform just to keep the batch visually aligned.
