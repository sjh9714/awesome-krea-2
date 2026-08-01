#!/usr/bin/env python3
"""
build_styles.py — generate styles/README.md and the wildcards files from data.

Rewritten on 2026-08-01, the night the Reddit post went out, because the section
it generated no longer matched what the post promised. A reader clicking through
from "8 copy-paste clauses, same seed" landed on a different subject, a
different clause list and a superseded conclusion. The page is now a mirror of
the post: the rule, the eight whole-scene clauses with their images, the three
styles that never converted, and the earlier lantern-subject sweep kept below as
an appendix because its data (including the FLUX.1 dev cross-check) is still
real.

Generated, not hand-written: a page that prints prompt text has to print the
text that was actually sent. These clauses lived only in shell history once and
had to be recovered from a session transcript.

    python3 build_styles.py
"""

from __future__ import annotations

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "styles/data.json"
SWEEP = HERE / "styles/sweep.json"

GOODS_ORDER = ["manga", "storybook", "comicink", "chibi",
               "poster", "retroanime", "popart", "sixties"]


def main() -> int:
    d = json.loads(DATA.read_text(encoding="utf-8"))
    sweep = json.loads(SWEEP.read_text(encoding="utf-8"))

    missing = [k for k in GOODS_ORDER if k not in d["goods"]] + \
              [k for k in d["goods"] if k not in GOODS_ORDER]
    if missing:
        print(f"GOODS_ORDER and data.json disagree: {missing}")
        return 1

    L = [
        "# Styles — how to ask this model for one",
        "",
        "[← back to the catalog](../README.md)",
        "",
        f"This page mirrors [the Reddit post]({d['post']}) so that what it "
        "promised is one click away: the clauses, the failures, the seeds, the "
        "wildcards file.",
        "",
        "## The rule",
        "",
        f"**{d['rule']}**",
        "",
        "Asked for *children's picture book drawing* as a style, the model drew "
        "a children's picture book and put it on the table. Same length, phrased "
        "as an instruction, and the whole frame converts:",
        "",
        f'<img src="{d["hook"]["named_image"]}" width="330" alt="named: a picture book appears on the table">',
        f'<img src="{d["hook"]["rephrased_image"]}" width="330" alt="rephrased: the whole frame converts">',
        "",
        f"- named — `{d['hook']['named_clause']}`",
        f"- rephrased — `{d['hook']['rephrased_clause']}`",
        "",
        "## Eight clauses that convert the whole frame",
        "",
        f"One subject, seed `{d['seed']}`, the clause is the only variable. "
        "Each is ~100 characters; they are plain English and carry nothing "
        "model-specific.",
        "",
    ]
    for k in GOODS_ORDER:
        g = d["goods"][k]
        L += [f'<img src="{g["image"]}" width="330" alt="{g["label"]}">', "",
              f"**{g['label']}** — `{g['clause']}`", ""]
    L += [
        "All eight, one per line, for a ComfyUI wildcard or dynamic-prompt node: "
        "[`wildcards/styles.txt`](../wildcards/styles.txt)",
        "",
        "The subject prompt behind every image:",
        "",
        "```",
        d["subject"],
        "```",
        "",
        "## The ones that never converted",
        "",
        "Three styles arrived as *things* no matter how they were phrased. If "
        "the style name is also an object, expect the object.",
        "",
        f'<img src="{d["never"]["rubberhose"]["image"]}" width="330" alt="a rubber-hose character seated next to her">',
        f'<img src="{d["never"]["doodle"]["image"]}" width="330" alt="a doodled second her beside the photo">',
        "",
        f"- **rubber hose** — {d['never']['rubberhose']['why']}",
        f"- **doodle** — {d['never']['doodle']['why']}",
        f"- **mosaic** — {d['never']['mosaic']['why']}:",
        "",
    ]
    for img in d["never"]["mosaic"]["images"]:
        L.append(f'<img src="{img}" width="220" alt="mosaic attempt">')
    L += [
        "",
        "Caveats: one seed, one subject, so one sample per cell; everything "
        "judged at full size. Correction from the thread: manga and pop art "
        "only half-convert \u2014 the figure turns, the street stays a photo, and "
        "three stronger phrasings at the same seed did not fix it, so it is 6 "
        "of 8.",
        "",
        "## Appendix — the earlier sweep",
        "",
        "An earlier version of this page varied the style clause over a "
        "different subject (two women in a lantern river). Its data is still "
        f"real and lives in [`sweep.json`](sweep.json): {len(sweep['kept'])} "
        f"clauses reproduced, {len(sweep['failed'])} failed on that subject, "
        f"{len(sweep['failed_earlier_subject'])} printing-process styles failed "
        "on a subject before that, and the same refusals reproduced on FLUX.1 "
        "dev at the same seed — so none of this is one endpoint being odd. "
        "Those older clauses are kept in "
        "[`wildcards/styles-extra.txt`](../wildcards/styles-extra.txt). The "
        "long-descriptor comparison started from "
        f"[this wildcards thread]({d['their_thread']}), whose 660-character "
        "clauses are worth having regardless.",
        "",
    ]
    (HERE / "styles/README.md").write_text("\n".join(L), encoding="utf-8")

    wc = HERE / "wildcards"
    wc.mkdir(exist_ok=True)
    (wc / "styles.txt").write_text(
        "\n".join(d["goods"][k]["clause"] for k in GOODS_ORDER) + "\n",
        encoding="utf-8")
    (wc / "styles-extra.txt").write_text(
        "\n".join(v["clause"] for v in sweep["kept"].values()) + "\n",
        encoding="utf-8")

    print(f"styles/README.md      {len(chr(10).join(L)):,} chars")
    print(f"wildcards/styles.txt  {len(GOODS_ORDER)} clauses (the post's eight)")
    print(f"wildcards/styles-extra.txt  {len(sweep['kept'])} clauses (earlier sweep)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
