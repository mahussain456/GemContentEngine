"""
Regenerate GEM-Sales-Strategy.pdf, GEM-User-Manual.pdf, and
GEM-Fulfillment-Playbook.pdf at v1.7 with the live pricing ladder
($9 -> $29 -> $79 -> $149).

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
    KeepTogether, ListFlowable, ListItem, Preformatted,
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
        'code': ParagraphStyle(
            'code', parent=styles['Code'], fontName='Courier',
            fontSize=8.5, leading=11.5, textColor=FOREST,
            backColor=MIST, borderColor=SAGE_TINT, borderWidth=0.5,
            borderPadding=8, leftIndent=0, rightIndent=0, spaceAfter=10,
            spaceBefore=4),
        'callout': ParagraphStyle(
            'callout', parent=styles['BodyText'], fontName='Helvetica',
            fontSize=10, leading=14, textColor=CHARCOAL, alignment=TA_LEFT,
            backColor=MIST, borderColor=GOLD, borderWidth=0,
            borderPadding=10, leftIndent=0, rightIndent=0,
            spaceAfter=10, spaceBefore=4),
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


def build_fulfillment_playbook(out_path):
    """Seller-facing fulfillment playbook: how to package, generate keys, deliver,
    support, refund, and run ongoing operations. v1.7."""
    s = make_styles()
    flowables = []

    def part(num_word, name):
        flowables.append(PageBreak())
        flowables.append(Paragraph(f'PART {num_word}', s['part_eyebrow']))
        flowables.append(Paragraph(name, s['h1']))
        flowables.append(HRFlowable(width='30%', thickness=1, color=GOLD, spaceAfter=14))

    def appendix(letter, name):
        flowables.append(PageBreak())
        flowables.append(Paragraph(f'APPENDIX {letter}', s['part_eyebrow']))
        flowables.append(Paragraph(name, s['h1']))
        flowables.append(HRFlowable(width='30%', thickness=1, color=GOLD, spaceAfter=14))

    def code_block(text):
        # Preformatted keeps whitespace exactly; we use the 'code' paragraph style.
        flowables.append(Preformatted(text, s['code']))

    # ═══════════════════════════════════════════════════════════════
    # PART ONE — The fulfillment flow
    # ═══════════════════════════════════════════════════════════════
    part('ONE', 'The Fulfillment Flow')
    flowables.append(Paragraph(
        "GEM is a digital product sold one-time, fulfilled instantly, supported lightly. "
        "Every order should move from <i>card charged</i> to <i>customer using the product</i> "
        "in under ten minutes with zero manual work from you. This part is the high-level map "
        "before the rest of the playbook drills into each step.", s['body']))

    flowables.append(Paragraph('The happy path — what happens for every sale', s['h3']))
    for n, h, body in [
        ('1', 'Buyer pays on Gumroad', 'Buyer hits "Get GEM — $9" on the landing page, types card details, clicks pay. Gumroad charges, generates the unique license key (auto), and triggers download.'),
        ('2', 'Buyer downloads the ZIP', 'Gumroad serves the bundled ZIP directly from its CDN. No action from you. The ZIP contains gem.html, the user manual PDF, the LICENSE.txt with their key, and a WELCOME.md.'),
        ('3', 'Gumroad emails the receipt + key', 'The receipt email includes the license key inline (handy for buyers who lose the ZIP). The same email contains a re-download link valid forever.'),
        ('4', 'Buyer opens gem.html', 'The product runs locally in their browser. No account, no server-side activation — the license is on the seller side, not the product side (see Part 4).'),
        ('5', 'You log the sale &amp; bump the counter', 'Update SEATS_REMAINING in landing.html as the Founder cohort fills. Add the order to your seller ledger (Part 8). Send the 24-hour follow-up email if they haven\'t opened gem.html yet (optional).'),
    ]:
        flowables.append(Paragraph(f'<b>{n}. {h}.</b> {body}', s['bullet'], bulletText='→'))

    flowables.append(Paragraph('What every buyer receives (the four artifacts)', s['h3']))
    artifacts = [
        ['Artifact', 'Format', 'Purpose'],
        ['gem.html', 'Single 330 KB HTML file', 'The product. Runs locally in any modern browser.'],
        ['GEM-User-Manual.pdf', '11-page PDF', 'Setup, daily workflow, troubleshooting, license terms.'],
        ['LICENSE-{order-id}.txt', '1 KB plain text', 'Their unique license key, purchase date, tier, support eligibility.'],
        ['WELCOME.md', '~2 KB markdown', '60-second getting-started: open gem.html, configure Ollama or cloud key, run first pipeline.'],
    ]
    art_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(artifacts)]
    art_t = Table(art_data, colWidths=[1.8*inch, 1.5*inch, 3.4*inch])
    art_t.setStyle(TableStyle([
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
    flowables.append(art_t)
    flowables.append(Spacer(1, 12))
    flowables.append(Paragraph(
        "<b>Service-level promises.</b> Auto-fulfillment within seconds of payment. License key delivered in the same email. "
        "First support reply within 48 hours business days. Founder's Edition buyers (first 100) get a direct line to the founder.",
        s['body']))

    # ═══════════════════════════════════════════════════════════════
    # PART TWO — The seller stack
    # ═══════════════════════════════════════════════════════════════
    part('TWO', 'The Seller Stack')
    flowables.append(Paragraph(
        "You don’t need a custom backend. Pick one merchant-of-record platform and let it do the heavy lifting: "
        "checkout, tax, fraud, license keys, refunds, file hosting, email receipts. Below is the decision matrix and the "
        "recommended setup.", s['body']))

    stack_rows = [
        ['Platform', 'Fee', 'License keys', 'Tax / VAT', 'Verdict for $9 indie launch'],
        ['Gumroad', '~10% per sale', 'Built-in toggle', 'Handled by Gumroad', '★ Recommended. Cheapest setup, fastest go-live.'],
        ['Lemon Squeezy', '5% + $0.50', 'Built-in API', 'Handled (MoR)', 'Best if you outgrow Gumroad. Better UX, higher fee floor.'],
        ['Stripe + custom', '~2.9% + $0.30', 'You build', 'You handle', 'Highest control, highest build cost. Skip for the first 500 sales.'],
        ['AppSumo', '~70% revenue share', 'Built-in', 'Handled', 'Use only if you want a 1,000-sale spike. Painful margin.'],
    ]
    stack_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(stack_rows)]
    stack_t = Table(stack_data, colWidths=[1.1*inch, 1.0*inch, 1.0*inch, 1.0*inch, 2.6*inch])
    stack_t.setStyle(TableStyle([
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
    flowables.append(stack_t)
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph('Gumroad setup — eight steps', s['h3']))
    for n, txt in [
        ('1', 'Create a Gumroad account at <font face="Courier">gumroad.com</font>. Free tier is fine until you cross $5K total revenue.'),
        ('2', 'Create the product: <b>Type:</b> Digital product. <b>Title:</b> "GEM Content Engine — Founder’s Edition". <b>Price:</b> $9.00.'),
        ('3', 'Upload the bundled ZIP (see Part 3 for what goes in it). Gumroad hosts the file on its CDN. Maximum file size: 16 GB free tier (you’ll use ~400 KB).'),
        ('4', 'Enable license keys: Product settings → "Generate license keys for this product" → toggle on. Gumroad now auto-creates a unique key per sale, sends it with the download.'),
        ('5', 'Customize the receipt email: Settings → Emails → Receipt. Paste the template from <b>Appendix A</b>. Include the license key with <font face="Courier">{{license_key}}</font>.'),
        ('6', 'Set the product URL on the live site. The Get GEM CTA in <font face="Courier">landing.html</font> already points to <font face="Courier">https://gumroad.com/l/gem-founder</font> — update the slug to match yours.'),
        ('7', 'Connect your payout method: Gumroad → Settings → Payouts. Choose direct deposit, PayPal, or Stripe Express. First payout lands on a Friday 7+ days after first sale.'),
        ('8', 'Test the flow yourself: place a $9 self-purchase, confirm the ZIP arrives with a valid key, then refund yourself. End-to-end smoke test takes 10 minutes.'),
    ]:
        flowables.append(Paragraph(f'<b>Step {n}.</b> {txt}', s['bullet'], bulletText='▸'))

    flowables.append(Paragraph('Lemon Squeezy alternative (when you outgrow Gumroad)', s['h3']))
    flowables.append(Paragraph(
        "Roughly the same flow with three differences worth knowing: (1) "
        "Lemon Squeezy is a true merchant of record in more jurisdictions, so VAT/GST is fully off your plate; "
        "(2) license-key validation has a proper REST API at <font face=\"Courier\">api.lemonsqueezy.com/v1/licenses/validate</font>; "
        "(3) the UX is better-looking out of the box. Trade-off is the 5% + $0.50 floor — on a $9 sale you net $7.95 vs $8.10 on Gumroad.",
        s['body']))

    flowables.append(Paragraph('Stripe + custom flow (when you have the engineering bandwidth)', s['h3']))
    flowables.append(Paragraph(
        "Use this only after 500+ sales and a real need for control (custom upsells, white-label, B2B invoicing). "
        "Minimum build: a small serverless function that listens to <font face=\"Courier\">checkout.session.completed</font>, "
        "generates an HMAC license key (Part 4), stores the order, and triggers an email with the ZIP link via Postmark or Resend. "
        "About a weekend of work if you’ve done it before.", s['body']))

    # ═══════════════════════════════════════════════════════════════
    # PART THREE — The buyer package
    # ═══════════════════════════════════════════════════════════════
    part('THREE', 'The Buyer Package')
    flowables.append(Paragraph(
        "Everything the buyer gets ships as a single ZIP. Small, clean, no fluff. "
        "Below is the exact structure to upload to Gumroad.", s['body']))

    code_block(
        "GEM-Content-Engine-v1.7.zip   (~370 KB total)\n"
        "├── gem.html                       ← the product (single-file app)\n"
        "├── GEM-User-Manual.pdf            ← 11-page setup + workflow guide\n"
        "├── WELCOME.md                     ← 60-second start guide (see below)\n"
        "├── LICENSE.txt                    ← buyer's license key + terms summary\n"
        "└── CHANGELOG.txt                  ← what's in v1.7 + roadmap teaser"
    )

    flowables.append(Paragraph('File-by-file rationale', s['h3']))
    for label, body in [
        ('gem.html', 'The single 330 KB HTML file. Self-contained, runs anywhere. <b>Do not minify</b> — buyers need to read it for trust.'),
        ('GEM-User-Manual.pdf', 'The 11-page user manual regenerated for each release (Part 5 of Sales Strategy explains the doc pipeline).'),
        ('WELCOME.md', 'A 2 KB markdown file with three things: (1) "Open gem.html in your browser." (2) "Paste your Ollama URL or cloud key in Settings." (3) "Hit Generate Content Drop." That’s it. Buyers want the on-ramp to be a paragraph, not a chapter.'),
        ('LICENSE.txt', 'Plain-text file with the buyer’s license key, their tier (Founder’s / Builder / Operator / Studio), the purchase date, and a five-line summary of license terms (linking to <font face="Courier">terms.html</font> on the live site).'),
        ('CHANGELOG.txt', 'A trimmed customer-facing version of <font face="Courier">CHANGELOG-v1.7.md</font> — "what’s new and what’s coming." Sets expectations that updates land in their inbox.'),
    ]:
        flowables.append(Paragraph(f'<b>{label}.</b> {body}', s['bullet'], bulletText='⋄'))

    flowables.append(Paragraph('Naming convention', s['h3']))
    flowables.append(Paragraph(
        "Always include the version in the ZIP filename: <b>GEM-Content-Engine-v1.7.zip</b>. "
        "When you ship v1.8, re-upload as <b>GEM-Content-Engine-v1.8.zip</b> — Gumroad serves the latest "
        "file to <i>all past buyers</i> automatically because lifetime updates are part of the license. "
        "Past versions stay in your local archive but should not stay on Gumroad.", s['body']))

    flowables.append(Paragraph('Optional: split into core + extras', s['h3']))
    flowables.append(Paragraph(
        "If you ever cross the 5 MB mark (custom templates, large branding kit, etc.), split into two Gumroad downloads:\n"
        "<b>GEM-Core-v1.7.zip</b> — product + manual + WELCOME + LICENSE (~400 KB).\n"
        "<b>GEM-Extras-v1.7.zip</b> — branding kit, niche templates, design files (anything optional).\n"
        "Both are gated behind the same purchase.", s['body']))

    # ═══════════════════════════════════════════════════════════════
    # PART FOUR — Activation keys
    # ═══════════════════════════════════════════════════════════════
    part('FOUR', 'Activation Keys')
    flowables.append(Paragraph(
        "GEM’s product philosophy is <i>privacy-first, no server, no account</i> — so the activation key is "
        "intentionally a soft one. It exists for the seller’s records (audit trail, support eligibility, abuse detection), "
        "not as a runtime lock on the product. Buyers can run gem.html without entering anything. They <i>reference</i> their "
        "license key when contacting support or upgrading tiers.", s['body']))
    flowables.append(Paragraph(
        "<b>Why have keys at all?</b> Three reasons. (1) Audit — you know who bought what when. (2) Support eligibility — "
        "the buyer quotes their key, you verify it in your seller ledger. (3) Abuse signal — if the same key appears in two "
        "support tickets from different emails, you have a clear resale signal.", s['callout']))

    flowables.append(Paragraph('Three approaches — pick one', s['h3']))
    flowables.append(Paragraph(
        "<b>A. Gumroad built-in (recommended for first 1,000 sales).</b> Toggle the "
        "<i>Generate license keys for this product</i> setting. Gumroad auto-creates a key per sale, includes it in the receipt "
        "email, and exposes a verify endpoint at <font face=\"Courier\">api.gumroad.com/v2/licenses/verify</font>. Zero engineering.",
        s['body']))
    flowables.append(Paragraph(
        "<b>B. Custom HMAC (recommended if you ever leave Gumroad).</b> Generate a deterministic key from "
        "<font face=\"Courier\">HMAC-SHA256(secret, order_id)</font>. You can re-derive any key from the order ID and your secret, "
        "so you don’t need a database. See the code snippet below.", s['body']))
    flowables.append(Paragraph(
        "<b>C. Manual UUIDs (only for &lt; 20 sales).</b> Run <font face=\"Courier\">python -c \"import uuid; print(uuid.uuid4())\"</font> "
        "per sale and paste the result into a spreadsheet. Fine for a private beta, not for scale.", s['body']))

    flowables.append(Paragraph('Recommended key format', s['h3']))
    code_block("GEM-XXXX-XXXX-XXXX-XXXX     (e.g. GEM-7B3C-91F0-4A2E-D8B6)")
    flowables.append(Paragraph(
        "Four hex groups of 4 characters, prefixed with <b>GEM-</b>. Easy to read aloud over a call. "
        "Sixteen hex chars = 64 bits of entropy — way more than you need for $9 indie product, but no reason not to.",
        s['body']))

    flowables.append(Paragraph('Python — custom HMAC key generator', s['h3']))
    code_block(
        "# scripts/keygen.py\n"
        "import hmac, hashlib, os\n"
        "\n"
        "SECRET = os.environ['GEM_KEYGEN_SECRET'].encode()   # keep this off Git\n"
        "\n"
        "def make_key(order_id: str) -> str:\n"
        "    raw = hmac.new(SECRET, order_id.encode(), hashlib.sha256).hexdigest()\n"
        "    chunks = [raw[0:4], raw[4:8], raw[8:12], raw[12:16]]\n"
        "    return 'GEM-' + '-'.join(c.upper() for c in chunks)\n"
        "\n"
        "def verify_key(order_id: str, claimed_key: str) -> bool:\n"
        "    return hmac.compare_digest(make_key(order_id), claimed_key)\n"
        "\n"
        "# Usage at sale time:\n"
        "#   key = make_key('gumroad-order-12345')\n"
        "#   write key into LICENSE.txt, email to buyer.\n"
        "# Usage at support time:\n"
        "#   if verify_key(order_id, buyer_quoted_key): grant support."
    )

    flowables.append(Paragraph('Seller ledger — the spreadsheet you actually keep', s['h3']))
    ledger = [
        ['Column', 'Why it matters'],
        ['order_id', 'The Gumroad / Stripe order reference. Primary key.'],
        ['license_key', 'The key you emailed the buyer. Deterministic if HMAC.'],
        ['email', 'Customer email. Used for support and revocation.'],
        ['tier', 'Founder’s / Builder / Operator / Studio. Drives support depth.'],
        ['purchased_at', 'ISO date. Used for the 14-day refund window.'],
        ['version_at_purchase', 'e.g. v1.7. So you know which manual they got.'],
        ['status', 'active / refunded / revoked. Filter on this in every support ticket.'],
        ['notes', 'Free-text. Refund reason, upgrade history, escalation flags.'],
    ]
    led_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(ledger)]
    led_t = Table(led_data, colWidths=[1.6*inch, 5.1*inch])
    led_t.setStyle(TableStyle([
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
    flowables.append(led_t)
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph(
        "A Google Sheet works for the first 500 sales. After that, move to a SQLite file or Airtable — "
        "Gumroad’s export covers most of this but doesn’t carry your <i>notes</i> column.", s['body']))

    flowables.append(Paragraph('Optional — gentle in-product license display', s['h3']))
    flowables.append(Paragraph(
        "If you want gem.html to <i>display</i> the license key (not gate behind it), paste this snippet inside "
        "the existing Settings panel. Pure display, no validation, no server call — true to the privacy promise.",
        s['body']))
    code_block(
        "<!-- Drop inside the Settings tab in gem.html -->\n"
        "<div class=\"gem-license\">\n"
        "  <label for=\"gem-license-key\">License key</label>\n"
        "  <input id=\"gem-license-key\" type=\"text\"\n"
        "         placeholder=\"GEM-XXXX-XXXX-XXXX-XXXX\"\n"
        "         pattern=\"GEM-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}\">\n"
        "  <small>From your LICENSE.txt. Stored locally only. Not validated online.</small>\n"
        "</div>\n"
        "<script>\n"
        "  const el = document.getElementById('gem-license-key');\n"
        "  el.value = localStorage.getItem('gem_license') || '';\n"
        "  el.addEventListener('change', () =>\n"
        "    localStorage.setItem('gem_license', el.value.trim()));\n"
        "</script>"
    )

    # ═══════════════════════════════════════════════════════════════
    # PART FIVE — Delivery
    # ═══════════════════════════════════════════════════════════════
    part('FIVE', 'Delivery')
    flowables.append(Paragraph(
        "On Gumroad, delivery is automatic. The buyer downloads the ZIP from a unique URL, and a receipt email lands "
        "in their inbox containing the license key plus a permanent re-download link. Your job is to make the receipt "
        "email and the WELCOME.md feel like a person wrote them, not a vending machine.", s['body']))

    flowables.append(Paragraph('The three emails the buyer should receive', s['h3']))
    emails = [
        ['When', 'Email', 'Goal'],
        ['T+0 seconds', 'Receipt + license key', 'Confirm purchase, surface key, reduce re-download friction.'],
        ['T+30 minutes (if first run not detected)', '“First-run nudge” (optional)', 'Catch buyers who downloaded and got distracted before opening gem.html.'],
        ['T+24 hours', '“How’s it going?” follow-up', 'Open the support conversation. Most buyers will reply with one specific question.'],
        ['T+14 days', '“Welcome past the refund window”', 'Celebrate the milestone, ask for a one-line testimonial. Optional but high-ROI.'],
    ]
    em_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(emails)]
    em_t = Table(em_data, colWidths=[1.8*inch, 2.4*inch, 2.5*inch])
    em_t.setStyle(TableStyle([
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
    flowables.append(em_t)
    flowables.append(Spacer(1, 12))
    flowables.append(Paragraph(
        "Full email templates are in Appendix A. Use Gumroad’s built-in receipt customizer for the T+0 email; "
        "everything past that goes through whatever email tool you already use (ConvertKit, Buttondown, Mailerlite, Resend).",
        s['body']))

    flowables.append(Paragraph('Re-delivery (when someone loses the file)', s['h3']))
    flowables.append(Paragraph(
        "Gumroad already handles this — every receipt email contains a permanent re-download link. If a buyer emails "
        "anyway: ask for the email they purchased with, look up the order in Gumroad, click <i>Resend receipt</i>. Total "
        "time: 90 seconds. Don’t treat re-delivery as a chore — it’s a chance to remind them v1.7 is the latest and "
        "they’re still on lifetime updates.", s['body']))

    # ═══════════════════════════════════════════════════════════════
    # PART SIX — Post-purchase support
    # ═══════════════════════════════════════════════════════════════
    part('SIX', 'Post-Purchase Support')
    flowables.append(Paragraph(
        "Support for a $9 product needs to be cheap enough to fit the price. Keep response targets generous and "
        "channel the bulk of questions to self-serve.", s['body']))

    sup_rows = [
        ['Channel', 'When to use', 'Response target'],
        ['Email (hello@thegeminfo.com)', 'Setup issues, refund requests, account questions', 'Within 48 business hours'],
        ['Discord community', 'Tips, sharing outputs, feature requests, peer help', 'Best-effort; community helps community'],
        ['Founder DM (Founder’s Edition only)', 'Strategic feedback, roadmap input, escalations', 'Within 7 days'],
        ['Knowledge base / FAQ', 'Most questions are answered here first', 'Live on the site'],
    ]
    sup_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(sup_rows)]
    sup_t = Table(sup_data, colWidths=[2.2*inch, 3.0*inch, 1.5*inch])
    sup_t.setStyle(TableStyle([
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
    flowables.append(sup_t)
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph('Common support questions &amp; canned replies', s['h3']))
    for q, a in [
        ('"Ollama says connection failed."', 'They forgot CORS. Reply with one line: "Quit Ollama and relaunch with <font face=\"Courier\">OLLAMA_ORIGINS=“*” ollama serve</font>. Then refresh gem.html and click Test Connection again."'),
        ('"Trending Mode only shows Reddit posts."', 'Expected behavior. Google Trends is CORS-blocked; we fall back to r/popular. Documented in the live FAQ and Chapter 7 of the manual. If they want unrestricted Google Trends, point them to the one-line proxy in the manual.'),
        ('"My API key is showing ‘Invalid.’"', 'Ask which provider. Confirm the prefix: <font face="Courier">sk-</font> (OpenAI), <font face="Courier">sk-ant-</font> (Anthropic), <font face="Courier">sk-or-</font> (OpenRouter). If correct, ask them to paste it freshly — pasting from password managers sometimes inserts trailing whitespace.'),
        ('"Can I use GEM for client work?"', 'Yes — Founder’s Edition includes a commercial-use license. Point them to <font face="Courier">terms.html § 5</font> on the live site for the formal grant.'),
        ('"My PDF export is blank."', 'Browser print blocked custom fonts. Switch to Chrome / Edge and re-export. If still blank: Settings → Export → "Use system fonts" toggle.'),
        ('"Will there be a v2.0?"', 'Yes. Daily auto-brief, approvals, direct publish, performance loop are all on the roadmap and Founder’s Edition buyers will receive a substantial discount on v2.0 if it ships as a separate paid upgrade. Linked from the live <font face="Courier">#roadmap</font> section.'),
    ]:
        flowables.append(Paragraph(f'<b>Q.</b> {q}', s['h3']))
        flowables.append(Paragraph(f'<b>A.</b> {a}', s['body']))

    # ═══════════════════════════════════════════════════════════════
    # PART SEVEN — Refunds, revocations, abuse
    # ═══════════════════════════════════════════════════════════════
    part('SEVEN', 'Refunds, Revocations, and Abuse')
    flowables.append(Paragraph(
        "The shorter your refund window and the cleaner your policy, the fewer disputes you’ll see. "
        "The Terms of Service (live on the site) already locks in the policy below — this part is the operational "
        "side: what you actually click.", s['body']))

    flowables.append(Paragraph('Refund policy (already published on terms.html § 7)', s['h3']))
    for b in [
        '<b>14-day no-questions-asked refund</b> on Founder’s and Builder tiers.',
        '<b>30-day refund</b> on Operator tier, conditional on the buyer documenting the issue.',
        '<b>Studio tier refunds are pro-rated</b> against any setup-call or onboarding hours already delivered.',
        '<b>Refunds are processed via the same merchant of record</b> the purchase used (Gumroad / Lemon Squeezy).',
        'Refund triggers automatic license revocation in the seller ledger (Part 4).',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='⋄'))

    flowables.append(Paragraph('Refund procedure — five clicks on Gumroad', s['h3']))
    for n, txt in [
        ('1', 'Open Gumroad → Sales → find the order by email or order ID.'),
        ('2', 'Click <i>Refund</i>. Gumroad reverses the charge and emails the buyer.'),
        ('3', 'In your seller ledger, set <font face="Courier">status = refunded</font>, paste a one-line note (e.g. "didn’t work for their niche").'),
        ('4', 'Mark the license key as revoked (Part 4) so any future support ticket quoting that key gets the gentle reply: "I can see this order was refunded. Happy to help still, but the license key isn’t active."'),
        ('5', 'Update the public seat counter on landing.html if the refunded sale was inside the Founder cohort (e.g. seats remaining goes from 73 back to 74).'),
    ]:
        flowables.append(Paragraph(f'<b>Step {n}.</b> {txt}', s['bullet'], bulletText='▸'))

    flowables.append(Paragraph('Abuse detection — patterns to watch', s['h3']))
    for b in [
        '<b>Same key, two emails.</b> Resale. Revoke the key and email both addresses.',
        '<b>Refund-then-redownload.</b> Gumroad already blocks downloads post-refund, but if you used a custom delivery, build the same gate in.',
        '<b>Bulk purchases from disposable email addresses.</b> Sometimes legitimate (gift cards, agency buying for seats), sometimes credit-card fraud. Gumroad flags most; review unusual orders manually.',
        '<b>Chargebacks.</b> Always reply to the dispute with the receipt email + license key + download log. Most disputes resolve in your favor with a single screenshot of the buyer downloading the file.',
    ]:
        flowables.append(Paragraph(b, s['bullet'], bulletText='▸'))

    flowables.append(Paragraph('Tier upgrade path (Builder → Operator → Studio)', s['h3']))
    flowables.append(Paragraph(
        "If a Founder’s buyer asks to upgrade later: don’t build a separate product. Send them a one-time "
        "Gumroad discount link for <b>(new tier price − amount already paid)</b>. Update their tier in the ledger. "
        "They keep their original license key — it now maps to the higher tier. Total operator time: ~5 minutes per upgrade.",
        s['body']))

    # ═══════════════════════════════════════════════════════════════
    # PART EIGHT — Operational cadence
    # ═══════════════════════════════════════════════════════════════
    part('EIGHT', 'Operational Cadence')
    flowables.append(Paragraph(
        "Most of the work in selling GEM is the ongoing, low-energy rhythm — not the launch sprint. "
        "Below is the realistic cadence for a one-person operation past the launch window.", s['body']))

    cadence = [
        ['Cadence', 'Task', 'Time'],
        ['Daily', 'Skim Gumroad sales notifications. Triage support inbox.', '5–10 min'],
        ['Daily', 'Reply to anything blocking a buyer (CORS errors, key questions).', '10–20 min'],
        ['Weekly', 'Update <font face="Courier">SEATS_REMAINING</font> in <font face="Courier">landing.html</font> as Founder cohort fills.', '2 min'],
        ['Weekly', 'Sync Gumroad sales into the seller ledger (CSV export).', '10 min'],
        ['Weekly', 'Ship one piece of organic content (Twitter thread, YouTube short, or blog).', '60–90 min'],
        ['Monthly', 'Refund the chargebacks worth refunding; dispute the rest.', '15 min'],
        ['Monthly', 'Tag a release in this repo if you shipped fixes — update <font face="Courier">CHANGELOG-v1.7.md</font> or open <font face="Courier">CHANGELOG-v1.8.md</font>.', '20 min'],
        ['Monthly', 'Re-run <font face="Courier">scripts/regenerate_pdfs.py</font> if any PDF content changed; bundle new ZIP, re-upload to Gumroad.', '10 min'],
        ['Quarterly', 'Reconcile payouts. Lemon Squeezy / Gumroad handle the VAT side; you reconcile income tax in your jurisdiction.', '30–60 min'],
        ['Quarterly', 'Audit the seller ledger for revoked keys still active, stale notes, unsubscribes.', '15 min'],
        ['As needed', 'Crossed a price-ratchet threshold? Bump price in Gumroad, update landing.html copy, send announce email.', '20 min'],
    ]
    cd_data = [[Paragraph(f'<b>{c}</b>' if r == 0 else c, s['small']) for c in row] for r, row in enumerate(cadence)]
    cd_t = Table(cd_data, colWidths=[1.0*inch, 4.7*inch, 1.0*inch])
    cd_t.setStyle(TableStyle([
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
    flowables.append(cd_t)

    # ═══════════════════════════════════════════════════════════════
    # APPENDIX A — Email templates
    # ═══════════════════════════════════════════════════════════════
    appendix('A', 'Email Templates')
    flowables.append(Paragraph(
        "Paste these into Gumroad’s receipt customizer (template 1) and your email tool (templates 2–4). "
        "Replace bracketed placeholders. Keep the tone direct and operator-grade — these are not corporate auto-emails.",
        s['body']))

    flowables.append(Paragraph('Template 1 — Order receipt + license key (T+0)', s['h3']))
    code_block(
        "Subject: Your GEM Content Engine download + license key\n"
        "\n"
        "Hi {{purchaser_name}},\n"
        "\n"
        "Thanks for buying GEM Content Engine — Founder's Edition.\n"
        "Your license key is below; tuck it somewhere safe.\n"
        "\n"
        "    License key: {{license_key}}\n"
        "    Tier:        Founder's Edition (first 100 buyers)\n"
        "    Purchased:   {{purchased_at}}\n"
        "\n"
        "Download (lifetime re-download from this link):\n"
        "{{download_url}}\n"
        "\n"
        "Two minutes to your first content drop:\n"
        "  1. Unzip and open gem.html in your browser.\n"
        "  2. Settings -> paste your Ollama URL or cloud API key.\n"
        "  3. Hit Generate Content Drop.\n"
        "\n"
        "Direct line for Founder's Edition buyers: hello@thegeminfo.com.\n"
        "Reply to this email anytime.\n"
        "\n"
        "-- The GEM team\n"
        "thegeminfo.com"
    )

    flowables.append(Paragraph('Template 2 — 24-hour follow-up', s['h3']))
    code_block(
        "Subject: Did GEM open OK?\n"
        "\n"
        "Hey {{first_name}},\n"
        "\n"
        "Yesterday you grabbed GEM Content Engine. Three quick things:\n"
        "\n"
        "1. The fastest first run is on Ollama (free, local). If you don't have it,\n"
        "   the manual's Chapter 3 walks through the 5-minute install.\n"
        "\n"
        "2. If you'd rather use a cloud LLM, paste any OpenAI / Anthropic /\n"
        "   OpenRouter key in Settings. A full pipeline run costs about 2-5 cents.\n"
        "\n"
        "3. If something's broken, hit reply. I read every email.\n"
        "\n"
        "What I'd love back: one sentence on the first piece of content you ship\n"
        "with GEM. I'm building the v1.8 roadmap from real feedback.\n"
        "\n"
        "-- {{your_first_name}}\n"
        "GEM Content Engine"
    )

    flowables.append(Paragraph('Template 3 — Past-refund-window check-in (T+14 days)', s['h3']))
    code_block(
        "Subject: 14 days in -- how's GEM treating you?\n"
        "\n"
        "Hey {{first_name}},\n"
        "\n"
        "Two weeks ago you bought GEM Content Engine.\n"
        "You're officially past the no-questions refund window -- which means\n"
        "you've already gotten enough value to keep it (or you forgot we exist;\n"
        "either is fine).\n"
        "\n"
        "If GEM has earned its keep on your channels, would you reply with a\n"
        "single sentence I can quote on the site? Founder-cohort testimonials\n"
        "are the most valuable thing I have right now.\n"
        "\n"
        "If GEM hasn't earned its keep, tell me why. I'd rather refund you on\n"
        "day 15 than keep $9 you regret.\n"
        "\n"
        "-- {{your_first_name}}"
    )

    flowables.append(Paragraph('Template 4 — Refund acknowledgment', s['h3']))
    code_block(
        "Subject: Refund processed -- GEM Content Engine\n"
        "\n"
        "Hi {{first_name}},\n"
        "\n"
        "Refund processed via {{merchant_of_record}}; you should see the credit\n"
        "back on your card within 5-10 business days.\n"
        "\n"
        "Your license key ({{license_key}}) is now marked inactive in our records.\n"
        "Please delete the gem.html file and the user manual from your machine.\n"
        "\n"
        "Two quick asks (totally optional):\n"
        "  - One sentence on what didn't work for you. Helps the next 100 buyers.\n"
        "  - Permission to email you if v2.0 ships something you'd want.\n"
        "\n"
        "Thanks for trying it.\n"
        "\n"
        "-- {{your_first_name}}\n"
        "GEM Content Engine"
    )

    # ═══════════════════════════════════════════════════════════════
    # APPENDIX B — Code & scripts
    # ═══════════════════════════════════════════════════════════════
    appendix('B', 'Code &amp; Scripts')
    flowables.append(Paragraph(
        "Three small scripts that automate the boring parts of fulfillment. Drop into <font face=\"Courier\">scripts/</font> "
        "alongside <font face=\"Courier\">regenerate_pdfs.py</font>.",
        s['body']))

    flowables.append(Paragraph('B.1 — Package the buyer ZIP (Bash)', s['h3']))
    code_block(
        "# scripts/package_buyer_zip.sh\n"
        "#!/usr/bin/env bash\n"
        "set -euo pipefail\n"
        "VERSION=\"v1.7\"\n"
        "OUTPUT=\"GEM-Content-Engine-${VERSION}.zip\"\n"
        "STAGING=\"$(mktemp -d)\"\n"
        "\n"
        "cp gem.html \"$STAGING/\"\n"
        "cp GEM-User-Manual.pdf \"$STAGING/\"\n"
        "cp dist/WELCOME.md \"$STAGING/\"\n"
        "cp dist/LICENSE.template.txt \"$STAGING/LICENSE.txt\"\n"
        "cp dist/CHANGELOG.txt \"$STAGING/\"\n"
        "\n"
        "(cd \"$STAGING\" && zip -r \"$OLDPWD/$OUTPUT\" .)\n"
        "rm -rf \"$STAGING\"\n"
        "echo \"Built $OUTPUT ($(du -h \"$OUTPUT\" | cut -f1))\""
    )

    flowables.append(Paragraph('B.2 — Render LICENSE.txt per order (Python)', s['h3']))
    code_block(
        "# scripts/render_license.py\n"
        "import sys, datetime, hmac, hashlib, os\n"
        "\n"
        "SECRET = os.environ['GEM_KEYGEN_SECRET'].encode()\n"
        "\n"
        "def make_key(order_id):\n"
        "    raw = hmac.new(SECRET, order_id.encode(), hashlib.sha256).hexdigest()\n"
        "    return 'GEM-' + '-'.join(raw[i:i+4].upper() for i in (0,4,8,12))\n"
        "\n"
        "def render(order_id, email, tier='Founder’s Edition'):\n"
        "    today = datetime.date.today().isoformat()\n"
        "    return f'''GEM Content Engine -- License\n"
        "\n"
        "License key:    {make_key(order_id)}\n"
        "Order ID:       {order_id}\n"
        "Licensee:       {email}\n"
        "Tier:           {tier}\n"
        "Purchased:      {today}\n"
        "Version:        v1.7\n"
        "\n"
        "Lifetime license for personal and commercial content creation.\n"
        "Lifetime updates within the v1.x major version.\n"
        "Full terms: https://thegeminfo.com/terms.html\n"
        "'''\n"
        "\n"
        "if __name__ == '__main__':\n"
        "    order_id, email = sys.argv[1], sys.argv[2]\n"
        "    print(render(order_id, email))"
    )

    flowables.append(Paragraph('B.3 — Verify a quoted key (Python one-liner)', s['h3']))
    code_block(
        "$ python -c \"\\\n"
        "from scripts.render_license import make_key; \\\n"
        "import os, sys; \\\n"
        "print(make_key(sys.argv[1]) == sys.argv[2])\" \\\n"
        "  gumroad-order-12345  GEM-7B3C-91F0-4A2E-D8B6"
    )

    flowables.append(Paragraph('Final note', s['h3']))
    flowables.append(Paragraph(
        "<i>The playbook above is the steady-state operating manual. The first 100 sales will be messier than this — "
        "and that’s fine. Founder’s Edition is for the cohort, not the spreadsheet. Once you cross 100 buyers, the "
        "playbook stops being theoretical and starts running itself.</i>", s['pull']))

    # ═══════════════════════════════════════════════════════════════
    # BUILD
    # ═══════════════════════════════════════════════════════════════
    doc = SimpleDocTemplate(
        out_path, pagesize=LETTER,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.8*inch, bottomMargin=0.7*inch,
        title='GEM Content Engine — Fulfillment Playbook (v1.7)',
        author='GEM Content Engine',
    )

    def first_page(c, d):
        cover_page(c, d,
            eyebrow='SELLER FULFILLMENT PLAYBOOK · v1.7 · CONFIDENTIAL',
            title_top='The Fulfillment',
            title_em='Playbook.',
            subtitle='From card-charged to activated customer in under ten minutes.\n'
                     'The seller stack. The activation-key system. The email templates.\n'
                     'The refund flow. The ongoing cadence.')
    def later_pages(c, d):
        header_footer(c, d, title_text='FULFILLMENT PLAYBOOK')

    doc.build(flowables, onFirstPage=first_page, onLaterPages=later_pages)


if __name__ == '__main__':
    import os
    base = r'D:\AI_Stuff\Gem_Content_Machine'
    sales = os.path.join(base, 'GEM-Sales-Strategy.pdf')
    manual = os.path.join(base, 'GEM-User-Manual.pdf')
    playbook = os.path.join(base, 'GEM-Fulfillment-Playbook.pdf')
    print(f'Writing {sales} ...')
    build_sales_strategy(sales)
    print(f'Writing {manual} ...')
    build_user_manual(manual)
    print(f'Writing {playbook} ...')
    build_fulfillment_playbook(playbook)
    print('Done.')
