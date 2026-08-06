#!/usr/bin/env python3
"""
verify.py — check the catalog against itself.

This exists because of one bug. The hands category was withdrawn, the subtitle
and the findings were corrected to 476 kept and 64 cut, and the paragraph that
introduces the findings kept saying 483 and 78. Two paragraphs of the same page
disagreed about the count for five hours, in a document whose entire argument is
that the counts were checked, while a public post pointed at it.

Nothing caught that, because nothing was looking. A repository that asks readers
to verify its claims should be able to verify its own, so this runs the checks
that would have caught it:

  - every entry and every failure carries a seed
  - every image the manifest names exists, and every image on disk is named
  - every image the READMEs and the gallery reference exists
  - every `seed: N` printed in the README is a seed that is actually in the data
  - the counts add up, and no document contradicts the manifest

    python3 verify.py            # exits non-zero if anything fails

Run it before pushing. It is fast and it has no dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


class Check:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passed = 0

    def __call__(self, ok: bool, label: str, detail: str = "") -> None:
        if ok:
            self.passed += 1
            print(f"  ok    {label}")
        else:
            self.failures.append(f"{label}{' — ' + detail if detail else ''}")
            print(f"  FAIL  {label}{' — ' + detail if detail else ''}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", default="prompts.json")
    args = ap.parse_args()

    d = json.loads((HERE / args.manifest).read_text(encoding="utf-8"))
    entries = d["entries"]
    failures = d.get("failures", {}).get("entries", [])
    both = entries + failures
    c = Check()

    print("seeds")
    seed = lambda e: (e.get("params") or {}).get("seed")
    missing = [e["id"] for e in both if seed(e) is None]
    c(not missing, f"all {len(both)} generations carry a seed", f"missing on {missing[:5]}")

    print("\nimages")
    named = {e["image"] for e in both}
    absent = sorted(p for p in named if not (HERE / p).exists())
    c(not absent, f"all {len(named)} manifest images exist", f"{absent[:5]}")

    on_disk = {str(p.relative_to(HERE)) for p in HERE.glob("images/**/*.webp")}
    orphans = sorted(on_disk - named - {"hero.webp"})
    c(not orphans, f"no orphan images among {len(on_disk)} on disk", f"{orphans[:5]}")

    print("\ndocuments")
    docs = ["README.md", "README_ZH.md", "README_KO.md", "index.html"]
    for name in docs:
        p = HERE / name
        if not p.exists():
            c(False, f"{name} exists")
            continue
        t = p.read_text(encoding="utf-8")
        refs = set(re.findall(r'(?:src="|\]\()((?:images|wildcards)/[^")\s]+)', t))
        broken = sorted(r for r in refs if not (HERE / r).exists())
        c(not broken, f"{name}: {len(refs)} image references resolve", f"{broken[:4]}")

    print("\nseeds quoted in prose")
    # A finding that cites `seed: N` is making a checkable claim. If N is not in
    # the data the claim is not checkable, which is the same as not being true.
    known = {seed(e) for e in both}
    readme = (HERE / "README.md").read_text(encoding="utf-8")
    quoted = {int(s) for s in re.findall(r"seed:\s*(\d+)", readme)}
    unknown = sorted(quoted - known)
    c(not unknown, f"all {len(quoted)} seeds quoted in README are in the manifest",
      f"not found: {unknown[:5]}")

    print("\ncounts")
    gens = d.get("generations")
    c(isinstance(gens, int) and gens >= len(both),
      f"generations ({gens}) >= kept + documented failures ({len(both)})",
      "a total lower than what is on disk cannot be right")

    declared = set(d.get("categories") or {})
    used = {e["category"] for e in entries}
    c(not (used - declared), "every category in use is declared",
      f"undeclared: {sorted(used - declared)}")
    # A declared category with no entries is allowed, but only if it says why —
    # that is how the withdrawn hands category is represented.
    silent = [k for k in declared - used if len(str((d["categories"] or {}).get(k, ""))) < 20]
    c(not silent, "declared-but-empty categories explain themselves", f"{silent}")

    # The intro is generated from these numbers now, so the literals that were
    # wrong must not come back.
    for stale in ("483 are here", "78 were cut"):
        c(stale not in readme, f"README no longer says {stale!r}")

    # GitHub does not process Markdown inside an HTML block, so a link written as
    # [ZH](README_ZH.md) inside <p align="center"> renders as literal brackets.
    # All three language switchers shipped that way and nobody could reach the
    # translations at all — which made the work of putting findings into them
    # pointless. Nothing else here would have caught it; it only shows on render.
    for name in ("README.md", "README_ZH.md", "README_KO.md"):
        path = HERE / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        raw = re.findall(r'<(p|div|h\d)[^>]*>[^<]*\[[^\]]+\]\([^)]+\)', text)
        c(not raw, f"{name}: no Markdown links inside HTML blocks",
          f"{len(raw)} would render as literal brackets, e.g. {raw[:1]}")
        # And the switcher has to actually point at the other two.
        others = {"README.md": ("README_ZH.md", "README_KO.md"),
                  "README_ZH.md": ("README.md", "README_KO.md"),
                  "README_KO.md": ("README.md", "README_ZH.md")}[name]
        for target in others:
            c(f'href="{target}"' in text, f"{name} links to {target}")

    # The hero has gone stale twice by carrying findings that later moved: it led
    # with "one sign holds, a list collapses" after the stringcount ladder
    # disproved it, and then with hands and interlocking after the hands category
    # was withdrawn and the interlocking rule was thrown away. Its own docstring
    # said to regenerate it whenever a finding changed, and nobody did. It now
    # shows output with seeds instead, and every frame it names must still be a
    # kept entry with a seed — so it cannot quietly start citing a withdrawn one.
    hero_src = (HERE / "build_hero.py")
    if hero_src.exists():
        # Scope to the PICKS literal. Matching ids across the whole file also
        # caught the string "utf-8", which looks exactly like an entry id.
        block = re.search(r'^PICKS = \[(.*?)^\]', hero_src.read_text(encoding="utf-8"),
                          re.S | re.M)
        picks = re.findall(r'"([a-z0-9-]+-\d+)"', block.group(1)) if block else []
        c(bool(picks), "build_hero.py declares a PICKS list")
        by_id = {e["id"]: e for e in entries}
        gone = [p for p in picks if p not in by_id]
        c(not gone, "every hero frame is still a kept entry",
          f"withdrawn or missing: {gone}")
        unseeded = [p for p in picks if p in by_id
                    and by_id[p].get("params", {}).get("seed") is None]
        c(not unseeded, "every hero frame has a seed to print", f"{unseeded}")

    # A reader who lands here wants to see output. The findings prose used to sit
    # between the hero image and the catalog as 48,527 unbroken characters — about
    # 24 screens with no image in them, against 6,172-11,318 for the three repos
    # in the comparison table below. It now lives in FINDINGS.md behind a summary
    # table. If it creeps back, this fails.
    findings = HERE / "FINDINGS.md"
    c(findings.exists(), "FINDINGS.md exists", "the long-form evidence has to live somewhere")
    for name, anchor in (("README.md", "## Categories"),
                         ("README_ZH.md", "## 类别"),
                         ("README_KO.md", "## 카테고리")):
        path = HERE / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if anchor not in text or "hero.webp" not in text:
            c(False, f"{name} has a hero image and a catalog heading")
            continue
        gap = text.index(anchor) - text.index("</p>", text.index("hero.webp"))
        c(gap < 8000, f"{name}: hero to catalog is scannable",
          f"{gap:,} characters of prose before the first catalog entry — "
          f"move the long form into FINDINGS.md")
        c("FINDINGS.md" in text, f"{name} links to FINDINGS.md")

    # README_ZH and README_KO shipped for a week as a translated intro followed
    # by the raw English catalog — every findings section was missing, so anyone
    # arriving from a Chinese or Korean link found a prompt list and none of the
    # reasoning that makes it worth reading. The badge row advertises both.
    for name in ("README_ZH.md", "README_KO.md"):
        path = HERE / name
        if not path.exists():
            c(False, f"{name} exists")
            continue
        text = path.read_text(encoding="utf-8")
        anchor = next((a for a in ("## 类别", "## 카테고리") if a in text), None)
        c(anchor is not None, f"{name} has a catalog heading")
        if anchor:
            intro = text[:text.index(anchor)]
            # The English intro runs ~49,000 characters. A translation that has
            # only the header block is under ~1,500; a condensed findings
            # section lands around 4,000.
            c(len(intro) > 2500,
              f"{name} carries the findings, not just a header",
              f"only {len(intro):,} characters before {anchor!r} — "
              f"the findings sections are missing")

    # The comparison table describes this repo to a reader who is deciding
    # between it and a 13,000-star competitor, and it is written by hand. It sat
    # at "85 prompts / 93 images / 8 failures / $1.26 / 150 gens" — the first
    # batch — for five batches, understating the catalog roughly five-fold in the
    # one place built to argue it is worth using. Nothing above catches that,
    # because every other check reads the generated prose.
    row = re.search(r"^\|\s*\*\*this repo\*\*\s*\|(.+)$", readme, re.M)
    if row is None:
        c(False, "comparison table has a 'this repo' row")
    else:
        cells = [x.strip() for x in row.group(1).split("|") if x.strip()]
        images_on_disk = len(list((HERE / "images").rglob("*.webp")))
        # Checked per cell, not against the row as a whole: the first version of
        # this check searched the whole row, so replacing the prompt count with a
        # stale 85 still passed because "all 475" two cells over kept 475 present.
        # A tamper test caught it. Column order matches the header above.
        want = [
            ("Prompts", len(entries)),
            ("Images in repo", images_on_disk),
            ("Seeds / params", len(entries)),
            ("Failures shown", len(failures)),
            ("Measured cost", gens),
        ]
        bad = []
        for i, (col, expect) in enumerate(want):
            got = [int(n.replace(",", "")) for n in re.findall(r"\d[\d,]*", cells[i])] \
                if i < len(cells) else []
            if expect not in got:
                bad.append(f"{col}: expected {expect}, cell reads {cells[i]!r}"
                           if i < len(cells) else f"{col}: cell missing")
        c(not bad, "comparison table row matches the manifest, cell by cell",
          "; ".join(bad))
        spend = d.get("spend")
        c(spend is None or f"{spend}" in cells[-1],
          f"comparison table quotes the real spend (${spend})",
          f"cost cell reads {cells[-1]!r}" if cells else "")

    # The styles page is generated from styles/data.json and mirrors the Reddit
    # post of 2026-08-01. Its whole promise is that a reader arriving from the
    # post finds the exact clauses the post printed. A previous version of this
    # page drifted to a different subject and a superseded conclusion, which is
    # why this block exists: the page and the wildcards file must both match the
    # canonical data, and the older sweep must stay published as the appendix.
    # The negatives row quotes three numbers straight out of the manifest. The
    # row exists because the folklore ("models ignore negative prompts") was
    # about to go into the table as settled, and counting showed the effect is
    # nearly nothing. If the catalog grows and the numbers drift, the row is
    # wrong and this should fail before anyone reads it.
    # The gallery is 475 images on one page. Without an id per category and a
    # list to jump from, the only way to reach anything is to scroll, and a link
    # to one category cannot be handed to anyone who asks about it. Someone did
    # ask, in the thread, and the answer was a README anchor into a 6,000-line
    # page that lands mid-image while the lazy figures above it resolve.
    print("\ngallery anchors")
    page = HERE / "index.html"
    if not page.exists():
        c(False, "index.html exists")
    else:
        h = page.read_text(encoding="utf-8")
        cats = sorted({e["category"] for e in entries})
        missing = [x for x in cats if f'id="{x}"' not in h]
        c(not missing, f"every one of the {len(cats)} categories has an anchor",
          f"{missing[:5]}")
        untargeted = [x for x in cats if f'href="#{x}"' not in h]
        c(not untargeted, "every category is reachable from the jump list",
          f"{untargeted[:5]}")
        c('id="top"' in h and 'href="#top"' in h,
          "the page has a top anchor and links back to it")
        c('id="failures"' in h, "the failures section has an anchor")
        c("scroll-margin-top" in h,
          "headings carry a scroll margin",
          "without it an anchor lands under the viewport edge")

    print("\nnegatives row")
    NEG = re.compile(r"\b(no|nothing|nobody|without|never)\b\s+\w", re.I)
    IGN = re.compile(r"asked for (no|nobody|nothing)|no face in frame|"
                     r"nobody in the reflection|hangers showing", re.I)
    with_neg = [r for r in both if NEG.search(r["prompt"])]
    fail_neg = [r for r in failures if NEG.search(r["prompt"])]
    rate_with = len(fail_neg) / len(with_neg) * 100
    rate_without = ((len(failures) - len(fail_neg))
                    / (len(both) - len(with_neg)) * 100)
    outright = [r for r in failures if IGN.search(r.get("claim", ""))]

    row = re.search(r"^\|\s*\*\*Negatives\*\*\s*\|(.+)$", readme, re.M)  # both cells
    c(row is not None, "README has a Negatives row")
    if row:
        cell = row.group(1)
        for want, label in ((f"{rate_with:.1f}%", "the with-negative failure rate"),
                            (f"{rate_without:.1f}%", "the without-negative rate"),
                            (f"{len(outright)} of {len(failures)}",
                             "the count of outright ignored negatives")):
            c(want in cell, f"Negatives row quotes {label} ({want})",
              f"row reads {cell.strip()[:120]}")
    c((HERE / "scripts/measure_negatives.py").exists(),
      "the script that produces those numbers is published")

    print("\nstyles page")
    dpath = HERE / "styles/data.json"
    if not dpath.exists():
        c(False, "styles/data.json exists")
    else:
        sd = json.loads(dpath.read_text(encoding="utf-8"))
        page = HERE / "styles/README.md"
        c(page.exists(), "styles/README.md is built")
        text = page.read_text(encoding="utf-8") if page.exists() else ""

        imgs = [sd["hook"]["named_image"], sd["hook"]["rephrased_image"]]
        imgs += [g["image"] for g in sd["goods"].values()]
        imgs += [sd["never"]["rubberhose"]["image"], sd["never"]["doodle"]["image"]]
        imgs += sd["never"]["mosaic"]["images"]
        gone = sorted(i for i in imgs if not (HERE / "styles" / i).exists())
        c(not gone, f"all {len(imgs)} post images exist", f"{gone[:4]}")

        c(isinstance(sd.get("seed"), int) and len(sd.get("subject", "")) > 100,
          "the page records the pinned seed and the subject prompt")

        missing = [k for k, g in sd["goods"].items() if g["clause"] not in text]
        c(not missing, f"styles/README.md prints all {len(sd['goods'])} clauses verbatim",
          f"{missing[:4]}")
        c(sd["hook"]["named_clause"] in text and sd["hook"]["rephrased_clause"] in text,
          "the picture-book pair prints both phrasings verbatim")

        wc = HERE / "wildcards/styles.txt"
        if not wc.exists():
            c(False, "wildcards/styles.txt exists")
        else:
            lines = [l for l in wc.read_text(encoding="utf-8").splitlines() if l.strip()]
            want = [g["clause"] for g in sd["goods"].values()]
            c(len(lines) == len(want),
              f"wildcards/styles.txt is exactly the post's {len(want)} clauses",
              f"file has {len(lines)}")
            c(sorted(lines) == sorted(want),
              "every wildcard line is a clause the post printed")

        # The refusals are the finding; losing them turns this back into a
        # pretty gallery. And a refusal must never migrate into the goods.
        c(len(sd.get("refusals", [])) >= 3, "the page still publishes its refusals")
        c(not set(sd.get("refusals", [])) & set(sd["goods"]),
          "no refusal is listed among the goods")

        # The appendix keeps the earlier sweep honest instead of deleting it.
        sw = HERE / "styles/sweep.json"
        c(sw.exists(), "the earlier sweep is still published (styles/sweep.json)")
        c("sweep.json" in text and "styles-extra.txt" in text,
          "styles/README.md links the appendix data and the extra wildcards")
        extra = HERE / "wildcards/styles-extra.txt"
        if sw.exists() and extra.exists():
            old = json.loads(sw.read_text(encoding="utf-8"))
            lines = [l for l in extra.read_text(encoding="utf-8").splitlines() if l.strip()]
            kept = [v["clause"] for v in old["kept"].values()]
            c(sorted(lines) == sorted(kept),
              f"styles-extra.txt is exactly the earlier sweep's {len(kept)} clauses")
        else:
            c(extra.exists(), "wildcards/styles-extra.txt exists")

        c(sd.get("post", "").startswith("https://www.reddit.com/"),
          "the page records which post it mirrors")
        c("README.md" in text or "../README.md" in text, "styles/README.md links back")
        c("styles/README.md" in readme, "README.md links to the styles page")
        c("wildcards/styles.txt" in readme, "README.md links to the wildcards file")

    # The vocabulary is the one place in this repo that points at specific words and
    # says they matter. That is exactly the kind of claim this catalog has had to
    # retract before, so the rule behind it (3+ entries, 2+ categories) is enforced
    # here as well as in the builder, and every warning has to still name a real
    # finding. If a term drifts below the rule the index quietly becomes an opinion.
    voc = HERE / "vocabulary.json"
    c(voc.exists(), "vocabulary.json exists")
    if voc.exists():
        import build_vocabulary as bv
        v, dd = bv.load()
        by = bv.usage(v, dd)
        thin = [t for t, r in by.items()
                if len(r["entries"]) < bv.MIN_ENTRIES
                or len(r["categories"]) < bv.MIN_CATEGORIES]
        c(not thin, f"all {len(by)} vocabulary terms meet the 3-entry 2-category rule"
                    + (f", but {thin} do not" if thin else ""))
        titles = {f["title"] for f in dd["findings"]["items"]}
        bad = [t for t, r in by.items() if r.get("finding") and r["finding"] not in titles]
        c(not bad, "every vocabulary warning names a finding that exists"
                   + (f", but {bad} do not" if bad else ""))
        vm = HERE / "VOCABULARY.md"
        c(vm.exists(), "VOCABULARY.md is built")
        if vm.exists():
            vtext = vm.read_text(encoding="utf-8")
            c(f"{len(by)} terms." in vtext,
              f"VOCABULARY.md is current at {len(by)} terms")
            warned = [t for t, r in by.items() if r.get("finding")]
            c(f"Read these {len(warned)} before you use them" in vtext,
              f"VOCABULARY.md counts its {len(warned)} warnings correctly")
            # Assert the disclaimer is present rather than that the word "caused"
            # is absent; the disclaimer itself contains it, and the first version
            # of this check failed on the sentence it was written to protect.
            c("Nothing here is a claim that a term caused a particular image" in vtext,
              "VOCABULARY.md still disclaims the causal reading")
            c("at least 3 entries across at least 2 categories" in vtext,
              "VOCABULARY.md states the rule its terms had to meet")
        idx = HERE / "index.html"
        if idx.exists():
            n = idx.read_text(encoding="utf-8").count("<mark>")
            c(n > 300, f"the gallery marks the vocabulary ({n} marks)")

    # The download block is the first thing a reader from that subreddit sees, and
    # the format it advertises is the one that outscored everything else there. A
    # dead link or a wrong file size in it costs more than a wrong sentence lower
    # down, so the sizes are checked against the files rather than trusted.
    RAW = "https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/"
    zip_path = HERE / "wildcards/krea2-wildcards.zip"
    c(zip_path.exists(), "wildcards/krea2-wildcards.zip is built")
    for f in ("all.txt", "krea2-wildcards.zip", "styles.txt"):
        c(RAW + f in readme, f"README.md links the raw {f}")
        c((HERE / "wildcards" / f).exists(), f"wildcards/{f} exists to be linked")
    for f, claimed in re.findall(
            r"\[([a-z0-9._-]+)\]\(" + re.escape(RAW) + r"[a-z0-9._-]+\)[^|]*\|[^|]*?(\d+) KB",
            readme):
        actual = round((HERE / "wildcards" / f).stat().st_size / 1024)
        c(abs(actual - int(claimed)) <= 2,
          f"README.md says {f} is {claimed} KB and it is {actual} KB")
    if zip_path.exists():
        import zipfile as _z
        names = set(_z.ZipFile(zip_path).namelist())
        c("all.txt" in names and "styles.txt" in names,
          f"the zip carries all.txt and styles.txt ({len(names)} files)")
        # build_wildcards.py used to unlink every *.txt in the folder, which
        # deleted build_styles.py's output whenever it ran second.
        c((HERE / "wildcards/styles.txt").exists()
          and (HERE / "wildcards/styles-extra.txt").exists(),
          "build_wildcards.py left the styles files alone")

    # REPRODUCING.md exists because the headline claim ("every entry carries its
    # seed") reads as a promise of reproducibility that the hosted endpoint cannot
    # keep. The endpoint publishes no step count, CFG, sampler or scheduler, so the
    # seed is good on fal and worthless in a local graph. If that caveat ever falls
    # out of the README, the repo goes back to overselling the one column it wins.
    rep = HERE / "REPRODUCING.md"
    c(rep.exists(), "REPRODUCING.md exists")
    if rep.exists():
        rtext = rep.read_text(encoding="utf-8")
        c("REPRODUCING.md" in readme, "README.md links to REPRODUCING.md")
        c("reproduce" in readme and "local" in readme,
          "README.md states the seeds do not reproduce locally")
        for term in ("fal-ai/krea-2/turbo", "square_hd", "enable_prompt_expansion",
                     "openapi.json"):
            c(term in rtext, f"REPRODUCING.md names {term}")
        for absent in ("guidance scale", "sampler", "scheduler"):
            c(absent in rtext,
              f"REPRODUCING.md says the endpoint has no {absent}")
        # The payload documented there has to be the payload the generator sends.
        gen = (HERE / "scripts/gen_fal.py").read_text(encoding="utf-8")
        c('"image_size": args.image_size, "enable_safety_checker": True' in gen
          or "'image_size': args.image_size" in gen,
          "gen_fal.py still sends the payload REPRODUCING.md documents")
        d = json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))
        edits = [e for e in d["entries"] if e["category"] == "editing"]
        c(all("strength" in e and "source" in e for e in edits),
          f"all {len(edits)} editing entries carry source and strength")
        c(all("seed" in e.get("params", {}) for e in d["entries"]),
          "every entry carries a seed")

    print()
    if c.failures:
        print(f"{len(c.failures)} failed, {c.passed} passed")
        for f in c.failures:
            print(f"  - {f}")
        return 1
    print(f"all {c.passed} checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
