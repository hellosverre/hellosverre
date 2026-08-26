# Palette for the profile banner, authored in OKLCH and converted to sRGB.
#
# Two rules drive every value here, both taken from the anti-slop consensus:
#   1. One accent, under 80% HSL saturation. Hierarchy comes from lightness, not chroma.
#   2. The dark base is a *chosen* hue (green-black), not the default slate-indigo ink
#      that every dark SaaS ships.
#
# Gradients stay inside a ~20 deg hue band and move mostly in lightness, so they read as
# a lit surface rather than as decoration. OKLCH interpolation keeps the midpoints from
# going muddy the way sRGB blends do.
import math


def _lin_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def _srgb_to_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def oklch_to_hex(L, C, H):
    a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    out = []
    clipped = False
    for v in (r, g, bl):
        v = _lin_to_srgb(v)
        if v < -0.001 or v > 1.001:
            clipped = True
        out.append(max(0.0, min(1.0, v)))
    return "#%02X%02X%02X" % tuple(round(v * 255) for v in out), clipped


def relative_luminance(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5))
    r, g, b = _srgb_to_lin(r), _srgb_to_lin(g), _srgb_to_lin(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = relative_luminance(a), relative_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hsl_sat(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5))
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return 0.0
    d = mx - mn
    return d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)


# Hue 158 = jade. Far enough from Supabase's #3ECF8E to not read as a clone,
# far enough from Tailwind green-500 to not read as a default.
HUE = 158

SPEC = {
    # surfaces: pure lightness ramp on one hue, very low chroma
    "ink":       (0.150, 0.018, HUE),   # deepest -- card base, bottom of the ramp
    "surface":   (0.196, 0.022, HUE),   # top of the ramp
    "elevated":  (0.245, 0.026, HUE),   # inner panels
    # text: off-white with a faint green cast, never #FFFFFF
    "text":      (0.965, 0.008, HUE),
    "muted":     (0.740, 0.012, HUE),
    "dim":       (0.585, 0.012, HUE),
    # the single accent
    "accent":    (0.800, 0.118, HUE),
    "accent_dim":(0.660, 0.100, HUE),
}

P = {}
for name, (L, C, H) in SPEC.items():
    hexv, clipped = oklch_to_hex(L, C, H)
    P[name] = hexv
    flag = "  <-- OUT OF GAMUT" if clipped else ""
    print("%-11s oklch(%.3f %.3f %d)  %s  sat=%3.0f%%%s"
          % (name, L, C, H, hexv, hsl_sat(hexv) * 100, flag))

print()
for fg in ("text", "muted", "dim", "accent"):
    print("%-7s on ink     %5.2f:1   %s"
          % (fg, contrast(P[fg], P["ink"]),
             "AA body" if contrast(P[fg], P["ink"]) >= 4.5
             else ("AA large" if contrast(P[fg], P["ink"]) >= 3.0 else "decorative only")))

print()
print("accent HSL saturation: %.0f%%  (anti-slop rule: keep under 80%%)" % (hsl_sat(P["accent"]) * 100))
print("PALETTE = %r" % (P,))
