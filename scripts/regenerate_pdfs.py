"""
Regenerate GEM-Sales-Strategy.pdf and GEM-User-Manual.pdf at v1.7
with the live pricing ladder ($9 -> $29 -> $79 -> $149).

Brand palette:
  Forest     #0E2A1F
  Pine       #1B4D3E
  MidForest  #2A6650
  Sage       #A7BFAE
  Cream      #F4EFE6
  Charcoal   #1A1A1A
  Gold       #C8A96A
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether, ListFlowable, ListItem,
)
from reportlab.platypus.flowables import HRFlowable

FOREST    = colors.HexColor('#0E2A1F')
PINE      = colors.HexColor('#1B4D3E')
MIDFOREST = colors.HexColor('#2A6650')
SAGE      = colors.HexColor('#A7BFAE')
SAGE_TINT = colors.HexColor('#D6E3DB')
MIST      = colors.HexColor('#E9F1EC')
CREAM     = colors.HexColor('#F4EFE6')
CHARCOAL  = colors.HexColor('#1A1A1A')
TEXT2     = colors.HexColor('#3A3A3A')
TEXT3     = colors.HexColor('#6E6E6E')
GOLD      = colors.HexColor('#C8A96A')
STONE     = colors.HexColor('#D8D2C7')

styles = getSampleStyleSheet()


def make_styles():
    return {
        'cover_title': ParagraphStyle(
            'cover_title', parent=styles['Heading1'], fontName='Times-Bold',
            fontSize=46, leading=52, textColor=FOREST, alignment=TA_LEFT,
            spaceAfter=8),
        'cover_sub': ParagraphStyle(
            'cover_sub', parent=styles['Normal'], fontName='Helvetica',
            fontSize=14, leading=20, textColor=TEXT2, alignment=TA_LEFT,
            spaceAfter=8),
        'cover_eyebrow': ParagraphStyle(
            'cover_eyebrow', parent=styles['Normal'], fontName='Helvetica-Bold',
            fontSize=10, leading=14, textColor=MIDFOREST, alignment=TA_LEFT,
            spaceAfter=20),
        'cover_footer': ParagraphStyle(
            'cover_footer', parent=styles['Normal'], fontName='Helvetica',
            fontSize=9, leading=12, textColor=TEXT3, alignment=TA_LEFT),
        'part_eyebrow': ParagraphStyle(
            'part_eyebrow', parent=styles['Normal'], fontName='Helvetica-Bold',
            fontSize=9, leading=12, textColor=MIDFOREST, alignment=TA_LEFT,
            spaceAfter=6),
        'h1': ParagraphStyle(
            'h1', parent=styles['Heading1'], fontName='Times-Bold',
            fontSize=28, leading=34, textColor=FOREST, alignment=TA_LEFT,
            spaceAfter=12, spaceBefore=0),
        'h2': ParagraphStyle(
            'h2', parent=styles['Heading2'], fontName='Times-Bold',
            fontSize=18, leading=24, textColor=FOREST, alignment=TA_LEFT,
            spaceAfter=8, spaceBefore=14),
        'h3': ParagraphStyle(
            'h3', parent=styles['Heading3'], fontName='Helvetica-Bold',
            fontSize=12, leading=16, textColor=PINE, alignment=TA_LEFT,
            spaceAfter=4, spaceBefore=10),
        'body': ParagraphStyle(
            'body', parent=styles['BodyText'], fontName='Helvetica',
            fontSize=10.5, leading=15, textColor=CHARCOAL, alignment=TA_LEFT,
            spaceAfter=8),
        'bullet': ParagraphStyle(
            'bullet', parent=styles['BodyText'], fontName='Helvetica',
            fontSize=10.5, leading=15, textColor=CHARCOAL, alignment=TA_LEFT,
            leftIndent=14, bulletIndent=2, spaceAfter=3),
        'small': ParagraphStyle(
            'small', parent=styles['Normal'], fontName='Helvetica',
            fontSize=8.5, leading=12, textColor=TEXT3, alignment=TA_LEFT),
        'pull': ParagraphStyle(
            'pull', parent=styles['BodyText'], fontName='Times-Italic',
            fontSize=12, leading=17, textColor=PINE, alignment=TA_LEFT,
            spaceAfter=8, spaceBefore=4, leftIndent=12, borderPadding=4),
    }


def header_footer(canvas, doc, *, title_text, version_text='v1.7', show_brand=True):
    canvas.saveState()
    # Top brand strip
    if show_brand:
        canvas.setFillColor(FOREST)
        canvas.setFont('Helvetica-Bold', 8.5)
        canvas.drawString(0.6 * inch, LETTER[1] - 0.4 * inch, 'GEM · CONTENT ENGINE')
        canvas.setFillColor(TEXT3)
        canvas.setFont('Helvetica', 8.5)
        canvas.drawRightString(LETTER[0] - 0.6 * inch, LETTER[1] - 0.4 * inch, title_text)
        canvas.setStrokeColor(STONE)
        canvas.setLineWidth(0.4)
        canvas.line(0.6 * inch, LETTER[1] - 0.5 * inch, LETTER[0] - 0.6 * inch, LETTER[1] - 0.5 * inch)
    # Footer
    canvas.setFillColor(TEXT3)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(0.6 * inch, 0.4 * inch, f'Page {doc.page}')
    canvas.drawCentredString(LETTER[0] / 2, 0.4 * inch, 'thegeminfo.com')
    canvas.drawRightString(LETTER[0] - 0.6 * inch, 0.4 * inch, version_text)
    canvas.restoreState()


def cover_page(canvas, doc, *, eyebrow, title_top, title_em, subtitle, version_text='Version 1.7'):
    canvas.saveState()
    # Cream background
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    # Gold accent line
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1.4)
    canvas.line(0.8 * inch, LETTER[1] - 0.9 * inch, 2.6 * inch, LETTER[1] - 0.9 * inch)
    # Eyebrow
    canvas.setFillColor(MIDFOREST)
    canvas.setFont('Helvetica-Bold', 10.5)
    canvas.drawString(0.8 * inch, LETTER[1] - 1.2 * inch, eyebrow)
    # Title (two-line)
    canvas.setFillColor(FOREST)
    canvas.setFont('Times-Bold', 56)
    canvas.drawString(0.8 * inch, LETTER[1] - 2.6 * inch, title_top)
    canvas.setFillColor(PINE)
    canvas.setFont('Times-BoldItalic', 56)
    canvas.drawString(0.8 * inch, LETTER[1] - 3.6 * inch, title_em)
    # Subtitle
    canvas.setFillColor(TEXT2)
    canvas.setFont('Helvetica', 14)
    text = canvas.beginText(0.8 * inch, LETTER[1] - 4.6 * inch)
    text.setLeading(20)
    for line in subtitle.split('\n'):
        text.textLine(line)
    canvas.drawText(text)
    # Hex pattern decoration in bottom right
    canvas.setStrokeColor(SAGE)
    canvas.setLineWidth(0.6)
    cx, cy, s = 6.8 * inch, 1.6 * inch, 0.5 * inch
    pts = [(cx + s, cy), (cx + s/2, cy + s*0.866), (cx - s/2, cy + s*0.866),
           (cx - s, cy), (cx - s/2, cy - s*0.866), (cx + s/2, cy - s*0.866)]
    p = canvas.beginPath(); p.moveTo(*pts[0])
    for x, y in pts[1:]: p.lineTo(x, y)
    p.close(); canvas.drawPath(p, stroke=1, fill=0)
    # Footer
    canvas.setFillColor(TEXT3)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(0.8 * inch, 0.6 * inch, version_text)
    canvas.drawRightString(LETTER[0] - 0.8 * inch, 0.6 * inch, 'thegeminfo.com')
    canvas.restoreState()


def pricing_table(s):
    data = [
        [Paragraph('<b>Tier</b>', s['small']),
         Paragraph('<b>Price</b>', s['small']),
         Paragraph('<b>For</b>', s['small']),
         Paragraph('<b>When</b>', s['small'])],
        [Paragraph('<b>Founder’s Edition</b>', s['body']),
         Paragraph('<b>$9 once</b><br/>lifetime', s['body']),
         Paragraph('Anyone willing to ship feedback', s['body']),
         Paragraph('First 100 buyers · <b>current</b>', s['body'])],
        [Paragraph('<b>Builder</b>', s['body']),
         Paragraph('<b>$29 once</b><br/>lifetime', s['body']),
         Paragraph('Solo creators & operators', s['body']),
         Paragraph('Sales 101–500', s['body'])],
        [Paragraph('<b>Operator</b>', s['body']),
         Paragraph('<b>$79 once</b><br/>lifetime', s['body']),
         Paragraph('Pro creators with multi-channel ops', s['body']),
         Paragraph('Sales 501–2,000', s['body'])],
        [Paragraph('<b>Studio</b>', s['body']),
         Paragraph('<b>$149 once</b><br/>lifetime', s['body']),
         Paragraph('Small agencies & content teams', s['body']),
         Paragraph('After 2,000 sales', s['body'])],
    ]
    t = Table(data, colWidths=[1.4*inch, 1.2*inch, 2.4*inch, 1.7*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PINE),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('FONT',       (0, 0), (-1, 0), 'Helvetica-Bold', 9),
        ('BACKGROUND', (0, 1), (-1, 1), MIST),
        ('TEXTCOLOR',  (0, 1), (-1, 1), FOREST),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',(0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 8),
    ]))
    return t


def competitor_table(s):
    rows = [
        ['Competitor', 'Price / Month', 'Their Weakness', 'GEM Advantage'],
        ['Jasper AI', '$49–$125', 'Generic, cloud-only, no video', '6 specialist agents + local'],
        ['Copy.ai', '$49–$249', 'Single-purpose, no per-channel', 'Multi-channel built-in'],
        ['ChatGPT Plus', '$20', 'Manual orchestration', 'Pipeline runs end-to-end'],
        ['Hootsuite AI', '$249–$739', 'Scheduling-first, weak gen', 'Generation-first + Quality Bar'],
        ['Pictory / Synthesia', '$23–$79', 'Video-only, no scripts', 'Full content drop'],
        ['HeyGen', '$24–$120', 'Avatar-only, no strategy', 'Strategy + script + visuals'],
    ]
    data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=[1.5*inch, 1.2*inch, 2.2*inch, 1.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    return t


def revenue_projection_table(s):
    rows = [
        ['Scenario', 'Sales / Mo', 'Tier Mix (F / B / O / S)', 'Avg ARPU', 'Monthly Revenue', 'Year 1'],
        ['Conservative', '25', '15 / 7 / 2 / 1', '~$28', '$691', '$8,292'],
        ['Realistic', '75', '40 / 25 / 8 / 2', '~$36', '$2,719', '$32,634'],
        ['Optimistic', '200', '90 / 75 / 25 / 10', '~$48', '$9,605', '$115,260'],
        ['Viral / PH spike', '500', '200 / 200 / 75 / 25', '~$53', '$26,475', '$95K+ (one-time)'],
    ]
    data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=[1.3*inch, 0.9*inch, 1.6*inch, 0.9*inch, 1.2*inch, 1.0*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    return t


def build_sales_strategy(out_path):
    s = make_styles()
    flowables = []
    def part(num, name):
        flowables.append(PageBreak())
        flowables.append(Paragraph(f'PART {num}', s['part_eyebrow']))
        flowables.append(Paragraph(name, s['h1']))
        flowables.append(HRFlowable(width='30%', thickness=1, color=GOLD, spaceAfter=14))

    # === PART ONE: Market Positioning ===
    part('ONE', 'Market Positioning')
    flowables.append(Paragraph(
        "GEM sits at the intersection of three growing markets: AI content tools, social media management, "
        "and faceless content creation. Where competition forces creators into expensive monthly subscriptions, "
        "GEM offers a one-time-purchase, self-hosted alternative — anchored on the AI &amp; tech creator wedge "
        "where trends move daily and audiences want concrete workflows.", s['body']))
    flowables.append(Paragraph('Who buys GEM', s['h3']))
    for label, body in [
        ('Solo content creators', 'Faceless YouTubers, Instagram theme-page operators, and TikTok creators who run 1–5 channels and want to scale output without hiring writers.'),
        ('Small agencies (1–10 people)', 'Social media agencies managing 5–30 client channels who need consistent quality without paying $300+/month per seat for Jasper, Copy.ai, or Hootsuite AI.'),
        ('Faceless brand operators', 'People running 3–10 niche brand accounts — the original buyer profile GEM was built around.'),
        ('Course creators &amp; coaches', 'Content marketers who need polished scripts, image generation prompts, and per-platform copy to fuel their funnel.'),
        ('AI-curious builders', 'Operators who want to own their tools and avoid SaaS lock-in. The single-HTML-file architecture is a feature for this group.'),
    ]:
        flowables.append(Paragraph(f'<b>{label}.</b> {body}', s['bullet'], bulletText='❖'))
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph('Competition analysis', s['h3']))
    flowables.append(competitor_table(s))

    # === PART TWO: Pricing Strategy ===
    part('TWO', 'Pricing Strategy')
    flowables.append(Paragraph(
        "GEM ships with a four-rung lifetime ladder. The Founder’s Edition is a deliberate loss-leader "
        "for feedback — the math compounds once the price ratchets through each tier. Pricing on the live "
        "site (thegeminfo.com) is the source of truth.", s['body']))
    flowables.append(Spacer(1, 8))
    flowables.append(pricing_table(s))
    flowables.append(Spacer(1, 14))
    flowables.append(Paragraph('Why this ladder works', s['h3']))
    for label, body in [
        ('$9 Founder’s Edition', 'Removes price as the reason a curious early adopter doesn’t try GEM today. Buys feedback, not revenue. Hard-capped at 100 buyers.'),
        ('$29 Builder', 'Still impulse-buy territory, with the social proof of 100 founders already shipped. Most volume sits here.'),
        ('$79 Operator', 'The legitimate "I run a real content operation" price. Compares favorably to ~1.5 months of Jasper.'),
        ('$149 Studio', 'Small agency / multi-brand ceiling. Includes commercial license. Sets up future white-label tier without committing today.'),
    ]:
        flowables.append(Paragraph(f'<b>{label}.</b> {body}', s['bullet'], bulletText='→'))

    # === PART THREE: Alternative Pricing Models ===
    part('THREE', 'Alternative Pricing Models')
    flowables.append(Paragraph(
        "If the four-rung ladder doesn’t fit your appetite for risk, here are the alternatives we considered and "
        "deliberately rejected.", s['body']))
    alt_rows = [
        ['Model', 'Price', 'Best for', 'Trade-off'],
        ['Single flat price', '$49', 'Simple positioning, fast launch', 'No FOMO, no founder loop'],
        ['Lifetime deal (AppSumo)', '$39 (capped)', 'Mass distribution', '~70% revenue share'],
        ['Subscription', '$9/mo', 'Predictable MRR', 'Conflicts with the privacy-first ethos'],
        ['Done-with-you', '$1,500+', 'High-touch enterprise', 'Slow cycle, requires demos'],
        ['Pay-what-you-want', '$0–$??', 'PR splash, viral pricing', 'Gross revenue usually 1/3 of fixed'],
    ]
    alt_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(alt_rows)]
    alt_t = Table(alt_data, colWidths=[1.6*inch, 1.2*inch, 2.0*inch, 2.0*inch])
    alt_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    flowables.append(alt_t)
    flowables.append(Spacer(1, 14))
    flowables.append(Paragraph('Final recommendation', s['h3']))
    flowables.append(Paragraph(
        "<b>$9 → $29 → $79 → $149.</b> The four-rung lifetime ladder is the production strategy. "
        "Use Founder’s Edition as marketing default — every page on thegeminfo.com leads with $9 and the "
        "100-seat counter creates honest scarcity.", s['body']))

    # === PART FOUR: How to Sell GEM ===
    part('FOUR', 'How to Sell GEM')
    flowables.append(Paragraph('Sales platforms', s['h3']))
    for label, body in [
        ('Gumroad', 'Best for launch + lifetime sales. ~10% fee. Built-in audience for digital tools. Recommended primary SKU for the $9 Founder’s Edition.'),
        ('Lemon Squeezy', 'Best for global tax handling. They are merchant of record. ~5% + $0.50.'),
        ('Stripe + your own site', 'Lowest fees (~2.9% + $0.30). Requires building checkout.'),
        ('AppSumo', 'Massive volume launch only. They take 70% but deliver 1,000–5,000 sales in 30 days.'),
        ('Whop / Cosmos', 'Audience-first communities. Better fit for Studio tier with Discord access.'),
    ]:
        flowables.append(Paragraph(f'<b>{label}.</b> {body}', s['bullet'], bulletText='❖'))
    flowables.append(Spacer(1, 8))
    flowables.append(Paragraph('Marketing channels', s['h3']))
    channels = [
        ['Channel', 'Tactic', 'Expected ROI'],
        ['Twitter / X', 'Build-in-public threads showing pipeline output', 'High — viral potential'],
        ['YouTube tutorials', 'Show GEM running, generating real assets', 'Highest — buyers see proof'],
        ['Reddit', 'r/Entrepreneur, r/sidehustle, r/AItools', 'Medium — strict rules'],
        ['Indie Hackers', 'Launch story + lessons learned', 'Medium — supportive audience'],
        ['Product Hunt', 'One-day spike on Founder pricing', 'High — needs prep'],
        ['Newsletter sponsorships', 'AI/marketing newsletters $50–$500/issue', 'Medium–High'],
        ['Affiliate program', '30% commission to creators who promote', 'Compounds over time'],
        ['Cold DM agency owners', 'Personalized DMs with the live sample', 'Low scale, high conversion'],
    ]
    ch_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(channels)]
    ch_t = Table(ch_data, colWidths=[1.4*inch, 3.4*inch, 1.8*inch])
    ch_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    flowables.append(ch_t)

    # === PART FIVE: Sales Page Copy ===
    part('FIVE', 'Sales Page Copy')
    flowables.append(Paragraph('Headline options', s['h3']))
    for h in [
        '"One idea. Every channel. Six AI agents." — GEM’s live hero.',
        '"Stop paying $50/month for generic AI content. Own your tool forever."',
        '"The daily content drop for AI &amp; tech creators — runs on your laptop, never expires."',
        '"A complete content pack in 90 seconds. Forever, for nine dollars."',
    ]:
        flowables.append(Paragraph(h, s['bullet'], bulletText='→'))
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph('Three-paragraph pitch', s['h3']))
    flowables.append(Paragraph(
        "<b>Hook.</b> You’re running multiple content channels. YouTube, Facebook, Instagram, maybe a blog. "
        "Every week you need ideas, scripts, hashtags, image prompts, video prompts — and you’re paying "
        "$50–$200/month for AI tools that produce generic output.", s['body']))
    flowables.append(Paragraph(
        "<b>Reveal.</b> GEM is different. Six AI agents work in sequence: Brand sets voice, Scout pulls live trends "
        "(Reddit/HN/Google Trends with a documented r/popular fallback), Architect structures the piece, Writer "
        "drafts the script, Visual writes prompts for Midjourney/DALL-E/FLUX/Kling/RunwayML, and Adapter rewrites "
        "for each platform. Each agent’s output is graded against a six-rule Quality Bar before the next runs.", s['body']))
    flowables.append(Paragraph(
        "<b>Close.</b> One-time purchase. Lifetime updates. Runs locally on Ollama or any cloud LLM. Compare to "
        "Jasper at $1,500/year or Hootsuite at $9,000/year. GEM is $9 once during Founder’s Edition, then "
        "$29 / $79 / $149 as the cohort grows. That’s the difference between renting and owning.", s['body']))
    flowables.append(Spacer(1, 8))
    flowables.append(Paragraph('Bullets for the landing page', s['h3']))
    for b in [
        '6 specialist AI agents — Brand, Scout, Architect, Writer, Visual, Adapter',
        'Master prompts for Midjourney v6, DALL-E 3, FLUX.1, Kling AI, RunwayML',
        'Per-channel adaptation — YouTube, IG, FB, TikTok, LinkedIn, blog',
        'Trending Mode — live Reddit / HackerNews signals (Google Trends via r/popular fallback)',
        'Quality Bar — every agent’s output graded before the next runs',
        '100% local on Ollama, or BYO key for OpenAI / Anthropic / OpenRouter',
        'Designer-grade PDF export, JSON save/load, 12 niche templates',
        'Founder’s Edition commercial-use license included',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='✓'))

    # === PART SIX: Product Roadmap ===
    part('SIX', 'Product Roadmap')
    flowables.append(Paragraph('Shipped in v1.7 (now live on thegeminfo.com)', s['h3']))
    for b in [
        'Quality Bar checks — six rules every drop must clear before publish',
        '"Today’s Brief" sample on landing — real AI / tech niche pack',
        'Roadmap teaser + Founder voting on what ships next',
        'Trending Mode CORS honesty surfaced directly in the live FAQ',
        'Founder credibility line + AI Decoded / Tools That Work case-study fuel',
        'Legacy three-tier launch ladder fully removed from public copy',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='✓'))
    flowables.append(Paragraph('Next quick wins (v1.8 — 2–3 weeks)', s['h3']))
    for b in [
        'Image generation in-app via Replicate / Together AI',
        'Search &amp; filter in the Library once it grows past 20+ pieces',
        'A/B title generator — 5 alternatives per piece',
        'Custom niche slot — user-defined niches beyond the built-in 12',
        'PDF custom branding — user logo / colors on the export cover',
        'YouTube comment scraper as a trending signal',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='→'))
    flowables.append(Paragraph('Major modules (v2.0 — 2–3 months)', s['h3']))
    for b in [
        'Daily auto-brief — ranked content brief delivered every morning',
        'Approval workflow — approve / edit / regenerate / reject + version history',
        'Direct publish — push approved drops to Buffer / Later / Meta / YouTube',
        'Performance loop — yesterday’s winners feed tomorrow’s brief',
        'Team collaboration — multi-user (still local), comments, role-based approvals',
        'Audio generation — ElevenLabs script-to-voiceover',
        'Custom agent builder — power users define their own agents',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='→'))

    # === PART SEVEN: Revenue Projections ===
    part('SEVEN', 'Revenue Projections')
    flowables.append(Paragraph(
        "Projections recalibrated for the $9 → $29 → $79 → $149 ladder. Founder’s Edition "
        "is a hard-capped 100 seats; everything past that ratchets up.", s['body']))
    flowables.append(Spacer(1, 8))
    flowables.append(revenue_projection_table(s))
    flowables.append(Spacer(1, 14))
    flowables.append(Paragraph('Ladder math — cumulative gross at each rung', s['h3']))
    for b in [
        '100 Founders × $9 = <b>$900</b> (cohort-builder, deliberate loss-leader)',
        '400 Builders × $29 = <b>$11,600</b>',
        '1,500 Operators × $79 = <b>$118,500</b>',
        '2,000 Studios × $149 = <b>$298,000</b>',
        'Cumulative ceiling: <b>~$429K gross</b> at ~95% margin across the four rungs.',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='→'))
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph('Cost structure', s['h3']))
    cost_rows = [
        ['Cost', 'Per Month', 'Notes'],
        ['Hosting', '$0–$20', 'Vercel / Cloudflare static; Gumroad checkout'],
        ['Email service', '$0–$30', 'ConvertKit or Buttondown'],
        ['Discord (community)', '$0', 'Nitro Server Boost optional'],
        ['Domain', '~$1', '$12/year'],
        ['Payment processing', '~3–10%', 'Gumroad ~10% / Stripe ~3% / Lemon Squeezy ~5%+$0.50'],
    ]
    cost_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(cost_rows)]
    cost_t = Table(cost_data, colWidths=[1.5*inch, 1.2*inch, 3.9*inch])
    cost_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    flowables.append(cost_t)

    # === BUILD ===
    doc = SimpleDocTemplate(
        out_path, pagesize=LETTER,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.8*inch, bottomMargin=0.7*inch,
        title='GEM Content Engine — Sales Strategy & Pricing (v1.7)',
        author='GEM Content Engine',
    )

    def first_page(c, d):
        cover_page(c, d,
            eyebrow='CONFIDENTIAL · BUSINESS BLUEPRINT · v1.7',
            title_top='Sales Strategy',
            title_em='& Pricing.',
            subtitle='How to package, position, and price GEM for sale.\n'
                     'Aligned with the live $9 → $29 → $79 → $149 ladder.')
    def later_pages(c, d):
        header_footer(c, d, title_text='SALES BLUEPRINT')

    doc.build(flowables, onFirstPage=first_page, onLaterPages=later_pages)


def build_user_manual(out_path):
    s = make_styles()
    flowables = []

    def chapter(num_word, name):
        flowables.append(PageBreak())
        flowables.append(Paragraph(f'CHAPTER {num_word}', s['part_eyebrow']))
        flowables.append(Paragraph(name, s['h1']))
        flowables.append(HRFlowable(width='30%', thickness=1, color=GOLD, spaceAfter=14))

    # === Chapter 1: Welcome ===
    chapter('ONE', 'Welcome to GEM')
    flowables.append(Paragraph(
        "GEM is a self-hosted AI content engine that turns a single content idea into a complete, "
        "platform-ready package for every channel you manage. It runs in any modern browser — entirely "
        "local on Ollama, or against any cloud LLM (OpenAI, Anthropic, OpenRouter) with your own key. "
        "No GEM servers. No data leaves your computer unless you choose a cloud provider.", s['body']))
    flowables.append(Paragraph(
        "Where most AI tools give you a generic blog post or a single caption, GEM orchestrates six "
        "specialist agents in sequence to produce: brand strategy, viral topic intelligence, a structured "
        "framework, a humanized voiceover script, master image and video prompts for every aspect ratio, "
        "and individually tailored copy for each of your YouTube, Facebook, Instagram, TikTok, LinkedIn, "
        "and blog channels.", s['body']))
    flowables.append(Paragraph('What makes GEM different', s['h3']))
    cmp_rows = [
        ['', 'Generic AI Tools', 'GEM Content Engine'],
        ['Cost', '$20–$100 / month forever', 'One-time purchase · $9 Founder’s Edition'],
        ['Privacy', 'Your data trains their AI', '100% local via Ollama (or BYO cloud key)'],
        ['Output', 'One generic blog post', '6 agents · 17+ asset types per run'],
        ['Channel-aware', 'Same copy for everywhere', 'Adapted per channel and per audience'],
        ['Image prompts', 'Basic text descriptions', 'Master prompts for MJ v6, DALL-E 3, FLUX.1'],
        ['Video prompts', 'Not included', 'Kling AI + RunwayML, scene-by-scene'],
        ['Script quality', 'Robotic, listicle-style', 'Humanized, conversational, graded by Quality Bar'],
        ['Trending data', 'LLM guesses', 'Live Reddit / HN (with r/popular fallback for Google Trends)'],
    ]
    cmp_data = [[Paragraph(f'<b>{c}</b>' if r == 0 or col == 0 else c, s['small']) for col, c in enumerate(row)] for r, row in enumerate(cmp_rows)]
    cmp_t = Table(cmp_data, colWidths=[1.4*inch, 2.5*inch, 2.7*inch])
    cmp_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    flowables.append(cmp_t)

    # === Chapter 2: The Six AI Agents ===
    chapter('TWO', 'The Six AI Agents')
    flowables.append(Paragraph(
        "GEM’s pipeline runs six specialist agents in sequence. Each agent has one job, hands its "
        "structured output down the line, and produces a downloadable report. The Quality Bar grades "
        "each agent’s output against six rules before the next agent runs.", s['body']))
    for n, h, desc in [
        ('1', 'Brand Brain — Channel strategy · voice · pillars',
         'Analyzes your channels and niche, produces brand voice doc, 3–5 content pillars, audience definition, competitive positioning, and the anchor hook used by every downstream agent.'),
        ('2', 'Trend Scout — Viral topic discovery',
         'Pulls live signals from Reddit and HackerNews (CORS-friendly). Google Trends falls back to r/popular (documented in Chapter 7). Ranks 5–6 topic candidates by viral score, estimated views, competition, and platform fit.'),
        ('3', 'Content Architect — Structure &amp; retention hooks',
         'Designs section-by-section structure with timestamped scenes, retention hooks at 30s / 2m / 5m, SEO title, thumbnail concept, upload timing, and revenue estimate per 1,000 views.'),
        ('4', 'Script Writer — Humanized voiceover',
         'Writes scripts that pass the Quality Bar two-second-hook test: natural speech, contractions, [pause] markers, rhetorical questions, sentences starting with "And/But/Look", tension-before-reveal pacing.'),
        ('5', 'Visual Director — Master prompts (the flagship agent)',
         'Ultra-detailed 4K master prompts for Midjourney v6, DALL-E 3 / Imagen, and FLUX.1 across every format you need: thumbnail, IG post, IG story, FB cover, YT banner, blog hero. Plus scene-by-scene Kling AI and RunwayML video prompts.'),
        ('6', 'Channel Adapter — Per-channel content',
         'Takes the master content and produces individually adapted copy for every channel you have configured. Each Facebook page gets its own caption. Each Instagram page gets its own Reel hook and hashtags. YouTube SEO package, blog intro — all platform-perfect.'),
    ]:
        flowables.append(Paragraph(f'<b>{n}. {h}</b>', s['h3']))
        flowables.append(Paragraph(desc, s['body']))

    # === Chapter 3: Setup & Installation ===
    chapter('THREE', 'Setup &amp; Installation')
    flowables.append(Paragraph('System requirements', s['h3']))
    sys_rows = [
        ['Component', 'Minimum', 'Recommended'],
        ['Operating system', 'Win 10 / macOS 11 / Linux', 'Any 64-bit OS'],
        ['RAM (Ollama mode)', '8 GB (7B models)', '16–32 GB (14B+ models)'],
        ['RAM (cloud mode)', '4 GB', '8 GB'],
        ['Disk', '10 GB free', '50 GB for multiple Ollama models'],
        ['CPU', 'Modern x86_64 / ARM64', 'Apple Silicon / Ryzen / Core i7+'],
        ['GPU', 'Not required', 'NVIDIA GPU dramatically speeds inference'],
        ['Browser', 'Chrome 100+ / Firefox 100+', 'Latest Chrome or Edge'],
    ]
    sys_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(sys_rows)]
    sys_t = Table(sys_data, colWidths=[1.8*inch, 2.2*inch, 2.6*inch])
    sys_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FOREST),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 0.3, STONE),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',(0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
    ]))
    flowables.append(sys_t)
    flowables.append(Spacer(1, 12))
    flowables.append(Paragraph('Local mode (Ollama) — 5 steps', s['h3']))
    for n, txt in [
        ('1', 'Install Ollama from <font color="#1B4D3E">ollama.ai</font>. On macOS / Linux: <font face="Courier">curl -fsSL https://ollama.ai/install.sh | sh</font>'),
        ('2', 'Pull a model. For 16 GB+ systems: <font face="Courier">ollama pull qwen2.5:14b</font>. For 8 GB systems: <font face="Courier">ollama pull qwen2.5:7b</font>.'),
        ('3', 'Start Ollama with CORS so the GEM browser interface can talk to it: <font face="Courier">OLLAMA_ORIGINS="*" ollama serve</font>'),
        ('4', 'Open <font face="Courier">gem.html</font> in your browser. Click Configure → Ollama → paste <font face="Courier">http://localhost:11434</font> → choose your model → Test connection. Green dot means success.'),
        ('5', 'Add your channels in the left sidebar. Channels live in your browser only — nothing is sent anywhere.'),
    ]:
        flowables.append(Paragraph(f'<b>Step {n}.</b> {txt}', s['bullet'], bulletText='❖'))
    flowables.append(Spacer(1, 6))
    flowables.append(Paragraph('Cloud mode (BYO key) — 1 step', s['h3']))
    flowables.append(Paragraph(
        "Open <font face=\"Courier\">gem.html</font> → Settings → Provider → pick OpenAI, Anthropic, "
        "or OpenRouter → paste your key. A full pipeline run costs roughly $0.02–$0.05 on gpt-4o-mini "
        "or $0.12 on Claude Sonnet. Keys live in your browser only; GEM never sees them.", s['body']))

    # === Chapter 4: Daily Workflow ===
    chapter('FOUR', 'Daily Workflow')
    flowables.append(Paragraph(
        "Once setup is complete, your daily workflow takes 5–10 minutes for a complete content drop. "
        "Quality Bar checks run automatically between agents — you can’t ship a generic hook by accident.", s['body']))
    for n, h, desc in [
        ('1', 'Pick a niche', 'On the welcome screen, choose your niche from the 12 templates or type a custom one. The more specific the input, the sharper the output.'),
        ('2', 'Toggle Trending Mode (optional)', 'On the welcome screen, flip the Trending Mode toggle to pull live Reddit / HackerNews signals. Google Trends falls back to r/popular per the disclosure in Chapter 7.'),
        ('3', 'Hit Generate', 'Click Generate Content Drop. Watch the agent activity log on the right — each agent reports in as it completes. Quality Bar gates are visible between agents.'),
        ('4', 'Review the drop', 'You’ll get script + image prompts + video prompts + per-channel captions + carousels + a 30-day calendar slot suggestion. Approve or edit each asset.'),
        ('5', 'Export', 'Designer-grade PDF, JSON (.gem.json), or copy-paste directly into your scheduler. The PDF is brand-styled.'),
    ]:
        flowables.append(Paragraph(f'<b>{n}. {h}.</b> {desc}', s['bullet'], bulletText='→'))

    # === Chapter 5: Feature Reference ===
    chapter('FIVE', 'Complete Feature Reference')
    flowables.append(Paragraph(
        "Each pipeline run produces 17+ asset types. Below is the full list by agent.", s['body']))
    for h, items in [
        ('Brand Brain', ['Brand voice document', 'Content pillars (3–5)', 'Audience definition + persona', 'Competitive positioning', 'Anchor hook for the pipeline']),
        ('Trend Scout', ['Ranked topic candidates (5–6)', 'Viral score + estimated views', 'Live Reddit / HackerNews signals', 'Google Trends via r/popular fallback']),
        ('Content Architect', ['Section-by-section structure', 'Timestamped retention hooks', 'SEO title + thumbnail concept', 'Optimal upload timing']),
        ('Script Writer', ['Humanized voiceover script', 'Hook → setup → reveal → close pacing', 'Two-second-hook check']),
        ('Visual Director', ['Midjourney v6 master prompts (every aspect ratio)', 'DALL-E 3 / Imagen prompts (5 per piece)', 'FLUX.1 prompts', 'Kling AI scene prompts', 'RunwayML scene prompts', 'Multi-slide Instagram + LinkedIn carousels']),
        ('Channel Adapter', ['YouTube SEO title + description + tags', 'Instagram caption + Reel hook + cover text', 'Facebook hook + caption', 'TikTok / Shorts hook', 'LinkedIn post', 'Blog title + meta + intro']),
    ]:
        flowables.append(Paragraph(f'<b>{h}</b>', s['h3']))
        for it in items:
            flowables.append(Paragraph(it, s['bullet'], bulletText='✓'))

    # === Chapter 6: Power Features (v1.7) ===
    chapter('SIX', 'Power Features (v1.7)')
    for h, body in [
        ('Quality Bar (new in v1.7)',
         'Six rules every drop must clear: one clear idea per post, two-second hook, specific examples not generic advice, on-brand visuals, business-goal CTA, human approval beat. Each agent’s output is graded automatically before the next runs.'),
        ('"Today’s Brief" sample (new in v1.7)',
         'The live landing page now ships a real "AI agents replacing office work" pack so prospects see exactly what GEM hands them. You can render the same demo locally by loading the bundled .gem.json from the templates folder.'),
        ('Roadmap voting (new in v1.7)',
         'Founder’s Edition buyers vote on what ships next. The four big modules in development: daily auto-brief, approval workflow, direct publish to Buffer / Later / Meta, performance loop.'),
        ('Trending Mode',
         'Live scraping of Reddit and HackerNews directly in your browser. Google Trends has stricter CORS and falls back to r/popular as a trending proxy — covers 95% of niches. Run a one-line local proxy for unrestricted Google Trends; see Chapter 7.'),
        ('Photo Post Prompts',
         '5 ready-to-paste ChatGPT / DALL-E 3 / Imagen prompts per piece for IG Feed, IG Reel, FB, TikTok, LinkedIn.'),
        ('Carousel Generator',
         'Multi-slide IG + LinkedIn carousels with role (Hook / Setup / Reveal / CTA), slide headline, and ChatGPT image prompt per slide.'),
        ('Brand Kit',
         'Color picker with hex input, native picker, and 8 preset palettes (Forest, Ocean, Sunset, Royal, Rose, Mono, Earth, Mint). Brand flows into every Visual prompt.'),
        ('My Library',
         'Auto-saved content history. Click any past piece to instantly reload it. Search and filter coming in v1.8.'),
        ('30-Day Calendar',
         'AI-generated content calendar across all your platforms in 60 seconds. Drag-to-reorder, with per-platform best-time-to-post suggestions.'),
        ('Tone Presets',
         'Balanced / Educational / Entertaining / Controversial / Inspirational. One-click voice swap.'),
        ('Channel Export / Import',
         'JSON download / upload of channel configs. Cross-device sync, team handoff, backup.'),
    ]:
        flowables.append(Paragraph(f'<b>{h}</b>', s['h3']))
        flowables.append(Paragraph(body, s['body']))

    # === Chapter 7: Troubleshooting ===
    chapter('SEVEN', 'Troubleshooting')
    for h, body in [
        ('Ollama "Connection failed" with green-dot test',
         'You probably forgot to start Ollama with CORS enabled. Quit Ollama and relaunch with <font face="Courier">OLLAMA_ORIGINS="*" ollama serve</font> in a terminal.'),
        ('Trending Mode shows only r/popular signals',
         'This is expected behavior when Google Trends is blocked by CORS — documented in the public FAQ. Reddit and HackerNews still work directly. For unrestricted Google Trends, run a one-line local proxy: <font face="Courier">npx cors-anywhere</font> on port 8080, then point Trending Mode at <font face="Courier">http://localhost:8080</font>.'),
        ('Cloud mode shows "Invalid API key"',
         'Check the key starts with the right prefix (<font face="Courier">sk-</font> for OpenAI, <font face="Courier">sk-ant-</font> for Anthropic). For OpenRouter, your key starts with <font face="Courier">sk-or-</font>. Keys are stored in your browser only — paste fresh ones if you rotate.'),
        ('Pipeline stalls between agents',
         'Quality Bar may be rejecting an agent’s output. Open the agent activity log on the right — it will show which rule failed and let you regenerate that specific agent without re-running upstream.'),
        ('Image prompts come out generic',
         'Your Brand Kit is probably empty. Fill in colors + style notes + 2–3 reference adjectives before running the pipeline; the Visual agent uses them on every prompt.'),
        ('PDF export is blank',
         'Browser print blocked custom fonts. Switch to Chrome / Edge and re-export. If still blank, open Settings → Export → "Use system fonts" and try again.'),
        ('Saved .gem.json won’t load',
         'File was edited externally. Re-export from the Library with the original file selected, or restore from My Library auto-save (last 30 runs are kept).'),
    ]:
        flowables.append(Paragraph(f'<b>{h}</b>', s['h3']))
        flowables.append(Paragraph(body, s['body']))

    # === Chapter 8: License & Final Notes ===
    chapter('EIGHT', 'License &amp; Final Notes')
    flowables.append(Paragraph('Your license', s['h3']))
    flowables.append(Paragraph(
        "Your purchase of GEM grants you a lifetime license to use the tool for personal and commercial "
        "content creation. Use it for your own brand, your clients, your agency, and your team. The single "
        "HTML file is yours to keep, modify, and integrate into your workflow forever — no recurring "
        "fees, no expiration, no telemetry. Founder’s Edition includes the commercial-use license.", s['body']))
    flowables.append(Paragraph('What’s included', s['h3']))
    for b in [
        'The complete gem.html file (single self-contained app)',
        'This v1.7 user manual PDF',
        'Lifetime updates within the v1.x major version',
        'Discord community access for users',
        'Direct line to the founder for feedback (Founder’s Edition)',
        'Email support for setup issues (first 30 days)',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='✓'))
    flowables.append(Paragraph('Privacy promise', s['h3']))
    flowables.append(Paragraph(
        "GEM runs 100% locally on Ollama mode. Your channel configurations, content ideas, generated scripts, "
        "and prompts never leave your computer. We have no servers, no analytics, no telemetry. The only "
        "network calls made by GEM in Ollama mode are between your browser and your local Ollama instance. "
        "In cloud mode, prompts go to your chosen provider (OpenAI / Anthropic / OpenRouter) and nowhere else "
        "— GEM has no intermediary server.", s['body']))
    flowables.append(Paragraph('A note from the creator', s['h3']))
    flowables.append(Paragraph(
        "<i>GEM exists because the AI tooling market is structured against creators. You pay $20–$100 "
        "a month for tools that own your data, lock you into their cloud, and produce output indistinguishable "
        "from a thousand other creators using the same prompts. GEM flips that: one fair price, your data stays "
        "yours, and the output is uniquely tuned to your channels. Make great content. Build your audience. "
        "Keep your data. — The GEM team.</i>", s['pull']))

    # === BUILD ===
    doc = SimpleDocTemplate(
        out_path, pagesize=LETTER,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.8*inch, bottomMargin=0.7*inch,
        title='GEM Content Engine — User Manual (v1.7)',
        author='GEM Content Engine',
    )

    def first_page(c, d):
        cover_page(c, d,
            eyebrow='COMPLETE FEATURE GUIDE · v1.7 · LOCAL OR CLOUD',
            title_top='User Manual.',
            title_em='Six agents.',
            subtitle='AI-powered content generation for multi-channel brands.\n'
                     'One idea. Every channel. Six AI agents. Forever.')
    def later_pages(c, d):
        header_footer(c, d, title_text='USER MANUAL')

    doc.build(flowables, onFirstPage=first_page, onLaterPages=later_pages)


if __name__ == '__main__':
    import os
    base = r'D:\AI_Stuff\Gem_Content_Machine'
    sales = os.path.join(base, 'GEM-Sales-Strategy.pdf')
    manual = os.path.join(base, 'GEM-User-Manual.pdf')
    print(f'Writing {sales} ...')
    build_sales_strategy(sales)
    print(f'Writing {manual} ...')
    build_user_manual(manual)
    print('Done.')
