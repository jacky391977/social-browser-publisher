# Per-user voice profile

Read this for first-time voice learning, switching users/brands, or refreshing a profile.

## Source authorization

Use only one of these sources:

1. Posts pasted or uploaded by the current user.
2. A profile/account URL the user explicitly identifies as their own or authorizes Codex to analyze.
3. A visible signed-in Chrome profile page the user explicitly asks Codex to inspect.

Never guess a profile URL, search for a likely person, use another student's samples, or treat examples bundled with a Skill as the user's voice. Do not read private messages, comments by other people, browser history, or unrelated tabs.

Ask for enough representative material to avoid overfitting. Eight to twenty varied posts is a useful range, but use fewer when that is all the user provides and label confidence accordingly. Exclude reposted text, quoted articles, ads written by an agency, and comments that are not the user's own words unless the user says they represent the desired voice.

## Profile isolation

The active profile lives at:

```text
~/.config/codex-social-publisher/profiles/<profile-id>/voice-profile.md
```

The sibling files `brand-profile.md` and `content-plan.md` belong to the same user/brand. The directory must be private (`0700` on POSIX) and files private (`0600`). Never save these files in the installed Skill or repository.

Use a different `profile-id` for every person or brand. Before drafting, state the active profile ID and visible destination. If they do not match, stop and ask the user to choose or create the correct profile.

## Analysis dimensions

Read posts as writing samples, not just a word-frequency corpus. Record:

- overall tone and emotional range
- typical sentence and paragraph length
- punctuation, line breaks, emoji, and hashtag habits
- common openings, transitions, and endings
- first-person/brand voice and audience address
- recurring topics and calls to action
- words, claims, jokes, or topics the user avoids
- differences between ordinary, educational, promotional, and reflective posts
- confidence level and sample count

Do not infer sensitive traits, health, politics, religion, identity, or private relationships unless the user explicitly asks and those details are necessary for the intended public writing.

## Required profile shape

Keep these sections in `voice-profile.md`:

```markdown
# Voice profile

Status: trained | untrained
Owner label: <user-approved label>
Source: pasted samples | authorized visible profile
Sample count: <number>
Last updated: <date>
Confidence: low | medium | high

## One-sentence voice
## Sentence and paragraph rhythm
## Punctuation and formatting
## Openings and endings
## Emoji and hashtags
## Topics and calls to action
## Avoid
## Platform differences
## User corrections
```

Do not store passwords, tokens, cookies, full browser exports, private messages, or more raw sample text than is needed. Prefer derived traits over copying full posts.

## Validation

After training:

1. Show the user the three most distinctive findings.
2. Produce one short neutral-topic sample in the learned voice.
3. Ask what is accurate or wrong.
4. Apply corrections under `## User corrections`; user corrections override statistical patterns.

If the user says the sample is not recognizable, do not publish with that profile. Refresh the analysis or draft neutrally.

