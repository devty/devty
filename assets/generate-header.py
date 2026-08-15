import os
# Generates the theme-aware profile banner. Deterministic: no randomness,
# so re-running produces byte-identical output.
W, H = 880, 176

# Piano-roll motif: (start_col, length_cols, lane). lane 0 = highest pitch.
# Hand-picked contour -- a rising arc that resolves down, so it reads as a
# phrase rather than noise.
NOTES = [
    (0, 3, 8), (3, 2, 6), (5, 3, 7), (8, 2, 4),
    (10, 4, 3), (11, 2, 5), (14, 3, 2), (15, 2, 4),
    (17, 2, 1), (18, 3, 3), (20, 2, 0), (21, 3, 2),
    (2, 2, 10), (7, 2, 9), (13, 2, 6), (19, 3, 5),
]

ROLL_X, ROLL_Y, ROLL_W = 502, 26, 376
LANES, LANE_H, LANE_GAP = 12, 8, 2
COLS = 24
COL_W = ROLL_W / COLS

THEMES = {
    "light": dict(bg="#ffffff", rule="#d8dee4", name="#1f2328", sub="#59636e",
                  meta="#6e7781", lane="#eef1f4", g1="#6E56CF", g2="#E0724A"),
    "dark":  dict(bg="#0d1117", rule="#30363d", name="#e6edf3", sub="#9198a1",
                  meta="#7d8590", lane="#161b22", g1="#A78BFA", g2="#F0885B"),
}

SANS = "-apple-system, BlinkMacSystemFont, &#39;Segoe UI&#39;, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, &#39;SF Mono&#39;, Menlo, Consolas, monospace"

for theme, c in THEMES.items():
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Tyler Singletary — Music, Code, ML and AI">')
    p.append('<defs>')
    p.append(f'<linearGradient id="g" gradientUnits="userSpaceOnUse" '
             f'x1="{ROLL_X}" y1="{ROLL_Y+118}" x2="{ROLL_X+ROLL_W}" y2="{ROLL_Y}">'
             f'<stop offset="0" stop-color="{c["g1"]}"/>'
             f'<stop offset="1" stop-color="{c["g2"]}"/></linearGradient>')
    p.append(f'<linearGradient id="r" gradientUnits="userSpaceOnUse" x1="2" y1="0" x2="66" y2="0">'
             f'<stop offset="0" stop-color="{c["g1"]}"/>'
             f'<stop offset="1" stop-color="{c["g2"]}"/></linearGradient>')
    p.append('</defs>')
    p.append(f'<rect width="{W}" height="{H}" rx="10" fill="{c["bg"]}"/>')

    # lane guides
    for i in range(LANES):
        y = ROLL_Y + i * (LANE_H + LANE_GAP)
        p.append(f'<rect x="{ROLL_X}" y="{y}" width="{ROLL_W}" height="{LANE_H}" rx="2" fill="{c["lane"]}"/>')

    # notes
    for col, length, lane in NOTES:
        x = ROLL_X + col * COL_W
        w = length * COL_W - 3
        y = ROLL_Y + lane * (LANE_H + LANE_GAP)
        op = round(0.62 + 0.38 * (1 - lane / (LANES - 1)), 3)
        p.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{LANE_H}" rx="2" fill="url(#g)" opacity="{op}"/>')

    # accent rule under the text block
    p.append(f'<rect x="2" y="124" width="64" height="3" rx="1.5" fill="url(#r)"/>')

    p.append(f'<text x="2" y="62" font-family="{SANS}" font-size="42" font-weight="700" letter-spacing="-0.8" fill="{c["name"]}">Tyler Singletary</text>')
    p.append(f'<text x="2" y="94" font-family="{MONO}" font-size="16" fill="{c["sub"]}">Music &#183; Code &#183; ML and AI</text>')
    p.append(f'<text x="2" y="150" font-family="{SANS}" font-size="13.5" fill="{c["meta"]}">Brooklyn, NY &#183; building under @orchestrately</text>')
    p.append('</svg>')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"header-{theme}.svg")
    open(out, "w").write("\n".join(p) + "\n")
    print("wrote", out)
