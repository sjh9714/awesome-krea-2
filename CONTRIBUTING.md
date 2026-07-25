# Contributing

Two rules, and they are the whole quality bar:

1. **The prompt must reproduce.** Paste it verbatim, run it, get something
   recognisably like the image. If it only worked once with a seed you lost,
   it does not belong here.
2. **The image must be the unedited model output.** No upscaling, no retouching,
   no cherry-picked crop. This catalog is a record of what the model does, not
   of what you can make it do with an hour in Photoshop.

## Adding an entry

Add an object to `prompts.json`:

```json
{
  "id": "photography-042",
  "category": "photography",
  "title": "Short descriptive title",
  "prompt": "The full prompt, exactly as you ran it",
  "image": "images/photography-042.png",
  "params": {"seed": 1234, "aspect_ratio": "3:4"},
  "notes": "Anything a reader needs to reproduce it"
}
```

Then drop the image at that path and open a PR. `python3 build_catalog.py --build`
regenerates the README — do not hand-edit README.md, it is generated.

## What gets rejected

- Prompts that are really just a style name with no content
- Near-duplicates of an existing entry
- Images with visible artefacts presented as successes
- Anything where the model clearly failed and the caption pretends otherwise
