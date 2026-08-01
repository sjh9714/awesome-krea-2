#!/usr/bin/env python3
"""
measure_negatives.py — do "no X" clauses actually cost you anything here?

Written on 2026-08-02 after a commenter on r/StableDiffusion pointed out that a
prompt in a post of mine said "no colour anywhere", and that models do not read
negative language in a positive prompt as one instruction. That is widely
believed and I was ready to write it into the findings table as settled.

Then I counted. Across the 540 generations in this catalog, roughly half carry
some "no X" clause, and their failure rate is barely distinguishable from the
prompts without one. The reason 38 of the 65 failures contain a negative is that
most prompts contain a negative; the denominator was doing the work.

What is true is narrower: three failures are a negative being ignored outright
(mirror-004, sport-003, fashion-007). Three out of 65. Worth knowing, not worth
a rule.

This script exists so the number in the README is reproducible rather than
asserted, and so it can be re-run when the catalog grows.

    python3 scripts/measure_negatives.py
"""

from __future__ import annotations

import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent

# A negative clause, not merely the word "no" inside another word. Requires a
# following word so that "no." or a hyphenated compound does not count.
NEGATIVE = re.compile(r"\b(no|nothing|nobody|without|never)\b\s+\w", re.I)

# Failures whose recorded claim says the negative itself was ignored, rather
# than the framing, the exposure or the subject going wrong for other reasons.
IGNORED_NEGATIVE = re.compile(
    r"asked for (no|nobody|nothing)|no face in frame|nobody in the reflection|"
    r"hangers showing", re.I)


def main() -> int:
    d = json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))
    kept = d["entries"]
    failed = d.get("failures", {}).get("entries", [])

    def neg(rows):
        return [r for r in rows if NEGATIVE.search(r["prompt"])]

    k_neg, f_neg = neg(kept), neg(failed)
    K, F = len(kept), len(failed)
    total, total_neg = K + F, len(k_neg) + len(f_neg)

    with_neg_fail = len(f_neg) / total_neg * 100
    without_neg_fail = (F - len(f_neg)) / (total - total_neg) * 100

    print(f"catalog: {total} generations, {F} recorded failures "
          f"({F / total * 100:.1f}%)\n")
    print(f"  prompts with a negative clause     {total_neg:4d}  "
          f"failure rate {with_neg_fail:5.1f}%")
    print(f"  prompts without a negative clause  {total - total_neg:4d}  "
          f"failure rate {without_neg_fail:5.1f}%")

    a, b = len(f_neg), total_neg - len(f_neg)
    c, e = F - len(f_neg), (total - total_neg) - (F - len(f_neg))
    odds = (a / b) / (c / e)
    print(f"\n  odds ratio {odds:.2f}\n")

    outright = [r for r in failed if IGNORED_NEGATIVE.search(r.get("claim", ""))]
    print(f"failures where the negative itself was ignored: "
          f"{len(outright)} of {F}")
    for r in outright:
        print(f"  {r['id']:16s} {r.get('claim', '')[:96]}")

    # The README states these numbers. If the catalog grows and they drift, the
    # table is wrong and someone should notice here first.
    print(f"\nREADME states 12.4% vs 11.6% and 3 of 65. "
          f"Now: {with_neg_fail:.1f}% vs {without_neg_fail:.1f}% "
          f"and {len(outright)} of {F}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
