# Wildcards

475 prompts from [this catalog](https://github.com/sjh9714/awesome-krea-2),
one per line, ready for a wildcard or dynamic-prompt node.

- `all.txt` — every prompt, 475 lines
- one file per category (61 of them), if you want to sample within a style

## ComfyUI

Drop this folder into `ComfyUI/wildcards/`, then reference it from a dynamic
prompt node:

```
__all__
__photography__
__typography__
```

## What is not in here

**The seeds.** A wildcard file is one prompt per line and has nowhere to put
them, so a prompt pulled from here will not reproduce the image in the
catalog. If you want the exact image, take the prompt *and* the seed from
`prompts.json` or from the gallery.

**The failures.** 65 generations were cut and they are
deliberately excluded — a wildcard file that occasionally serves a
known-broken prompt is worse than none. They are still in the repository,
with the reason each one failed.

Regenerate with `python3 build_wildcards.py`.
