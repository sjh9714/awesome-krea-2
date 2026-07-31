#!/usr/bin/env python3
"""
build_styles.py — generate styles/README.md and wildcards/styles.txt from sweep.json.

The rest of this catalog varies the subject and holds the style. This section
does the opposite: one subject, one seed, and the style clause is the only thing
that moves. That isolates a question the catalog could not otherwise answer —
which style requests this model will actually honour.

Twenty clauses were run. Fifteen came back as the style named. Five did not, and
they did not fail at random: every one of them is a style defined by what it
*removes* — colour, tone, detail, surface. Seven more, run earlier on a different
subject, were printing processes, and those failed the same way. That is the
finding, and it is the reason the failures are published next to the successes
instead of being quietly dropped.

Generated, not hand-written, because a page that prints prompt text has to print
the text that was actually sent. These clauses lived only in shell history once
and had to be recovered from a session transcript.

    python3 build_styles.py
"""

from __future__ import annotations

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SWEEP = HERE / "styles/sweep.json"

# Display order for the gallery table: alternate painterly / graphic /
# photographic so the differences are next to each other, not grouped.
ORDER = ["oil", "celanime", "ukiyoe", "watercolour", "cyberpunk", "ghibli",
         "pixelart", "kodachrome", "cg3d", "comicink", "lithograph",
         "conceptart", "retroanime", "gouache", "pastel"]


def main() -> int:
    d = json.loads(SWEEP.read_text(encoding="utf-8"))
    kept, failed = d["kept"], d["failed"]
    earlier = d["failed_earlier_subject"]

    missing = [k for k in kept if k not in ORDER] + [k for k in ORDER if k not in kept]
    if missing:
        print(f"ORDER and sweep.json disagree: {missing}")
        return 1

    L = [
        "# Styles — one subject, one seed, one variable",
        "",
        "[← back to the catalog](../README.md)",
        "",
        "Everywhere else in this repo the style is held and the subject varies. "
        "Here it is the other way round. The subject prompt and the seed are "
        f"identical in every image below; the only text that changes is the "
        "style clause.",
        "",
        f"**Model** `{d['model']}` · **Seed** `{d['seed']}` · "
        f"**{len(kept)} of {len(kept) + len(failed)} clauses reproduced**",
        "",
        "## The subject prompt",
        "",
        "```",
        d["subject"],
        "```",
        "",
        "## What the model honoured",
        "",
        "Each clause below was appended to the subject prompt above, unchanged.",
        "",
    ]
    for slug in ORDER:
        v = kept[slug]
        L += [f'<img src="{v["image"]}" width="320" alt="{slug}">', "",
              f"**`{slug}`** — {v['clause']}", ""]

    L += [
        "## What it refused, and why that is the useful part",
        "",
        "Five clauses came back with their defining constraint ignored. They are "
        "not a random five.",
        "",
        "| clause | what came back |",
        "|---|---|",
    ]
    for slug, v in sorted(failed.items()):
        L.append(f"| `{slug}` | {v['why']} |")

    L += [
        "",
    ]
    for slug, v in sorted(failed.items()):
        L += [f'<img src="{v["image"]}" width="240" alt="{slug}">']
    L += [
        "",
        "Every one of those is defined by what it *takes away* — colour, tone, "
        "detail, surface. On a subject this saturated and this busy, the model "
        "would not take it away.",
        "",
        "Seven more clauses, run earlier against a different subject, name a "
        "printing process rather than a way of painting. They failed the same "
        "way — the process arrived as decoration around a photograph.",
        "",
        "| clause | what came back |",
        "|---|---|",
    ]
    for slug, v in sorted(earlier.items()):
        L.append(f"| `{slug}` | {v['why']} |")

    L += [
        "",
        "### The rule this gives you",
        "",
        "Name a **painting** or an **animation** and you get the whole frame. "
        "Name a **process** — a press, a plate, a single ink, a monochrome stock "
        "— and you get your subject wearing a costume. If you want the reductive "
        "style, reduce the subject first: take the colour out of the prompt "
        "before you ask for charcoal.",
        "",
        "## Using these",
        "",
        "All clauses, one per line, ready for a ComfyUI dynamic-prompt or "
        "wildcard node:",
        "",
        "```",
        "wildcards/styles.txt",
        "```",
        "",
        "They are plain English and carry nothing model-specific, so they are "
        "worth trying against whatever you already run locally. Whether the "
        "refusals above reproduce on an open-weights model is not something this "
        "repo has measured yet, and it is the obvious next experiment.",
        "",
    ]
    (HERE / "styles/README.md").write_text("\n".join(L), encoding="utf-8")

    (HERE / "wildcards").mkdir(exist_ok=True)
    (HERE / "wildcards/styles.txt").write_text(
        "\n".join(kept[s]["clause"] for s in ORDER) + "\n", encoding="utf-8")

    print(f"styles/README.md      {len(chr(10).join(L)):,} chars, {len(kept)} kept, "
          f"{len(failed) + len(earlier)} documented failures")
    print(f"wildcards/styles.txt  {len(kept)} clauses, one per line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
