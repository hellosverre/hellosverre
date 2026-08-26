# Shared material for every panel on the profile.
#
# One surface language: green-black slab, superellipse corners, film grain, a rim light
# on the top edge, and exactly one slow-moving specular band. Every panel is built from
# these primitives so the README reads as one designed object rather than a header
# followed by a pile of third-party badges.
#
# Colours come from tools/palette.py -- authored in OKLCH, one hue (158), varying almost
# entirely in lightness. Contrast ratios are asserted there.
#
# Text that must survive GitHub's camo proxy is either a system monospace stack (camo
# blocks webfont requests, so the family has to be one the reader already has) or, for
# the wordmark, outlined to vector paths at build time.
import io

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Identity

P = {
    "ink":     "#030D07",   # bottom of the surface ramp
    "surface": "#081A10",   # top of the surface ramp
    "text":    "#EFF5F1",
    "muted":   "#A5ADA8",
    "dim":     "#767E79",
    "accent":  "#76D5A1",
}

MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"

# A monospace advance is a fixed fraction of the font size, which is the only reason
# chip widths can be laid out without measuring text at build time. Verified against
# the rendered output rather than assumed.
MONO_ADVANCE = 0.601


def mono_width(text, size):
    return len(text) * size * MONO_ADVANCE


def squircle(w, h, r, n=4.5, seg=18):
    """Rounded rect whose corners are superellipse quadrants (|x|^n + |y|^n = r^n).

    A border-radius corner has discontinuous curvature where the arc meets the straight
    edge; a superellipse does not, which is why Apple's shapes use one.
    """
    def quad(cx, cy, sx, sy):
        return [(cx + sx * (r * i / seg),
                 cy + sy * (max(r ** n - (r * i / seg) ** n, 0.0)) ** (1.0 / n))
                for i in range(seg + 1)]

    # Clockwise from the top edge. Each quadrant lands on the two edges it joins, so the
    # straight runs between corners come for free.
    d = ["M %.2f %.2f" % (r, 0)]
    for pts in (quad(w - r, r, 1, -1),
                quad(w - r, h - r, 1, 1)[::-1],
                quad(r, h - r, -1, 1),
                quad(r, r, -1, -1)[::-1]):
        d += ["L %.2f %.2f" % pt for pt in pts]
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


def defs(uid, w, h, radius=30, sweep_dur=13, sweep_delay=0, band=360):
    """The shared <defs> for one panel.

    ids are namespaced per panel because GitHub inlines several of these images into one
    document; colliding ids would make the last panel's gradients win everywhere.
    """
    return f'''
    <linearGradient id="{uid}-slab" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0" stop-color="{P['surface']}"/>
      <stop offset="1" stop-color="{P['ink']}"/>
    </linearGradient>

    <linearGradient id="{uid}-rim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"    stop-color="#FFFFFF" stop-opacity="0.02"/>
      <stop offset="0.35" stop-color="#FFFFFF" stop-opacity="0.16"/>
      <stop offset="1"    stop-color="#FFFFFF" stop-opacity="0.03"/>
    </linearGradient>

    <linearGradient id="{uid}-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"    stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="0.25" stop-color="#FFFFFF" stop-opacity="0.018"/>
      <stop offset="0.5"  stop-color="#FFFFFF" stop-opacity="0.075"/>
      <stop offset="0.75" stop-color="#FFFFFF" stop-opacity="0.018"/>
      <stop offset="1"    stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>

    <filter id="{uid}-grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch" result="n"/>
      <feColorMatrix in="n" type="saturate" values="0"/>
    </filter>

    <clipPath id="{uid}-clip"><path d="{squircle(w, h, radius)}"/></clipPath>'''


def slab(uid, w, h, sweep_dur=13, sweep_delay=0, band=360):
    """Background layers: gradient, travelling specular band, grain."""
    return f'''
    <rect width="{w}" height="{h}" fill="url(#{uid}-slab)"/>
    <g transform="translate({-band - 100},0)">
      <rect x="0" y="{-h}" width="{band}" height="{h * 3}" fill="url(#{uid}-sheen)"
            transform="rotate(14 {band/2} {h/2})"/>
      <animateTransform attributeName="transform" type="translate"
                        values="{-band - 100},0; {w + band},0" dur="{sweep_dur}s"
                        begin="{sweep_delay}s" repeatCount="indefinite"/>
    </g>
    <rect width="{w}" height="{h}" filter="url(#{uid}-grain)" opacity="0.055"/>'''


def edges(uid, w, h, radius=30):
    """Rim light along the top edge, then the hairline border on top of everything."""
    return (f'<rect width="{w}" height="1.25" fill="url(#{uid}-rim)"/>',
            f'<path d="{squircle(w, h, radius)}" fill="none" stroke="#FFFFFF" '
            f'stroke-opacity="0.07" stroke-width="1"/>')


def write(path, svg):
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    import os
    print("  %-28s %6d bytes" % (os.path.basename(path), os.path.getsize(path)))
