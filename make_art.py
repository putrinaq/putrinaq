"""Draws banner.svg and divider.svg. Run: python assets/make_art.py"""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))

FONT = {  # 5x7 pixel letters
    "A": "01110 10001 10001 11111 10001 10001 10001", "B": "11110 10001 10001 11110 10001 10001 11110",
    "C": "01111 10000 10000 10000 10000 10000 01111", "D": "11110 10001 10001 10001 10001 10001 11110",
    "E": "11111 10000 10000 11110 10000 10000 11111", "F": "11111 10000 10000 11110 10000 10000 10000",
    "G": "01111 10000 10000 10011 10001 10001 01111", "H": "10001 10001 10001 11111 10001 10001 10001",
    "I": "01110 00100 00100 00100 00100 00100 01110", "J": "00111 00010 00010 00010 00010 10010 01100",
    "K": "10001 10010 10100 11000 10100 10010 10001", "L": "10000 10000 10000 10000 10000 10000 11111",
    "M": "10001 11011 10101 10101 10001 10001 10001", "N": "10001 11001 10101 10011 10001 10001 10001",
    "O": "01110 10001 10001 10001 10001 10001 01110", "P": "11110 10001 10001 11110 10000 10000 10000",
    "Q": "01110 10001 10001 10001 10101 10010 01101", "R": "11110 10001 10001 11110 10100 10010 10001",
    "S": "01111 10000 10000 01110 00001 00001 11110", "T": "11111 00100 00100 00100 00100 00100 00100",
    "U": "10001 10001 10001 10001 10001 10001 01110", "V": "10001 10001 10001 10001 10001 01010 00100",
    "W": "10001 10001 10001 10101 10101 11011 10001", "X": "10001 01010 00100 00100 00100 01010 10001",
    "Y": "10001 01010 00100 00100 00100 00100 00100", "Z": "11111 00001 00010 00100 01000 10000 11111",
    "3": "11110 00001 00001 01110 00001 00001 11110", "!": "00100 00100 00100 00100 00100 00000 00100",
    "'": "010 010 000 000 000 000 000", ",": "000 000 000 000 000 010 100",
    "/": "00001 00001 00010 00100 01000 10000 10000", "+": "00000 00100 00100 11111 00100 00100 00000",
    "-": "00000 00000 00000 11111 00000 00000 00000", " ": "000 000 000 000 000 000 000",
}

BUNNY = [
    ".......oo.oo....",
    "......owwowwo...",
    "......owpowpo...",
    "......owpowpo...",
    "......owpowpo...",
    ".......owwwwwo..",
    "..oooo.owwwwwwo.",
    ".owwwwoowwwkwwo.",
    "owwwwwwwwwwwcwpo",
    "owwwwwwwwwwwwwo.",
    "owwwwwwwwwwwwo..",
    "oswwwwwwwwwwo...",
    "owsswwwwswwso...",
    ".oowwwoowwowwo..",
    "...ooo..oo.oo...",
]
SITTING = [
    "..oo...oo..",
    ".owwo.owwo.",
    ".owpo.opwo.",
    ".owpo.opwo.",
    ".owwooowwo.",
    ".owwwwwwwo.",
    "owwwwwwwwwo",
    "owwkwwwkwwo",
    "owcwwpwwcwo",
    ".owwwwwwwo.",
    "owwwwwwwwwo",
    "owswwwwwswo",
    ".ooooooooo.",
]
CARROT = [
    "..g.g.",
    "...gg.",
    "..rrg.",
    ".rrrr.",
    ".rrr..",
    "rrr...",
    "rr....",
]
HEART = [".hh.hh.", "hhhhhhh", "hhhhhhh", ".hhhhh.", "..hhh..", "...h..."]
TULIP = ["f.f.f", "fffff", ".fff.", "..e..", "e.e..", ".ee.."]
COL = {"o": "#4a3566", "w": "#fff7fb", "p": "#ff9ec7", "k": "#2b1b45", "c": "#ffc6de", "s": "#e3cfee",
       "g": "#6fd08c", "r": "#ff9a52", "h": "#ff8fb8", "e": "#4f9a7a", "f": "#ff9ec7"}


def cells(rows, x, y, px, col=COL):
    """Draw rows of characters as squares, joining neighbours of one colour."""
    out = []
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            n = c
            while n < len(row) and row[n] == row[c]:
                n += 1
            if row[c] in col:
                out.append(f'<rect x="{x + c * px}" y="{y + r * px}" width="{(n - c) * px}" height="{px}" fill="{col[row[c]]}"/>')
            c = n
    return "".join(out)


def text(s, cx, y, px, fill):
    rows = ["".join(FONT[ch].split()[r].replace("0", ".").replace("1", "#") + "." for ch in s) for r in range(7)]
    x = cx - (len(rows[0]) - 1) * px // 2
    return cells(rows, x, y, px, {"#": fill})


def banner():
    W, H, rnd = 1000, 340, random.Random(7)
    sky = ["#1b1238", "#231748", "#2d1d59", "#3a256b", "#4b2f7d", "#613b8c", "#7c4b99", "#9a5fa5", "#bb78b0", "#d994bb"]
    o = []
    for i, c in enumerate(sky):
        o.append(f'<rect y="{i * 26}" width="{W}" height="27" fill="{c}"/>')
        if i:  # dithered edge between two bands
            o.append("".join(f'<rect x="{x}" y="{i * 26 - 5}" width="5" height="5" fill="{c}"/>'
                             for x in range(5 * (i % 2), W, 10)))
    for i in range(70):
        x, y = rnd.randrange(200) * 5, rnd.randrange(32) * 5
        s = 5 if i % 6 == 0 else 3
        o.append(f'<rect class="t{i % 3}" x="{x}" y="{y}" width="{s}" height="{s}" fill="#fff4d6"/>')
    # moon
    for dy in range(-6, 7):
        half = int((6.4 ** 2 - dy * dy) ** .5)
        o.append(f'<rect x="{865 - half * 5}" y="{70 + dy * 5}" width="{half * 10 + 5}" height="5" fill="#fff1c9"/>')
    for x, y, w in ((845, 55, 10), (875, 75, 15), (855, 85, 5), (880, 50, 5)):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w // 2 // 5 * 5 + 5}" fill="#f3dba3"/>')
    # clouds
    for cls, x, y, k in (("cl1", 90, 70, 1), ("cl2", 690, 60, 1)):
        o.append(f'<g class="{cls}" fill="#fff" opacity=".22"><rect x="{x}" y="{y}" width="120" height="10"/>'
                 f'<rect x="{x + 15}" y="{y - 10}" width="80" height="10"/><rect x="{x + 35}" y="{y - 20}" width="35" height="10"/></g>')
    # hills
    import math
    for base, amp, per, off, c in ((238, 20, 260, 0, "#6b3f86"), (258, 14, 180, 90, "#4d2f72")):
        for x in range(0, W, 5):
            y = int((base + amp * math.sin((x + off) / per * 6.283)) // 5 * 5)
            o.append(f'<rect x="{x}" y="{y}" width="5" height="{H - y}" fill="{c}"/>')
    # title
    for dx, dy, c in ((5, 5, "#2b1b45"), (0, 0, "#fff7fb")):
        o.append(text("HI, I'M PUTRI!", 500 + dx, 76 + dy, 8, c))
    for i, s in enumerate(("SOFTWARE ENGINEERING STUDENT", "UI/UX DESIGNER + DEVELOPER", "PROFESSIONAL BUNNY ENJOYER")):
        o.append(f'<g class="tag g{i}">' + text(s, 502, 164, 4, "#2b1b45") + text(s, 500, 162, 4, "#ffd1e4") + "</g>")
    # meadow
    o.append(f'<rect y="290" width="{W}" height="50" fill="#2f5d5a"/><rect y="290" width="{W}" height="5" fill="#4f9a7a"/>')
    for x in range(0, W, 5):
        if rnd.random() < .3:
            h = rnd.choice((5, 5, 10))
            o.append(f'<rect x="{x}" y="{290 - h}" width="5" height="{h}" fill="#4f9a7a"/>')
        if rnd.random() < .16:
            o.append(f'<rect x="{x}" y="{300 + rnd.randrange(7) * 5}" width="5" height="5" fill="#3f7a6b"/>')
    for i, x in enumerate((40, 140, 215, 330, 420, 560, 615, 770, 905, 965)):
        o.append(cells(TULIP, x, 290 - 24 + (i % 3) * 3, 4, {**COL, "f": ("#ff9ec7", "#ffd27d", "#c7a6ff")[i % 3]}))
    o.append(cells(CARROT, 478, 268, 4))
    o.append(cells(SITTING, 690, 246, 4))
    o.append('<g class="love">' + cells(HEART, 722, 222, 3) + "</g>")
    o.append('<g class="run"><g class="hop">' + cells(BUNNY, 0, 246, 4) + "</g></g>")
    o.append(f'<rect y="{H - 5}" width="{W}" height="5" fill="#244a4a"/>')
    css = """
.t0,.t1,.t2{animation:tw 3s steps(3) infinite}.t1{animation-delay:-1s}.t2{animation-delay:-2s}
@keyframes tw{50%{opacity:.15}}
.cl1,.cl2{animation:dr 26s ease-in-out infinite alternate}.cl2{animation-direction:alternate-reverse}
@keyframes dr{from{transform:translateX(-40px)}to{transform:translateX(60px)}}
.tag{opacity:0;animation:tag 12s steps(1) infinite}.g1{animation-delay:-8s}.g2{animation-delay:-4s}
@keyframes tag{0%{opacity:1}33.33%,100%{opacity:0}}
.run{transform:translateX(250px);animation:run 13s linear infinite}
@keyframes run{from{transform:translateX(-80px)}to{transform:translateX(1020px)}}
.hop{animation:hop .65s cubic-bezier(.3,0,.7,1) infinite alternate}
@keyframes hop{from{transform:translateY(10px)}to{transform:translateY(-18px)}}
.love{animation:love 2.6s ease-out infinite}
@keyframes love{0%{transform:translateY(12px);opacity:0}30%{opacity:1}100%{transform:translateY(-22px);opacity:0}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.g0{opacity:1}}
"""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" shape-rendering="crispEdges">'
            f"<title>Hi, I'm Putri! A bunny hops through a garden at night.</title><style>{css}</style>"
            f'<clipPath id="r"><rect width="{W}" height="{H}" rx="18" shape-rendering="auto"/></clipPath>'
            f'<g clip-path="url(#r)">{"".join(o)}</g></svg>\n')


def divider():
    o, x = [], 0
    items = [HEART, CARROT, SITTING, CARROT, HEART]
    total = sum(len(i[0]) * 3 for i in items) + 40 * (len(items) - 1)
    x = (1000 - total) // 2
    for n, it in enumerate(items):
        h = len(it) * 3
        o.append(f'<g class="b" style="animation-delay:-{n * .3:.1f}s">' + cells(it, x, 50 - h, 3) + "</g>")
        x += len(it[0]) * 3 + 40
    for a in (0, 620):
        o.append(f'<g fill="#c7a6ff">' + "".join(f'<rect x="{a + i}" y="30" width="6" height="3"/>' for i in range(30, 350, 18)) + "</g>")
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 60" shape-rendering="crispEdges">'
            "<style>.b{animation:b 1.2s ease-in-out infinite alternate}@keyframes b{to{transform:translateY(-6px)}}"
            "@media (prefers-reduced-motion:reduce){.b{animation:none}}</style>" + "".join(o) + "</svg>\n")


for name, body in (("banner.svg", banner()), ("divider.svg", divider())):
    with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(body)
    print(name, len(body))
