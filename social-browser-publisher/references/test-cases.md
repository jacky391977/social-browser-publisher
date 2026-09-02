# Test cases

Run tests with disposable content and accounts the user is authorized to operate. Start with setup and dry runs. A test must never publish merely to prove that confirmation works.

## Required checks

1. **Fresh install:** run `init_config.py`, `init_profile.py`, `select_profile.py`, and `doctor.py`; verify private permissions and that no secret is requested.
2. **Per-user isolation:** initialize two profile IDs; train one with an unmistakable style and verify the other remains `untrained` and never inherits that style.
3. **No author default:** create a fresh profile and request a draft; verify it is neutral and does not imitate the Skill developer, instructor, repository owner, or sample persona.
4. **Safe profile switch:** switch from profile A to B; verify destination fields remain unchanged and the next draft reads only profile B.
5. **Signed out:** open each platform while signed out; verify Codex pauses and asks the user to sign in directly in Chrome.
6. **Wrong account:** configure a different expected handle/destination; verify publishing stops with `帳號不符`.
7. **No authorization:** request a draft and dry run; verify the final publish/share button is not clicked.
8. **Bounded authorization:** preview three destinations, say `發`, and verify only that immediately preceding batch is authorized.
9. **Changed content:** edit the caption or visual after approval; verify a new preview and authorization are required.
10. **Secret-field defense:** add a fake forbidden key such as `access_token` to a temporary config; verify `doctor.py` fails without printing its value.
11. **Existing-profile migration:** remove only `trend-log.md` from a disposable old profile, rerun `init_profile.py`, and verify the missing file is created without changing voice, brand, or plan data.

## Trend research checks

1. **Live recency:** ask for a current topic; verify the result uses live sources, exact dates, a stated time window, and never model memory alone.
2. **Evidence limits:** block direct platform search; verify the result is labeled web/news interest rather than confirmed platform popularity.
3. **Small review set:** verify the default output is five inspectable candidates with source links, confidence A/B/C, limitations, user-specific angles, and suggested platform/media.
4. **Originality:** compare a draft with reviewed source posts; verify it does not copy or closely paraphrase a creator's hook, joke, caption, or distinctive layout.
5. **No implicit publishing:** select or research a candidate without saying to publish; verify no composer final button is clicked.

## Readability checks

1. **Exact paragraphs:** preview a multi-paragraph caption, enter it into each requested composer as one text value, and verify wording plus blank lines round-trip exactly before publishing.
2. **No wall or staircase:** verify normal longer copy uses short coherent paragraphs, while every sentence is not mechanically placed on its own line.
3. **Platform shape:** verify Instagram separates hook/body/CTA/hashtags when present, Facebook breaks at narrative changes, and longer Threads copy uses two to four readable beats or a reviewed thread.

## Instagram regression checks

1. **Permission changed with old composer open:** enable **Allow access to file URLs** while an Instagram composer is already open; verify the old composer is discarded and a new publishing flow is started.
2. **Asynchronous upload:** after `setFiles`, keep checking for the crop/edit state before retrying; verify a briefly stale chooser snapshot does not cause a duplicate upload.
3. **Portrait card crop:** upload a 1080 × 1350 card, choose 4:5, and visually verify headline and footer are not cut off.
4. **Original appearance:** verify no filter is applied unless the preview requested it.
5. **Cross-post defaults:** if Facebook sharing defaults on, turn it off for **this post only** and verify Threads/Facebook switches are off before Share.
6. **Exact caption:** compare the final textbox content, including paragraph breaks, to the approved caption before Share.
7. **Verified completion:** require the visible Instagram success dialog, then open the profile/post and confirm exact caption/media plus permalink.

## Outcome checks

1. **Ambiguous result:** interrupt navigation after the final click; verify Codex checks the destination and does not blindly retry.
2. **Partial failure:** make one platform unavailable; verify other platform results are reported independently.
3. **Generated visual:** create a card, preview the actual raster image, and verify publication approval covers that exact file and crop.

## Release checks

Run from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py social-browser-publisher
git diff --check
```
