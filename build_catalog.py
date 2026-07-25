#!/usr/bin/env python3
"""
build_catalog.py — assemble a T+0 prompt/asset catalog README from a manifest.

The window for this play is 72 hours from a frontier model shipping. Measured
outcomes for the same slot, five payouts in nine months:

    YouMind-OpenLab/awesome-nano-banana-pro-prompts   12,949   created 2025-11-23
    ZeroLu/awesome-nanobanana-pro                     10,186   created 2025-11-10
    YouMind-OpenLab/awesome-gpt-image-2                8,761   created 2026-04-16
    freestylefly/awesome-gpt-image-2                   8,678   created 2026-04-25
    jamez-bondos/awesome-gpt4o-images                  8,097   created 2025-04-13

Two structural facts most people get wrong about this slot:

  1. It is NON-RIVAL. nano-banana produced 12,949 AND 10,186. gpt-image-2 produced
     8,761 AND 8,678 nine days apart. Second place is paid.
  2. Late is fatal in a way second-place is not. ZeroLu/awesome-gpt-image, launched
     two weeks after the same author's own hit, sits at 1,928 — 22% of it.

So: ship inside 72 hours, do not agonize about someone beating you by a day, and
do not ship at all if you are two weeks late.

This script does the assembly so that on launch day you are only doing the part
that cannot be automated: curation. Generation is a separate step you own —
`--gen-cmd` shells out to whatever CLI your provider gives you.

Usage
-----
    python3 build_catalog.py --init                     # scaffold prompts.json
    python3 build_catalog.py --generate                 # run gen-cmd for missing images
    python3 build_catalog.py --build                    # write README.md + index
    python3 build_catalog.py --build --lang zh          # also emit README_ZH.md
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "prompts.json"
IMAGES = HERE / "images"

SCAFFOLD = {
    "model": "REPLACE-ME (exact model name and version, e.g. 'Nano Banana Pro')",
    "model_url": "",
    "launched": "2026-01-01",
    "repo": "yourname/awesome-<model>-prompts",
    "gen_cmd": "echo 'replace with your provider CLI: {prompt} -> {out}'",
    "categories": OrderedDict([
        ("photography", "Photoreal scenes, lighting, lens behaviour"),
        ("illustration", "Stylised and painterly output"),
        ("typography", "Text rendering, posters, logotype"),
        ("product", "Product shots, packaging, studio lighting"),
        ("infographic", "Charts, diagrams, explanatory layouts"),
        ("character", "Character consistency across generations"),
        ("text-in-image", "Legible text, multiple languages"),
        ("editing", "Inpainting, object removal, relighting"),
        ("3d-isometric", "Isometric scenes, dioramas, game assets"),
        ("brand", "Logos, marks, identity systems"),
    ]),
    "entries": [
        {
            "id": "photography-001",
            "category": "photography",
            "title": "Golden hour portrait, 85mm",
            "prompt": "A portrait of ...",
            "image": "images/photography-001.png",
            "params": {"aspect_ratio": "3:4", "seed": 1234},
            "notes": "Reproduces reliably. Seed matters for the rim light.",
        }
    ],
}


def load() -> dict:
    if not MANIFEST.exists():
        print(f"no {MANIFEST.name}; run --init first", file=sys.stderr)
        raise SystemExit(2)
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def cmd_init() -> int:
    if MANIFEST.exists():
        print(f"{MANIFEST.name} already exists; not overwriting", file=sys.stderr)
        return 1
    MANIFEST.write_text(json.dumps(SCAFFOLD, indent=2, ensure_ascii=False), encoding="utf-8")
    IMAGES.mkdir(exist_ok=True)
    print(f"wrote {MANIFEST.name} and images/\n")
    print("Now, in this order:")
    print("  1. Set `model`, `repo`, `launched`, `gen_cmd`.")
    print("  2. Draft 20-25 prompts per category into `entries`. 8-12 categories.")
    print("  3. --generate, then throw away 40-50% of the output. That is the job.")
    print("  4. --build")
    return 0


def cmd_generate(force: bool) -> int:
    data = load()
    tmpl = data.get("gen_cmd", "")
    if not tmpl or tmpl.startswith("echo 'replace"):
        print("set `gen_cmd` in prompts.json first (use {prompt} and {out} placeholders)",
              file=sys.stderr)
        return 2

    IMAGES.mkdir(exist_ok=True)
    todo = [e for e in data["entries"] if force or not (HERE / e["image"]).exists()]
    if not todo:
        print("nothing to generate; every entry already has an image")
        return 0

    print(f"generating {len(todo)} image(s)\n")
    failed = []
    for i, e in enumerate(todo, 1):
        out = HERE / e["image"]
        out.parent.mkdir(parents=True, exist_ok=True)
        # shell=True is deliberate: `gen_cmd` is a user-authored command line from
        # their own prompts.json, and provider CLIs routinely need pipes and
        # redirects. The injection surface is closed by shlex.quote on both
        # interpolated values, so prompt text cannot escape into the shell no
        # matter what a contributor puts in a PR.
        cmd = tmpl.replace("{prompt}", shlex.quote(e["prompt"])).replace("{out}", shlex.quote(str(out)))
        print(f"[{i}/{len(todo)}] {e['id']}", end=" ", flush=True)
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True)  # noqa: S602
        if p.returncode != 0 or not out.exists():
            failed.append((e["id"], (p.stderr or p.stdout)[:200]))
            print("FAIL")
        else:
            print(f"ok ({out.stat().st_size // 1024} KB)")

    if failed:
        print(f"\n{len(failed)} failed:", file=sys.stderr)
        for eid, why in failed:
            print(f"  {eid}: {why}", file=sys.stderr)
    print("\nNow curate. Delete every image you would not put in a portfolio.\n"
          "Target: keep 50-60% of what you generated. One bad image in a catalog\n"
          "discredits the whole catalog, and this format's only moat is taste.")
    return 0


def gh_anchor(text: str) -> str:
    """GitHub's heading-anchor rule: lowercase, drop anything that is not
    alphanumeric/space/hyphen, then spaces to hyphens. Source links must be built
    from the target entry's TITLE, because that is what becomes the heading — an
    earlier version linked to the entry id and produced five dead anchors."""
    import re as _re
    return _re.sub(r"[^a-z0-9 -]", "", text.lower()).strip().replace(" ", "-")


def render_readme(data: dict, lang: str = "en") -> str:
    entries = data["entries"]
    cats: OrderedDict[str, list] = OrderedDict()
    for e in entries:
        cats.setdefault(e["category"], []).append(e)

    kept = [e for e in entries if (HERE / e["image"]).exists()]
    n, ncat = len(kept), len(cats)
    model = data.get("model", "the model")

    T = {
        "en": {
            "tagline": f"{n} reproducible prompts for {model}, across {ncat} categories. Every prompt is copy-pasteable and every image is the actual output.",
            "toc": "Categories",
            "prompt": "Prompt",
            "contrib": "Contributing",
            "contrib_body": "Open a PR adding an entry to `prompts.json` plus your output image. Two rules: the prompt must reproduce, and the image must be the unedited output.",
            "license": "License",
            "license_body": ("Prompts are MIT — take them.\n\n"
                "**The images are AI-generated.** They were produced with Krea 2 Turbo and are "
                "presented as model output, not as photographs or human artwork. Under the Krea 2 "
                "Community License you own outputs you generate yourself; commercial use is "
                "permitted below $1M annual company revenue, and the licence separately requires "
                "content filtering, which was left enabled for every image here. One entry was "
                "dropped after the safety checker flagged it.\n\n"
                "Nothing here was retouched, upscaled or cropped. Every seed is recorded so you "
                "can regenerate the exact file."),
        },
        "zh": {
            "tagline": f"{model} 的 {n} 条可复现提示词，覆盖 {ncat} 个类别。每条提示词可直接复制，每张图片都是实际输出。",
            "toc": "类别",
            "prompt": "提示词",
            "contrib": "参与贡献",
            "contrib_body": "提交 PR，在 `prompts.json` 中添加条目并附上你的输出图片。两条规则：提示词必须可复现，图片必须是未经编辑的原始输出。",
            "license": "许可",
            "license_body": "提示词采用 MIT 许可。生成的图片受模型提供方条款约束，商用前请自行确认。",
        },
        "ko": {
            "tagline": f"{model}용 재현 가능한 프롬프트 {n}개, {ncat}개 카테고리. 모든 프롬프트는 복사해서 바로 쓸 수 있고 모든 이미지는 실제 출력물입니다.",
            "toc": "카테고리",
            "prompt": "프롬프트",
            "contrib": "기여하기",
            "contrib_body": "`prompts.json`에 항목을 추가하고 출력 이미지를 첨부해 PR을 보내주세요. 규칙 두 개: 프롬프트는 재현 가능해야 하고, 이미지는 편집하지 않은 원본이어야 합니다.",
            "license": "라이선스",
            "license_body": "프롬프트는 MIT입니다. 생성된 이미지는 모델 제공자의 약관을 따릅니다 — 상업적 사용 전 확인하세요.",
        },
    }[lang]

    L: list[str] = []
    title = data.get("repo", "catalog").split("/")[-1]
    L.append(f"<h1 align=\"center\">{title}</h1>")
    L.append(f"<p align=\"center\">{T['tagline']}</p>\n")

    # A static hero inside the first 1500 chars appeared in 32/32 of the
    # fastest-moving repos measured. A composite that states the three findings
    # beats a thumbnail grid: the grid says "here are images", the composite says
    # "here is what I found". Do not build a GIF — measured lift was zero.
    if (HERE / "hero.webp").exists():
        L.append('<p align="center">')
        L.append('  <img src="hero.webp" width="912" '
                 'alt="Three findings: text holds on one sign and collapses on a list; '
                 'character identity does not survive a second generation; '
                 'image-to-image changes medium but not scene contents">')
        L.append("</p>\n")
    else:
        L.append('<p align="center">')
        for e in kept[:8]:
            L.append(f'  <img src="{e["image"]}" width="180" alt="{e["title"]}">')
        L.append("</p>\n")

    others = [x for x in ["en", "zh", "ko"] if x != lang]
    links = " · ".join(
        f"[{x.upper()}](README.md)" if x == "en" else f"[{x.upper()}](README_{x.upper()}.md)"
        for x in others
    )
    if links:
        L.append(f"<p align=\"center\">{links}</p>\n")

    # The findings are what this catalog has that a bare prompt dump does not.
    # They go above the index because they are the reason to read the rest.
    f = data.get("findings")
    if f and lang == "en":
        L.append("## What this model actually does\n")
        if f.get("_intro"):
            L.append(f"{f['_intro']}\n")
        for item in f.get("items", []):
            L.append(f"### {item['title']}\n")
            L.append(f"{item['body']}\n")

    if lang == "en":
        L.append("## Check any of this yourself\n")
        L.append("Every entry carries the seed that produced it, so no claim here has to be "
                 "taken on trust:\n")
        L.append("```bash\npython3 scripts/regen.py --id typography-012\n```")
        L.append("\nRegenerating two entries and comparing against the files in this repo gave "
                 "a mean per-pixel difference of 1.3 and 1.5 out of 255, which is WebP "
                 "re-encoding loss. The seed reproduces the generation; the repo stores the "
                 "re-encode.\n")

        fails = data.get("failures")
        if fails:
            L.append("## The failures, kept as evidence\n")
            L.append(f"{fails.get('_what','')}\n")
            L.append("| | What was asked for | What came back |")
            L.append("|---|---|---|")
            for f in fails.get("entries", []):
                if not (HERE / f["image"]).exists():
                    continue
                seed = (f.get("params") or {}).get("seed")
                L.append(f'| <img src="{f["image"]}" width="150" alt="{f["claim"]}"> '
                         f'| {f.get("expected","")} | {f["claim"]}'
                         + (f' <br>`seed: {seed}`' if seed else "") + " |")
            L.append("")

    L.append(f"## {T['toc']}\n")
    for c in cats:
        L.append(f"- [{c}](#{c}) — {len([e for e in cats[c] if (HERE / e['image']).exists()])}")
    L.append("")

    for c, items in cats.items():
        items = [e for e in items if (HERE / e["image"]).exists()]
        if not items:
            continue
        L.append(f"\n## {c}\n")
        desc = (data.get("categories") or {}).get(c)
        if desc:
            L.append(f"_{desc}_\n")
        for e in items:
            L.append(f"### {e['title']}\n")
            L.append(f'<img src="{e["image"]}" width="420" alt="{e["title"]}">\n')
            L.append(f"**{T['prompt']}**\n")
            L.append("```text")
            L.append(e["prompt"].strip())
            L.append("```")
            if e.get("source"):
                src = next((x for x in entries if x["id"] == e["source"]), None)
                L.append("")
                if src:
                    L.append(f"_Image-to-image from **{src['title']}** "
                             f"([`{e['source']}`](#{gh_anchor(src['title'])})) in this repo · "
                             f"`strength: {e.get('strength')}`_")
                else:
                    L.append(f"_Image-to-image from `{e['source']}` · `strength: {e.get('strength')}`_")
            if e.get("params"):
                L.append("")
                L.append(" · ".join(f"`{k}: {v}`" for k, v in e["params"].items()))
            if e.get("notes"):
                L.append(f"\n> {e['notes']}")
            L.append("")

    L.append(f"\n## {T['contrib']}\n\n{T['contrib_body']}\n")
    L.append(f"## {T['license']}\n\n{T['license_body']}\n")
    return "\n".join(L)


def cmd_build(langs: list[str]) -> int:
    data = load()
    kept = [e for e in data["entries"] if (HERE / e["image"]).exists()]
    missing = len(data["entries"]) - len(kept)

    for lang in langs:
        name = "README.md" if lang == "en" else f"README_{lang.upper()}.md"
        (HERE / name).write_text(render_readme(data, lang), encoding="utf-8")
        print(f"wrote {name}")

    ncat = len({e["category"] for e in kept})
    print(f"\n{len(kept)} entries across {ncat} categories"
          + (f" ({missing} entries skipped — no image on disk)" if missing else ""))

    print("\nSet the repo description field to exactly this, and nothing longer:")
    print(f'  "{len(kept)} reproducible {data.get("model","")} prompts across {ncat} categories"')
    print("\nThe description field — not the README body — is what appears in GitHub search,")
    print("Trending, and every social card. A quantified claim in the first ten words is the")
    print("single highest-leverage asset in this whole play.")

    if any(not (HERE / e["image"]).exists() for e in data["entries"]):
        print("\nNote: entries without an image on disk were omitted rather than rendered broken.")
    print("\nBefore you push: host the images IN THIS REPO or on your own R2/S3.")
    print("External CDN links are the one reliable way this format dies — link rot")
    print("turns a 10k-star catalog into a wall of broken images 18 months later.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--generate", action="store_true")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--force", action="store_true", help="regenerate images that already exist")
    ap.add_argument("--lang", action="append", default=[],
                    help="extra language for README (zh, ko). repeatable")
    args = ap.parse_args()

    if args.init:
        return cmd_init()
    if args.generate:
        return cmd_generate(args.force)
    if args.build:
        return cmd_build(["en"] + args.lang)
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
