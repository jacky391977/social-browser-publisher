# Current trend and hot-topic research

Read this when the user asks for recent, popular, trending, highly discussed, or timely content ideas.

## Define the search

Resolve from the request when possible:

- topic, industry, product, or location
- target audience and business goal
- target platform(s)
- recency window, such as today, 24 hours, 7 days, or 30 days
- exclusions or sensitive topics

If the user does not specify a window, choose a reasonable recent window for the subject and state it. Use exact dates in the result so "recent" is auditable.

## Live evidence is required

Trending status is time-sensitive. Use current web search or a platform's visible recent-search UI; never rely on model memory alone.

- Prefer primary sources, official announcements, first-party data, and original posts for factual claims.
- For news-driven topics, compare publish date with the date the event occurred.
- For platform-specific conversation, use the user's logged-in Chrome only when the user explicitly asks or authorizes it. Do not read unrelated feeds, DMs, browser history, or private groups.
- Use the platform's recent/newest filter when available and verify visible timestamps plus direct post links.
- Public search can be incomplete or rate-limited. If direct platform evidence is unavailable, say so and label the result as web/news interest rather than platform popularity.

Do not scrape at scale. Review a small, inspectable sample and stop when enough evidence exists.

## Evidence standard

Do not rank topics only by raw likes because account size, platform, format, and post age differ. Consider:

- recency and event timing
- multiple independent sources or posts discussing the same theme
- visible engagement velocity when available
- relevance to the active user's audience and offers
- whether the conversation has a useful, non-derivative angle

Label confidence:

- **A — strong:** multiple recent independent sources plus direct conversation evidence.
- **B — useful:** one authoritative current source or several recent social examples.
- **C — exploratory:** early/niche signal, incomplete platform visibility, or weak comparative evidence.

Never present C as a confirmed trend.

## Safety and quality filters

Unless the user explicitly requests a sensitive category, skip tragedy exploitation, unverified accusations, hate/harassment, private-person targeting, medical misinformation, obvious spam, and low-quality engagement bait. For politics, medical, legal, or financial topics, use authoritative current sources and clearly separate facts from suggested opinion.

## Avoid copying

Research provides facts, questions, and conversation tension—not text to imitate.

- Do not copy captions, hooks, jokes, visual layouts, or distinctive phrasing.
- Do not closely paraphrase one creator's post.
- Synthesize across sources, then create a genuinely new angle grounded in the active user's experience, expertise, product, or audience question.
- Preserve source links for factual verification, but do not insert them into the final post unless the user approves and the platform version calls for them.

## Research output

Return a small reviewable set, normally five candidates unless the user requests another number. For each candidate include:

1. topic/title
2. why it is timely now
3. source dates and direct links
4. confidence A/B/C and evidence limitation
5. a distinct angle for the active user
6. best platform and suggested format/media

Do not draft or publish all candidates automatically. Let the user select or combine an angle, then use `platform-writing.md`, the active voice profile, and the normal preview/approval boundary.

## Private trend log

Record only the reviewed summary—not copied source text—in the active profile's `trend-log.md`:

```text
research date | window | topic | source URLs | confidence | chosen angle | used/published
```

Check the log before suggesting topics so the same angle is not repeated too soon. Trend research never authorizes publication.
