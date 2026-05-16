# SEO & AEO Roadmap

Tracking doc for SEO (search engine optimization) and AEO (answer engine optimization) work on `thegeminfo.com`. Captures what's done, what's planned, and the reasoning behind each enhancement so future-you (or a future contributor) can pick up where the work left off.

**Last updated:** 2026-05-15
**Author:** Claude Opus 4.7 + the GEM operator

---

## Phase 0: Foundations (DONE)

Shipped earlier in the v1.7 production pass. Recapping here so the SEO/AEO context is complete.

- [x] Single H1 per page, clean H2 → H3 hierarchy across all pages
- [x] Canonical tags on every public page
- [x] Open Graph + Twitter Card on every public page
- [x] JSON-LD on every public page: `Organization`, `WebSite`, `SoftwareApplication`, `FAQPage`, `BreadcrumbList`, `HowTo`, `WebPage`, `AboutPage`, `ContactPage`
- [x] `robots.txt` with AdSense and AEO crawler allowlist (`Mediapartners-Google`, `Google-Extended`, `GPTBot`, `ChatGPT-User`, `OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`, `anthropic-ai`, `Applebot`, `Applebot-Extended`, `cohere-ai`)
- [x] `sitemap.xml` with all public URLs and section anchors
- [x] `ads.txt` placeholder ready for AdSense
- [x] Internal linking: footer of every page links to all sibling pages
- [x] Theme color, viewport, language attributes set
- [x] Skip-link for keyboard accessibility
- [x] All decorative SVGs use `aria-hidden`, functional SVGs use `role="img"` + `aria-label`
- [x] HTTPS via Vercel (auto-issued Let's Encrypt cert)

---

## Phase 1: Humanization (DONE)

Stripped AI-flavored prose tells (em-dashes, "Not X. Y." pattern interrupts, "Most X..." marketing voice) and rewrote in a natural founder voice. This matters for SEO/AEO because:

1. Google's helpful-content updates penalize obvious AI-generated copy
2. AI detection tools (Originality.ai, GPTZero, ZeroGPT) flag em-dashes hard
3. AEO citation prefers natural, quotable prose

**Em-dash counts after the pass:**

| File | Before | After (visible prose) |
|---|---:|---:|
| `landing.html` | 96 | 0 |
| `about.html` | 14 | 0 |
| `privacy.html` | 12 | 0 |
| `terms.html` | 13 | 0 |
| `app/index.html` | 13 | 0 |

Remaining em-dashes in the codebase are confined to CSS palette comments, JS comments, and the comparison table's "N/A" markers — none of which are user-visible prose.

---

## Phase 2: SEO/AEO Enrichment (IN PROGRESS)

The current pass. Specific enhancements being applied:

### Schema markup additions

- [ ] **`ItemList`** for the 6 AI agents on `landing.html`. Each agent gets its own `Item` with name + description. This is what AI assistants reach for when asked "what are the 6 agents in GEM Content Engine."
- [ ] **`Person` schema** for the founder on `about.html` (anonymous role-based: "Operator behind AI Decoded and Tools That Work"). Builds E-E-A-T signal.
- [ ] **`SpeakableSpecification`** pointing at hero + FAQ. Voice assistants (Siri, Alexa, Google Assistant) preferentially read content marked Speakable.
- [ ] **Expanded `FAQPage`** with 4–6 more long-tail Q&A entries covering "people also ask" patterns: model support, offline use, agent count, refund policy, beginner-friendliness.
- [ ] **`Service` schema** alongside `SoftwareApplication` to widen the discovery surface.
- [ ] **`mainEntityOfPage`** linking each public page to its schema graph.

### On-page content additions

- [ ] **"What is GEM Content Engine?"** definition block. 40–60 word semantic answer in plain prose, no bullets, immediately after the hero. Google's featured snippet algorithm and AI assistants both prefer this format.
- [ ] **"Who is GEM for?"** use-cases section. Names the target audiences explicitly (faceless YouTube operators, social media managers, indie creators, AI / tech newsletter writers, small content agencies). Builds topical authority and matches long-tail search intent.
- [ ] **Long-tail FAQ expansion**. Adding question-format coverage for queries like "Does GEM work with Claude?", "Can I use GEM without internet?", "What's the difference between GEM and Jasper?".

### Meta tag enrichment

- [ ] **`article:tag`** meta entries for the top 10 target keywords on each page.
- [ ] **Expanded meta descriptions** at the 155-character Google snippet sweet spot.
- [ ] **`article:section`** for content categorization.

### Linking architecture

- [ ] **Cross-page anchor links** from About → FAQ, About → Pricing, FAQ → Sample. Helps Google understand topical relationships.
- [ ] **Section IDs on all H2/H3** so AI assistants can deep-link to specific answers.

---

## Phase 3: Post-launch (TODO once live)

To be done after `thegeminfo.com` is fully resolved on the new DNS and Vercel is serving cleanly.

- [ ] **Submit `sitemap.xml`** to Google Search Console
- [ ] **Submit to Bing Webmaster Tools** (import directly from Search Console)
- [ ] **Verify ownership** via DNS TXT record or meta-tag method
- [ ] **Baseline Core Web Vitals** on [PageSpeed Insights](https://pagespeed.web.dev/?url=https%3A%2F%2Fthegeminfo.com)
- [ ] **Run a Lighthouse SEO audit** and fix any flagged issues
- [ ] **Apply to Google AdSense** once organic traffic baselines (typically 1000+ monthly visitors)
- [ ] **Backlink campaign**: submit GEM to indie hacker directories, Product Hunt, Hacker News Show HN, Reddit r/indiehackers, AppSumo Briefcase, BetaList, Indie Hackers products page
- [ ] **First-30-day content cadence** per `GEM-30-Day-Marketing-Push.html` to seed organic links

---

## Phase 4: Ongoing measurement

The metrics that matter once the site has been live for ~30 days.

| Metric | Source | Target |
|---|---|---|
| Organic clicks | Search Console | 100/day by day 60 |
| Avg position for "GEM Content Engine" | Search Console | Top 3 |
| Avg position for "AI content engine" | Search Console | Top 10 |
| Avg position for "Jasper alternative" | Search Console | Top 20 |
| Featured snippets won | Search Console | 1 by day 90 |
| AI assistant citations (Perplexity, ChatGPT, Claude) | Manual sampling | 1 per month by day 90 |
| Core Web Vitals (mobile) | PageSpeed Insights | All green |
| Lighthouse SEO score | Lighthouse | 100 / 100 |

---

## Phase 5: Content marketing flywheel (TODO)

The defensible long-term SEO play. None of this is in scope for the current pass, captured here so it doesn't get lost.

- [ ] Add a `/blog/` directory with 10 founder posts: build-in-public diary, dogfooding case studies from AI Decoded and Tools That Work, deep dives on each of the six agents, "GEM vs Jasper / Copy.ai / ChatGPT" comparison posts.
- [ ] Add a `/guides/` directory with how-to guides that target informational queries: "how to write a YouTube script with AI", "best Midjourney prompts for thumbnails", "Ollama vs OpenAI cost analysis".
- [ ] Add a `/changelog/` page powered by the existing CHANGELOG markdown so each release becomes its own indexable URL.
- [ ] Add a `/customers/` page with anonymized buyer case studies once the Founder cohort generates them.

---

## Reference: target keyword map

The seed keywords used to shape the schema, meta, and on-page content.

### Primary (compete on these first)
- "GEM Content Engine"
- "AI content engine"
- "AI content generator for creators"
- "multi-agent AI content tool"
- "lifetime AI content tool"

### Secondary (medium-tail)
- "Jasper alternative"
- "Copy.ai alternative"
- "ChatGPT alternative for content"
- "local AI content generator"
- "Ollama content generator"
- "AI carousel generator Instagram LinkedIn"
- "Midjourney prompt generator"
- "Kling AI prompt generator"
- "RunwayML prompt generator"

### Long-tail (AEO + featured snippets)
- "what is the best AI content tool for solopreneurs"
- "how do I use AI to write YouTube scripts"
- "can I run AI content generation locally"
- "what's the difference between Jasper and GEM"
- "AI tool to generate Instagram and LinkedIn carousels"
- "how to write image prompts for Midjourney with AI"
- "best AI tool for faceless YouTube channels"

---

*This doc is a living roadmap. Update the checkboxes as each phase ships, and add new phases at the bottom. Lives in the repo under `docs/SEO-AEO-ROADMAP.md`.*
