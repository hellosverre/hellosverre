# Generates every panel on the profile README.
#
#   assets/banner.svg   hero -- wordmark, tagline, orchestration motif
#   assets/stack.svg    the stack, lit by a raking light that crosses it
#   assets/footer.svg   contact bookend
#
# Run: python tools/build.py
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import material as M
from material import P, MONO, mono_width, squircle, outline, defs, slab, edges, write

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")

WORDMARK_FONT = r"C:/Users/AK/AppData/Local/Microsoft/Windows/Fonts/AquireBold-8Ma60.otf"
NAME = "SVERRE"
TAGLINE = "building AI systems, fundamentals first"
STACK_LINE = "TypeScript  \u00b7  Python  \u00b7  Next.js  \u00b7  Hono  \u00b7  Postgres  \u00b7  Docker  \u00b7  Linux"
PLACE = "Ski \u00b7 Norge"
EMAIL = "sverresig@proton.me"
PITCH = "Building an AI system that has to survive contact with real users?"
AVAILABILITY = "\u00e5pen for l\u00e6replass \u00b7 aug 2027"

PAD = 56


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
        f'</g>')


# ---------------------------------------------------------------- banner

def banner():
    W, H = 1000, 288
    uid = "b"
    cx, cy, s = 872, 128, 1.15

    # Orchestration motif: a controller dispatching work to four workers and collecting
    # it back. Hairlines and one accent -- a diagram, not decoration.
    peers = [(-58, -46), (62, -30), (-36, 58), (58, 50)]
    graph = []
    for dx, dy in peers:
        graph.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+dx*s:.1f}" y2="{cy+dy*s:.1f}" '
                     f'stroke="{P["accent"]}" stroke-width="1" opacity="0.28"/>')
    for i, (dx, dy) in enumerate(peers):
        px, py = cx + dx * s, cy + dy * s
        graph.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="none" '
                     f'stroke="{P["accent"]}" stroke-width="1.3" opacity="0.6">'
                     f'<animate attributeName="opacity" values="0.45;0.95;0.45" dur="{4.0+i*0.6}s" '
                     f'repeatCount="indefinite" begin="{i*0.7}s"/></circle>')
        # request out, response back -- the round trip, not a one-way particle
        for j, (a, b, delay) in enumerate(((cx, px, i * 0.85), (px, cx, i * 0.85 + 1.7))):
            ay, by = (cy, py) if j == 0 else (py, cy)
            graph.append(
                f'<circle r="{2.0 if j == 0 else 1.6}" fill="{P["accent"]}" opacity="0">'
                f'<animate attributeName="cx" values="{a};{b:.1f}" dur="3.4s" repeatCount="indefinite" begin="{delay}s"/>'
                f'<animate attributeName="cy" values="{ay};{by:.1f}" dur="3.4s" repeatCount="indefinite" begin="{delay}s"/>'
                f'<animate attributeName="opacity" values="0;{0.9 if j == 0 else 0.5};{0.9 if j == 0 else 0.5};0" '
                f'keyTimes="0;0.2;0.65;1" dur="3.4s" repeatCount="indefinite" begin="{delay}s"/></circle>')
    graph.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{P["accent"]}" opacity="0.9"/>')

    d, wmw, wms = outline(WORDMARK_FONT, NAME, 54.0, 0.022)
    rim, border = edges(uid, W, H)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Sverre - {TAGLINE}">
  <defs>{defs(uid, W, H)}</defs>
  <g clip-path="url(#{uid}-clip)">
    {slab(uid, W, H, sweep_dur=13)}
    {"".join(graph)}
    <g transform="translate({PAD},112) scale({wms:.5f})"><path d="{d}" fill="{P['text']}"/></g>
    <rect x="{PAD + 2}" y="128" width="62" height="3" rx="1.5" fill="{P['accent']}"/>
    <text x="{PAD}" y="180" font-family="{MONO}" font-size="19.5" fill="{P['accent']}">&#8250;</text>
    <text x="{PAD + 22}" y="180" font-family="{MONO}" font-size="19.5" fill="{P['muted']}">{TAGLINE}</text>
    <text x="{PAD}" y="240" font-family="{MONO}" font-size="13" fill="{P['dim']}" letter-spacing="0.3">{STACK_LINE}</text>
    {flag(W - PAD - 21 - 8 - mono_width(PLACE, 12.5), 229)}
    <text x="{W - PAD}" y="240" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{P['dim']}">{PLACE}</text>
    {rim}
  </g>
  {border}
</svg>
'''


# ---------------------------------------------------------------- stack

GROUPS = [
    ("WRITE", ["TypeScript", "JavaScript", "Python"]),
    ("BUILD", ["Next.js", "React", "Hono", "Tailwind", "Tauri"]),
    ("STORE", ["Postgres", "libSQL", "Redis", "Drizzle"]),
    ("RUN",   ["Linux", "Docker", "Cloudflare Tunnel", "Vercel", "Proxmox"]),
]

CHIP_H, CHIP_FS, CHIP_PAD, CHIP_GAP = 36, 15, 16, 10
ROW_STEP, ROW_FIRST = 60, 66
CHIPS_X, DIVIDER_X = 168, 146


def _chips(lit):
    """One pass over the chip grid. `lit` renders the copy the raking light reveals.

    Group label sits in its own left column so the rows use the full panel width
    instead of trailing off into dead space on the right.
    """
    stroke = P["accent"] if lit else "#FFFFFF"
    stroke_op = "0.55" if lit else "0.09"
    fill_op = "0.05" if lit else "0.025"
    label = P["accent"] if lit else P["muted"]
    out = []
    for gi, (group, items) in enumerate(GROUPS):
        mid = ROW_FIRST + gi * ROW_STEP
        if not lit:
            out.append(f'<text x="{PAD}" y="{mid + 4}" font-family="{MONO}" font-size="10.5" '
                       f'fill="{P["dim"]}" letter-spacing="1.6">{group}</text>')
        x = CHIPS_X
        for item in items:
            w = mono_width(item, CHIP_FS) + CHIP_PAD * 2
            out.append(
                f'<rect x="{x:.1f}" y="{mid - CHIP_H/2}" width="{w:.1f}" height="{CHIP_H}" rx="9" '
                f'fill="#FFFFFF" fill-opacity="{fill_op}" stroke="{stroke}" stroke-opacity="{stroke_op}" stroke-width="1"/>'
                f'<text x="{x + w/2:.1f}" y="{mid + 5}" text-anchor="middle" font-family="{MONO}" '
                f'font-size="{CHIP_FS}" fill="{label}">{item}</text>')
            x += w + CHIP_GAP
    return "".join(out)


def stack():
    W = 1000
    H = ROW_FIRST + (len(GROUPS) - 1) * ROW_STEP + CHIP_H // 2 + 36
    uid = "s"
    rim, border = edges(uid, W, H)
    BAND = 300

    # The lit copy of the grid is masked by a soft band travelling left to right, so
    # chips brighten as the light rakes over them and fall back as it passes.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Stack: {', '.join(i for _, g in GROUPS for i in g)}">
  <defs>{defs(uid, W, H)}
    <linearGradient id="{uid}-rakeg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"   stop-color="#000000"/>
      <stop offset="0.5" stop-color="#FFFFFF"/>
      <stop offset="1"   stop-color="#000000"/>
    </linearGradient>
    <mask id="{uid}-rake">
      <rect width="{W}" height="{H}" fill="#000000"/>
      <g transform="translate({-BAND},0)">
        <rect width="{BAND}" height="{H}" fill="url(#{uid}-rakeg)"/>
        <animateTransform attributeName="transform" type="translate"
                          values="{-BAND},0; {W},0" dur="9s" repeatCount="indefinite"/>
      </g>
    </mask>
  </defs>
  <g clip-path="url(#{uid}-clip)">
    {slab(uid, W, H, sweep_dur=17, sweep_delay=2)}
    <line x1="{DIVIDER_X}" y1="{ROW_FIRST - 30}" x2="{DIVIDER_X}" y2="{H - 36}"
          stroke="#FFFFFF" stroke-opacity="0.06" stroke-width="1"/>
    {_chips(lit=False)}
    <g mask="url(#{uid}-rake)">{_chips(lit=True)}</g>
    {rim}
  </g>
  {border}
</svg>
'''


# ---------------------------------------------------------------- footer

def footer():
    W, H = 1000, 140
    uid = "f"
    rim, border = edges(uid, W, H)
    dot_x = W - PAD - mono_width(AVAILABILITY, 12.5) - 20

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Contact: {EMAIL}">
  <defs>{defs(uid, W, H)}</defs>
  <g clip-path="url(#{uid}-clip)">
    {slab(uid, W, H, sweep_dur=15, sweep_delay=5)}
    <text x="{PAD}" y="62" font-family="{MONO}" font-size="24" fill="{P['accent']}">{EMAIL}</text>
    <text x="{PAD}" y="94" font-family="{MONO}" font-size="13" fill="{P['muted']}">{PITCH}</text>

    <circle cx="{dot_x:.1f}" cy="72" r="4" fill="{P['accent']}"/>
    <circle cx="{dot_x:.1f}" cy="72" r="4" fill="none" stroke="{P['accent']}" stroke-width="1">
      <animate attributeName="r" values="4;13;13" keyTimes="0;0.7;1" dur="2.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0" keyTimes="0;0.7;1" dur="2.6s" repeatCount="indefinite"/>
    </circle>
    <text x="{W - PAD}" y="77" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{P['dim']}">{AVAILABILITY}</text>
    {rim}
  </g>
  {border}
</svg>
'''


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("building panels:")
    write(os.path.join(OUT, "banner.svg"), banner())
    write(os.path.join(OUT, "stack.svg"), stack())
    write(os.path.join(OUT, "footer.svg"), footer())
