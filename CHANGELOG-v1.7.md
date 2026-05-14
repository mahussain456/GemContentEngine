# CHANGELOG — v1.7

**Release:** 2026-05-13
**Theme:** Production-ready landing, SEO / AEO hardening, AdSense approval prep, full pricing alignment.

> The live site at [thegeminfo.com](https://thegeminfo.com/) is the source of truth. The Founder's Edition price ladder is **$9 → $29 → $79 → $149** (one-time, lifetime, four rungs).

---

## Highlights

- 🎯 **New landing-page sections:** Today's Brief sample · Quality Bar · Roadmap teaser.
- 🛡 **AdSense-ready:** privacy policy, terms of service, about + contact, `ads.txt` placeholder, `Mediapartners-Google` allowed in `robots.txt`.
- 🔎 **AEO citation surface:** `HowTo`, `ContactPoint`, `WebPage`, expanded `FAQPage` JSON-LD. AI-crawler allowlist (`GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`, `OAI-SearchBot`, etc.).
- 📄 **PDFs regenerated:** `GEM-Sales-Strategy.pdf` and `GEM-User-Manual.pdf` rebuilt at v1.7 with the new ladder.
- 🧭 **Header nav extended** with Sample + Roadmap, with a new ≤1139 px hide breakpoint so intermediate widths don't wrap.

---

## Changed files

### Pages
| File | Status | Notes |
|---|---|---|
| `landing.html` | **modified** | New sections (`#sample`, `#quality`, `#roadmap`), credibility byline, pricing fix in comparison row, FAQ honesty pass, nav extended, footer rebuilt with legal links, JSON-LD expanded (`HowTo`, `ContactPoint`, `WebPage`). |
| `about.html` | **new** | Mission + dogfooding statement + four-channel contact grid. Carries `AboutPage` + `ContactPage` + `Organization` schema. |
| `privacy.html` | **new** | Full GDPR / UK GDPR / CCPA privacy policy with AdSense disclosure. 13-section TOC. |
| `terms.html` | **new** | License grant + restrictions + AI-output disclaimers + limitation of liability + governing law. 16-section TOC. |

### SEO / crawl
| File | Status | Notes |
|---|---|---|
| `robots.txt` | **modified** | Added `Mediapartners-Google` (AdSense), `Google-Extended`, AEO crawlers. Explicitly disallowed `/scripts/`, `/Pitch_Deck/`, internal logs. |
| `sitemap.xml` | **modified** | Added `/about.html`, `/privacy.html`, `/terms.html` + `#sample`, `#quality`, `#roadmap`. `lastmod` bumped to 2026-05-13. |
| `ads.txt` | **new** | Placeholder for AdSense activation — replace the placeholder line once approved. |

### PDFs (regenerated)
| File | Status | Notes |
|---|---|---|
| `GEM-Sales-Strategy.pdf` | **rebuilt** | 8 pages · 18.9 KB · zero legacy pricing refs. Includes new four-rung ladder, v1.7 roadmap, recomputed revenue projections. |
| `GEM-User-Manual.pdf` | **rebuilt** | 11 pages · 22 KB. v1.7 Quality Bar in Chapter 6, Trending Mode CORS in Chapter 7, Founder's Edition in Chapter 8 license. |
| `scripts/regenerate_pdfs.py` | **new** | reportlab generator script. Run with `python scripts/regenerate_pdfs.py` from the repo root. |

### Docs
| File | Status | Notes |
|---|---|---|
| `README.md` | **modified** | Aligned with the live ladder. Added positioning wedge, v1.7 additions, notes that the legacy `Personal/Pro/Agency` PDF tiers are no longer active. |
| `CHANGELOG-v1.7.md` | **new** | This file. Consolidates the previous internal dev log into one customer-facing release note. |
| `GEM-Launch-Playbook.html` | **modified** | Cover meta bumped to v1.7 with the explicit $9 → $149 ladder framing. |
| `GEM-30-Day-Marketing-Push.html` | **modified** | Cover meta + footer wordmark bumped to v1.7. |
| `files/README.md` | **replaced** | Now a stale-duplicate notice pointing at the root README. |

---

## SEO / AEO checklist

### Technical
- [x] One H1 per page; clean H2 → H3 hierarchy.
- [x] Canonical tag on every public page.
- [x] Open Graph + Twitter Card on every public page.
- [x] Theme color, viewport, language attributes set.
- [x] Skip link for keyboard users (`<a href="#main" class="skip-link">`).
- [x] All decorative SVGs use `aria-hidden="true"`; all functional SVGs have `role="img"` + `aria-label`.
- [x] Mobile viewport verified at 375 px; intermediate (1024 px) and desktop (1280 px) verified.
- [x] Sticky header with backdrop blur; no layout shift on scroll.
- [x] Console clean during a full section walkthrough.
- [x] No render-blocking third-party scripts; fonts via `preconnect` to `fonts.gstatic.com`.

### Structured data (JSON-LD)
- [x] `Organization` with `contactPoint` array (general, privacy, legal).
- [x] `WebSite` with `inLanguage`.
- [x] `SoftwareApplication` with `offers`, `featureList`, `softwareVersion: 1.7`.
- [x] `FAQPage` with 9 Q/A entries (Trending Mode + Roadmap added in v1.7).
- [x] `HowTo` for the five-step Ollama setup.
- [x] `BreadcrumbList` on every page.
- [x] `WebPage` entries for About / Privacy / Terms.
- [x] `AboutPage` + `ContactPage` on `about.html`.

### Crawling
- [x] `robots.txt` allows Googlebot, Bingbot, `Mediapartners-Google`, `Google-Extended`, AEO crawlers.
- [x] `robots.txt` disallows aggressive SEO scrapers (`AhrefsBot`, `SemrushBot`, `MJ12bot`, `DotBot`, `BLEXBot`, `PetalBot`, `DataForSeoBot`).
- [x] `robots.txt` disallows internal working folders (`/scripts/`, `/files/`, `/files1.6/`, `/Pitch_Deck/`, `/.claude/`).
- [x] `sitemap.xml` references all indexable pages.

---

## AdSense approval checklist

Google AdSense approval typically requires the following — all are now in place:

- [x] **Privacy policy** present and linked from every page footer (`privacy.html`).
- [x] **Terms of service** present and linked from every page footer (`terms.html`).
- [x] **About / Contact** present with at least one verifiable channel (`about.html` with four contact emails).
- [x] **Original, useful content** — landing page has 9 distinct content sections (Problem, Features, Sample, Compare, Quality, Pricing, FAQ, Roadmap, Final CTA), plus three legal/about pages totaling > 6,000 words of original copy.
- [x] **Clear navigation** — sticky header on every page, breadcrumb on legal/about pages.
- [x] **Mobile-friendly** — responsive viewport with media queries at 760 and 1140 px.
- [x] **HTTPS** — site served from `https://thegeminfo.com` (Vercel / your host).
- [x] **No prohibited content** — site sells a software product; no adult, hate, weapons, or other policy-violating content.
- [x] **`ads.txt`** present at the domain root with placeholder ready to swap for the real publisher ID.
- [x] **`Mediapartners-Google`** explicitly allowed in `robots.txt`.

When AdSense approval lands, replace the placeholder in `ads.txt` with:

```
google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
```

---

## Verification commands

```bash
# Sanity: no legacy pricing in indexable assets
grep -rE '\$(97|197|497)' landing.html about.html privacy.html terms.html

# Sanity: PDFs have zero legacy refs
python -c "
from pypdf import PdfReader
for f in ['GEM-Sales-Strategy.pdf','GEM-User-Manual.pdf']:
    r = PdfReader(f)
    t = '\n'.join((p.extract_text() or '') for p in r.pages)
    assert not any(s in t for s in ['\$97','\$197','\$497','Personal tier','Professional tier','Agency tier']), f
    print(f, 'clean')
"

# Sitemap + robots smoke test
python -m http.server 8765 --bind 127.0.0.1 &
curl -s http://127.0.0.1:8765/sitemap.xml | head
curl -s http://127.0.0.1:8765/robots.txt | head
curl -s http://127.0.0.1:8765/ads.txt
```

---

## What's not done (deliberately)

- **AdSense activation.** Until you actually apply and receive a publisher ID, `ads.txt` ships the placeholder line.
- **Brand-Guide HTML pricing.** Brand Guide doesn't reference pricing tiers — left untouched.
- **Pitch Deck.** Not audited in this pass (`/Pitch_Deck/` is excluded from indexing via `robots.txt`).
- **gem.html (the product).** The product file is the buyer's deliverable, not the marketing surface — left untouched.
- **Real founder name / address.** `terms.html` defers to "operator's home jurisdiction" so you can fill in before going live; `privacy.html` uses generic operator framing.

---

## Next steps (post-merge)

1. Replace `ads.txt` placeholder once AdSense approves.
2. Submit `sitemap.xml` to Google Search Console + Bing Webmaster Tools.
3. Verify domain ownership on Search Console / Bing.
4. (Optional) Add a small Plausible / privacy-respecting analytics snippet — update `privacy.html` § Cookies to disclose.
5. (Optional) Bundle the four contact emails as forwarding rules on `thegeminfo.com` so they don't 404.

---

*GEM Content Engine · v1.7 · thegeminfo.com · 2026-05-13*
