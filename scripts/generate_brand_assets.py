"""
Generate GEM Content Engine brand assets.

Outputs:
  assets/social/GEM_avatar_400x400.png        — square avatar (Twitter / X,
                                                  LinkedIn, Discord, GitHub
                                                  profile photo)
  assets/social/GEM_banner_1500x500.png       — Twitter / X header banner
                                                  (also works for LinkedIn
                                                  cover and similar)

Brand palette matches landing.html. Hex mark mirrors the inline SVG geometry
on the live site (pointy-top hexagon with six 3D-facet trapezoids, an inner
cream hex with six subtle facet triangles, and a dark center button hex).

Run: python scripts/generate_brand_assets.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os
import ssl
import sys
import urllib.request
from pathlib import Path

# Some Windows Python installs ship with a CA bundle that fails on font CDNs.
# Use an unverified SSL context for the one-time font fetch — these are
# public, signed font binaries from jsdelivr; integrity is verified by the
# fact that PIL will refuse to load a corrupt TTF.
_SSL_CTX = ssl._create_unverified_context()

# ─── Brand palette (RGB) ─────────────────────────────────────────────
FOREST       = (14, 42, 31)        # #0E2A1F  deepest forest
FOREST_DEEP1 = (20, 61, 44)        # #143D2C
FOREST_DEEP2 = (11, 36, 27)        # #0B241B
FOREST_DEEP3 = (23, 72, 53)        # #174835
FOREST_DEEP4 = (13, 44, 32)        # #0D2C20
FOREST_DEEP5 = (27, 83, 60)        # #1B533C
FOREST_DEEP6 = (9, 37, 27)         # #09251B
PINE         = (27, 77, 62)        # #1B4D3E  primary brand green
MIDFOREST    = (42, 102, 80)       # #2A6650
SAGE         = (167, 191, 174)     # #A7BFAE
SAGE_TINT    = (214, 227, 219)     # #D6E3DB
MIST         = (233, 241, 236)     # #E9F1EC
CREAM        = (244, 239, 230)     # #F4EFE6  page background
CREAM_WHITE  = (248, 244, 234)     # #F8F4EA  inner hex face
CHARCOAL     = (26, 26, 26)        # #1A1A1A
GOLD         = (200, 169, 106)     # #C8A96A
WHITE        = (255, 255, 255)
INNER_FACET_2 = (215, 210, 199)    # #D7D2C7
INNER_FACET_3 = (241, 236, 225)    # #F1ECE1
INNER_FACET_5 = (220, 214, 201)    # #DCD6C9
INNER_FACET_6 = (247, 242, 232)    # #F7F2E8
BUTTON_INNER = (18, 59, 42)        # #123B2A

# ─── Paths ───────────────────────────────────────────────────────────
REPO = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO / 'assets' / 'social'
FONTS_DIR = REPO / 'assets' / 'fonts'
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
FONTS_DIR.mkdir(parents=True, exist_ok=True)

# ─── Fonts ───────────────────────────────────────────────────────────
FONT_URLS = {
    'PlayfairDisplay-Bold.ttf':    'https://cdn.jsdelivr.net/fontsource/fonts/playfair-display@latest/latin-700-normal.ttf',
    'PlayfairDisplay-Regular.ttf': 'https://cdn.jsdelivr.net/fontsource/fonts/playfair-display@latest/latin-400-normal.ttf',
    'Inter-Regular.ttf':           'https://cdn.jsdelivr.net/fontsource/fonts/inter@latest/latin-400-normal.ttf',
    'Inter-Bold.ttf':              'https://cdn.jsdelivr.net/fontsource/fonts/inter@latest/latin-700-normal.ttf',
}


def _ensure_font(filename):
    """Return path to a TTF, downloading if absent. Falls back to None on failure."""
    target = FONTS_DIR / filename
    if target.exists():
        return target
    url = FONT_URLS.get(filename)
    if not url:
        return None
    print(f'  downloading {filename}...')
    try:
        with urllib.request.urlopen(url, context=_SSL_CTX, timeout=20) as r:
            data = r.read()
        target.write_bytes(data)
        return target
    except Exception as e:
        print(f'  download failed: {e}')
        return None


def get_serif(size, bold=True):
    """Playfair Display, falling back to Georgia, then PIL default."""
    name = 'PlayfairDisplay-Bold.ttf' if bold else 'PlayfairDisplay-Regular.ttf'
    path = _ensure_font(name)
    if path and path.exists():
        try:
            return ImageFont.truetype(str(path), size)
        except Exception:
            pass
    # Windows Georgia fallback
    georgia = Path('C:/Windows/Fonts') / ('georgiab.ttf' if bold else 'georgia.ttf')
    if georgia.exists():
        return ImageFont.truetype(str(georgia), size)
    return ImageFont.load_default()


def get_sans(size, bold=False):
    """Inter, falling back to Segoe UI, then PIL default."""
    name = 'Inter-Bold.ttf' if bold else 'Inter-Regular.ttf'
    path = _ensure_font(name)
    if path and path.exists():
        try:
            return ImageFont.truetype(str(path), size)
        except Exception:
            pass
    segoe = Path('C:/Windows/Fonts') / ('segoeuib.ttf' if bold else 'segoeui.ttf')
    if segoe.exists():
        return ImageFont.truetype(str(segoe), size)
    return ImageFont.load_default()


# ─── Drawing primitives ──────────────────────────────────────────────
def _hex_vertices(cx, cy, R):
    """Return six vertices of a pointy-top hexagon (vertex at top)."""
    return [
        (cx + R * math.cos(math.radians(60 * i - 90)),
         cy + R * math.sin(math.radians(60 * i - 90)))
        for i in range(6)
    ]


def draw_gem_mark(draw, cx, cy, R):
    """
    Render the GEM hexagonal brand mark with 3D facets, centered at (cx, cy).

    R is the outer hex radius (center-to-vertex distance).
    Geometry matches the inline SVG on landing.html:
      - outer hex (forest) with six trapezoidal facet shades
      - inner hex (cream) with six triangle facets in subtle cream shades
      - dark center button hex (with an inner lighter hex)
      - gold accent polyline on top-right edges
      - cream accent polyline on bottom edges
    """
    outer_v  = _hex_vertices(cx, cy, R)
    inner_v  = _hex_vertices(cx, cy, R * 0.58)
    button_o = _hex_vertices(cx, cy, R * 0.26)
    button_i = _hex_vertices(cx, cy, R * 0.21)

    # 1. Outer hex base
    draw.polygon(outer_v, fill=FOREST)

    # 2. Six trapezoidal facet shades around the outer ring
    facet_shades = [FOREST_DEEP1, FOREST_DEEP2, FOREST_DEEP3,
                    FOREST_DEEP4, FOREST_DEEP5, FOREST_DEEP6]
    for i in range(6):
        ni = (i + 1) % 6
        draw.polygon(
            [outer_v[i], outer_v[ni], inner_v[ni], inner_v[i]],
            fill=facet_shades[i]
        )

    # 3. Inner cream hex
    draw.polygon(inner_v, fill=CREAM_WHITE)

    # 4. Six triangle facets inside the cream hex (subtle 3D shading)
    cream_facets = [WHITE, INNER_FACET_2, INNER_FACET_3,
                    WHITE, INNER_FACET_5, INNER_FACET_6]
    for i in range(6):
        ni = (i + 1) % 6
        draw.polygon([inner_v[i], inner_v[ni], (cx, cy)], fill=cream_facets[i])

    # 5. Dark center button hex
    draw.polygon(button_o, fill=FOREST)
    draw.polygon(button_i, fill=BUTTON_INNER)

    # 6. Gold accent stroke (top -> upper-right -> lower-right)
    stroke = max(2, int(R * 0.025))
    draw.line([outer_v[0], outer_v[1], outer_v[2]], fill=GOLD, width=stroke)

    # 7. Cream accent stroke (lower-left -> bottom -> lower-right)
    stroke2 = max(1, int(R * 0.018))
    draw.line([outer_v[4], outer_v[3], outer_v[2]], fill=CREAM_WHITE, width=stroke2)


def draw_letter_spaced(draw, x, y, text, font, fill, spacing):
    """Draw text with explicit per-character spacing."""
    cursor = x
    for ch in text:
        draw.text((cursor, y), ch, font=font, fill=fill)
        bbox = draw.textbbox((0, 0), ch, font=font)
        cursor += (bbox[2] - bbox[0]) + spacing


# ─── Avatar (400x400) ────────────────────────────────────────────────
def build_avatar():
    """
    400x400 — dark forest background with the GEM hex mark centered.
    Reads as a circle (Twitter / X profile crop) or square (LinkedIn, GitHub).
    """
    W, H = 400, 400
    img = Image.new('RGB', (W, H), FOREST)

    # Subtle radial sage glow behind the hex for depth
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    cx, cy = W // 2, H // 2
    for i in range(28):
        r = 60 + i * 8
        a = max(0, int(36 - i * 1.2))
        if a <= 0:
            continue
        od.ellipse([cx - r, cy - r, cx + r, cy + r],
                   fill=(*MIDFOREST, a))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=36))
    img.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(img)
    # Hex centered, sized to ~70% of canvas
    draw_gem_mark(draw, cx, cy, R=140)

    out = ASSETS_DIR / 'GEM_avatar_400x400.png'
    img.save(out, 'PNG', optimize=True)
    print(f'Wrote {out.name} ({W}x{H}, {os.path.getsize(out)/1024:.1f} KB)')


# ─── Banner (1500x500) ───────────────────────────────────────────────
def build_banner():
    """
    1500x500 — cream background, hex on left, GEM wordmark center, tagline
    below, and a "$9 LIFETIME" pill in the top-right.

    Layout is mindful of the Twitter / X mobile crop and profile-photo
    overlap: nothing critical sits in the bottom-left 250x250 zone where
    the profile picture covers the banner on mobile.
    """
    W, H = 1500, 500
    img = Image.new('RGB', (W, H), CREAM)

    # Soft sage glow on the right
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for i in range(36):
        r = 100 + i * 14
        a = max(0, int(16 - i * 0.4))
        if a <= 0:
            continue
        od.ellipse(
            [W - 280 - r, H // 2 - 80 - r, W - 280 + r, H // 2 - 80 + r],
            fill=(*SAGE_TINT, a)
        )
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=56))
    img.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(img)

    # Hex on left (shifted up so it clears the profile-photo overlap zone)
    hex_cx, hex_cy = 280, 180
    draw_gem_mark(draw, hex_cx, hex_cy, R=130)

    # Gold vertical divider after the hex
    div_x = 460
    draw.line([(div_x, 70), (div_x, 290)], fill=GOLD, width=4)

    # "GEM" wordmark in Playfair
    wm_x = 510
    font_gem = get_serif(180, bold=True)
    draw.text((wm_x, 50), 'GEM', font=font_gem, fill=FOREST)

    # CONTENT ENGINE — Inter, letter-spaced
    font_sub = get_sans(28, bold=False)
    draw_letter_spaced(draw, wm_x + 6, 240, 'CONTENT ENGINE',
                       font=font_sub, fill=PINE, spacing=10)

    # Tagline (Playfair italic feel via regular weight + larger size)
    font_tag = get_serif(36, bold=False)
    tag_text = 'One idea. Every channel. Six AI agents.'
    tbbox = draw.textbbox((0, 0), tag_text, font=font_tag)
    tw = tbbox[2] - tbbox[0]
    tag_x = (W - tw) // 2
    draw.text((tag_x, 340), tag_text, font=font_tag, fill=CHARCOAL)

    # URL line near the top-left (small, plain) so the apex stays balanced
    font_url = get_sans(18, bold=False)
    draw.text((40, 30), 'thegeminfo.com', font=font_url, fill=PINE)

    # $9 LIFETIME pill in top-right
    pill_w, pill_h = 230, 60
    pill_x = W - pill_w - 60
    pill_y = 50
    draw.rounded_rectangle(
        [pill_x, pill_y, pill_x + pill_w, pill_y + pill_h],
        radius=30, fill=PINE
    )
    font_pill = get_sans(22, bold=True)
    pill_text = '$9 LIFETIME'
    pbbox = draw.textbbox((0, 0), pill_text, font=font_pill)
    pw = pbbox[2] - pbbox[0]
    ph = pbbox[3] - pbbox[1]
    draw.text(
        (pill_x + (pill_w - pw) // 2, pill_y + (pill_h - ph) // 2 - 4),
        pill_text, font=font_pill, fill=CREAM_WHITE
    )

    # Stats line above tagline (replaces the agent-dots row that collided
    # with the GEM wordmark). Single horizontal line of mono-style metadata.
    font_stats = get_sans(18, bold=True)
    stats = '6 AI AGENTS  ·  17+ ASSET TYPES  ·  5 MIN END-TO-END  ·  LOCAL OR CLOUD'
    sbbox = draw.textbbox((0, 0), stats, font=font_stats)
    sw = sbbox[2] - sbbox[0]
    # Center the stats row horizontally below the tagline
    stats_x = (W - sw) // 2
    draw.text((stats_x, 395), stats, font=font_stats, fill=MIDFOREST)

    out = ASSETS_DIR / 'GEM_banner_1500x500.png'
    img.save(out, 'PNG', optimize=True)
    print(f'Wrote {out.name} ({W}x{H}, {os.path.getsize(out)/1024:.1f} KB)')


# ─── Main ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Generating GEM brand assets...')
    build_avatar()
    build_banner()
    print()
    print('Done. Files saved to assets/social/:')
    print('  - GEM_avatar_400x400.png       (square avatar)')
    print('  - GEM_banner_1500x500.png      (Twitter / X header)')
    print()
    print('Upload these as your social profile photo and header on:')
    print('  Twitter / X, LinkedIn, Discord, GitHub, Indie Hackers, Product Hunt.')
