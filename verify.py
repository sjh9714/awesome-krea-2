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
