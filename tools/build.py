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
STACK_LINE = "TypeScript  \u00b7  Python  \u00b7  Next.js  \u00b7  Hono  \u00b7  Postgres  \u00b7  Docker  \u00b7  Linux"
EMAIL = "sverresig@proton.me"

# GitHub strips <style> and JS from markdown, so a live language switch is impossible.
# The toggle is two linked pills and a second README; the panels carrying copy are
# therefore built once per language. stack.svg is tech names only, so it stays shared.
COPY = {
    "en": dict(
        tagline="building AI systems, fundamentals first",
        place="Ski \u00b7 Norway",
        pitch="Building an AI system that has to survive contact with real users?",
        availability="open to apprenticeship \u00b7 aug 2027",
    ),
    "no": dict(
        tagline="bygger AI-systemer, grunnprinsipper f\u00f8rst",
        place="Ski \u00b7 Norge",
        pitch="Bygger du et AI-system som m\u00e5 t\u00e5le m\u00f8tet med ekte brukere?",
        availability="\u00e5pen for l\u00e6replass \u00b7 aug 2027",
        arch_caption="Ingen \u00e5pne innkommende porter p\u00e5 VM-en \u2014 tunnelen ringer ut til Cloudflare.",
        arch_sub="foresp\u00f8rselens vei",
    ),
}
COPY["en"].update(
    arch_caption="No inbound ports open on the VM \u2014 the tunnel dials out to Cloudflare.",
    arch_sub="request path",
)


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

def banner(lang):
    TAGLINE, PLACE = COPY[lang]["tagline"], COPY[lang]["place"]
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
    ("RUN",   ["Linux", "Docker", "Cloudflare Tunnel", "Vercel"]),
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

def footer(lang):
    PITCH, AVAILABILITY = COPY[lang]["pitch"], COPY[lang]["availability"]
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


# ---------------------------------------------------------------- architecture

# aether, taken from the two repo descriptions: a Next.js 15 frontend on Vercel and a
# Hono + Drizzle backend on a VM reached through a Cloudflare Tunnel.
NODES = [
    dict(x=56,  w=118, cy=142, label="browser",    sub=""),
    dict(x=214, w=168, cy=142, label="Vercel",     sub="Next.js 15"),
    dict(x=422, w=176, cy=142, label="Cloudflare", sub="Tunnel"),
    dict(x=638, w=150, cy=142, label="VM",         sub="Hono + Drizzle"),
    dict(x=828, w=126, cy=100, label="Postgres",   sub=""),
    dict(x=828, w=126, cy=184, label="Redis",      sub=""),
]
HOPS = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5)]
BOX_H = 56


def _hop(a, b, begin, back=False):
    """A packet crossing one connector. Request out in accent, response back smaller."""
    x1, y1 = a["x"] + a["w"], a["cy"]
    x2, y2 = b["x"], b["cy"]
    if back:
        x1, y1, x2, y2 = x2, y2, x1, y1
    r, op = (2.1, 0.95) if not back else (1.6, 0.5)
    return (f'<circle r="{r}" fill="{P["accent"]}" opacity="0">'
            f'<animate attributeName="cx" values="{x1};{x2}" dur="0.9s" repeatCount="indefinite" begin="{begin}s"/>'
            f'<animate attributeName="cy" values="{y1};{y2}" dur="0.9s" repeatCount="indefinite" begin="{begin}s"/>'
            f'<animate attributeName="opacity" values="0;{op};{op};0" keyTimes="0;0.15;0.75;1" '
            f'dur="0.9s" repeatCount="indefinite" begin="{begin}s"/></circle>')


def architecture(lang):
    C = COPY[lang]
    W, H = 1000, 268
    uid = "a"
    rim, border = edges(uid, W, H)

    parts = []
    for a_i, b_i in HOPS:
        a, b = NODES[a_i], NODES[b_i]
        parts.append(f'<path d="M {a["x"]+a["w"]} {a["cy"]} L {b["x"]} {b["cy"]}" fill="none" '
                     f'stroke="{P["accent"]}" stroke-width="1" opacity="0.26"/>')
    for n in NODES:
        top = n["cy"] - BOX_H / 2
        parts.append(
            f'<rect x="{n["x"]}" y="{top}" width="{n["w"]}" height="{BOX_H}" rx="10" '
            f'fill="#FFFFFF" fill-opacity="0.028" stroke="#FFFFFF" stroke-opacity="0.10" stroke-width="1"/>')
        cx = n["x"] + n["w"] / 2
        if n["sub"]:
            parts.append(f'<text x="{cx}" y="{n["cy"] - 2}" text-anchor="middle" font-family="{MONO}" '
                         f'font-size="13" fill="{P["text"]}">{n["label"]}</text>'
                         f'<text x="{cx}" y="{n["cy"] + 15}" text-anchor="middle" font-family="{MONO}" '
                         f'font-size="10.5" fill="{P["dim"]}">{n["sub"]}</text>')
        else:
            parts.append(f'<text x="{cx}" y="{n["cy"] + 5}" text-anchor="middle" font-family="{MONO}" '
                         f'font-size="13" fill="{P["text"]}">{n["label"]}</text>')
    # one relay per hop, staggered, then the responses coming back the other way
    for i, (a_i, b_i) in enumerate(HOPS):
        a, b = NODES[a_i], NODES[b_i]
        out = i * 0.75 if b_i != 5 else 3 * 0.75
        parts.append(_hop(a, b, out))
        parts.append(_hop(a, b, out + 3.2, back=True))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="aether architecture: browser to Vercel to Cloudflare Tunnel to VM running Hono, backed by Postgres and Redis">
  <defs>{defs(uid, W, H)}</defs>
  <g clip-path="url(#{uid}-clip)">
    {slab(uid, W, H, sweep_dur=21, sweep_delay=3)}
    <text x="{PAD}" y="46" font-family="{MONO}" font-size="10.5" fill="{P['dim']}" letter-spacing="1.6">AETHER</text>
    <text x="{PAD + 76}" y="46" font-family="{MONO}" font-size="10.5" fill="{P['accent']}" letter-spacing="1.2">{C['arch_sub']}</text>
    {"".join(parts)}
    <text x="{PAD}" y="240" font-family="{MONO}" font-size="12" fill="{P['muted']}">{C['arch_caption']}</text>
    {rim}
  </g>
  {border}
</svg>
'''


# ---------------------------------------------------------------- language pills

PILL_H, PILL_FS = 36, 13


def pill(label, on):
    """One half of the language toggle.

    Two separate images rather than one, because a single SVG can only carry one link
    in markdown -- per-region hrefs inside an <img> never reach the reader.
    """
    W = int(mono_width(label, PILL_FS) + 38)
    H = PILL_H
    uid = "p"
    stroke, stroke_op = (P["accent"], "0.55") if on else ("#FFFFFF", "0.10")
    text = P["accent"] if on else P["muted"]
    shape = squircle(W, H, 10)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}{' (current)' if on else ''}">
  <defs>
    <linearGradient id="{uid}-slab" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0" stop-color="{P['surface']}"/>
      <stop offset="1" stop-color="{P['ink']}"/>
    </linearGradient>
    <clipPath id="{uid}-clip"><path d="{shape}"/></clipPath>
  </defs>
  <g clip-path="url(#{uid}-clip)">
    <rect width="{W}" height="{H}" fill="url(#{uid}-slab)"/>
    <text x="{W/2}" y="{H/2 + 4.5}" text-anchor="middle" font-family="{MONO}"
          font-size="{PILL_FS}" fill="{text}" letter-spacing="0.4">{label}</text>
  </g>
  <path d="{shape}" fill="none" stroke="{stroke}" stroke-opacity="{stroke_op}" stroke-width="1"/>
</svg>
'''


PILLS = {"en": "English", "no": "Norsk"}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)

    print("building panels:")
    write(os.path.join(OUT, "stack.svg"), stack())
    for lang in COPY:
        write(os.path.join(OUT, "banner-%s.svg" % lang), banner(lang))
        write(os.path.join(OUT, "footer-%s.svg" % lang), footer(lang))
        write(os.path.join(OUT, "architecture-%s.svg" % lang), architecture(lang))
    for lang, label in PILLS.items():
        for state in (True, False):
            write(os.path.join(OUT, "lang-%s-%s.svg" % (lang, "on" if state else "off")),
                  pill(label, state))
