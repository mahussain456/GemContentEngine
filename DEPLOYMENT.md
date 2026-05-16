# Deploying `thegeminfo.com`

End-to-end walkthrough to take the repo from "live on GitHub" to "live at https://thegeminfo.com". Vercel-first because the repo ships with a tuned `vercel.json` and Vercel's free tier covers everything this site needs.

Estimated time: **15 minutes of clicking** + DNS propagation wait (5 min – 24 h).

---

## What's already in the repo (no extra work needed)

- `vercel.json` — Vercel-native routing config:
  - `/` is rewritten to serve `landing.html` (so the canonical stays clean)
  - `/app` and `/app/` serve `app/index.html` (the demo placeholder page)
  - `/landing.html` 301-redirects to `/` (avoids duplicate-URL SEO issues)
  - Security headers (X-Content-Type-Options, Referrer-Policy, Permissions-Policy) applied site-wide
  - HTML cached for 5 minutes; images / PDFs / fonts cached for 24 h with stale-while-revalidate
- `app/index.html` — brand-matched placeholder for the Try Demo CTA. CTAs route to Gumroad until the live in-browser demo ships in v1.8.
- `robots.txt`, `sitemap.xml`, `ads.txt` — all served at the domain root by default.

---

## 1. Register the domain (skip if already done)

If `thegeminfo.com` is not yet registered:

| Registrar | Why pick it | Price (.com) |
|---|---|---|
| **Cloudflare Registrar** | At-cost pricing, no upsells, easy DNS | ~$9.15/yr |
| Namecheap | Cheap year-1, decent dashboard | ~$10–13/yr |
| Porkbun | At-cost, indie-favourite | ~$10/yr |

Pick one, register, sign in. **Cloudflare** is the recommendation — at-cost domain + their DNS dashboard is the cleanest of the three.

---

## 2. Connect the repo to Vercel

1. Sign in to <https://vercel.com> with the same GitHub account that owns `mahussain456/GemContentEngine`. Use the free Hobby plan.
2. From the dashboard click **Add New… → Project**.
3. Find `GemContentEngine` in the import list. Click **Import**.
4. On the configure screen:
   - **Framework Preset:** *Other* (it's a static site — Vercel will auto-detect this).
   - **Build Command:** leave blank.
   - **Output Directory:** leave blank.
   - **Install Command:** leave blank.
   - **Root Directory:** `.` (default).
5. Click **Deploy**. First deploy takes ~30 seconds.
6. Vercel gives you a preview URL like `gem-content-engine-xyz.vercel.app`. Click it — the landing page should load, `/app/` should show the demo placeholder, `/about.html`, `/privacy.html`, `/terms.html` should all render. If any 404, the routing config didn't apply — re-check that `vercel.json` is at the repo root.

From this point on, **every push to `main` auto-deploys to production** within 30 seconds. Every PR gets a unique preview URL.

---

## 3. Add the custom domain

1. In the Vercel project, go to **Settings → Domains**.
2. Add **`thegeminfo.com`** — click Add.
3. Vercel will show you DNS records to add at your registrar. They look like:

   | Type | Name | Value |
   |---|---|---|
   | A | `@` | `76.76.21.21` |
   | CNAME | `www` | `cname.vercel-dns.com` |

   *(Vercel's IP/CNAME values are stable but always copy from your Vercel dashboard — they're the source of truth.)*

4. Also add **`www.thegeminfo.com`** in Vercel — Vercel will offer to redirect it to the apex (`thegeminfo.com`). Accept that.

---

## 4. Configure DNS at your registrar

### If you're on Cloudflare (recommended)

1. Sign in to Cloudflare → select `thegeminfo.com`.
2. Go to **DNS → Records**.
3. Add the two records Vercel gave you:
   - Type **A**, Name `@`, IPv4 `76.76.21.21`, Proxy status **DNS only** (grey cloud, not orange — Cloudflare proxying conflicts with Vercel's automatic SSL until you tune SSL settings).
   - Type **CNAME**, Name `www`, Target `cname.vercel-dns.com`, Proxy status **DNS only**.
4. Save.
5. *(Optional)* If you want Cloudflare's proxy on for analytics/CDN bonuses, switch the proxy to orange-cloud after the Vercel domain shows "Valid Configuration" — then set Cloudflare SSL to **Full (strict)** to avoid a redirect loop.

### If you're on Namecheap

1. Namecheap dashboard → Domain List → **Manage** next to `thegeminfo.com`.
2. **Advanced DNS** tab.
3. Add the two records:
   - **A Record**, Host `@`, Value `76.76.21.21`, TTL Automatic.
   - **CNAME Record**, Host `www`, Value `cname.vercel-dns.com.`, TTL Automatic.
4. Remove any default Parked / Redirect URL records Namecheap added at signup (they'll override your A record otherwise).
5. Save.

### Other registrars

The pattern is identical:
- Apex `@` → A record → `76.76.21.21`
- `www` → CNAME → `cname.vercel-dns.com`

---

## 5. Wait for DNS to propagate

Usually **5–30 minutes**. Vercel will show *"Valid Configuration"* next to the domain when ready. SSL certificate issues automatically (Let's Encrypt) within ~60 seconds of the DNS resolving.

Sanity check from your terminal while you wait:

```bash
dig thegeminfo.com +short
# Expected: 76.76.21.21 (eventually)

dig www.thegeminfo.com +short
# Expected: cname.vercel-dns.com. then resolves to Vercel IPs
```

Or visit <https://www.whatsmydns.net/#A/thegeminfo.com> to watch the A record propagate worldwide.

---

## 6. Verify the live site

Once the domain shows green in Vercel, walk these URLs in a browser and confirm:

| URL | Expected |
|---|---|
| `https://thegeminfo.com/` | Landing page renders, padlock icon (HTTPS) |
| `https://www.thegeminfo.com/` | Redirects to `https://thegeminfo.com/` |
| `https://thegeminfo.com/about.html` | About + Contact page |
| `https://thegeminfo.com/privacy.html` | Privacy Policy |
| `https://thegeminfo.com/terms.html` | Terms of Service |
| `https://thegeminfo.com/app/` | Try Demo placeholder with Gumroad CTAs |
| `https://thegeminfo.com/robots.txt` | Plain text, includes `Sitemap:` line |
| `https://thegeminfo.com/sitemap.xml` | XML with 13 URLs |
| `https://thegeminfo.com/ads.txt` | Plain text placeholder for AdSense |

If any of these break: open the Vercel project's **Deployments** tab, click the latest deploy, check the build log for errors. Most likely cause is a missing file path or a typo in `vercel.json`.

---

## 7. Submit to search engines

After the site is verified live:

1. **Google Search Console** — <https://search.google.com/search-console>
   - Add property → `https://thegeminfo.com/` → verify via DNS TXT record (Vercel can host this if needed) or via the HTML meta-tag method.
   - Submit `https://thegeminfo.com/sitemap.xml`.
2. **Bing Webmaster Tools** — <https://www.bing.com/webmasters>
   - Same flow. Once verified, import directly from Search Console with one click.

Both take 1–7 days to index. Run <https://pagespeed.web.dev/?url=https%3A%2F%2Fthegeminfo.com> the first day live to baseline your Core Web Vitals — should be all green given the static build.

---

## 8. Once GoogleAdSense approves (later)

When you get the approval email:

1. Edit `ads.txt`: replace the placeholder line with the real Google line from the AdSense dashboard. Format:

   ```
   google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
   ```

2. Add the AdSense script to `landing.html` head:

   ```html
   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
   ```

3. Commit + push to main. Vercel redeploys in ~30 seconds.

---

## Troubleshooting

**"Vercel says Invalid Configuration."**
DNS hasn't propagated yet. Wait 10 more minutes. If still red after an hour, double-check the A-record value matches Vercel's current IP (re-copy from the dashboard).

**"Site loads but `/` shows the file listing instead of the landing page."**
`vercel.json` didn't take effect. Confirm the file is at the repo root, not inside a subfolder, and that the latest commit on `main` contains it. Redeploy from the Vercel dashboard (Deployments → ⋯ → Redeploy).

**"`/app/` shows 404 instead of the placeholder."**
The `app/index.html` file didn't make it into the deployment. Verify with `git ls-tree -r HEAD | grep app/index.html` from your local repo. If missing, commit it and push.

**"HTTPS works but loads with a security warning."**
Mixed-content issue — some asset is being loaded via HTTP. The repo doesn't have any HTTP-only assets, so check if you added something recently. Browser DevTools → Console will name the offending URL.

**"Custom message in the Gumroad receipt isn't rendering line breaks."**
That's a Gumroad UI bug, not a deploy issue. Edit the message and use blank lines between paragraphs.

---

*Generated 2026-05-15 · v1.7 · paired with `vercel.json` at the repo root.*
