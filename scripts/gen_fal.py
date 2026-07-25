#!/usr/bin/env python3
"""
gen_fal.py — batch-generate catalog images through fal.ai's queue API.

Defaults to Krea 2 Turbo, which is the only place the actual open-weights Turbo
is hosted. Verified 2026-07-25: fal-ai/krea-2/turbo resolves an OpenAPI schema,
`prompt` is the only required field, and the posted rate is $0.008 per megapixel
— about $0.0084 per 1024x1024 image, so a 500-image catalog costs roughly $4.

Do not substitute Replicate or the Krea API without knowing what you are buying:
those serve krea-2-**medium-turbo**, a different model, at ~2x the price.
`krea/krea-2-turbo` on Replicate is a 404.

Local execution was evaluated and rejected on this machine: the ComfyUI stack
needs ~18.6 GB of working set (13.14 GB fp8 transformer + 5.24 GB text encoder +
VAE) against 16 GB of unified memory, and no one has published a working Krea 2
inference run on Apple Silicon at all.

    export FAL_KEY=...
    python3 gen_fal.py --manifest prompts.json
    python3 gen_fal.py --manifest prompts.json --only photography --force
    python3 gen_fal.py --prompt "a single prompt" --out /tmp/one.png

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

QUEUE = "https://queue.fal.run"
DEFAULT_MODEL = "fal-ai/krea-2/turbo"


def load_dotenv() -> None:
    """Read KEY=value from the nearest .env, walking up from this script.

    A .env file is the right place for this: the key never enters your shell
    history, never reaches a chat transcript, and .gitignore already excludes it.
    Values already in the environment win, so CI and one-off overrides still work.
    """
    here = Path(__file__).resolve()
    for d in [Path.cwd(), *here.parents[:4]]:
        f = d / ".env"
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip("'\""))
        return


def key() -> str:
    load_dotenv()
    k = os.environ.get("FAL_KEY") or os.environ.get("FAL_API_KEY")
    if not k:
        print(
            "FAL_KEY is not set.\n\n"
            "  1. Sign up at https://fal.ai (email + card)\n"
            "  2. Dashboard -> Keys -> create a key\n"
            "  3. Write it to a .env file — do NOT paste it into a chat:\n\n"
            "       cd ~/orca/projects/np\n"
            "       printf 'FAL_KEY=%s\\n' 'PASTE_KEY_HERE' > .env\n"
            "       chmod 600 .env\n\n"
            "  .env is already gitignored. Any parent directory up to four levels\n"
            "  above this script works, so np/.env covers the whole toolkit.",
            file=sys.stderr)
        raise SystemExit(2)
    return k


class FalError(RuntimeError):
    """Carries the response body. urllib's default message is just the status
    line, which hides the one useful sentence — a 403 here reads "Exhausted
    balance", not "forbidden", and without the body that costs a debugging round
    trip."""

    def __init__(self, code: int, body: str):
        self.code, self.body = code, body
        hint = ""
        low = body.lower()
        if "exhausted balance" in low or "top up" in low:
            hint = "\n  → Add credits at https://fal.ai/dashboard/billing. The key itself is fine."
        elif code == 401:
            hint = "\n  → The key was not accepted. Check FAL_KEY in your .env."
        elif code == 422:
            hint = "\n  → The request body was rejected; check the model's schema for required fields."
        super().__init__(f"HTTP {code}: {body[:400]}{hint}")


def call(url: str, payload: dict | None = None, method: str = "GET") -> dict:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={"Authorization": f"Key {key()}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise FalError(e.code, e.read().decode("utf-8", "replace")) from None


I2I_MODEL = "fal-ai/krea-2/turbo/image-to-image"


def data_uri(path: Path) -> str:
    """Inline a local image as a data URI.

    fal needs a URL it can fetch, and uploading to their storage would mean the
    catalog's inputs live somewhere the reader cannot see. Inlining keeps every
    source image inside the repo, so an `editing` entry that says "remove the car
    from photography-002" is reproducible by anyone who clones it.
    """
    import base64
    import mimetypes
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def submit(model: str, prompt: str, extra: dict) -> tuple[str, str]:
    """Returns (status_url, response_url) as fal gave them.

    Do not rebuild these from the model slug. fal truncates the path in the URLs
    it hands back — submitting to `fal-ai/krea-2/turbo` yields a status_url under
    `fal-ai/krea-2/requests/<id>/status`, dropping the trailing segment. Rebuilding
    with the full slug gets a 405.
    """
    body = {"prompt": prompt}
    body.update(extra)
    res = call(f"{QUEUE}/{model}", body, "POST")
    rid = res.get("request_id")
    if not rid:
        raise RuntimeError(f"no request_id in response: {res}")
    status_url = res.get("status_url") or f"{QUEUE}/{model}/requests/{rid}/status"
    response_url = res.get("response_url") or f"{QUEUE}/{model}/requests/{rid}"
    return status_url, response_url


def wait(status_url: str, response_url: str, timeout_s: int) -> dict:
    deadline = time.time() + timeout_s
    delay, s = 1.0, "UNKNOWN"
    while time.time() < deadline:
        st = call(status_url)
        s = st.get("status")
        if s == "COMPLETED":
            return call(response_url)
        if s in ("FAILED", "CANCELLED"):
            raise RuntimeError(f"{s}: {json.dumps(st)[:400]}")
        time.sleep(delay)
        delay = min(delay * 1.4, 8.0)
    raise TimeoutError(f"still {s} after {timeout_s}s")


def download(url: str, dest: Path) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": "catalog-gen"})
    with urllib.request.urlopen(req, timeout=180) as r:
        blob = r.read()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(blob)
    return len(blob)


def generate_one(model: str, prompt: str, dest: Path, extra: dict, timeout_s: int) -> dict:
    status_url, response_url = submit(model, prompt, extra)
    out = wait(status_url, response_url, timeout_s)
    images = out.get("images") or []
    if not images:
        raise RuntimeError(f"no images returned: {json.dumps(out)[:300]}")
    size = download(images[0]["url"], dest)
    return {
        "request_id": status_url.rsplit("/", 2)[-2],
        "seed": out.get("seed"),
        "bytes": size,
        # fal returns this when the safety checker trips. The Krea 2 community
        # licence §4.2 makes content filtering a MANDATORY obligation, not an
        # option, so leave enable_safety_checker on and record what it caught.
        "nsfw": (out.get("has_nsfw_concepts") or [None])[0],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--i2i-model", default=I2I_MODEL,
                    help="endpoint used for entries that declare a `source`")
    ap.add_argument("--manifest", help="prompts.json to walk")
    ap.add_argument("--prompt", help="single ad-hoc prompt")
    ap.add_argument("--out", help="output path for --prompt")
    ap.add_argument("--only", help="comma-separated categories")
    ap.add_argument("--id", help="comma-separated entry ids")
    ap.add_argument("--sources", help="extra manifest to resolve `source` ids against")
    ap.add_argument("--force", action="store_true", help="regenerate existing images")
    ap.add_argument("--image-size", default="square_hd",
                    help="square_hd | landscape_16_9 | portrait_4_3 | ...")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--limit", type=int, help="stop after N generations")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    extra = {"image_size": args.image_size, "enable_safety_checker": True}

    if args.prompt:
        dest = Path(args.out or "out.png")
        if args.dry_run:
            print(f"would generate → {dest}")
            return 0
        info = generate_one(args.model, args.prompt, dest, extra, args.timeout)
        print(f"{dest}  seed={info['seed']}  {info['bytes']//1024} KB")
        return 0

    if not args.manifest:
        ap.error("need --manifest or --prompt")

    mpath = Path(args.manifest)
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    root = mpath.parent
    entries = manifest["entries"]

    if args.only:
        keep = {c.strip() for c in args.only.split(",")}
        entries = [e for e in entries if e["category"] in keep]
    if args.id:
        want = {i.strip() for i in args.id.split(",")}
        entries = [e for e in entries if e["id"] in want]

    todo = []
    for e in entries:
        if "PENDING API VERIFICATION" in e.get("prompt", ""):
            continue
        if not args.force and (root / e["image"]).exists():
            continue
        todo.append(e)
    todo.sort(key=lambda e: bool(e.get("source")))  # sources before edits
    if args.limit:
        todo = todo[: args.limit]

    if not todo:
        print("nothing to generate")
        return 0

    est = len(todo) * 0.0084
    print(f"{len(todo)} image(s) via {args.model} — estimated ${est:.2f}\n")
    if args.dry_run:
        for e in todo:
            print(f"  {e['id']}")
        return 0

    by_id = {x["id"]: x for x in manifest["entries"]}
    # A failures manifest cites entries that live in the main catalog, so source
    # lookup has to be able to span manifests.
    if args.sources:
        extra = json.loads(Path(args.sources).read_text(encoding="utf-8"))
        for x in extra["entries"]:
            by_id.setdefault(x["id"], x)
        src_root = Path(args.sources).parent
    ok, failed, flagged = 0, [], []
    for i, e in enumerate(todo, 1):
        dest = root / e["image"]
        print(f"[{i}/{len(todo)}] {e['id']}", end=" ", flush=True)
        try:
            model, call_extra = args.model, dict(extra)
            # An entry with `source` is an image-to-image edit whose input is
            # another entry in this same catalog. Keeping sources in-repo is what
            # makes an edit reproducible for a reader who only has the clone.
            src_id = e.get("source")
            if src_id:
                src = by_id.get(src_id)
                if not src:
                    raise RuntimeError(f"source '{src_id}' not in manifest")
                src_path = root / src["image"]
                if not src_path.exists() and args.sources:
                    src_path = src_root / src["image"]
                if not src_path.exists():
                    raise RuntimeError(f"source image missing: {src['image']} — generate it first")
                model = args.i2i_model
                call_extra["image_url"] = data_uri(src_path)
                call_extra["strength"] = e.get("strength", 0.85)
                print(f"(i2i<-{src_id})", end=" ", flush=True)
            info = generate_one(model, e["prompt"], dest, call_extra, args.timeout)
            e.setdefault("params", {})["seed"] = info["seed"]
            if info.get("nsfw"):
                flagged.append(e["id"])
            print(f"ok  seed={info['seed']}  {info['bytes']//1024} KB")
            ok += 1
        except Exception as exc:  # noqa: BLE001 — one bad prompt must not stop a batch
            print(f"FAIL  {type(exc).__name__}: {str(exc)[:110]}")
            failed.append((e["id"], str(exc)[:200]))

    # Seeds are what make the catalog reproducible, which is the whole claim.
    mpath.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\n{ok} generated, {len(failed)} failed — seeds written back to {mpath.name}")
    if flagged:
        print(f"safety checker flagged: {', '.join(flagged)} — drop these, do not ship them")
    for eid, why in failed:
        print(f"  {eid}: {why}", file=sys.stderr)

    print("\nNow curate. Delete every image you would not put in a portfolio — target\n"
          "keeping 50-60%. One bad image discredits the catalog, and curation is the\n"
          "only moat this format has.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
