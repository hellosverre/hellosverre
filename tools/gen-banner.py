# Builds the profile banner.
#
# Design constraints, all deliberate:
#   * One accent (jade, 53% HSL saturation). Hierarchy comes from lightness, not chroma.
#   * Green-black base, not the default slate-indigo ink every dark SaaS ships.
#   * The wordmark is solid off-white. Gradient-clipped headline text is a slop tell.
#   * Depth is one hairline border plus a rim light -- no coloured glow, no glow blobs.
#   * Corners are a superellipse, not border-radius: continuous curvature, no seam where
#     the arc meets the straight edge.
#   * Grain over the whole slab. A perfectly smooth gradient is the giveaway; real
#     surfaces have noise.
#   * Only one thing moves, slowly: a specular sheen crossing the glass.
#
# The wordmark ships as vector paths because GitHub proxies README images through camo,
# which blocks webfont requests -- a font-family reference would silently fall back.
import io, math, os

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Identity

OUT = r"C:/Users/AK/Desktop/test/hellosverre-profile/assets"

W, H = 1000, 240
RADIUS, SQUIRCLE_N = 30.0, 4.5

P = {
    "ink":      "#030D07",   # bottom of the surface ramp
    "surface":  "#081A10",   # top of the surface ramp
    "text":     "#EFF5F1",
    "muted":    "#A5ADA8",
    "dim":      "#767E79",
    "accent":   "#76D5A1",
}

WORDMARK_FONT = r"C:/Users/AK/AppData/Local/Microsoft/Windows/Fonts/AquireBold-8Ma60.otf"
WORDMARK_TRACKING, WORDMARK_CAP = 0.022, 54.0
WORDMARK_X, WORDMARK_BASELINE = 44, 96

NAME = "SVERRE"
TAGLINE = "building AI systems, fundamentals first"
STACK = "TypeScript  ·  Python  ·  Next.js  ·  Hono  ·  Postgres  ·  Docker  ·  Linux"
PLACE = "Ski \u00b7 Norge"

MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"


def squircle(w, h, r, n, seg=18):
    """Rounded rect whose corners are superellipse quadrants (|x|^n + |y|^n = r^n).

    A border-radius corner has discontinuous curvature where the arc meets the straight
    edge; a superellipse does not, which is why Apple's shapes use one.
    """
    def quad(cx, cy, sx, sy):
        pts = []
        for i in range(seg + 1):
            x = r * i / seg
            y = (max(r ** n - x ** n, 0.0)) ** (1.0 / n)
            pts.append((cx + sx * x, cy + sy * y))
        return pts

    # Clockwise from the top edge. Each quadrant already lands on the two edges it
    # joins, so the straight runs between corners come for free.
    d = ["M %.2f %.2f" % (r, 0)]
    for pt in quad(w - r, r, 1, -1):                # top-right:    (w-r,0) -> (w,r)
        d.append("L %.2f %.2f" % pt)
    for pt in quad(w - r, h - r, 1, 1)[::-1]:       # bottom-right: (w,h-r) -> (w-r,h)
        d.append("L %.2f %.2f" % pt)
    for pt in quad(r, h - r, -1, 1):                # bottom-left:  (r,h)   -> (0,h-r)
        d.append("L %.2f %.2f" % pt)
    for pt in quad(r, r, -1, -1)[::-1]:             # top-left:     (0,r)   -> (r,0)
        d.append("L %.2f %.2f" % pt)
    d.append("Z")
    return " ".join(d)


def outline(font_path, text, cap_height, tracking_em):
    """Glyph outlines as one SVG path, y-flipped into user space, sitting on y=0."""
    font = TTFont(font_path, fontNumber=0)
    cmap, gs = font.getBestCmap(), font.getGlyphSet()
    upem = font["head"].unitsPerEm
    cap = getattr(font["OS/2"], "sCapHeight", 0) if "OS/2" in font else 0
    scale = cap_height / float(cap or upem * 0.7)

    pen = SVGPathPen(gs, ntos=lambda v: "%.1f" % v)
    x, track = 0.0, tracking_em * upem
    for ch in text:
        gname = cmap.get(ord(ch))
        if gname is None:
            raise SystemExit("missing glyph %r in %s" % (ch, font_path))
        gs[gname].draw(TransformPen(pen, Identity.translate(x, 0).scale(1, -1)))
        x += gs[gname].width + track
    return pen.getCommands(), (x - track) * scale, scale


def flag(x, y, w=21.0, h=15.0):
    """Norwegian flag at the correct 6:1:2:1:12 band proportions."""
    ux, uy = w / 22.0, h / 16.0
    return (
        f'<g transform="translate({x},{y})">'
        f'<rect width="{w}" height="{h}" rx="1.5" fill="#BA0C2F"/>'
        f'<rect x="{6*ux:.2f}" width="{4*ux:.2f}" height="{h}" fill="#F7F7F7"/>'
        f'<rect y="{6*uy:.2f}" width="{w}" height="{4*uy:.2f}" fill="#F7F7F7"/>'
        f'<rect x="{7*ux:.2f}" width="{2*ux:.2f}" height="{h}" fill="#00205B"/>'
        f'<rect y="{7*uy:.2f}" width="{w}" height="{2*uy:.2f}" fill="#00205B"/>'
        f'</g>'
    )


def node_graph(cx=884, cy=100, scale=1.0):
    """Orchestration motif: a controller dispatching work to four workers and
    collecting it back.

    Hairlines and a single accent -- no halo, no glow. It is a diagram, not decoration.
    """
    peers = [(-58, -42), (62, -28), (-34, 56), (58, 48)]
    parts = []
    for dx, dy in peers:
        px, py = cx + dx * scale, cy + dy * scale
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" '
                     f'stroke="{P["accent"]}" stroke-width="1" opacity="0.30"/>')
    for i, (dx, dy) in enumerate(peers):
        px, py = cx + dx * scale, cy + dy * scale
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.4" fill="none" '
                     f'stroke="{P["accent"]}" stroke-width="1.3" opacity="0.70"/>')
        parts.append(
            f'<circle r="2" fill="{P["accent"]}" opacity="0">'
            f'<animate attributeName="cx" values="{cx};{px:.1f}" dur="3.4s" repeatCount="indefinite" begin="{i*0.85}s"/>'
            f'<animate attributeName="cy" values="{cy};{py:.1f}" dur="3.4s" repeatCount="indefinite" begin="{i*0.85}s"/>'
            f'<animate attributeName="opacity" values="0;0.9;0.9;0" keyTimes="0;0.2;0.65;1" '
            f'dur="3.4s" repeatCount="indefinite" begin="{i*0.85}s"/></circle>'
        )
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="6.5" fill="{P["accent"]}" opacity="0.9"/>')
    return "".join(parts)


WORDMARK_D, WORDMARK_W, WORDMARK_S = outline(
    WORDMARK_FONT, NAME, WORDMARK_CAP, WORDMARK_TRACKING)
SHAPE = squircle(W, H, RADIUS, SQUIRCLE_N)


def build():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Sverre - building AI systems, fundamentals first">
  <defs>
    <linearGradient id="slab" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0" stop-color="{P['surface']}"/>
      <stop offset="1" stop-color="{P['ink']}"/>
    </linearGradient>

    <!-- Fresnel: a surface catches light hardest along its top edge. -->
    <linearGradient id="rim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"    stop-color="#FFFFFF" stop-opacity="0.02"/>
      <stop offset="0.35" stop-color="#FFFFFF" stop-opacity="0.16"/>
      <stop offset="1"    stop-color="#FFFFFF" stop-opacity="0.03"/>
    </linearGradient>

    <!-- The one moving thing: a specular band crossing the glass. -->
    <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"    stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="0.25" stop-color="#FFFFFF" stop-opacity="0.018"/>
      <stop offset="0.5"  stop-color="#FFFFFF" stop-opacity="0.075"/>
      <stop offset="0.75" stop-color="#FFFFFF" stop-opacity="0.018"/>
      <stop offset="1"    stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>

    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch" result="n"/>
      <feColorMatrix in="n" type="saturate" values="0"/>
    </filter>

    <clipPath id="slabClip"><path d="{SHAPE}"/></clipPath>
  </defs>

  <g clip-path="url(#slabClip)">
    <rect width="{W}" height="{H}" fill="url(#slab)"/>

    <g transform="translate(-460,0)">
      <rect x="0" y="-140" width="360" height="520" fill="url(#sheen)" transform="rotate(14 150 120)"/>
      <animateTransform attributeName="transform" type="translate"
                        values="-460,0; 1180,0" dur="13s" repeatCount="indefinite"/>
    </g>

    <rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.055"/>

    {node_graph()}

    <g transform="translate({WORDMARK_X},{WORDMARK_BASELINE}) scale({WORDMARK_S:.5f})">
      <path d="{WORDMARK_D}" fill="{P['text']}"/>
    </g>
    <rect x="{WORDMARK_X + 2}" y="112" width="62" height="3" rx="1.5" fill="{P['accent']}"/>

    <text x="{WORDMARK_X}" y="154" font-family="{MONO}" font-size="19.5" fill="{P['accent']}">&#8250;</text>
    <text x="{WORDMARK_X + 22}" y="154" font-family="{MONO}" font-size="19.5" fill="{P['muted']}">{TAGLINE}</text>

    <text x="{WORDMARK_X}" y="202" font-family="{MONO}" font-size="13" fill="{P['dim']}"
          letter-spacing="0.3">{STACK}</text>

    {flag(846, 191)}
    <text x="{W - 44}" y="202" text-anchor="end" font-family="{MONO}" font-size="12.5"
          fill="{P['dim']}">{PLACE}</text>

    <rect width="{W}" height="1.25" fill="url(#rim)"/>
  </g>

  <path d="{SHAPE}" fill="none" stroke="#FFFFFF" stroke-opacity="0.07" stroke-width="1"/>
</svg>
'''


os.makedirs(OUT, exist_ok=True)
svg = build()
p = os.path.join(OUT, "banner.svg")
with io.open(p, "w", encoding="utf-8") as f:
    f.write(svg)
print("wordmark %.1fpx wide  |  wrote %s  %d bytes" % (WORDMARK_W, p, os.path.getsize(p)))
