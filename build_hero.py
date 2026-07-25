#!/usr/bin/env python3
"""
build_hero.py — compose the README hero from the findings that are current.

This exists because the first hero outlived its own claims. It was built in
batch one and led with "Text: one sign holds, a list collapses", which batch
four disproved with the stringcount ladder. For three batches the first image
a visitor saw contradicted the repository's own headline finding — and that
finding is the reason anyone shares this.

So the hero is generated, not drawn once: three columns, working case on top,
failure underneath, captions from what the catalog currently says. Regenerate
it whenever a finding changes.

Captions are deliberately ASCII only. The previous hero rendered arrows and
typographic dashes as tofu boxes because the fallback font had no glyph.

    python3 build_hero.py            # writes hero.webp
"""

from __future__ import annotations

import argparse
import pathlib

from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent

# (column caption, top image, top note, bottom image, bottom note)
COLUMNS = [
    ("Text: write it out and it renders. Ask it to invent and it does not.",
     "images/stringcount-8.webp", "8 separate strings, every one correct",
     "images/failures/fail-menu.webp", "same board, rows left to the model: CATEPe, MILTERS"),
    ("Hands: I said 7 of 8 and a reader counted the fingers. Six on both.",
     "images/failures/hands-8.webp", "asked for exactly 3 raised: correct, on a six-digit hand",
     "images/failures/hands-5.webp", "asked for interlaced fingers, got a clasp"),
    ("A rule I built from two domains and had to throw away in a third.",
     "images/weave-6.webp", "chain: predicted to fail, came back correct",
     "images/failures/weave-4.webp", "figure-eight: the shape, never the knot"),
]


def font(size: int, bold: bool = False):
    names = ["Arial Bold.ttf", "Helvetica.ttc"] if bold else ["Arial.ttf", "Helvetica.ttc"]
    for n in names:
        for d in ("/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"):
            p = pathlib.Path(d + n)
            if p.exists():
                try:
                    return ImageFont.truetype(str(p), size)
                except Exception:
                    pass
    return ImageFont.load_default()


def wrap(draw, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="hero.webp")
    ap.add_argument("--cell", type=int, default=304)
    args = ap.parse_args()

    C = args.cell
    head, note = 44, 26
    W, H = C * 3, head + C + note + C + note
    im = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(im)
    fh, fn = font(13, bold=True), font(12)

    for i, (cap, top, tnote, bot, bnote) in enumerate(COLUMNS):
        x = i * C
        for j, line in enumerate(wrap(d, cap, fh, C - 20)[:2]):
            d.text((x + 10, 8 + j * 16), line, fill=(20, 20, 20), font=fh)
        for k, (path, txt) in enumerate(((top, tnote), (bot, bnote))):
            y = head + k * (C + note)
            im.paste(Image.open(HERE / path).convert("RGB").resize((C, C)), (x, y))
            d.text((x + 10, y + C + 7), wrap(d, txt, fn, C - 20)[0],
                   fill=(90, 90, 90), font=fn)

    out = HERE / args.out
    im.save(out, "WEBP", quality=88, method=6)
    print(f"wrote {out.name}  {im.size}  {out.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
