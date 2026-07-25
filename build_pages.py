#!/usr/bin/env python3
"""
build_pages.py — emit a single-file gallery for GitHub Pages from the manifest.

Why this exists: 67% of Show HN posts above 300 points point at a hosted page on
the author's own domain rather than at a repository. A README is not a demo. This
is the smallest thing that satisfies that without becoming a web app — one HTML
file, no JavaScript, no build step, served from /docs on the default branch.

It deliberately does NOT add search. "searchable" is a measured winning word in
Show HN titles (8.9% hit rate against a 0.2% baseline), which makes it tempting,
and that is exactly why it must not go in a title unless the feature exists.
Ctrl+F is not a search feature.

    python3 build_pages.py            # writes docs/index.html
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

CSS = """
:root{--bg:#faf9f7;--fg:#17191a;--mut:#6a6f70;--line:#e0dedb;--acc:#1f5d4c;--card:#fff}
@media(prefers-color-scheme:dark){:root{--bg:#111312;--fg:#e9ebe6;--mut:#8b918c;--line:#2a2e2b;--acc:#62bfa1;--card:#181b19}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo",Roboto,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 96px}
header{border-bottom:2px solid var(--fg);padding:56px 0 20px;margin-bottom:36px}
h1{font-size:clamp(1.8rem,4vw,2.6rem);margin:0 0 10px;letter-spacing:-.02em}
.sub{color:var(--mut);max-width:60ch;margin:0}
.meta{margin-top:18px;font:13px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mut)}
.meta b{color:var(--fg)}
h2{font-size:1.35rem;margin:56px 0 6px;letter-spacing:-.01em}
h2:first-of-type{margin-top:0}
h2 .n{font:12px ui-monospace,monospace;color:var(--mut);margin-left:8px}
.cat-desc{color:var(--mut);margin:0 0 20px;max-width:70ch;font-size:.94rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}
figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:6px;overflow:hidden}
figure img{width:100%;display:block;aspect-ratio:1;object-fit:cover;background:var(--line)}
figcaption{padding:12px 14px}
.t{font-weight:640;font-size:.93rem;margin-bottom:7px}
pre{margin:0;background:transparent;color:var(--mut);font:11.5px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;word-break:break-word;max-height:8.4em;overflow:auto}
.seed{margin-top:8px;font:11px ui-monospace,monospace;color:var(--mut)}
.finding{border-left:3px solid var(--acc);padding:2px 0 2px 18px;margin:0 0 30px;max-width:74ch}
.finding h3{margin:0 0 8px;font-size:1.05rem}
.finding p{margin:0 0 10px;color:var(--mut)}
.finding code{background:var(--line);padding:.1em .35em;border-radius:3px;font-size:.88em;color:var(--fg)}
.fail{border-color:#9e2b25}
@media(prefers-color-scheme:dark){.fail{border-color:#e0776c}}
.fail .t{color:#9e2b25}
@media(prefers-color-scheme:dark){.fail .t{color:#e0776c}}
a{color:var(--acc)}
footer{margin-top:72px;padding-top:22px;border-top:1px solid var(--line);color:var(--mut);font-size:.9rem;max-width:74ch}
"""


def md_lite(s: str) -> str:
    """Just enough markdown for the findings prose: bold, code, paragraphs."""
    out = html.escape(s)
    import re
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out, flags=re.S)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return "".join(f"<p>{p.strip()}</p>" for p in out.split("\n\n") if p.strip())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", default="prompts.json")
    ap.add_argument("--out", default="docs/index.html")
    args = ap.parse_args()

    d = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    root = Path(args.manifest).parent
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # Pages serves /docs AS THE SITE ROOT, so "../images/..." escapes the served
    # tree and every image 404s. Copy them in instead — 10 MB duplicated is the
    # price of a self-contained page that the Pages CDN can serve under load,
    # and it avoids leaning on raw.githubusercontent.com, which is rate-limited.
    import shutil
    up = ""
    for e in list(d["entries"]) + (d.get("failures") or {}).get("entries", []):
        src = root / e["image"]
        if src.exists():
            dst = out.parent / e["image"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    if (root / "hero.webp").exists():
        shutil.copy2(root / "hero.webp", out.parent / "hero.webp")

    kept = [e for e in d["entries"] if (root / e["image"]).exists()]
    model = d.get("model", "the model")
    repo = d.get("repo", "")

    L = ['<!doctype html><html lang="en"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f"<title>{html.escape(model)} — {len(kept)} prompts, with the seeds and the failures</title>",
         f'<meta name="description" content="{len(kept)} reproducible {html.escape(model)} prompts with recorded seeds, plus the generations that failed and why.">',
         f"<style>{CSS}</style></head><body><div class=wrap>"]

    L.append("<header>")
    L.append(f"<h1>{html.escape(model)}: {len(kept)} prompts, the seeds, and the failures</h1>")
    L.append('<p class=sub>Every prompt below was run once, every image is the raw model output, '
             'and every entry carries the seed that produced it. The generations that did not work '
             'are kept too, at the bottom, because the limits are the part nobody publishes.</p>')
    L.append(f'<p class=meta>{d.get("generations", 150)} generations · <b>{len(kept)} kept</b> · '
             f'{d.get("generations", 150) - len(kept)} cut · ${d.get("spend", 1.26):.2f} total'
             f' · <a href="https://github.com/{html.escape(repo)}">github.com/{html.escape(repo)}</a></p>')
    L.append("</header>")

    f = d.get("findings")
    if f:
        L.append("<h2>What this model actually does</h2>")
        L.append(f'<p class=cat-desc>{html.escape(f.get("_intro",""))}</p>')
        for it in f.get("items", []):
            L.append(f'<div class=finding><h3>{html.escape(it["title"])}</h3>{md_lite(it["body"])}</div>')

    by = {}
    for e in kept:
        by.setdefault(e["category"], []).append(e)
    for cat, items in by.items():
        L.append(f'<h2>{html.escape(cat)}<span class=n>{len(items)}</span></h2>')
        desc = (d.get("categories") or {}).get(cat)
        if desc:
            L.append(f"<p class=cat-desc>{html.escape(desc)}</p>")
        L.append("<div class=grid>")
        for e in items:
            seed = (e.get("params") or {}).get("seed")
            extra = f' · from <code>{html.escape(e["source"])}</code> at strength {e.get("strength")}' if e.get("source") else ""
            L.append(f'<figure><img loading=lazy src="{up}{html.escape(e["image"])}" alt="{html.escape(e["title"])}">'
                     f'<figcaption><div class=t>{html.escape(e["title"])}</div>'
                     f'<pre>{html.escape(e["prompt"])}</pre>'
                     f'<div class=seed>seed {seed}{extra}</div></figcaption></figure>')
        L.append("</div>")

    fails = [x for x in (d.get("failures") or {}).get("entries", []) if (root / x["image"]).exists()]
    if fails:
        L.append(f'<h2>The failures<span class=n>{len(fails)}</span></h2>')
        L.append(f'<p class=cat-desc>{html.escape((d["failures"]).get("_what",""))}</p>')
        L.append("<div class=grid>")
        for x in fails:
            seed = (x.get("params") or {}).get("seed")
            L.append(f'<figure class=fail><img loading=lazy src="{up}{html.escape(x["image"])}" alt="{html.escape(x["claim"])}">'
                     f'<figcaption><div class=t>{html.escape(x["claim"])}</div>'
                     f'<pre>asked for: {html.escape(x.get("expected",""))}\n\n{html.escape(x["prompt"])}</pre>'
                     f'<div class=seed>seed {seed}</div></figcaption></figure>')
        L.append("</div>")

    # The reproducibility sentence has to be exact, because the whole claim here
    # is that you can check it yourself. Measured 2026-07-25: the endpoint is
    # deterministic — same seed, strength, prompt and input bytes returned a
    # pixel-identical image across two runs (0 of 1,048,576 pixels differed). But
    # the images in this repo are lossy WebP re-encodes, so re-running an
    # image-to-image entry against the copy here does not hand the model the
    # bytes that produced the original. Composition, palette and medium come
    # back; brush-level texture does not. Text-to-image entries take no image
    # input and are unaffected.
    L.append('<footer>Prompts are MIT. The images are AI-generated output from '
             f'{html.escape(model)}, presented as model output rather than as photographs or human '
             'artwork, and were produced by the repository owner under the Krea 2 Community '
             'License. The safety checker was left enabled for every request; one image it '
             'flagged was dropped. Images are re-encoded from PNG to WebP to keep the repository '
             'clonable. The endpoint is deterministic, so a recorded seed regenerates a '
             'text-to-image entry exactly. The five image-to-image entries are re-runnable from '
             'the WebP source in this repo rather than the original PNG, so they reproduce the '
             'edit — composition, palette, medium — but not the exact pixels.</footer>')
    L.append("</div></body></html>")

    out.write_text("\n".join(L), encoding="utf-8")
    kb = out.stat().st_size // 1024
    print(f"wrote {out} ({kb} KB, {len(kept)} entries + {len(fails)} failures)")
    print("\nEnable Pages: Settings -> Pages -> Deploy from branch -> main / docs")
    print(f"Then the page is https://<owner>.github.io/{repo.split('/')[-1]}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
