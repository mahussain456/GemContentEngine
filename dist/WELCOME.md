# Welcome to GEM Content Engine

Thanks for buying. This file is a 60-second on-ramp so you can ship your first content drop today.

---

## 1. Open the product

Unzip this folder somewhere you'll remember (Desktop is fine). Then **double-click `gem.html`** — it'll open in your default browser. That's the product. No installer, no account, no server.

## 2. Pick a provider

Click the **gear icon (Settings)** in the top right of GEM and choose one of:

### Option A — Ollama (free, local, fully private)

If you don't already have Ollama:

1. Download from <https://ollama.ai> for your platform.
2. Pull a model (run in a terminal):

   ```
   ollama pull qwen2.5:14b      # if you have 16 GB+ RAM
   ollama pull qwen2.5:7b       # if you have 8 GB RAM
   ```

3. Start Ollama with CORS so GEM can talk to it:

   ```
   OLLAMA_ORIGINS="*" ollama serve
   ```

4. In GEM's Settings: paste `http://localhost:11434`, pick your model, click **Test Connection**. Green dot means you're live.

### Option B — Cloud LLM (~2–5 cents per run)

Paste an API key in Settings. GEM works with OpenAI (`sk-…`), Anthropic (`sk-ant-…`), and OpenRouter (`sk-or-…`). Your key lives in your browser only — GEM has no server, so we never see it.

## 3. Generate your first drop

Pick a niche from the dropdown (12 templates ship in the box — AI tools, fitness, finance, real estate, food, etc.), drop in one specific content idea, and hit **Generate Content Drop**.

About 90 seconds later you'll have:

- A 60-second YouTube Short script
- 2 carousel outlines (Instagram + LinkedIn)
- Master image prompts for Midjourney, DALL-E 3, FLUX
- Video scene prompts for Kling AI + RunwayML
- Per-channel captions for YouTube, Instagram, Facebook, TikTok, LinkedIn, blog
- 12 hashtags and a best-time-to-post suggestion

---

## Where things live

- **Manual:** `GEM-User-Manual.pdf` — 11 chapters, deeper than this WELCOME.
- **License key:** in your Gumroad receipt email. Save it; reference it when you contact support.
- **Updates:** lifetime within v1.x. New releases land in the same email you bought with.

## When you get stuck

- Read `GEM-User-Manual.pdf` Chapter 7 (Troubleshooting). Covers the top 7 issues.
- Live FAQ: <https://thegeminfo.com/#faq>
- Email: <hello@thegeminfo.com> — usually back within 48 business hours. Founder's Edition buyers get a direct line.

## One favour

If GEM earns its keep, reply to your receipt email with a single sentence about your first published piece. Founder-cohort feedback is what builds v1.8 and v2.0.

— The GEM team
