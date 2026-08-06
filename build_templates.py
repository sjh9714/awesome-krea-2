#!/usr/bin/env python3
"""
build_templates.py - the catalog as fill-in-the-blank recipes.

Why this exists. The reference catalog in this niche, jamez-bondos at 8,115
stars, does not publish finished sentences. It publishes prompts with bracketed
slots the reader swaps out: "a real [object] combined with hand-drawn doodles
that [interact with it]". You take the shape home, not the sentence. This repo
publishes 475 finished sentences, which you either run verbatim or discard.

What this deliberately does not do. Slotting all 475 would mean deciding, 475
times, which clause is the substitutable one, without ever having tested a
substitution. That is exactly the kind of claim this catalog has already had to
retract in public. So there are six templates, not four hundred, and each one
names the finding or the vocabulary entry that measured it.

Every `evidence` reference is resolved against the manifest, so a template
cannot outlive the result behind it.

    python3 build_templates.py

Writes TEMPLATES.md.
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def resolve(ref: str, d: dict, vocab: dict) -> tuple[bool, str]:
    """`finding:Title` or `vocabulary:term`, checked against the real thing."""
    kind, _, value = ref.partition(":")
    if kind == "finding":
        ok = any(f["title"] == value for f in d["findings"]["items"])
        return ok, f"[{value}](FINDINGS.md)"
    if kind == "styles":
        # The whole-frame conversion result lives in styles/data.json, not in the
        # findings list. Citing the nearest finding instead would have been a
        # wrong citation attached to a correct claim.
        sd = json.loads((HERE / "styles/data.json").read_text(encoding="utf-8"))
        ok = bool(sd.get("rule")) and value in sd
        return ok, "[the styles page](styles/README.md)"
    if kind == "vocabulary":
        ok = any(t["t"] == value for t in vocab["terms"])
        return ok, f"[`{value}`](VOCABULARY.md)"
    return False, ref


def main() -> int:
    d = json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))
    vocab = json.loads((HERE / "vocabulary.json").read_text(encoding="utf-8"))
    tpl = d["templates"]

    bad = [i["name"] for i in tpl["items"]
           if not resolve(i["evidence"], d, vocab)[0]]
    if bad:
        print("these templates cite evidence that does not exist:")
        for b in bad:
            print("  " + b)
        return 1

    L = ["# Templates", "", tpl["_intro"], "", f"*{tpl['_caution']}*", "",
         f"{len(tpl['items'])} of them. Every prompt in the catalog is a finished "
         f"sentence; these are the shapes underneath the ones that were tested.", ""]

    for i, item in enumerate(tpl["items"], 1):
        _, ev = resolve(item["evidence"], d, vocab)
        L += [f"## {i}. {item['name']}", "", "```text", item["template"], "```", ""]
        L += ["| slot | what goes in it |", "|---|---|"]
        for k, v in item["slots"].items():
            L.append(f"| `[{k}]` | {v} |")
        L += ["", item["why"], "",
              f"**Evidence** {ev} · **tested on** {item['tested']}"]
        if item.get("file"):
            L.append(f" · **ready-made** [`{item['file']}`]({item['file']})")
        L += ["", "---", ""]

    L += ["## What is not here", "",
          "A template for every entry. Deciding which clause of a prompt is the "
          "substitutable one is a claim about the model, and making that claim 475 "
          "times without testing it once is how this catalog got two findings wrong "
          "before. If you substitute into one of these and it breaks, that is worth "
          "an issue: it is a measurable thing and nobody has measured it yet.", ""]

    (HERE / "TEMPLATES.md").write_text("\n".join(L), encoding="utf-8")
    print(f"TEMPLATES.md  {len(tpl['items'])} templates, all evidence resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
