<h1 align="center">awesome-krea-2</h1>
<p align="center">267 reproducible prompts for Krea 2 Turbo, across 32 categories. Every prompt is copy-pasteable and every image is the actual output.</p>

<p align="center">
  <img src="hero.webp" width="912" alt="Three findings: text holds on one sign and collapses on a list; character identity does not survive a second generation; image-to-image changes medium but not scene contents">
</p>

<p align="center">
<a href="https://github.com/sjh9714/awesome-krea-2/stargazers"><img src="https://img.shields.io/github/stars/sjh9714/awesome-krea-2?style=flat&color=1f5d4c" alt="stars"></a>
<a href="https://sjh9714.github.io/awesome-krea-2/"><img src="https://img.shields.io/badge/gallery-browse%20all-1f5d4c" alt="gallery"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/prompts-MIT-1f5d4c" alt="license"></a>
</p>

<p align="center">[ZH](README_ZH.md) · [KO](README_KO.md) · [**Browse the gallery →**](https://sjh9714.github.io/awesome-krea-2/)</p>

## Categories

**267 prompts, every one with its seed** · [photography](#photography) 18 · [typography](#typography) 15 · [product](#product) 18 · [illustration](#illustration) 18 · [reference-sheet](#reference-sheet) 1 · [isometric-3d](#isometric-3d) 10 · [editing](#editing) 5 · [portrait](#portrait) 8 · [infographic](#infographic) 8 · [collectible](#collectible) 5 · [stationery](#stationery) 6 · [food](#food) 9 · [interior](#interior) 10 · [pattern](#pattern) 8 · [brand-mark](#brand-mark) 7 · [miniature](#miniature) 8 · [coloring-page](#coloring-page) 6 · [ui](#ui) 1 · [stringcount](#stringcount) 8 · [animal](#animal) 10 · [landscape](#landscape) 10 · [fashion](#fashion) 7 · [automotive](#automotive) 7 · [exterior](#exterior) 8 · [abstract](#abstract) 7 · [objectcount](#objectcount) 7 · [monogram](#monogram) 2 · [poster](#poster) 9 · [still-life](#still-life) 8 · [macro-nature](#macro-nature) 8 · [street](#street) 8 · [night](#night) 7

## What this model actually does

Everything below was measured while building this catalog, not quoted from the model card. 322 generations across five batches, 267 are here, 55 were cut. Each claim names the entries that demonstrate it; every entry carries its seed and its batch number, so you can check any of this against the images in this repo.

Three of these findings replace earlier ones that were wrong, and all three were overturned by controlled experiments built to confirm them. The pattern is the same every time: a rule inferred from one or two failures, and a ladder that holds everything constant except the one variable, which then shows the rule was about something else.

### It renders text you write. It cannot invent text.

**This replaces the finding that stood here for three batches, and the replacement came from an experiment designed to confirm it.**

The old claim was that text fails by *count*: one sign holds, a list collapses, and somewhere between four strings and six there is a ceiling. To find the ceiling I built a ladder — the same brass nameplate, the same style, the same short word-like strings, varying only in how many share the frame. `stringcount-1` through `stringcount-8`.

**All eight are correct.** VULCAN. 1938. MODEL 7. SHEFFIELD. SERIAL 4412. 440 VOLTS. 50 CYCLES. MADE IN ENGLAND. Every string legible, on a plate, at eight independent strings. The single error in the whole ladder is a spurious `7` after SHEFFIELD in `stringcount-5`.

So count was never the variable. Going back through every text failure in this repo, the split is exact and it is about **who wrote the string**:

- The chalkboard menu specified `FILTER 4.50`, `CORTADO 4.00` and `OAT +0.60` and asked the model to fill the rest of the board. **Those three rendered correctly.** The unspecified rows came back `CAPEME`, `CABIELO`, `PANSRUR`.
- The twelve book spines said "invent plausible titles". Twelve failures.
- The transit map asked for "legible station names" without naming any. Thirty failures.
- The timeline fixed the range at 1970–2030 and left the labels free. **The years rendered. The labels did not.**
- The terminal specified `$ make install` and asked for "three lines of plausible build output". **The command rendered. The output did not.**
- Of ten UI mockups, the one that worked is `ui-004`, where every string was written out: `Sign in`, `Email`, `Password`, `Continue`. In the cuts, `ui-007` got `Add to cart` exactly right beside an invented product title of pure noise, and `ui-010`, given no column names at all, headed all three columns with the word `Kanban` — reaching for the nearest word in the prompt.

There is one genuine exception, and it is about script rather than authorship: Korean fails even when written out. See below.

**Practical rule: write out every string you want to see, in the prompt, exactly. Never ask this model to make up a word.** Eight strings is not a limit — it is just where I stopped testing.

**Batch five tested this on purpose.** If the rule is right, a category built entirely on written-out strings should work. Ten poster and packaging layouts, every string specified: `KLANG` / `14 MARCH` / `HALLE 7`; `ALPINA` / `BY RAIL`; `LOWLIGHT` / `SIDE A`; `WORKS ON PAPER` / `GALLERY NINE`; `STATIC` / `FRIDAY`; `EYE PROTECTION` / `AREA 4`; `CLOS MARIN` / `2019` / `MIS EN BOUTEILLE`; `MEND IT` / `DON'T END IT`. **All correct.** `poster-008` carries five strings across a book cover and its spine, including the title repeated vertically, and every one of them is right.

One of the ten failed, and not by count: `poster-004` renders `NORTHERN LIGHT` with **both R's mirrored**. The string is right and the glyph is drawn backwards. So specifying the text buys you the text, not a guarantee about every letterform in it — read the output.

### Korean fails even when you write it out

The rule above has one exception in this catalog and it matters if you work in Korean. I asked for a shopfront sign reading exactly `정직한 국수` — specified, four syllables, a real phrase. It came back `정적한 국수`: one vowel wrong in the second syllable.

Everything else about the image is perfect. The brush lettering, the weathered blue panel, the rust bleeding from the screw heads. If you do not read Korean it looks finished; if you do, the error is the first thing you see.

So authorship is not sufficient for non-Latin script. If Hangul is going in the frame, a person who reads it has to check the output.

### Character identity does not survive across generations

A reference sheet of a specific person renders well — see **reference-sheet-001**. Reusing that person in a new scene does not work, and image-to-image does not rescue it, because the two useful settings fail in opposite directions:

- `strength 0.72` — genuinely new scene, but a different person. Only the sweater and the palette carry over.
- `strength 0.45` — recognisably the same person, but the source composition comes with her. A three-view studio sheet became the same three views at a harbour.

There is no middle setting that gives the same face in a different photograph. If you need a consistent character, train a LoRA; prompting cannot do it. This is why there is no character-consistency category here.

### It changes medium willingly and scene content reluctantly

Image-to-image is reliable when you ask for a different *rendering* of the same scene. Rice terraces became a convincing gouache painting with the terrace contours intact (**editing-003**); a woodblock wave took a dusk palette while every keyblock outline stayed put (**editing-005**); an exploded camera diagram became a clean cyanotype blueprint with every component in place (**editing-008**).

It is unreliable when you ask it to add or remove *things*. Three attempts failed and were cut rather than shipped with captions that did not match the images: removing the steam from a mug returned the steam; adding snow and sea ice to a coastline returned the same coastline slightly cooler; darkening a sauna's window returned the window still lit.

`strength` between 0.50 and 0.60 preserved composition while allowing the medium to change. No value made object-level edits work.

### It counts objects. It does not count attributes.

**This is the second finding in this catalog overturned by an experiment built to confirm it.**

It used to say numbers were treated as flavour: I had asked for "exactly two flat colours" and got four, and for a map "divided into five regions" and got eight. To find where counting breaks I ran a ladder — one slate shelf, one white ceramic egg, `exactly N` of them, N from two to eight, nothing else changed. `objectcount-2` through `objectcount-8`.

**All seven are correct.** Two eggs, three, four, five, six, seven, eight. Counted straight off the shelf. Elsewhere in the same batch, `still-life-003` asked for five pieces of glassware and delivered five, `still-life-005` asked for six ceramics and delivered six, `still-life-007` asked for three pears and delivered three.

So the split is not numbers versus no numbers. It is **objects versus attributes**:

- **Discrete separable things that are the subject of the frame get counted.** Eggs, pears, columns, markers, table rows, cake layers.
- **Attributes and emergent divisions do not.** "Exactly two flat colours" is a property of the rendering, not a set of objects, and came back as four with shading (`portrait-008`). "Five regions" on a watercolour map are boundaries that emerge from where the pigment stops, not things you could point at one at a time, and came back as eight (`infographic-007`). "One light source" is not a visible object either, and produced two lamps.

Practical rule: if you can point at each one, ask for a number and expect to get it. If you are counting colours, zones, materials or light sources, count the output yourself.

### Name a light and you get the light. Name the softbox and you get the softbox.

Twice in one batch, naming the physical lighting equipment put that equipment in the frame as a subject.

`portrait-012` asked for a corporate headshot with a **large softbox front and slightly above** against a seamless grey background, and returned a portrait with two large white softboxes flanking the subject. `collectible-008` asked for a rubber duck under **a single large softbox above and behind** and returned a duck with a full lighting umbrella open behind it, filling half the frame.

The prompts that worked describe the *light*, not the *fixture*: "hard low-angle late afternoon sun from frame right", "single hard light high and to camera left", "soft directional daylight". All three rendered the lighting condition with nothing extra in shot.

Practical rule: say what the light does, never what makes it.

### Stationery went six for six, and the reason turned out not to be brevity

The six `stationery-*` entries all rendered their text correctly on the first attempt — `NORTHFIELD & CO`, `FRAGILE`, `ADMIT ONE`, `PAID` — with nothing cut. It is still the cleanest text result in the catalog.

I originally read that as evidence for a brevity rule: one short string in one frame is the shape the model is good at. The `stringcount` ladder says otherwise. Those six succeeded because **every one of them was written out in the prompt**, not because there was only one of them.

`stationery-006` is still the entry to look at. The red `PAID` impression on the paper is correct, and the rubber stamp lying beside it carries the same word **mirrored**, which is what a real stamp face does. Nobody asked for that.

### Interface mockups: the layout is always right, and the words are only as good as your prompt

I added ten UI mockups to batch three expecting nine of them to fail, and nine of them failed. That was the point — a limit you only predict is not a measured limit.

What is striking is *which* half breaks. The structure is consistently correct: `ui-002` has three grouped sections of three rows with a toggle on each, some on and some off, hairlines between; `ui-008` has alternating chat bubbles with avatars, timestamps and a pinned input; `ui-010` has three kanban columns with count badges, tag pills and avatars. Every one of those is exactly what was asked for.

The strings are not. `ui-002` renders the first section header as `Settings` and then degrades to `Sectings` for the next two. `ui-006` fails at the day headers *and* at the dates — the first week reads 5, 6, 51, 13, which is not a week.

The one that worked is **ui-004**, the login screen, and it worked because it has four short real strings: `Sign in`, `Email`, `Password`, `Continue`. All four are letter-perfect. The same effect shows in the cuts — `ui-007` got `Add to cart` exactly right while inventing gibberish for the product title.

At the time I read this as a hard limit on interface work. The `stringcount` ladder shows it is not: **the strings failed because I did not write them.** `ui-004` proves it from inside the same category — four written-out strings, four correct renders — and `ui-010` proves it from the other side, heading all three columns `Kanban` because that was the only word I had given it.

Practical rule: mock up an interface by writing out every label you want to see. What you leave to the model comes back as noise; what you specify comes back correct.

### Letters are fine. Interlocking them is not.

**Third correction, same cause: a claim built on one failure.**

Batch four asked for a monogram of the letters `KJ` interlocked in a circle, got three letterforms, and concluded that the model renders words and not arbitrary letters — reasoning that `COOPERAGE` at nine letters worked while `KJ` at two did not.

Batch five put three more arbitrary letter pairs through. `monogram-002` asked for an A and an E joined into a ligature and returned a clean, correct engraved Æ. `monogram-003` asked for H and B side by side, blind-embossed, and returned exactly that. Both are arbitrary pairs and neither is a word.

The one that failed again is `monogram-001`, R and W **interlocked** — and where the two forms overlap, the R reads as a P.

So it was never about words. Letters render. What fails is asking the model to fuse two letterforms into a composite where they share strokes, because at that point neither letter has an intact shape to be drawn. A real ligature like Æ is a single glyph it already knows, which is why that one worked.

Practical rule: set letters side by side, or ask for a ligature that actually exists. Do not ask for an invented interlock.

### "Seamless" produces a pattern that does not tile

All eight `pattern-*` prompts asked for a seamless repeat. I tiled the outputs and measured the seam by comparing each image's left edge column against its right, and its top row against its bottom, against the baseline difference between two arbitrary interior columns of the same image.

**One of the eight tiles.** That one is `pattern-007`, vertical hand-drawn stripes, where the edges match because vertical stripes match trivially — structural luck, not the instruction being followed. `pattern-005` tiles horizontally and not vertically. The remaining six have edge differences at or above their own interior baseline, meaning the two edges are as unrelated as two random slices.

The images are good. Several are genuinely beautiful surface designs. They are just not repeat tiles, and if you drop one into a wallpaper or textile pipeline expecting it to run, it will seam.

Practical rule: treat these as one-off surfaces. Making them actually tile is a post-process, not a prompt.

## The image-to-image entries, taken further

The five `editing-*` entries were pulled out into [**same-frame**](https://github.com/sjh9714/same-frame), an agent skill for Claude Code and Codex, and each one was re-run against a source it was *not* derived from. Two held, two came back partial, one failed — and the failures produced a sharper rule than this catalog started with: **geometry is locked, material is not.** Relighting wet rice terraces under hard sun keeps every contour in position and returns dry stone.

That repo also carries the two edits cut from here as refusals: it blocks an object-removal or character-consistency request before it is spent, and shows you the image where it already failed.

## Check any of this yourself

Every entry carries the seed that produced it, so no claim here has to be taken on trust:

```bash
python3 scripts/regen.py --id typography-012
```

Regenerating two text-to-image entries and comparing against the files in this repo gave a mean per-pixel difference of 1.3 and 1.5 out of 255, which is WebP re-encoding loss. The seed reproduces the generation; the repo stores the re-encode.

The five `editing-*` entries are the exception, and the number is much larger. The endpoint itself is deterministic — a repeat run at identical seed, strength, prompt and input bytes came back pixel-identical, 0 of 1,048,576 pixels different. But an image-to-image re-run from a clone is fed the WebP in this repo, not the original PNG the edit was made from, and that input difference compounds: regenerating `editing-003` this way gives a mean per-pixel difference of **17.0 out of 255**. The composition, palette and medium come back; the brush-level texture does not. Read those five as reproducible edits, not as reproducible pixels.

## The failures, kept as evidence

Deliberately reproduced failures. Every claim in the README's findings section points at one of these, with the seed that produced it, so the limits are checkable rather than asserted. These are NOT part of the 85-entry catalog.

| | What was asked for | What came back |
|---|---|---|
| <img src="images/failures/fail-menu.webp" width="150" alt="Text: a list of many strings collapses after the first few"> | Ten legible menu rows | Text: a list of many strings collapses after the first few <br>`seed: 1729505870` |
| <img src="images/failures/fail-spines.webp" width="150" alt="Text: twelve independent strings in one frame, all unreadable"> | Twelve readable invented titles | Text: twelve independent strings in one frame, all unreadable <br>`seed: 1095803014` |
| <img src="images/failures/fail-map.webp" width="150" alt="Text: thirty station names, none of them words"> | Legible station names | Text: thirty station names, none of them words <br>`seed: 57616412` |
| <img src="images/failures/fail-timeline.webp" width="150" alt="Text: years render, labels do not"> | Eight year+label pairs | Text: years render, labels do not <br>`seed: 797625079` |
| <img src="images/failures/fail-korean.webp" width="150" alt="Text: Korean fails one character in, and looks clean if you cannot read it"> | 정직한 국수 | Text: Korean fails one character in, and looks clean if you cannot read it <br>`seed: 1910572019` |
| <img src="images/failures/fail-terminal.webp" width="150" alt="Text: the command line renders, the output beneath it does not"> | $ make install plus three lines of build output | Text: the command line renders, the output beneath it does not <br>`seed: 1530960951` |
| <img src="images/failures/fail-identity.webp" width="150" alt="Identity: at strength 0.72 the scene is new and the person is not the same"> | The woman from reference-sheet-001 | Identity: at strength 0.72 the scene is new and the person is not the same <br>`seed: 1317515569` |
| <img src="images/failures/fail-removal.webp" width="150" alt="Editing: asked to remove the steam, returns the steam"> | No steam | Editing: asked to remove the steam, returns the steam <br>`seed: 1499506316` |
| <img src="images/failures/portrait-006.webp" width="150" alt="Portrait: asked for a silhouette, got a fully modelled face"> | A clean dark silhouette, exposed for the sky | Portrait: asked for a silhouette, got a fully modelled face <br>`seed: 2099062475` |
| <img src="images/failures/portrait-008.webp" width="150" alt="Count: 'exactly two flat colours plus white' returned four plus shading"> | Two flat colours, no gradients | Count: 'exactly two flat colours plus white' returned four plus shading <br>`seed: 1251562984` |
| <img src="images/failures/portrait-010.webp" width="150" alt="Light: two named colours from opposite sides did not cross on the face"> | Magenta from frame left and cyan from frame right meeting across the face | Light: two named colours from opposite sides did not cross on the face <br>`seed: 416503906` |
| <img src="images/failures/portrait-012.webp" width="150" alt="Equipment: naming the softbox put the softbox in the frame"> | Seamless mid-grey background, light source out of shot | Equipment: naming the softbox put the softbox in the frame <br>`seed: 639894452` |
| <img src="images/failures/infographic-004.webp" width="150" alt="Text: the chalk heading rendered, the three bullet lines under it did not"> | A heading plus three short bullet lines | Text: the chalk heading rendered, the three bullet lines under it did not <br>`seed: 1043088059` |
| <img src="images/failures/infographic-007.webp" width="150" alt="Count: 'five regions' returned eight, and the ink coastline never appeared"> | Five regions with a thin brown ink coastline | Count: 'five regions' returned eight, and the ink coastline never appeared <br>`seed: 125241101` |
| <img src="images/failures/collectible-003.webp" width="150" alt="Text: four keycap legends came back as letter-shaped noise"> | Four legible dye-sublimated legends | Text: four keycap legends came back as letter-shaped noise <br>`seed: 1958353167` |
| <img src="images/failures/collectible-004.webp" width="150" alt="Layout: the creature artwork went to the top and the centre panel stayed empty"> | Illustrated creature artwork in the central panel | Layout: the creature artwork went to the top and the centre panel stayed empty <br>`seed: 167021886` |
| <img src="images/failures/collectible-008.webp" width="150" alt="Equipment: naming the softbox put the softbox in the frame"> | A single softbox lighting the duck, out of shot | Equipment: naming the softbox put the softbox in the frame <br>`seed: 1935262212` |
| <img src="images/failures/food-003.webp" width="150" alt="Mechanism: the espresso renders as an amber disc where the basket should be, and one stream instead of two"> | Two thin streams from a portafilter | Mechanism: the espresso renders as an amber disc where the basket should be, and one stream instead of two <br>`seed: 117001054` |
| <img src="images/failures/brand-mark-002.webp" width="150" alt="Letters: asked for the monogram 'KJ', got three letterforms that are not those two"> | The letters K and J interlocked | Letters: asked for the monogram 'KJ', got three letterforms that are not those two <br>`seed: 1276536027` |
| <img src="images/failures/ui-001.webp" width="150" alt="UI: every invented label is noise while the currency amounts render correctly"> | Transaction names, dates and amounts | UI: every invented label is noise while the currency amounts render correctly <br>`seed: 1378883083` |
| <img src="images/failures/ui-002.webp" width="150" alt="UI: the first section header reads 'Settings'; the next two degrade to 'Sectings'"> | Three section headers and six row labels | UI: the first section header reads 'Settings'; the next two degrade to 'Sectings' <br>`seed: 1537435411` |
| <img src="images/failures/ui-003.webp" width="150" alt="UI: metric numbers survive, every label around them does not"> | Four labelled metric cards and a five-row table | UI: metric numbers survive, every label around them does not <br>`seed: 401297056` |
| <img src="images/failures/ui-005.webp" width="150" alt="UI: a code editor renders as convincing syntax-coloured noise with no readable token"> | Syntax-highlighted code | UI: a code editor renders as convincing syntax-coloured noise with no readable token <br>`seed: 1224413193` |
| <img src="images/failures/ui-006.webp" width="150" alt="UI: the day headers fail and so do the dates — 5, 6, 51, 13 is not a week"> | Seven weekday headers and a sequential date grid | UI: the day headers fail and so do the dates — 5, 6, 51, 13 is not a week <br>`seed: 982476354` |
| <img src="images/failures/ui-007.webp" width="150" alt="UI: 'Add to cart' is correct, the product title is not, and the size buttons all read 'Size'"> | A product title, a price, and size options | UI: 'Add to cart' is correct, the product title is not, and the size buttons all read 'Size' <br>`seed: 1056892936` |
| <img src="images/failures/ui-008.webp" width="150" alt="UI: chat bubbles are structurally perfect and every message is unreadable"> | Readable alternating messages | UI: chat bubbles are structurally perfect and every message is unreadable <br>`seed: 880659524` |
| <img src="images/failures/ui-009.webp" width="150" alt="UI: the illustration is good, the headline and the button label are not"> | A headline, supporting text and a button label | UI: the illustration is good, the headline and the button label are not <br>`seed: 727964264` |
| <img src="images/failures/ui-010.webp" width="150" alt="UI: all three columns are literally headed 'Kanban' — the model rendered the word from the prompt"> | Three distinct column names | UI: all three columns are literally headed 'Kanban' — the model rendered the word from the prompt <br>`seed: 1672153217` |
| <img src="images/failures/fashion-007.webp" width="150" alt="Composition: asked for the rail end-on as receding silhouettes, got it side-on with the hangers showing"> | An end-on rail reading as layered silhouettes | Composition: asked for the rail end-on as receding silhouettes, got it side-on with the hangers showing <br>`seed: 1999599151` |
| <img src="images/failures/automotive-002.webp" width="150" alt="Text: the tyre sidewall lettering is legible enough to read as wrong"> | Out-of-focus sidewall lettering | Text: the tyre sidewall lettering is legible enough to read as wrong <br>`seed: 318918336` |
| <img src="images/failures/abstract-004.webp" width="150" alt="Colour: 'coloured light trails' came back as four pale near-white lines"> | Crossing, looping, coloured trails | Colour: 'coloured light trails' came back as four pale near-white lines <br>`seed: 478699619` |
| <img src="images/failures/monogram-001.webp" width="150" alt="Letters: asked to interlock R and W, the R reads as a P where the two forms overlap"> | R and W, both legible | Letters: asked to interlock R and W, the R reads as a P where the two forms overlap <br>`seed: 1193159535` |
| <img src="images/failures/poster-004.webp" width="150" alt="Glyph: the string is right and both R's are drawn mirrored — NOЯTHEЯN LIGHT"> | NORTHERN LIGHT | Glyph: the string is right and both R's are drawn mirrored — NOЯTHEЯN LIGHT <br>`seed: 1064082710` |
| <img src="images/failures/night-002.webp" width="150" alt="Scene: the reflection never resolves into water; the lower half reads as a second sky"> | The Milky Way reflected in still water | Scene: the reflection never resolves into water; the lower half reads as a second sky <br>`seed: 1089231047` |

## How this compares

Verified on 2026-07-25 by reading each repository's tree, README and data files, and by requesting the image URLs. These are good catalogs and two of them do the in-repo thing better than I expected, so the table gives them credit for it. The two columns where nothing exists yet are the reason this repo bothered.

| | Prompts | Images in repo | Seeds / params | Failures shown | Measured cost |
|---|---|---|---|---|---|
| **this repo** | 85 | ✅ 93 | ✅ **all 85** | ✅ **8, with seeds** | ✅ **$1.26 / 150 gens** |
| [YouMind/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) · 12,956★ | 14,916 claimed, 129 in README | ❌ external CMS | ❌ | ❌ | ❌ |
| [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) · 10,190★ | 70 | ❌ external, 3 already dead | ❌ | ❌ | ❌ |
| [YouMind/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) · 8,772★ | 13,663 claimed, 126 in README | ❌ external CMS | ❌ | ❌ | ❌ |
| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) · 8,687★ | 517 | ✅ 549 | ❌ | ⚠️ prose caveats, no images | ❌ |
| [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) · 8,097★ | 100 | ✅ 100 | ❌ | ❌ | ⚠️ tool per case, no cost |

- **Nobody records seeds.** Checked every entry in all five: YouMind's per-entry block carries Author / Source / Published / Languages and nothing else, and its submission form has no seed field either. freestylefly's `cases.json` has thirteen keys, none of them a seed. jamez's `case.yml` and `ATTRIBUTION.yml` schemas have no seed field. This is the only claim here that holds without qualification.
- **Nobody publishes what it cost.** jamez does record `creation_tool` (Sora on 97 of 100 cases, GPT-4o on 3) and freestylefly documents its generation path, which is more than the others — but neither states a figure.
- **Credit where it is due on reproducibility.** freestylefly commits 549 images and jamez 100, both with relative paths and copy-pasteable prompts. Those two are self-contained and I am not claiming otherwise.
- **Link rot is not hypothetical.** ZeroLu's 86 images are all external. Requesting them on 2026-07-25 found three already gone — two Twitter CDN links returning 403/404 and one path that no longer exists in the repo. That is why the images here are committed rather than linked.
- **Scale claims deserve reading twice.** The two YouMind repos advertise 14,916 and 13,663 prompts. Their own FAQ says images live on a CMS, not in git, and their README says GitHub's length limit caps the visible list — 129 and 126 entries respectively, under 1% of the headline number. The rest are on their website.
- jamez-bondos has not been pushed since 2025-05-26.


## photography

_Photoreal scenes — lighting, lens behaviour, film stock_

### Ceramicist at golden hour, 85mm

<img src="images/photography-001.webp" width="420" alt="Ceramicist at golden hour, 85mm">

**Prompt**

```text
A ceramicist in her studio at golden hour, hands wet with slip, throwing a bowl on a kick wheel. Shot on 85mm at f/1.8, shallow depth of field, warm rim light from a west-facing window, dust motes in the beam. Muted earth palette, visible clay dust on her forearms.
```

`seed: 1913817765`

### Rain-soaked crosswalk, neon reflections

<img src="images/photography-002.webp" width="420" alt="Rain-soaked crosswalk, neon reflections">

**Prompt**

```text
A rain-soaked crosswalk at night in Seoul, seen from a low angle at pavement level. Neon signage reflected and broken across the wet asphalt, a single pedestrian mid-stride with an umbrella. 35mm, deep focus, high contrast, cyan and magenta cast against black.
```

`seed: 1037393037`

### Cold-lit surgical corridor

<img src="images/photography-003.webp" width="420" alt="Cold-lit surgical corridor">

**Prompt**

```text
An empty hospital corridor lit only by overhead fluorescents, one tube flickering. Polished linoleum reflecting the ceiling lights into long streaks. Symmetrical one-point perspective, 24mm, slight barrel distortion, desaturated green-grey palette, absolutely no people.
```

`seed: 306108529`

### Portra 400 family kitchen

<img src="images/photography-004.webp" width="420" alt="Portra 400 family kitchen">

**Prompt**

```text
A cluttered family kitchen mid-morning, shot on Kodak Portra 400, slight grain and halation on the highlights. Steam from a kettle catching the window light, dishes stacked, a child's drawing taped to a cabinet. Natural skin tones, soft contrast, 50mm.
```

`seed: 1671971794`

### Macro: solder joint

<img src="images/photography-005.webp" width="420" alt="Macro: solder joint">

**Prompt**

```text
Extreme macro of a hand-soldered joint on a green PCB, 5:1 magnification, focus stacked so the entire solder fillet is sharp. Visible flux residue, the silkscreen label R14 legible beside it. Cold ring light, shallow background falloff into black.
```

`seed: 1136909792`

### Overcast coastline, long exposure

<img src="images/photography-006.webp" width="420" alt="Overcast coastline, long exposure">

**Prompt**

```text
A basalt coastline under heavy overcast, 30-second long exposure so the surf becomes a low white mist around the rocks. Horizon dead level, no sun, 16mm, ND1000, cool grey palette with a single ochre patch of lichen in the foreground.
```

`seed: 589730875`

### Backlit dust in a warehouse

<img src="images/photography-007.webp" width="420" alt="Backlit dust in a warehouse">

**Prompt**

```text
A disused warehouse interior, late afternoon sun entering through a high broken window as a hard visible shaft. Dust suspended in the beam, everything outside the beam falling to near-black. 35mm, heavy contrast, one strong light source only.
```

`seed: 1496444718`

### Flash-lit street portrait at night

<img src="images/photography-008.webp" width="420" alt="Flash-lit street portrait at night">

**Prompt**

```text
A street portrait at night, direct on-camera flash, subject one metre from the lens, background falling off to black within two metres. Harsh specular highlights on skin, red-eye avoided, 28mm, the raw snapshot aesthetic of 1990s tabloid photography.
```

`seed: 1204392285`

### Aerial: terraced rice fields

<img src="images/photography-009.webp" width="420" alt="Aerial: terraced rice fields">

**Prompt**

```text
Directly overhead drone shot of terraced rice fields at flooding stage, water surfaces mirroring a pale sky so the terraces read as abstract silver contours. No horizon. Late afternoon, long shadows from the retaining walls, subtle green fringe of new growth.
```

`seed: 1726756617`

### Tungsten-lit diner booth

<img src="images/photography-010.webp" width="420" alt="Tungsten-lit diner booth">

**Prompt**

```text
A booth in an empty roadside diner at 2am, lit by warm tungsten pendants against cold blue exterior night through the window. Chrome napkin dispenser catching both colour temperatures. 40mm, slight vignette, colour contrast between the two light sources is the subject.
```

`seed: 1590663786`

### Fog bank on a suspension bridge

<img src="images/photography-011.webp" width="420" alt="Fog bank on a suspension bridge">

**Prompt**

```text
The upper cables of a suspension bridge disappearing into a fog bank, shot from the deck with a 200mm lens so the towers compress into flat silhouetted layers. Visibility drops to nothing by the second tower. Cool grey monochrome broken only by one amber sodium lamp.
```

`seed: 1647355798`

### Window seat, altitude

<img src="images/photography-012.webp" width="420" alt="Window seat, altitude">

**Prompt**

```text
From an aircraft window at cruising altitude: the wing's trailing edge in the lower third, a solid deck of cloud below, and the curvature of the horizon under a gradient from pale gold to deep indigo. Slight scratches and haze in the acrylic pane, deliberately not corrected.
```

`seed: 849986701`

### Sauna interior, steam

<img src="images/photography-013.webp" width="420" alt="Sauna interior, steam">

**Prompt**

```text
A cedar sauna interior lit by one small high window, steam rolling off the stove rocks and catching the light. Wet benches, condensation running down the wall boards. 24mm, warm brown palette, the air itself is the subject.
```

`seed: 1447903387`

### Night market, tungsten and smoke

<img src="images/photography-014.webp" width="420" alt="Night market, tungsten and smoke">

**Prompt**

```text
A night market food stall shot from across the aisle, tungsten bulbs overhead, smoke from a griddle drifting through the light. Vendor mid-motion so the hands blur while the stall stays sharp. 35mm, 1/15s, handheld.
```

`seed: 860958653`

### Frost on single-glazed glass

<img src="images/photography-015.webp" width="420" alt="Frost on single-glazed glass">

**Prompt**

```text
Macro of frost crystals on the inside of a single-glazed window at dawn, backlit by low sun so each dendrite glows. Focus falls off within a centimetre. Blue shadow tones against a warm bloom, no other subject.
```

`seed: 1223022199`

### Empty swimming pool, drained

<img src="images/photography-016.webp" width="420" alt="Empty swimming pool, drained">

**Prompt**

```text
A drained municipal swimming pool photographed from the deep end floor looking up at the diving board. Cracked blue paint, leaf litter in the corners, harsh midday sun cutting a hard diagonal across the tiled wall. 20mm, exaggerated verticals.
```

`seed: 1658386034`

### Workshop hands, no face

<img src="images/photography-017.webp" width="420" alt="Workshop hands, no face">

**Prompt**

```text
Close crop of a woodworker's hands setting a hand plane on a bench, wrist and forearm only, no face in frame. Shavings curling from the mouth of the plane. Soft north light, 60mm macro, shallow focus on the blade edge.
```

`seed: 1007639879`

### Motorway at dusk, long lens

<img src="images/photography-018.webp" width="420" alt="Motorway at dusk, long lens">

**Prompt**

```text
A motorway interchange shot from an overpass with a 400mm lens at dusk, headlight and taillight streams compressed into stacked ribbons of white and red. Traffic and infrastructure become pure horizontal bands. 8-second exposure, no sky visible.
```

`seed: 1873728665`


## typography

_Short-string text rendering. Krea 2 holds a single sign or label at any length, including an eight-word plaque, but degrades once several independent strings or a paragraph share the frame._

### Enamel pin packaging

<img src="images/typography-003.webp" width="420" alt="Enamel pin packaging">

**Prompt**

```text
Retail backing card for an enamel pin, photographed flat. The card reads "NIGHT SHIFT" in a condensed grotesque at the top and "limited to 200" in small caps at the bottom. Riso-style two-colour print, fluorescent orange and navy, visible paper tooth and slight misregistration.
```

`seed: 333206637`

### Letterpress business card, macro

<img src="images/typography-008.webp" width="420" alt="Letterpress business card, macro">

**Prompt**

```text
Macro of a letterpress business card on cotton stock, raking light from the left so the deep impression casts visible shadows in the counters. The card reads "HOLLOW & SON — MILLWRIGHTS — EST 1908" in a small caps serif. Single ink colour, deep indigo, generous letterspacing.
```

`seed: 1431711597`

### Stencilled crate marking

<img src="images/typography-011.webp" width="420" alt="Stencilled crate marking">

**Prompt**

```text
A wooden shipping crate photographed straight on, stencilled in black spray paint with exactly "FRAGILE" above "THIS WAY UP". Paint has bled slightly through the stencil edges. Weathered pine, raking side light.
```

`seed: 1101869585`

### Enamel station sign

<img src="images/typography-012.webp" width="420" alt="Enamel station sign">

**Prompt**

```text
A vitreous enamel railway platform sign on a brick wall, dark blue ground with white letters reading exactly "PLATFORM 4". Chipped at one corner exposing the steel. Straight-on, overcast light.
```

`seed: 1556240670`

### Embroidered cap

<img src="images/typography-013.webp" width="420" alt="Embroidered cap">

**Prompt**

```text
Macro of a canvas cap's front panel with "NORTH YARD" embroidered in cream chain-stitch on olive twill. Visible thread texture and slight puckering of the fabric under the stitching.
```

`seed: 1864240842`

### Neon, one word

<img src="images/typography-014.webp" width="420" alt="Neon, one word">

**Prompt**

```text
A single neon sign on a brick wall at dusk reading exactly "OPEN" in cursive rose-pink tube, visible glass path and mounting standoffs, pink spill on the brick. One segment dark.
```

`seed: 235613196`

### Hot-foil business card

<img src="images/typography-015.webp" width="420" alt="Hot-foil business card">

**Prompt**

```text
Macro of a black cotton business card with "MERIDIAN" hot-foil stamped in copper, raking light catching the foil. No other text. Shallow depth of field.
```

`seed: 2040305462`

### Chalk price tag

<img src="images/typography-016.webp" width="420" alt="Chalk price tag">

**Prompt**

```text
A small slate price tag propped in a bakery basket, hand-chalked with exactly "SOURDOUGH" and "£4.20" beneath it. Warm morning light, shallow focus, flour dust on the slate.
```

`seed: 1659883`

### Painted boat transom

<img src="images/typography-017.webp" width="420" alt="Painted boat transom">

**Prompt**

```text
The transom of a wooden fishing boat, hand-painted in white serif capitals reading exactly "MARY ANNE". Green hull, salt-weathered paint, waterline just visible. Straight-on documentary framing.
```

`seed: 375084430`

### Letterpress poster, two words

<img src="images/typography-018.webp" width="420" alt="Letterpress poster, two words">

**Prompt**

```text
A letterpress poster on cotton paper reading exactly "KEEP GOING" in wood type, deep impression visible under raking light, single ink colour oxblood, generous margins, no other elements.
```

`seed: 833951684`

### Machine-shop door

<img src="images/typography-019.webp" width="420" alt="Machine-shop door">

**Prompt**

```text
A steel workshop door with an aluminium plate riveted at eye level, engraved "TOOL ROOM" in machine-cut capitals filled with black paint. Scuffed metal, industrial lighting.
```

`seed: 984217211`

### Airport gate display

<img src="images/typography-020.webp" width="420" alt="Airport gate display">

**Prompt**

```text
A split-flap departure board close-up showing a single row reading exactly "SEOUL" and "GATE 12". Mechanical flaps mid-settle on one character. Warm indicator lighting, shallow depth.
```

`seed: 1590119155`

### Fire door sign

<img src="images/typography-021.webp" width="420" alt="Fire door sign">

**Prompt**

```text
A steel fire door with a rectangular sign at eye level reading exactly "FIRE EXIT" in white on green, small running-figure pictogram beside the text. Scuffed paint, institutional corridor lighting, straight-on.
```

`seed: 2060170403`

### Engraved brass plaque

<img src="images/typography-022.webp" width="420" alt="Engraved brass plaque">

**Prompt**

```text
A small brass plaque screwed to a stone wall, engraved and blacked with exactly "EST 1884". Patina in the letter recesses, raking afternoon light, shallow depth of field.
```

`seed: 425919870`

### Tin sign, two words

<img src="images/typography-023.webp" width="420" alt="Tin sign, two words">

**Prompt**

```text
A weathered enamel tin sign nailed to a barn wall reading exactly "FRESH EGGS" in hand-painted red capitals on cream. Rust bleeding from two nail heads, overcast light, straight-on documentary framing.
```

`seed: 722835994`


## product

_Product and packaging shots, studio and in-context_

### Perfume bottle, hard light

<img src="images/product-001.webp" width="420" alt="Perfume bottle, hard light">

**Prompt**

```text
A faceted glass perfume bottle on a polished black surface, single hard key light from upper left creating one crisp specular edge down the bottle's spine and a sharp reflection beneath. Deep shadow elsewhere. No label. Product photography, 100mm macro, f/11.
```

`seed: 524883984`

### Coffee bag, in-context

<img src="images/product-002.webp" width="420" alt="Coffee bag, in-context">

**Prompt**

```text
A kraft coffee bag with a matte white label standing on a scratched steel countertop in a working roastery, bokeh of roasting drums behind. Natural window light from camera left. The bag looks used, one corner folded and clipped. Editorial rather than studio.
```

`seed: 98544605`

### Mechanical keyboard, top-down

<img src="images/product-003.webp" width="420" alt="Mechanical keyboard, top-down">

**Prompt**

```text
Top-down flat lay of an aluminium 65% mechanical keyboard on a grey desk mat, keycaps in beige and slate with one red escape key. Even diffuse light, no hotspots, every legend crisp and readable. Coiled aviator cable arranged in a loose S to the upper right.
```

`seed: 1919442279`

### Skincare on wet stone

<img src="images/product-004.webp" width="420" alt="Skincare on wet stone">

**Prompt**

```text
A frosted glass dropper bottle resting on a wet slate slab, water beading and running off the edge. Cool north light, soft gradient background from pale grey to white. A single eucalyptus leaf, slightly out of focus, in the lower right. Clean, cold, clinical.
```

`seed: 2048927115`

### Sneaker, floating explode

<img src="images/product-005.webp" width="420" alt="Sneaker, floating explode">

**Prompt**

```text
A running shoe photographed against seamless light grey with its components separated and suspended in an exploded view — outsole, midsole, upper, laces, insole — each layer held apart with even spacing. Soft top light, consistent shadows implying a single source, technical and legible.
```

`seed: 700222067`

### Watch macro, brushed steel

<img src="images/product-006.webp" width="420" alt="Watch macro, brushed steel">

**Prompt**

```text
Macro of a brushed steel dive watch bezel and crown, focus stacked so the knurling on the crown and the brushing grain on the case are both sharp. Controlled reflection strip along the polished chamfer. Dark grey background, no logo visible.
```

`seed: 1367506460`

### Cast iron pan, overhead with food

<img src="images/product-007.webp" width="420" alt="Cast iron pan, overhead with food">

**Prompt**

```text
Overhead of a seasoned cast iron skillet on a scorched linen cloth, containing a half-eaten galette with visible flaking layers. Crumbs on the cloth. Directional afternoon light from the top of frame with real falloff toward the bottom. Nothing styled to perfection.
```

`seed: 2127336597`

### Cable and connector detail

<img src="images/product-008.webp" width="420" alt="Cable and connector detail">

**Prompt**

```text
A braided USB-C cable coiled loosely on a white acrylic surface, one connector standing upright and in focus showing the moulded strain relief and contacts. Bright even light, faint shadow, the coil falling out of focus behind. Catalogue clarity.
```

`seed: 2081046429`

### Ceramic mug, steam

<img src="images/product-009.webp" width="420" alt="Ceramic mug, steam">

**Prompt**

```text
A speckled stoneware mug of black coffee on a pale oak table, backlit so the rising steam is clearly visible against a dark background. Reactive glaze pooling at the base. The steam is the hero — it must read as real vapour, not smoke.
```

`seed: 130047460`

### Packaging flat lay, unboxed

<img src="images/product-010.webp" width="420" alt="Packaging flat lay, unboxed">

**Prompt**

```text
An unboxed product flat lay: rigid box lid to the left, tissue paper unfolded, a small booklet, and the product itself centre right. Shot from directly overhead on a warm grey backdrop, soft shadowless light, elements aligned to an invisible grid with generous negative space.
```

`seed: 1260154266`

### Vinyl record and sleeve

<img src="images/product-011.webp" width="420" alt="Vinyl record and sleeve">

**Prompt**

```text
A vinyl record half-withdrawn from its sleeve on a walnut surface, raking light picking out the groove texture and one fingerprint on the run-out. Sleeve plain matte black, no artwork. 50mm, single softbox from the left, deep falloff to the right.
```

`seed: 1427728813`

### Fountain pen nib, extreme macro

<img src="images/product-012.webp" width="420" alt="Fountain pen nib, extreme macro">

**Prompt**

```text
Extreme macro of a fountain pen nib, focus stacked so the tipping material, the slit and the breather hole are all sharp. Ink residue in the feed channels. Dark field lighting so the steel reads as bright edges against black.
```

`seed: 2063722228`

### Climbing shoe, worn

<img src="images/product-013.webp" width="420" alt="Climbing shoe, worn">

**Prompt**

```text
A single well-worn climbing shoe on raw concrete, rubber scuffed through at the toe, laces frayed. Hard overhead light casting a tight shadow. Nothing styled — the wear is the subject. 85mm, f/8.
```

`seed: 1309089861`

### Glassware set, backlit

<img src="images/product-014.webp" width="420" alt="Glassware set, backlit">

**Prompt**

```text
Three drinking glasses of graduated height on a white acrylic surface, backlit so the walls read as bright rims and the bases as dense caustics. No labels, no reflections of the studio. Perfectly level camera, clinical.
```

`seed: 329967531`

### Leather satchel, texture

<img src="images/product-015.webp" width="420" alt="Leather satchel, texture">

**Prompt**

```text
A tan leather satchel on a linen backdrop, side-lit to bring out the grain, stitch holes and the darkening around the buckle where it is handled. Slight sag in the flap from real use. 90mm macro, f/5.6.
```

`seed: 2115381394`

### Espresso tamper on grounds

<img src="images/product-016.webp" width="420" alt="Espresso tamper on grounds">

**Prompt**

```text
A stainless espresso tamper resting on a bed of fresh grounds in a portafilter, top-down, single hard light from the upper right. Grounds crisp enough to read individual particles at the edge of the puck.
```

`seed: 987689524`

### Wool swatch stack

<img src="images/product-017.webp" width="420" alt="Wool swatch stack">

**Prompt**

```text
A stack of eight folded wool fabric swatches in muted heather tones, shot from a low three-quarter angle so the stack reads as bands of colour and texture. Soft even light, no shadow drama, catalogue clarity.
```

`seed: 1858895601`

### Bike drivetrain, dirty

<img src="images/product-018.webp" width="420" alt="Bike drivetrain, dirty">

**Prompt**

```text
A road bike's rear cassette and derailleur photographed side-on, chain grimy with real road dirt, one cog catching a highlight. Garage light, unglamorous, mechanical honesty. 100mm macro, f/6.3.
```

`seed: 1450341996`


## illustration

_Stylised, painterly, editorial_

### Editorial: burnout

<img src="images/illustration-001.webp" width="420" alt="Editorial: burnout">

**Prompt**

```text
An editorial illustration for an article on developer burnout. A figure at a desk rendered as a slowly unravelling ball of yarn, the loose thread running off the desk and out of frame. Limited palette: ink black, bone white, one dusty coral. Textured screenprint grain, generous negative space.
```

`seed: 1809538529`

### Gouache mountain hut

<img src="images/illustration-002.webp" width="420" alt="Gouache mountain hut">

**Prompt**

```text
A small stone hut on an alpine ridge at dusk, painted in gouache with visible brush texture and slightly chalky opacity. Cool blue snow shadows against a warm ochre sky. Simplified shapes, no outlines, hard edges where the paint has dried in layers.
```

`seed: 989989533`

### Ligne claire street scene

<img src="images/illustration-003.webp" width="420" alt="Ligne claire street scene">

**Prompt**

```text
A European city street in ligne claire style — uniform black contour lines of even weight, flat unmodulated colour fills, no hatching or gradients. A cyclist passing a bakery, a cat on a windowsill. Clear midday light implied purely through colour choice, not shading.
```

`seed: 193829588`

### Woodblock wave study

<img src="images/illustration-004.webp" width="420" alt="Woodblock wave study">

**Prompt**

```text
A single breaking wave in the manner of a Japanese woodblock print: flat colour fields, keyblock outlines, visible wood grain texture in the sky area, deliberate slight misregistration of the blue plate. Indigo, pale sand, off-white paper tone. No figures.
```

`seed: 2141994631`

### Technical cutaway, hand-drawn

<img src="images/illustration-005.webp" width="420" alt="Technical cutaway, hand-drawn">

**Prompt**

```text
A hand-drawn technical cutaway of a mechanical wristwatch movement, ink line with light watercolour wash, leader lines pointing to unlabelled callout circles. Slightly imperfect linework showing it was drawn by hand. Warm paper tone, sepia ink.
```

`seed: 711741992`

### Risograph two-colour poster

<img src="images/illustration-006.webp" width="420" alt="Risograph two-colour poster">

**Prompt**

```text
A two-colour risograph poster of a lone figure walking a dog across a wide empty field. Fluorescent pink and teal only, overprint where they cross producing a muddy third tone. Visible paper grain, roller streaks, 2mm misregistration on the teal layer.
```

`seed: 1958333047`

### Children's book interior

<img src="images/illustration-007.webp" width="420" alt="Children's book interior">

**Prompt**

```text
An interior spread from a children's picture book: a badger in a knitted scarf reading by lamplight in a burrow, roots visible through the earth walls. Soft coloured pencil texture, warm palette, no harsh outlines, plenty of quiet space in the composition.
```

`seed: 437733224`

### Brutalist architecture, ink

<img src="images/illustration-008.webp" width="420" alt="Brutalist architecture, ink">

**Prompt**

```text
An ink drawing of a brutalist concrete community centre, cross-hatched shading only, no grey wash. Heavy contrast between lit and shadowed planes achieved entirely through hatch density. Slight wobble in the straight lines betraying a human hand.
```

`seed: 1322534157`

### Botanical plate

<img src="images/illustration-009.webp" width="420" alt="Botanical plate">

**Prompt**

```text
A scientific botanical plate of a fig branch: full branch centre, with a dissected fruit cross-section and a single leaf detail arranged around it. Fine stippled shading, muted natural colour, aged cream paper, small unobtrusive numbered labels.
```

`seed: 1395552785`

### Noir spot illustration

<img src="images/illustration-010.webp" width="420" alt="Noir spot illustration">

**Prompt**

```text
A small spot illustration in high-contrast black and white: a hand pushing open a frosted glass office door, silhouetted venetian blind shadows falling across it. Pure black and pure white only, no midtones, shapes reading instantly at thumbnail size.
```

`seed: 662846866`

### Editorial: the commute

<img src="images/illustration-011.webp" width="420" alt="Editorial: the commute">

**Prompt**

```text
An editorial illustration about commuting: a figure rendered as a folded paper boat drifting down a river of grey office windows. Two colours plus black, screenprint grain, large areas of untouched paper.
```

`seed: 971992746`

### Cyanotype fern

<img src="images/illustration-012.webp" width="420" alt="Cyanotype fern">

**Prompt**

```text
A single fern frond in the manner of a cyanotype photogram — Prussian blue ground, the frond rendered as a soft white silhouette with slight halation at the edges. Uneven wash and paper texture visible.
```

`seed: 403745806`

### Scratchboard owl

<img src="images/illustration-013.webp" width="420" alt="Scratchboard owl">

**Prompt**

```text
A barn owl rendered in scratchboard: white lines carved from solid black, feather detail built entirely from directional scratches of varying density. No grey, no colour, high drama.
```

`seed: 94561777`

### Isotype-style pictogram set

<img src="images/illustration-014.webp" width="420" alt="Isotype-style pictogram set">

**Prompt**

```text
A set of nine pictograms in the Isotype tradition arranged in a grid: figures, vehicles and buildings reduced to flat black silhouettes with uniform stroke logic. No outlines, no detail, instantly legible at any size.
```

`seed: 1365362645`

### Watercolour harbour, wet-in-wet

<img src="images/illustration-015.webp" width="420" alt="Watercolour harbour, wet-in-wet">

**Prompt**

```text
A small harbour at low tide painted wet-in-wet so the sky and water bleed into each other with hard drying edges where the paint pooled. Boats reduced to a few loaded brushstrokes. Muted ochre and slate.
```

`seed: 1827344974`

### Comic panel, chiaroscuro

<img src="images/illustration-016.webp" width="420" alt="Comic panel, chiaroscuro">

**Prompt**

```text
A single comic panel: a figure descending a stairwell lit by one bare bulb, drawn in heavy brush-and-ink chiaroscuro with large solid blacks and minimal hatching. No panel border, no text.
```

`seed: 235666898`

### Mid-century travel poster

<img src="images/illustration-017.webp" width="420" alt="Mid-century travel poster">

**Prompt**

```text
A mid-century travel poster for a fictional coastal town: flat colour blocks, simplified geometry, a lighthouse and cliff reduced to three shapes, screenprint texture and one warm accent against cool tones. No text.
```

`seed: 1377917160`

### Anatomical study, red chalk

<img src="images/illustration-018.webp" width="420" alt="Anatomical study, red chalk">

**Prompt**

```text
An anatomical study of a human hand in red chalk on toned paper, in the manner of a Renaissance sketchbook — construction lines left visible, several overlapping attempts at the thumb on the same sheet.
```

`seed: 221852696`


## reference-sheet

_Character reference sheets and turnarounds_

### Reference sheet — establishing

<img src="images/reference-sheet-001.webp" width="420" alt="Reference sheet — establishing">

**Prompt**

```text
Character reference sheet for a woman in her sixties: silver hair cut short, a small crescent scar above the right eyebrow, wire-frame glasses, a heavy navy fisherman's sweater. Three views on one sheet — front, three-quarter, profile — consistent proportions, neutral grey background, even light.
```

`seed: 1453254312`

> Generate this first and use it as the reference for character-002 through 005.


## isometric-3d

_Isometric scenes, dioramas, game-ready assets_

### Isometric repair shop

<img src="images/isometric-3d-001.webp" width="420" alt="Isometric repair shop">

**Prompt**

```text
A small isometric diorama of a bicycle repair shop with the front wall removed: workbench, wheel truing stand, parts bins, a bike upside down on a stand. True isometric projection with no perspective convergence, soft clay-render materials, single warm key light from upper left, floating on a plain background.
```

`seed: 1886079203`

### Isometric server room

<img src="images/isometric-3d-002.webp" width="420" alt="Isometric server room">

**Prompt**

```text
Isometric cutaway of a small server room: two racks with visible cable management, an overhead cable tray, a floor-standing UPS, and a portable AC unit. Cool blue LED accents against neutral grey hardware. Clean edges, ambient occlusion in the corners, no text on the equipment.
```

`seed: 1075533955`

### Game asset — modular tiles

<img src="images/isometric-3d-003.webp" width="420" alt="Game asset — modular tiles">

**Prompt**

```text
A sheet of six modular isometric floor and wall tiles for a game: stone floor, cracked stone floor, wooden floor, plain wall, wall with a doorway, wall with a barred window. Consistent lighting angle and tile dimensions across all six so they tessellate. Flat background, evenly spaced grid.
```

`seed: 1357449396`

### Low-poly island

<img src="images/isometric-3d-004.webp" width="420" alt="Low-poly island">

**Prompt**

```text
A low-poly floating island: faceted terrain with visible flat triangles, a single stylised pine, a waterfall spilling from the underside into nothing. Hard-edged shading with no smoothing, saturated but limited palette, three-quarter isometric view against a pale gradient.
```

`seed: 1882712822`

### Exploded isometric — camera

<img src="images/isometric-3d-005.webp" width="420" alt="Exploded isometric — camera">

**Prompt**

```text
An exploded isometric view of a 35mm film camera, components separated vertically along a single axis: body, lens elements, shutter assembly, film back, winding mechanism. Consistent spacing, thin grey guide lines connecting the parts, matte technical rendering.
```

`seed: 1583709833`

### Isometric coffee bar

<img src="images/isometric-3d-006.webp" width="420" alt="Isometric coffee bar">

**Prompt**

```text
An isometric cutaway of a small coffee bar: espresso machine, grinder, pastry case, two stools and a back shelf of cups. True isometric with no perspective convergence, soft clay materials, single warm key from upper left, floating on a plain ground.
```

`seed: 882577384`

### Isometric printing workshop

<img src="images/isometric-3d-007.webp" width="420" alt="Isometric printing workshop">

**Prompt**

```text
Isometric diorama of a letterpress workshop with the front wall removed: a platen press, type cases, an inking slab and drying racks with sheets hanging. Consistent 30-degree axes, matte materials, ambient occlusion in the corners.
```

`seed: 1975246446`

### Low-poly desert canyon

<img src="images/isometric-3d-008.webp" width="420" alt="Low-poly desert canyon">

**Prompt**

```text
A low-poly desert canyon section: faceted rock strata in graduated ochre bands, a dry riverbed, two stylised saguaro. Hard-edged flat shading with no smoothing, three-quarter isometric against a pale gradient.
```

`seed: 1391597167`

### Exploded isometric — bicycle hub

<img src="images/isometric-3d-009.webp" width="420" alt="Exploded isometric — bicycle hub">

**Prompt**

```text
An exploded isometric view of a bicycle rear hub, components separated along the axle: axle, bearings, freehub body, cassette spacer, end caps. Even spacing, thin grey guide lines, matte technical rendering, no text.
```

`seed: 226111579`

### Isometric rooftop garden

<img src="images/isometric-3d-010.webp" width="420" alt="Isometric rooftop garden">

**Prompt**

```text
Isometric rooftop garden: raised beds, a small greenhouse, water butt, folding chairs and a ventilation stack. Plants stylised as simple massed forms. Soft top light, gentle shadows, floating on a plain background.
```

`seed: 1496030377`


## editing

_Image-to-image edits whose source is another entry in this catalog_

### Relight this coastline

<img src="images/editing-001.webp" width="420" alt="Relight this coastline">

**Prompt**

```text
Relight this coastline: replace the flat overcast with hard low-angle late afternoon sun from frame right, casting long shadows across the basalt. Keep the rock placement, horizon line and framing identical.
```

_Image-to-image from **Overcast coastline, long exposure** ([`photography-006`](#overcast-coastline-long-exposure)) in this repo · `strength: 0.55`_

`seed: 364022812`

> Source is photography-006 in this repo, so the edit is reproducible from a clone.

### Keep this corridor's geometry and perspective exactly. Chang

<img src="images/editing-002.webp" width="420" alt="Keep this corridor's geometry and perspective exactly. Chang">

**Prompt**

```text
Keep this corridor's geometry and perspective exactly. Change only the time and mood: warm amber emergency lighting instead of cold fluorescents, one light source at the far end, everything nearer falling into shadow.
```

_Image-to-image from **Cold-lit surgical corridor** ([`photography-003`](#cold-lit-surgical-corridor)) in this repo · `strength: 0.5`_

`seed: 1459264371`

> Source is photography-003 in this repo, so the edit is reproducible from a clone.

### Re-render these terraced fields as a gouache painting with v

<img src="images/editing-003.webp" width="420" alt="Re-render these terraced fields as a gouache painting with v">

**Prompt**

```text
Re-render these terraced fields as a gouache painting with visible brush texture and chalky opacity. Every terrace contour stays in exactly the same position; only the medium changes.
```

_Image-to-image from **Aerial: terraced rice fields** ([`photography-009`](#aerial-terraced-rice-fields)) in this repo · `strength: 0.6`_

`seed: 583476278`

> Source is photography-009 in this repo, so the edit is reproducible from a clone.

### Recolour this woodblock wave to a dusk palette — deep violet

<img src="images/editing-005.webp" width="420" alt="Recolour this woodblock wave to a dusk palette — deep violet">

**Prompt**

```text
Recolour this woodblock wave to a dusk palette — deep violet water, salmon sky, warm cream foam. Keep every keyblock outline and flat colour field boundary exactly where it is.
```

_Image-to-image from **Woodblock wave study** ([`illustration-004`](#woodblock-wave-study)) in this repo · `strength: 0.55`_

`seed: 2083277726`

> Source is illustration-004 in this repo, so the edit is reproducible from a clone.

### Blueprint version of the exploded camera

<img src="images/editing-008.webp" width="420" alt="Blueprint version of the exploded camera">

**Prompt**

```text
Re-render this exploded camera diagram as a cyanotype blueprint: white line work on Prussian blue, every component in exactly the same position and spacing.
```

_Image-to-image from **Exploded isometric — camera** ([`isometric-3d-005`](#exploded-isometric--camera)) in this repo · `strength: 0.6`_

`seed: 1652457598`


## portrait

_Profile pictures and avatars — the single most requested category in every prompt catalog measured_

### Window-light portrait, 85mm

<img src="images/portrait-001.webp" width="420" alt="Window-light portrait, 85mm">

**Prompt**

```text
A portrait of a woman in her thirties beside a north-facing window, 85mm at f/1.8, soft directional daylight falling across one side of the face and the other dropping into gentle shadow. Natural skin texture with visible pores, no retouching, catchlight in both eyes. Charcoal wool sweater, plain warm grey wall behind, shallow depth of field.
```

`seed: 1613165866`

### High-contrast studio, single hard light

<img src="images/portrait-002.webp" width="420" alt="High-contrast studio, single hard light">

**Prompt**

```text
Studio portrait of a man in his forties, single hard light high and to camera left, deep shadow filling the right of the face, black seamless background. Sharp specular highlight on the cheekbone, close-cropped beard, direct eye contact with the lens. Medium format look, 110mm equivalent.
```

`seed: 1110166560`

### Golden hour backlit, rim light

<img src="images/portrait-003.webp" width="420" alt="Golden hour backlit, rim light">

**Prompt**

```text
Backlit outdoor portrait at golden hour, sun directly behind the subject creating a bright rim along the hair and shoulders, face lifted by soft bounce. Warm haze, out-of-focus grass and fence line behind. Linen shirt, relaxed expression, 135mm compression, f/2.
```

`seed: 648134594`

### Overcast environmental portrait

<img src="images/portrait-004.webp" width="420" alt="Overcast environmental portrait">

**Prompt**

```text
Environmental portrait of a woodworker standing in her shop doorway under flat overcast light, sawdust on a canvas apron, hands relaxed at her sides. The shop interior falls off into darkness behind her. 35mm, waist up, documentary framing with the doorframe as a natural border.
```

`seed: 1794897089`

### Portra 400 candid, mixed indoor light

<img src="images/portrait-005.webp" width="420" alt="Portra 400 candid, mixed indoor light">

**Prompt**

```text
Candid indoor portrait on Kodak Portra 400, a man laughing mid-conversation at a kitchen table, tungsten lamp warm on one side and cool window light on the other. Visible film grain, soft halation on the highlights, slightly warm cast. 50mm, handheld, not looking at the camera.
```

`seed: 1126231015`

### Painterly oil portrait, chiaroscuro

<img src="images/portrait-007.webp" width="420" alt="Painterly oil portrait, chiaroscuro">

**Prompt**

```text
An oil painting portrait in the chiaroscuro tradition, three-quarter view, single warm light source from upper left, background falling to near black. Visible brushwork in the flesh tones, glazed shadows, muted earth palette of ochre, umber and lead white. Not photorealistic — the paint should be visible.
```

`seed: 1461986812`

### Black and white, harsh noon sun

<img src="images/portrait-009.webp" width="420" alt="Black and white, harsh noon sun">

**Prompt**

```text
Black and white portrait shot in harsh overhead noon sun, deep shadows in the eye sockets and under the nose, strong contrast, grain pushed. Subject squinting slightly, sweat on the forehead, plain concrete wall behind. Tri-X pushed to 1600, 35mm.
```

`seed: 1915439531`

### Charcoal drawing on toned paper

<img src="images/portrait-011.webp" width="420" alt="Charcoal drawing on toned paper">

**Prompt**

```text
A charcoal portrait drawn on mid-grey toned paper, white chalk for the highlights, compressed charcoal for the darks, the paper tone doing the mid-values. Loose hatching around the edges, tight rendering only around the eyes. Smudged, worked, visibly hand-made.
```

`seed: 121909817`


## infographic

_Explainer layouts, quote cards, dashboards — text-heavy by design, which is where this model is weakest and most worth documenting_

### Quote card with rule lines

<img src="images/infographic-001.webp" width="420" alt="Quote card with rule lines">

**Prompt**

```text
A minimal quote card layout: the words "MEASURE TWICE" set large in a condensed grotesque, a thin horizontal rule beneath, and "CUT ONCE" smaller and right-aligned below it. Cream background, near-black type, generous margins. Nothing else in the frame.
```

`seed: 662649445`

### Bento grid, four modules

<img src="images/infographic-002.webp" width="420" alt="Bento grid, four modules">

**Prompt**

```text
A bento-box dashboard layout with four rounded rectangular modules of different sizes on a soft grey background. Each module holds a simple abstract chart — one bar, one donut, one sparkline, one large number. Soft shadows, generous padding, one teal accent colour, no legible body text.
```

`seed: 1870145278`

### Cutaway diagram with leader lines

<img src="images/infographic-003.webp" width="420" alt="Cutaway diagram with leader lines">

**Prompt**

```text
A technical cutaway of a thermos flask, drawn as a clean line diagram with the interior layers visible, thin leader lines pointing out from four components to empty label positions at the edges. No text on the labels — just the lines and the dots. White background, single ink weight.
```

`seed: 2045906439`

### Vintage patent drawing

<img src="images/infographic-005.webp" width="420" alt="Vintage patent drawing">

**Prompt**

```text
A vintage patent illustration of a folding bicycle, black ink line work on aged off-white paper, hatched shading, numbered reference marks beside the components, a ruled border around the sheet. Figure numbers only, no descriptive text. The aesthetic of a 1920s patent office filing.
```

`seed: 1151604106`

### Weather card, single glyph

<img src="images/infographic-006.webp" width="420" alt="Weather card, single glyph">

**Prompt**

```text
A weather card: a large simple cloud-and-rain glyph centred, the numerals "14°" beneath it in a geometric sans, and nothing else. Deep blue gradient background, white elements, soft outer glow on the glyph. Square, app-icon proportions.
```

`seed: 487662832`

### Timeline ribbon, five markers

<img src="images/infographic-008.webp" width="420" alt="Timeline ribbon, five markers">

**Prompt**

```text
A horizontal timeline drawn as a flat ribbon curving gently across the frame, five circular markers spaced along it, alternating above and below, each marker containing a single simple icon. One accent colour against off-white, plenty of empty space. No text.
```

`seed: 1089997705`

### Comparison table, two columns

<img src="images/infographic-009.webp" width="420" alt="Comparison table, two columns">

**Prompt**

```text
A clean two-column comparison layout, left column headed "BEFORE" and right headed "AFTER", each column a stack of four rounded rows with a check or cross glyph and a short blank bar where text would sit. Light background, green ticks, red crosses, hairline dividers.
```

`seed: 536645071`

### Isometric process, three stages

<img src="images/infographic-010.webp" width="420" alt="Isometric process, three stages">

**Prompt**

```text
Three isometric blocks arranged diagonally across the frame representing stages of a process, connected by thick arrows, each block a simplified object — a box, a gear, a package. Flat colour with a single light source, long soft shadows, pastel palette, white background.
```

`seed: 2043998615`


## collectible

_Figurines, pins, keycaps, trading cards — physical-object mockups_

### Vinyl figure in blister pack

<img src="images/collectible-001.webp" width="420" alt="Vinyl figure in blister pack">

**Prompt**

```text
A stylised vinyl collectible figure of a small astronaut sealed in a blister pack against a printed cardboard backer, shot straight on under even studio light. The plastic bubble catches a soft reflection. Matte figure finish, chunky proportions, oversized helmet. The backer is a flat two-colour print.
```

`seed: 641600971`

### Enamel pin on denim

<img src="images/collectible-002.webp" width="420" alt="Enamel pin on denim">

**Prompt**

```text
A hard enamel pin shaped like a crescent moon with a small star, gold plating between the colour fields, pinned to indigo denim. Macro, shallow depth of field, raking light picking out the polished metal ridges and the slight dome of the enamel.
```

`seed: 317255029`

### Knitted plush on shelf

<img src="images/collectible-005.webp" width="420" alt="Knitted plush on shelf">

**Prompt**

```text
A hand-knitted plush fox sitting on a pale wooden shelf, chunky visible stitches in rust and cream yarn, slightly uneven ears, embroidered eyes. Soft window light from the left, plain white wall behind, shallow depth of field.
```

`seed: 1717706071`

### Die-cast model on turntable

<img src="images/collectible-006.webp" width="420" alt="Die-cast model on turntable">

**Prompt**

```text
A 1:64 die-cast model of a boxy 1980s estate car on a black acrylic turntable, three-quarter front view, studio strip lights reflected in the paint as two long soft highlights. Rubber tyres, printed number plate, tiny visible casting seam along the roof.
```

`seed: 161380541`

### Resin diorama in a jar

<img src="images/collectible-007.webp" width="420" alt="Resin diorama in a jar">

**Prompt**

```text
A miniature diorama sealed inside a clear glass jar: a tiny pine forest on a mossy hill with a single lit cabin window, cast in clear resin that reads as still water at the base. Backlit so the resin glows, everything else in shadow. Macro, dark background.
```

`seed: 506403015`


## stationery

_Cards, letterheads, packaging inserts_

### Letterpress card, deep impression

<img src="images/stationery-001.webp" width="420" alt="Letterpress card, deep impression">

**Prompt**

```text
A letterpress business card photographed at a raking angle so the deep impression of the type casts visible shadow in the cotton stock. The card reads "NORTHFIELD & CO" in a small caps serif with a thin rule beneath. Ecru paper, single black ink, deckled edge on one side.
```

`seed: 1926545409`

### Wax seal on kraft envelope

<img src="images/stationery-002.webp" width="420" alt="Wax seal on kraft envelope">

**Prompt**

```text
A deep red wax seal pressed with a simple monogram, closing the flap of a kraft paper envelope on a dark wood surface. Warm side light, the wax showing the ridge and slight overflow of a real pour. Shallow depth of field, envelope corner in frame.
```

`seed: 444300041`

### Notebook flat lay, ruled paper

<img src="images/stationery-003.webp" width="420" alt="Notebook flat lay, ruled paper">

**Prompt**

```text
An open notebook flat lay on a linen surface, ruled cream pages, a fountain pen resting in the gutter, a small brass paperclip at the corner. Soft even overhead light, no harsh shadows, muted palette. The pages are blank — no writing.
```

`seed: 1719173423`

### Shipping label on parcel

<img src="images/stationery-004.webp" width="420" alt="Shipping label on parcel">

**Prompt**

```text
A brown paper parcel tied with cotton twine, a plain white shipping label affixed at a slight angle reading "FRAGILE" in bold condensed capitals with a thick black border. Overhead studio light, visible paper fibre and the shadow line under the twine.
```

`seed: 1043227084`

### Ticket stub, torn edge

<img src="images/stationery-005.webp" width="420" alt="Ticket stub, torn edge">

**Prompt**

```text
A torn ticket stub on a dark surface, letterpress-printed in two colours with "ADMIT ONE" across the middle and a perforated edge where the other half was removed. Aged card stock, slight foxing, one corner soft with wear. Macro, single light from the left.
```

`seed: 1333487198`

### Rubber stamp impression

<img src="images/stationery-006.webp" width="420" alt="Rubber stamp impression">

**Prompt**

```text
A rubber stamp impression of the word "PAID" struck in red ink at a slight angle on an off-white document, deliberately uneven — heavier on one side, a gap where the rubber lifted. The wooden stamp itself resting beside it, out of focus. Overhead, flat light.
```

`seed: 2044996526`


## food

_Food and drink, studio and in-context_

### Cut sourdough loaf, side light

<img src="images/food-001.webp" width="420" alt="Cut sourdough loaf, side light">

**Prompt**

```text
A sourdough loaf cut in half on a floured board, hard side light from the left raking across the open crumb so every hole casts its own shadow. Blistered dark crust, flour dusting the surface, a serrated knife just out of the frame edge. Shot at f/8, tight.
```

`seed: 207887450`

### Ramen bowl, overhead steam

<img src="images/food-002.webp" width="420" alt="Ramen bowl, overhead steam">

**Prompt**

```text
An overhead shot of a ramen bowl on dark wood, soft-boiled egg halved and glossy, nori standing at the edge, chopped scallion scattered. Steam rising and catching a backlight. Deep tonkotsu broth, visible fat droplets, condensation on the rim of the bowl.
```

`seed: 996431689`

### Citrus cross-sections on marble

<img src="images/food-004.webp" width="420" alt="Citrus cross-sections on marble">

**Prompt**

```text
Halved citrus fruits arranged on white marble, shot straight down under a large diffuse source. Blood orange, grapefruit, lime, lemon. Juice beading on the cut faces, translucent segments, a few seeds visible. Cool, clean, high key, no props.
```

`seed: 1002826123`

### Cast iron steak, hard rim light

<img src="images/food-005.webp" width="420" alt="Cast iron steak, hard rim light">

**Prompt**

```text
A steak resting in a cast iron pan, dark crust with visible sear marks, one hard light from behind creating a bright rim along the top edge and rendering the rest in deep shadow. Butter foaming at the base, thyme sprigs, tongs at the frame edge.
```

`seed: 752325181`

### Ice cream melting, tight macro

<img src="images/food-006.webp" width="420" alt="Ice cream melting, tight macro">

**Prompt**

```text
Macro of a scoop of pistachio ice cream beginning to melt on a ceramic plate, one drip running down and pooling. Visible nut fragments and ice crystals, cold blue-white light, condensation on the plate. Extremely shallow depth of field.
```

`seed: 1757822826`

### Market vegetable stall, overcast

<img src="images/food-007.webp" width="420" alt="Market vegetable stall, overcast">

**Prompt**

```text
A market stall of root vegetables under flat overcast light, mud still on the carrots and beetroot, crates stacked at angles, a canvas awning cutting the top of the frame. Documentary, 35mm, colours slightly desaturated by the grey sky.
```

`seed: 1110593834`

### Layer cake cross-section

<img src="images/food-008.webp" width="420" alt="Layer cake cross-section">

**Prompt**

```text
A slice removed from a four-layer cake so the cross-section faces camera, buttercream between each layer, crumb visible and slightly moist. Even soft light, pale pink background, cake stand edge in frame. Straight on, symmetrical.
```

`seed: 1632613977`

### Whisky glass, single hard source

<img src="images/food-009.webp" width="420" alt="Whisky glass, single hard source">

**Prompt**

```text
A cut crystal glass of whisky on dark slate, a single hard light behind and to the right throwing the cut facets into bright caustics on the stone. Large clear ice sphere, amber liquid, everything else black. Product-grade, no props.
```

`seed: 1133820066`

### Dumplings in a bamboo steamer

<img src="images/food-010.webp" width="420" alt="Dumplings in a bamboo steamer">

**Prompt**

```text
Open bamboo steamer of pleated dumplings, translucent wrappers showing the filling through, steam still rising. Warm overhead light, a second closed steamer stacked beneath, dark table. Slight top-down angle, shallow focus falling off at the back.
```

`seed: 1310175144`


## interior

_Rooms, architecture, spatial light_

### Sunlit reading corner

<img src="images/interior-001.webp" width="420" alt="Sunlit reading corner">

**Prompt**

```text
A reading corner in late afternoon: a worn leather armchair, a floor lamp switched off, low sun coming through a tall window and throwing a hard trapezoid of light across the floorboards and up the wall. Dust in the beam. Wide, 24mm, no people.
```

`seed: 633029565`

### Concrete stairwell, top light

<img src="images/interior-002.webp" width="420" alt="Concrete stairwell, top light">

**Prompt**

```text
A brutalist concrete stairwell shot upward, daylight entering from a skylight far above and falling off with distance. Board-formed concrete texture, steel handrail, deep shadow in the lower flights. Symmetrical composition, ultra-wide.
```

`seed: 1168418123`

### Kitchen at blue hour

<img src="images/interior-003.webp" width="420" alt="Kitchen at blue hour">

**Prompt**

```text
A kitchen at blue hour, under-cabinet lights the only warm source, cool blue window light balancing it from the left. Marble worktop, a single glass left out, everything tidy. Mixed colour temperature held rather than corrected. Tripod, long exposure.
```

`seed: 1981161439`

### Empty gallery room

<img src="images/interior-004.webp" width="420" alt="Empty gallery room">

**Prompt**

```text
An empty white gallery room with a polished concrete floor, track lighting pointing at bare walls, one doorway leading to a darker second room. No artwork, no people. Even diffuse light, straight-on one-point perspective, 28mm.
```

`seed: 1318705704`

### Attic workshop, north light

<img src="images/interior-005.webp" width="420" alt="Attic workshop, north light">

**Prompt**

```text
An attic workshop under a sloping roof with a north-facing skylight, workbench cluttered with hand tools, sawdust on the floor, exposed rafters. Soft even daylight with no direct sun. Warm wood tones, slight haze, 35mm.
```

`seed: 613896431`

### Hotel corridor, receding lights

<img src="images/interior-006.webp" width="420" alt="Hotel corridor, receding lights">

**Prompt**

```text
A long hotel corridor with identical doors receding to a vanishing point, wall sconces at regular intervals creating a rhythm of pools of light on patterned carpet. Slightly wide, dead centre, symmetrical. Nobody in frame.
```

`seed: 965972945`

### Greenhouse interior, humid light

<img src="images/interior-007.webp" width="420" alt="Greenhouse interior, humid light">

**Prompt**

```text
Inside a Victorian glasshouse, wrought iron ribs overhead, condensation on the panes diffusing the sunlight into a soft glow. Palms and ferns crowding a central path, terracotta pots, water on the flagstones. Humid, green, slightly overexposed.
```

`seed: 1871087603`

### Japanese tatami room

<img src="images/interior-008.webp" width="420" alt="Japanese tatami room">

**Prompt**

```text
A tatami room with shoji screens filtering daylight into an even soft wash, a low wooden table, one cushion, an alcove with a single branch in a vase. Nothing else. Straight on, symmetrical, muted natural palette.
```

`seed: 1875634416`

### Basement server room

<img src="images/interior-009.webp" width="420" alt="Basement server room">

**Prompt**

```text
A basement server room lit only by rack indicator LEDs and one open cabinet door spilling white light, cable bundles running overhead in trays, polished raised floor reflecting the glow. Cold, blue-green, long exposure, nobody present.
```

`seed: 769155750`

### Loft under renovation

<img src="images/interior-010.webp" width="420" alt="Loft under renovation">

**Prompt**

```text
A loft mid-renovation: plaster dust, a stepladder, plastic sheeting over a window softening the light, bare brick where the plaster has come off, exposed joists. Work lights on stands casting hard overlapping shadows. Documentary, wide.
```

`seed: 736283544`


## pattern

_Repeating surface design — textile, wallpaper, wrapping_

### Botanical block print repeat

<img src="images/pattern-001.webp" width="420" alt="Botanical block print repeat">

**Prompt**

```text
A seamless botanical repeat in the style of a hand-carved block print: fern fronds and seed heads in dark indigo on unbleached linen, slight registration wobble and visible ink texture where the block pressed unevenly. Flat, straight on, edge to edge.
```

`seed: 1576109877`

### Geometric bauhaus repeat

<img src="images/pattern-002.webp" width="420" alt="Geometric bauhaus repeat">

**Prompt**

```text
A seamless geometric pattern of circles, quarter-circles and thin rules in primary red, blue, yellow and black on cream, arranged on a strict grid. Flat vector, no shading, no texture. Fills the frame edge to edge with no border.
```

`seed: 1026790550`

### Marbled paper, combed

<img src="images/pattern-003.webp" width="420" alt="Marbled paper, combed">

**Prompt**

```text
Traditional combed marbled paper: teal, ochre and oxblood pigments drawn into a regular feathered comb pattern on a pale ground, with the fine veining of real size-bath marbling. Fills the frame, no border, no paper edge visible.
```

`seed: 1341762699`

### Terrazzo surface

<img src="images/pattern-004.webp" width="420" alt="Terrazzo surface">

**Prompt**

```text
A terrazzo surface shot flat and straight down: irregular chips of marble in sage, terracotta and charcoal set into a warm off-white binder, polished so each chip has a slight sheen. Even lighting, no shadows, fills the frame.
```

`seed: 1380217993`

### Art deco fan repeat

<img src="images/pattern-005.webp" width="420" alt="Art deco fan repeat">

**Prompt**

```text
A seamless art deco pattern of overlapping fan shapes in gold on deep green, thin gold outlines, stepped scallops, strict horizontal rows. Flat, screen-print feel, no gradients. Edge to edge, no border.
```

`seed: 1139303172`

### Woodgrain, quarter sawn

<img src="images/pattern-006.webp" width="420" alt="Woodgrain, quarter sawn">

**Prompt**

```text
A close, flat photograph of quarter-sawn oak, the medullary rays showing as pale flecks across straight grain lines. Even soft light, no shadows, no edges of the board visible. Filling the frame like a material swatch.
```

`seed: 1026021497`

### Hand-drawn stripe, wobbly

<img src="images/pattern-007.webp" width="420" alt="Hand-drawn stripe, wobbly">

**Prompt**

```text
A seamless stripe pattern drawn by hand with a brush: uneven vertical stripes in ink blue on off-white, each one varying in width and opacity where the brush ran dry. Visible bristle marks. Flat, edge to edge, no border.
```

`seed: 967510819`

### Cyanotype fern repeat

<img src="images/pattern-008.webp" width="420" alt="Cyanotype fern repeat">

**Prompt**

```text
A seamless repeat of fern silhouettes as a cyanotype photogram — white plant shapes against deep Prussian blue, soft edges where the leaves lifted off the paper, uneven wash in the blue. Fills the frame, no border.
```

`seed: 958813884`


## brand-mark

_Logos and marks. Single short strings, which the typography findings predict is the model's strongest text case_

### Wordmark: HALLOW

<img src="images/brand-mark-001.webp" width="420" alt="Wordmark: HALLOW">

**Prompt**

```text
A wordmark reading exactly "HALLOW" in a high-contrast serif with generous letterspacing, set in near-black on a warm off-white field, centred with a lot of air around it. Nothing else in the frame. Flat, no texture, no effects.
```

`seed: 1564712968`

### Embossed logo on leather

<img src="images/brand-mark-003.webp" width="420" alt="Embossed logo on leather">

**Prompt**

```text
The word "FIELDNOTE" blind-embossed into tan vegetable-tanned leather, raking light from the left so the impression reads entirely through shadow with no ink. Visible leather grain and a slight sheen on the raised edges. Macro, tight crop.
```

`seed: 28931635`

### Neon sign, one word

<img src="images/brand-mark-004.webp" width="420" alt="Neon sign, one word">

**Prompt**

```text
A neon sign reading exactly "OPEN" in warm pink script, mounted on a dark brick wall at night, the glass tubing visible with its supports and the glow spilling onto the brick behind. Slight haze, no other signage in frame.
```

`seed: 221054103`

### Etched brass plate

<img src="images/brand-mark-005.webp" width="420" alt="Etched brass plate">

**Prompt**

```text
A brass plaque etched with "EST 1904" in engraved capitals filled with black, mounted with four visible screws on a weathered stone wall. Patina and verdigris in the recesses, hard afternoon sun raking across at an angle. Macro.
```

`seed: 638748744`

### Foil-stamped logo on box

<img src="images/brand-mark-006.webp" width="420" alt="Foil-stamped logo on box">

**Prompt**

```text
A matte charcoal gift box with the word "ASTER" foil-stamped in copper on the lid, shot at a low three-quarter angle so the foil catches a single highlight and reads dark elsewhere. Soft studio light, seamless grey background.
```

`seed: 204370515`

### Painted ghost sign

<img src="images/brand-mark-007.webp" width="420" alt="Painted ghost sign">

**Prompt**

```text
A faded painted ghost sign on an old brick wall reading "COOPERAGE" in tall condensed capitals, the paint worn back to brick in patches, sun-bleached from red to dusty pink. Straight on, flat afternoon light, no other text.
```

`seed: 757705299`

### Sandblasted glass door

<img src="images/brand-mark-008.webp" width="420" alt="Sandblasted glass door">

**Prompt**

```text
A frosted sandblasted panel on a glass door reading "STUDIO 4", the letters clear against the frosted ground, a blurred interior visible through them. Even daylight, brass handle at the frame edge, straight on.
```

`seed: 2068017137`


## miniature

_Tilt-shift, dioramas, scale models of places_

### Tilt-shift harbour

<img src="images/miniature-001.webp" width="420" alt="Tilt-shift harbour">

**Prompt**

```text
A harbour seen from high above with a strong tilt-shift effect: a narrow band of sharp focus across the quay and everything above and below thrown into heavy blur, colours pushed to high saturation so the boats and containers read as plastic toys.
```

`seed: 707503180`

### Model railway station

<img src="images/miniature-002.webp" width="420" alt="Model railway station">

**Prompt**

```text
A finely detailed HO-scale model railway station on a layout, tiny figures on the platform, static grass and lichen trees, a locomotive at the edge of frame. Shot at platform height with shallow depth of field so the scale reads ambiguous.
```

`seed: 1975224634`

### Paper-craft city block

<img src="images/miniature-003.webp" width="420" alt="Paper-craft city block">

**Prompt**

```text
A city block built entirely from folded and cut card: buildings, street trees and a bus, all in muted paper colours with visible fold creases and cut edges. Soft directional light casting clean shadows on a paper ground. Three-quarter view.
```

`seed: 885394300`

### Snow globe interior

<img src="images/miniature-004.webp" width="420" alt="Snow globe interior">

**Prompt**

```text
Looking into a snow globe: a tiny alpine chalet with lit windows on a white base, glitter suspended mid-fall in the water, the glass distorting the background into a soft ring. Dark surround, single warm light source, macro.
```

`seed: 657474403`

### Bonsai on a stand

<img src="images/miniature-005.webp" width="420" alt="Bonsai on a stand">

**Prompt**

```text
A mature bonsai pine in a shallow unglazed pot on a dark wooden stand, moss on the soil, needle detail crisp, shot against a plain grey studio background under soft directional light. The trunk gnarled and wired. Straight on, full tree.
```

`seed: 1743541111`

### Cutaway dollhouse room

<img src="images/miniature-006.webp" width="420" alt="Cutaway dollhouse room">

**Prompt**

```text
A dollhouse room seen with its fourth wall removed: miniature furniture, a rug, a tiny lamp actually lit, patterned wallpaper. Shot straight on so it reads as a stage set. Warm practical light from inside, cool ambient from outside.
```

`seed: 1895175876`

### Sand table battlefield

<img src="images/miniature-007.webp" width="420" alt="Sand table battlefield">

**Prompt**

```text
A wargaming sand table from a low angle: sculpted terrain, lichen scrub, painted infantry figures in loose formation behind a ridge, a ruined building of foam board. Overcast studio light, shallow focus on the front rank.
```

`seed: 568280305`

### Miniature food, macro

<img src="images/miniature-008.webp" width="420" alt="Miniature food, macro">

**Prompt**

```text
A miniature clay breakfast — fried egg, toast, tomato — on a plate the size of a coin, held between finger and thumb for scale at the edge of frame. Extreme macro, the polymer clay texture and tool marks visible up close.
```

`seed: 1295431062`


## coloring-page

_Uncoloured line art for printing_

### Coloring page: garden scene

<img src="images/coloring-page-001.webp" width="420" alt="Coloring page: garden scene">

**Prompt**

```text
A children's coloring page: a garden scene with a watering can, sunflowers, a snail and a butterfly, drawn as clean uniform black outlines on pure white with no shading, no grey, no fill. Thick friendly lines, generous white areas to colour in.
```

`seed: 230163006`

### Coloring page: sea creatures

<img src="images/coloring-page-002.webp" width="420" alt="Coloring page: sea creatures">

**Prompt**

```text
A children's coloring page of sea creatures — an octopus, two fish, a starfish and seaweed — as bold even black outlines on white, no shading or hatching anywhere, simple shapes, large enclosed areas. Nothing filled in.
```

`seed: 927169882`

### Coloring page: mandala

<img src="images/coloring-page-003.webp" width="420" alt="Coloring page: mandala">

**Prompt**

```text
A symmetrical mandala coloring page: concentric rings of petals, leaves and geometric motifs in fine even black line on white, eightfold symmetry, every region closed so it can be coloured. No fills, no grey, no shading.
```

`seed: 690682918`

### Coloring page: dinosaur

<img src="images/coloring-page-004.webp" width="420" alt="Coloring page: dinosaur">

**Prompt**

```text
A friendly cartoon stegosaurus for a children's coloring book, thick black outlines only on white, simple ferns behind it, no shading, no texture, no fill. Rounded shapes suitable for a young child with crayons.
```

`seed: 343603193`

### Coloring page: cityscape

<img src="images/coloring-page-005.webp" width="420" alt="Coloring page: cityscape">

**Prompt**

```text
A coloring page of a stylised city skyline with varied building shapes, windows drawn as simple rectangles, a bridge and a few clouds, all as clean uniform black outlines on white. No shading, no solid black areas, no fill.
```

`seed: 797917670`

### Coloring page: teacup still life

<img src="images/coloring-page-006.webp" width="420" alt="Coloring page: teacup still life">

**Prompt**

```text
A coloring page still life: a teacup on a saucer, a teapot, a slice of cake on a plate and a folded napkin, drawn in even black outline on white with decorative patterns on the china left as empty outlines to colour. No shading.
```

`seed: 1880531119`


## ui

_App and web interface mockups. Included as a deliberate test of the multi-string text limit, not because it is expected to work_

### Login screen

<img src="images/ui-004.webp" width="420" alt="Login screen">

**Prompt**

```text
A minimal login screen: a small logo mark, the heading "Sign in", an email field, a password field, a primary button reading "Continue", and a small link beneath. Centred card on a soft gradient background. Nothing else.
```

`seed: 1367300139`


## stringcount

_A controlled experiment: one nameplate design, one to eight independent strings, everything else held constant_

### Nameplate: 1 string

<img src="images/stringcount-1.webp" width="420" alt="Nameplate: 1 string">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN
```

`seed: 656981461`

### Nameplate: 2 strings

<img src="images/stringcount-2.webp" width="420" alt="Nameplate: 2 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938
```

`seed: 1941926068`

### Nameplate: 3 strings

<img src="images/stringcount-3.webp" width="420" alt="Nameplate: 3 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938 / MODEL 7
```

`seed: 562744296`

### Nameplate: 4 strings

<img src="images/stringcount-4.webp" width="420" alt="Nameplate: 4 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938 / MODEL 7 / SHEFFIELD
```

`seed: 179604082`

### Nameplate: 5 strings

<img src="images/stringcount-5.webp" width="420" alt="Nameplate: 5 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938 / MODEL 7 / SHEFFIELD / SERIAL 4412
```

`seed: 669484398`

### Nameplate: 6 strings

<img src="images/stringcount-6.webp" width="420" alt="Nameplate: 6 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938 / MODEL 7 / SHEFFIELD / SERIAL 4412 / 440 VOLTS
```

`seed: 1597415794`

### Nameplate: 7 strings

<img src="images/stringcount-7.webp" width="420" alt="Nameplate: 7 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938 / MODEL 7 / SHEFFIELD / SERIAL 4412 / 440 VOLTS / 50 CYCLES
```

`seed: 742958406`

### Nameplate: 8 strings

<img src="images/stringcount-8.webp" width="420" alt="Nameplate: 8 strings">

**Prompt**

```text
A stamped brass equipment nameplate riveted to a painted steel machine housing, engraved capitals filled with black, raking light from the left. The plate reads exactly: VULCAN / 1938 / MODEL 7 / SHEFFIELD / SERIAL 4412 / 440 VOLTS / 50 CYCLES / MADE IN ENGLAND
```

`seed: 762332150`


## animal

_Animals and birds, wild and domestic_

### Red fox in frost

<img src="images/animal-001.webp" width="420" alt="Red fox in frost">

**Prompt**

```text
A red fox standing alert in frosted grass at first light, breath visible, low sun catching the guard hairs along its back as a bright rim. 400mm, shallow depth of field, background collapsed to soft ochre. Eye sharp, ears forward.
```

`seed: 1133238396`

### Barn owl in flight, backlit

<img src="images/animal-002.webp" width="420" alt="Barn owl in flight, backlit">

**Prompt**

```text
A barn owl in level flight across an open field at dusk, backlit so the flight feathers glow translucent at the trailing edge. Wings at full extension, head turned toward camera. 1/2000s, dark treeline behind, everything else falling away.
```

`seed: 1363642666`

### Sleeping cat, window light

<img src="images/animal-003.webp" width="420" alt="Sleeping cat, window light">

**Prompt**

```text
A tabby cat asleep on a windowsill in soft afternoon light, one paw over its face, individual whiskers catching the light. Dust motes in the air, the window frame casting a soft edge across the fur. 50mm, f/2, warm and quiet.
```

`seed: 1871088047`

### Highland cow, overcast

<img src="images/animal-004.webp" width="420" alt="Highland cow, overcast">

**Prompt**

```text
A Highland cow facing camera under flat overcast light, long ginger fringe hanging over its eyes and wet at the tips, breath steaming, mud on the muzzle. Moorland behind reduced to grey-green. 200mm, chest up, documentary.
```

`seed: 628225508`

### Koi from above

<img src="images/animal-005.webp" width="420" alt="Koi from above">

**Prompt**

```text
Three koi seen from directly above in dark green water, their white and orange markings the only bright thing in frame, surface ripples distorting the tails. Overcast daylight, no reflections of sky, polarised look.
```

`seed: 652401162`

### Border collie mid-run

<img src="images/animal-006.webp" width="420" alt="Border collie mid-run">

**Prompt**

```text
A border collie at full stretch across short grass, all four feet off the ground, ears flattened, tongue out, mud spraying behind. Panned at 1/250s so the background streaks and the dog stays sharp. Low camera, side on.
```

`seed: 1945170114`

### Elephant skin, macro

<img src="images/animal-007.webp" width="420" alt="Elephant skin, macro">

**Prompt**

```text
Extreme close-up of elephant skin: deep cracked fissures, dried mud in the crevices, a few coarse dark hairs. Hard side light raking across so every fissure casts its own shadow. Fills the frame entirely, no context, almost abstract.
```

`seed: 1410474870`

### Hummingbird at a flower

<img src="images/animal-008.webp" width="420" alt="Hummingbird at a flower">

**Prompt**

```text
A hummingbird hovering at a red trumpet flower, wings blurred to a haze while the body and eye stay sharp, iridescent green throat catching the light. High-speed flash, black background, a single drop of nectar visible.
```

`seed: 87090589`

### Sheep flock in fog

<img src="images/animal-009.webp" width="420" alt="Sheep flock in fog">

**Prompt**

```text
A flock of sheep on a hillside in thick fog, the nearest three sharp and the rest dissolving into grey at increasing distance. Wet wool, no horizon, no sky. Muted, almost monochrome, 135mm compression.
```

`seed: 2100916653`

### Horse in dust, backlit

<img src="images/animal-010.webp" width="420" alt="Horse in dust, backlit">

**Prompt**

```text
A horse turning in a dusty paddock with low sun directly behind, the raised dust glowing gold and the animal reading almost as a silhouette with a bright rim along the neck and mane. Hard contrast, 200mm, dark foreground.
```

`seed: 2049057806`


## landscape

_Land, weather and light at scale_

### Storm light over ridgeline

<img src="images/landscape-001.webp" width="420" alt="Storm light over ridgeline">

**Prompt**

```text
A mountain ridgeline under breaking storm light: dark cloud filling the upper frame, a single shaft of sun striking one slope and leaving the rest in shadow. Wet rock, no people, no path. 70mm, high contrast, cold shadows and warm highlight.
```

`seed: 1853365286`

### Salt flat at dusk

<img src="images/landscape-002.webp" width="420" alt="Salt flat at dusk">

**Prompt**

```text
A cracked salt flat stretching to a flat horizon at dusk, the polygon crust catching low pink light, a thin film of water in the nearest cracks reflecting the sky. Ultra-wide, horizon low, nothing else in frame.
```

`seed: 1866698437`

### Beech wood in mist

<img src="images/landscape-003.webp" width="420" alt="Beech wood in mist">

**Prompt**

```text
A beech wood in early morning mist, pale trunks receding in even ranks until they dissolve, leaf litter deep and orange underfoot, light coming from behind the trees. No sky visible, no path, no people. 85mm, compressed.
```

`seed: 1947533128`

### Basalt columns at low tide

<img src="images/landscape-004.webp" width="420" alt="Basalt columns at low tide">

**Prompt**

```text
Hexagonal basalt columns exposed at low tide, wet and dark, seaweed in the joints, the sea flat and pale behind under overcast light. Shot low so the column tops recede as a stepped surface. Long exposure smoothing the water.
```

`seed: 1022031261`

### Wheat field before rain

<img src="images/landscape-005.webp" width="420" alt="Wheat field before rain">

**Prompt**

```text
A wheat field under a bruised sky just before rain, wind laying the crop in moving waves, one distant line of trees, no buildings. The light green-grey and flat except for one pale gap in the cloud. Wide, horizon on the lower third.
```

`seed: 1820685942`

### Glacier snout, cold light

<img src="images/landscape-006.webp" width="420" alt="Glacier snout, cold light">

**Prompt**

```text
The snout of a glacier meeting grey moraine, deep blue compressed ice visible in the crevasses, meltwater running out from beneath. Flat overcast light, no sun, no sky in frame. Scale ambiguous — no people or objects for reference.
```

`seed: 1365266474`

### Desert dune ridge, first light

<img src="images/landscape-007.webp" width="420" alt="Desert dune ridge, first light">

**Prompt**

```text
A single dune ridge at first light, the windward face lit warm and the lee face in deep blue shadow, the ridgeline running diagonally across the frame with a crisp unbroken edge. Ripples in the sand catching side light. Nothing else.
```

`seed: 1077975326`

### Rice terraces in cloud

<img src="images/landscape-008.webp" width="420" alt="Rice terraces in cloud">

**Prompt**

```text
Flooded rice terraces on a steep hillside with low cloud sitting in the valley below, the water surfaces reflecting a white sky so the terraces read as bright ribbons against dark banks. Overcast, aerial three-quarter view.
```

`seed: 1381739119`

### Frozen lake, cracked ice

<img src="images/landscape-009.webp" width="420" alt="Frozen lake, cracked ice">

**Prompt**

```text
A frozen lake surface shot low and close, cracks radiating and trapped bubbles suspended in the ice, a distant far shore reduced to a thin dark line. Cold blue light, thin snow drifted into the cracks. Ultra-wide, foreground dominant.
```

`seed: 267516027`

### Coastal cliff in gale

<img src="images/landscape-010.webp" width="420" alt="Coastal cliff in gale">

**Prompt**

```text
A coastal cliff in a gale, spray thrown high up the rock face, grass on the clifftop flattened, the sea below white and confused. Grey flat light, no sun. Shot from the clifftop looking along the coast, 35mm, everything wet.
```

`seed: 1122641191`


## fashion

_Garments, textile detail, lookbook and flat lay_

### Wool coat flat lay

<img src="images/fashion-001.webp" width="420" alt="Wool coat flat lay">

**Prompt**

```text
A charcoal wool overcoat laid flat and shot directly overhead on a pale linen surface, sleeves arranged symmetrically, collar open, horn buttons visible. Soft even light, the wool texture and the twill weave both readable. No model, no props.
```

`seed: 1025323172`

### Denim detail, macro

<img src="images/fashion-002.webp" width="420" alt="Denim detail, macro">

**Prompt**

```text
Macro of a selvedge denim seam: the red-line selvedge edge, chain-stitch run-off, copper rivet, and the indigo faded unevenly along the fold. Raking light so the twill diagonal is visible. Extremely shallow depth of field.
```

`seed: 374180050`

### Silk in motion, studio

<img src="images/fashion-003.webp" width="420" alt="Silk in motion, studio">

**Prompt**

```text
A length of oyster-coloured silk thrown into the air in a studio and frozen mid-fall, the fabric catching light along its folds and going translucent where it is single-layered. Black background, one hard light from the right, 1/8000s.
```

`seed: 74128835`

### Knitwear texture close-up

<img src="images/fashion-004.webp" width="420" alt="Knitwear texture close-up">

**Prompt**

```text
Close-up of a hand-knitted Aran sweater: cable panels, moss stitch, and a visible join where the yarn changed. Undyed cream wool with the natural halo of the fibre catching soft side light. Fills the frame, slight depth falloff.
```

`seed: 1554099169`

### Boot on wet cobbles

<img src="images/fashion-005.webp" width="420" alt="Boot on wet cobbles">

**Prompt**

```text
A single worn leather boot standing on wet cobblestones, laces uneven, the toe scuffed pale, welt stitching visible, reflections in the water between the stones. Overcast light, low camera, shallow focus falling off behind.
```

`seed: 2059154957`

### Sunglasses on stone, hard light

<img src="images/fashion-006.webp" width="420" alt="Sunglasses on stone, hard light">

**Prompt**

```text
A pair of tortoiseshell sunglasses resting on warm limestone in hard midday sun, the frame casting a crisp double shadow, the lenses reflecting a slice of blue sky. Product-grade but shot outdoors. Macro, top-down, high contrast.
```

`seed: 1961244750`

### Pleated skirt, wind

<img src="images/fashion-008.webp" width="420" alt="Pleated skirt, wind">

**Prompt**

```text
A pleated midi skirt caught by wind against a plain concrete wall, the pleats opening into a fan and each fold catching a different value of the same colour. Waist down only, hard afternoon side light, sharp shadow on the wall.
```

`seed: 1497786953`


## automotive

_Cars and motorcycles, studio and location_

### Classic coupe, studio strip lights

<img src="images/automotive-001.webp" width="420" alt="Classic coupe, studio strip lights">

**Prompt**

```text
A 1960s coupe in a dark studio with two long overhead strip lights reflected as continuous highlights running the length of the body, three-quarter front view, everything else falling to black. Chrome bumper picking up a hard specular.
```

`seed: 784853870`

### Motorcycle on wet road, panned

<img src="images/automotive-003.webp" width="420" alt="Motorcycle on wet road, panned">

**Prompt**

```text
A motorcycle leaned into a bend on a wet road, panned at 1/60s so the road and hedgerow streak while the bike and rider stay sharp. Spray off the rear tyre, overcast grey light, headlight on. Side on, low angle.
```

`seed: 748778927`

### Engine bay, top-down

<img src="images/automotive-004.webp" width="420" alt="Engine bay, top-down">

**Prompt**

```text
An engine bay shot directly down with the bonnet removed: cam cover, braided lines, alloy castings, a patina of use rather than a show-car polish. Even overcast daylight, no harsh reflections, everything readable.
```

`seed: 1618892058`

### Car interior at night

<img src="images/automotive-005.webp" width="420" alt="Car interior at night">

**Prompt**

```text
A car interior at night from the rear seat, instrument cluster and centre screen the only light sources, rain on the side glass diffusing streetlights into soft orange blobs. Nobody in frame. Long exposure, warm dashboard glow.
```

`seed: 210253850`

### Rally car on gravel

<img src="images/automotive-006.webp" width="420" alt="Rally car on gravel">

**Prompt**

```text
A rally car mid-corner on a gravel stage throwing a wall of stones and dust, all four wheels loaded, mud up the flanks. Forest behind in shadow, hard shaft of sun on the car. 1/1000s, side on, low.
```

`seed: 1191811108`

### Rusting truck in a field

<img src="images/automotive-007.webp" width="420" alt="Rusting truck in a field">

**Prompt**

```text
An abandoned pickup truck sinking into long grass, paint gone to rust and primer, one door open, glass missing. Flat overcast light, no drama, documentary framing at 35mm. Weeds growing through the wheel arches.
```

`seed: 1346029088`

### Headlight macro, water beads

<img src="images/automotive-008.webp" width="420" alt="Headlight macro, water beads">

**Prompt**

```text
Macro of a modern headlight cluster with water beaded across the lens, the LED elements visible as bright points refracted through each droplet. Dark paint around it out of focus. Hard light from above, very shallow focus.
```

`seed: 2093173173`


## exterior

_Buildings from outside — facades, materials, weather_

### Brutalist facade, hard sun

<img src="images/exterior-001.webp" width="420" alt="Brutalist facade, hard sun">

**Prompt**

```text
A brutalist concrete facade in hard afternoon sun, deep window reveals throwing black rectangles of shadow, board-marked concrete texture readable across the whole surface. Straight on, no sky, no people. Slight lens correction.
```

`seed: 2005377678`

### Rain-streaked glass tower

<img src="images/exterior-002.webp" width="420" alt="Rain-streaked glass tower">

**Prompt**

```text
A glass office tower photographed looking up in the rain, the facade reflecting fragments of grey cloud, water streaking down the panels, the grid of mullions receding to a vanishing point. Cold, desaturated, ultra-wide.
```

`seed: 1527311382`

### Terraced houses, low sun

<img src="images/exterior-003.webp" width="420" alt="Terraced houses, low sun">

**Prompt**

```text
A row of brick terraced houses in low winter sun, chimney shadows falling across the roofs opposite, sash windows, a wheelie bin, wet pavement. Documentary, straight on, 35mm, nobody in frame.
```

`seed: 145725328`

### Timber barn, weathered

<img src="images/exterior-004.webp" width="420" alt="Timber barn, weathered">

**Prompt**

```text
A weathered timber barn with silvered boards and a rusted corrugated roof, standing in flat grassland under a wide overcast sky. One door open into darkness. Straight on, symmetrical, horizon low, no other buildings.
```

`seed: 416415737`

### Stone church in fog

<img src="images/exterior-005.webp" width="420" alt="Stone church in fog">

**Prompt**

```text
A small stone church with a square tower half lost in fog, gravestones leaning in the foreground, wet grass, bare trees reduced to grey outlines. No sun, no sky detail, muted almost monochrome. 50mm, quiet.
```

`seed: 2045582615`

### Modernist house at dusk

<img src="images/exterior-006.webp" width="420" alt="Modernist house at dusk">

**Prompt**

```text
A single-storey modernist house at dusk with warm interior light spilling through full-height glazing onto a terrace, the sky still holding deep blue. Flat roof, exposed steel, planting in silhouette. Long exposure, tripod, no people.
```

`seed: 455391691`

### Fire escape shadows

<img src="images/exterior-007.webp" width="420" alt="Fire escape shadows">

**Prompt**

```text
A cast-iron fire escape on a brick wall in hard low sun, its shadow drawn precisely across the brickwork beside it as a second graphic structure. Straight on, flat, no sky. The shadow more legible than the object.
```

`seed: 335239700`

### Coastal lighthouse, gale

<img src="images/exterior-008.webp" width="420" alt="Coastal lighthouse, gale">

**Prompt**

```text
A white lighthouse on a rocky headland in a gale, spray reaching halfway up the tower, grey sea and grey sky nearly the same value. Lamp lit and just visible. Shot from land, 200mm, everything wet and flat-lit.
```

`seed: 1925132923`


## abstract

_Non-representational: fluid, macro, gradient, texture_

### Ink in water

<img src="images/abstract-001.webp" width="420" alt="Ink in water">

**Prompt**

```text
Black ink dispersing in clear water, frozen mid-bloom, tendrils branching into fine filaments against a white backlit ground. High-speed, extremely sharp, no container edges visible. Fills the frame.
```

`seed: 1099275261`

### Oil and water macro

<img src="images/abstract-002.webp" width="420" alt="Oil and water macro">

**Prompt**

```text
Macro of oil beads floating on water over a coloured background, each bead acting as a lens and refracting a different fragment of colour, the beads clustering into a cellular structure. Backlit, no edges, fills the frame.
```

`seed: 52430611`

### Cracked glaze, macro

<img src="images/abstract-003.webp" width="420" alt="Cracked glaze, macro">

**Prompt**

```text
Macro of crazed ceramic glaze: a fine irregular network of cracks over a celadon surface, each crack darkened by age, the glaze pooling thicker in places. Raking light, no edges of the vessel visible. Almost a map.
```

`seed: 801181841`

### Sand ripples, aerial

<img src="images/abstract-005.webp" width="420" alt="Sand ripples, aerial">

**Prompt**

```text
An aerial view straight down onto tidal sand ripples, the pattern branching like a river system, wet sand darker than dry, no horizon and no objects to give scale. Low sun raking so every ridge casts a fine shadow.
```

`seed: 1425727649`

### Torn paper layers

<img src="images/abstract-006.webp" width="420" alt="Torn paper layers">

**Prompt**

```text
Layers of torn coloured paper overlapping, each tear showing the white core of the stock, arranged so the composition reads as strata. Soft even light, subtle shadows between layers, muted palette of ochre, teal and grey.
```

`seed: 2097906804`

### Frost on glass

<img src="images/abstract-007.webp" width="420" alt="Frost on glass">

**Prompt**

```text
Ice crystals growing across a window pane, fern-like branching structures backlit by a cold pale sky, sharp where the crystals are thick and dissolving where they thin. No frame, no view through, fills the entire frame.
```

`seed: 370355428`

### Molten metal pour

<img src="images/abstract-008.webp" width="420" alt="Molten metal pour">

**Prompt**

```text
A stream of molten metal pouring in a dark foundry, sparks arcing away from the stream, the glow lighting nothing but itself. Deep orange to white in the core, everything around it black. Fast shutter freezing the sparks.
```

`seed: 838584990`


## objectcount

_A controlled experiment: one shelf, one object, two to eight of them, everything else held constant_

### Count: 2 eggs

<img src="images/objectcount-2.webp" width="420" alt="Count: 2 eggs">

**Prompt**

```text
Exactly 2 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 1121773227`

### Count: 3 eggs

<img src="images/objectcount-3.webp" width="420" alt="Count: 3 eggs">

**Prompt**

```text
Exactly 3 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 13160654`

### Count: 4 eggs

<img src="images/objectcount-4.webp" width="420" alt="Count: 4 eggs">

**Prompt**

```text
Exactly 4 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 1716350491`

### Count: 5 eggs

<img src="images/objectcount-5.webp" width="420" alt="Count: 5 eggs">

**Prompt**

```text
Exactly 5 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 7277243`

### Count: 6 eggs

<img src="images/objectcount-6.webp" width="420" alt="Count: 6 eggs">

**Prompt**

```text
Exactly 6 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 344187822`

### Count: 7 eggs

<img src="images/objectcount-7.webp" width="420" alt="Count: 7 eggs">

**Prompt**

```text
Exactly 7 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 1044080084`

### Count: 8 eggs

<img src="images/objectcount-8.webp" width="420" alt="Count: 8 eggs">

**Prompt**

```text
Exactly 8 identical white ceramic eggs standing in a row on a dark slate shelf, evenly spaced, shot straight on under soft even light. Plain charcoal wall behind. Nothing else in the frame.
```

`seed: 205379899`


## monogram

_A second look at arbitrary letter pairs, which failed once in batch four_

### Monogram: AE ligature

<img src="images/monogram-002.webp" width="420" alt="Monogram: AE ligature">

**Prompt**

```text
An engraved ligature of the two letters A and E joined into a single form, cut into polished brass with the grooves darkened, macro, raking light. The ligature reads exactly: AE
```

`seed: 1348613049`

### Monogram: HB embossed

<img src="images/monogram-003.webp" width="420" alt="Monogram: HB embossed">

**Prompt**

```text
The two letters H and B side by side, blind-embossed into cream cotton paper, raking light so they read entirely through shadow. Wide letterspacing, high-contrast serif. The impression reads exactly: HB
```

`seed: 1941203383`


## poster

_Poster and cover layouts. Every string is written out in the prompt — a direct test of the batch-four finding_

### Swiss grid concert poster

<img src="images/poster-001.webp" width="420" alt="Swiss grid concert poster">

**Prompt**

```text
A Swiss-style concert poster on a strict grid: the word "KLANG" set very large in a bold grotesque across the upper half, "14 MARCH" beneath it in small caps, and "HALLE 7" bottom right. Red on off-white, one diagonal rule, generous white space. No other text.
```

`seed: 779075243`

### Vintage travel poster

<img src="images/poster-002.webp" width="420" alt="Vintage travel poster">

**Prompt**

```text
A 1930s-style travel poster, flat screen-printed colour, stylised mountains and a lake. The word "ALPINA" arcs across the sky in a geometric sans, and "BY RAIL" sits in a small band at the foot. Muted teal, ochre and cream. No other text.
```

`seed: 927458607`

### Album cover, minimal

<img src="images/poster-003.webp" width="420" alt="Album cover, minimal">

**Prompt**

```text
A square album cover: a single dark circle centred on a warm grey field, the word "LOWLIGHT" set small in the lower left in a light sans, and "SIDE A" in the lower right. Nothing else. Flat, no texture, generous margins.
```

`seed: 1102144654`

### Exhibition poster, type only

<img src="images/poster-005.webp" width="420" alt="Exhibition poster, type only">

**Prompt**

```text
A type-only exhibition poster: "WORKS ON PAPER" set in three stacked lines of a high-contrast serif, filling most of the sheet, with "GALLERY NINE" small and centred beneath. Black on warm white, tight leading, wide margins. No image, no other text.
```

`seed: 1486768439`

### Risograph gig poster

<img src="images/poster-006.webp" width="420" alt="Risograph gig poster">

**Prompt**

```text
A two-colour risograph gig poster in fluorescent pink and blue with visible misregistration and paper texture. The word "STATIC" is set huge and distressed across the centre, with "FRIDAY" beneath it. Halftone dots visible. No other text.
```

`seed: 2144045641`

### Safety notice, industrial

<img src="images/poster-007.webp" width="420" alt="Safety notice, industrial">

**Prompt**

```text
An industrial safety notice printed on a metal plate bolted to a wall: "EYE PROTECTION" in bold condensed capitals on a yellow band, a black triangle warning symbol above it, and "AREA 4" stencilled beneath. Weathered, scratched, hard raking light.
```

`seed: 1652078050`

### Book cover, spine and face

<img src="images/poster-008.webp" width="420" alt="Book cover, spine and face">

**Prompt**

```text
A hardback book standing on a plain surface, three-quarter view so the cover and spine are both visible. The cover reads "THE LONG FIELD" in a modern serif with "E. HALLIDAY" small beneath; the spine repeats "THE LONG FIELD" vertically. Cloth binding, foil-stamped, single warm light.
```

`seed: 2085405029`

### Wine label on bottle

<img src="images/poster-009.webp" width="420" alt="Wine label on bottle">

**Prompt**

```text
A wine bottle shot straight on against a dark ground, the label reading "CLOS MARIN" in an engraved serif with "2019" beneath it and "MIS EN BOUTEILLE" in tiny capitals at the foot. Cream paper label, deep green glass, single soft light from the left.
```

`seed: 278755335`

### Protest placard, hand-lettered

<img src="images/poster-010.webp" width="420" alt="Protest placard, hand-lettered">

**Prompt**

```text
A hand-lettered cardboard placard held up outdoors, the words "MEND IT" painted in thick uneven black brush capitals with "DON'T END IT" smaller beneath. Corrugated board texture, drips, overcast daylight, blurred crowd behind. No other text.
```

`seed: 889409508`


## still-life

_Arranged objects, classical and modern_

### Dutch vanitas

<img src="images/still-life-001.webp" width="420" alt="Dutch vanitas">

**Prompt**

```text
A Dutch vanitas still life: a pewter jug, a half-peeled lemon with the rind spiralling over the table edge, a snuffed candle and a folded cloth, lit from a single high window on the left and falling to deep brown shadow. Oil on panel, visible glazing.
```

`seed: 474373990`

### Tools laid out, top-down

<img src="images/still-life-002.webp" width="420" alt="Tools laid out, top-down">

**Prompt**

```text
A set of woodworking hand tools arranged flat and shot directly overhead on grey linen: a marking gauge, two chisels, a brass-backed saw and a plane. Aligned to an invisible grid, even soft light, patina and use visible on each.
```

`seed: 1498493405`

### Glassware, backlit

<img src="images/still-life-003.webp" width="420" alt="Glassware, backlit">

**Prompt**

```text
Five pieces of clear laboratory glassware of different heights arranged in a line and backlit against a white ground, so each reads as an outline of refraction and caustic. No labels, no liquid, no props. Straight on, symmetrical light.
```

`seed: 81785803`

### Breakfast table, morning sun

<img src="images/still-life-004.webp" width="420" alt="Breakfast table, morning sun">

**Prompt**

```text
A breakfast table in low morning sun: a cafetière, one cup, a torn piece of bread and a folded newspaper, hard light throwing long shadows across a scrubbed pine table. Crumbs, a spill ring, nothing styled. 35mm, slight angle.
```

`seed: 1891948431`

### Ceramics on a shelf

<img src="images/still-life-005.webp" width="420" alt="Ceramics on a shelf">

**Prompt**

```text
Six pieces of studio ceramics on a plain wooden shelf, glazes ranging from matte oatmeal to glossy tenmoku, one piece deliberately turned to show a chipped foot. Soft directional light from the left, plain wall, straight on.
```

`seed: 452847039`

### Dried botanicals in glass

<img src="images/still-life-006.webp" width="420" alt="Dried botanicals in glass">

**Prompt**

```text
Dried seed heads and grasses in a clear glass bottle on a windowsill, backlit so the structures read as silhouettes with light finding the gaps. Dust on the glass, cool overcast light, plain wall behind. Muted, almost monochrome.
```

`seed: 819096213`

### Fruit under hard light

<img src="images/still-life-007.webp" width="420" alt="Fruit under hard light">

**Prompt**

```text
Three pears on a matte black surface under a single hard light from above and behind, casting long crisp shadows toward camera. Skin texture and bloom visible, one pear bruised. Deep shadow everywhere else. Product-grade but severe.
```

`seed: 1126053453`

### Desk objects, cool light

<img src="images/still-life-008.webp" width="420" alt="Desk objects, cool light">

**Prompt**

```text
An arrangement of desk objects on a concrete surface in cool north light: a fountain pen, a brass ruler, a folded pair of spectacles and a stone. Restrained palette, soft shadows, everything placed with deliberate spacing. Overhead, straight down.
```

`seed: 503659668`


## macro-nature

_Insects, botanicals and small structures at high magnification_

### Dragonfly wing, macro

<img src="images/macro-nature-001.webp" width="420" alt="Dragonfly wing, macro">

**Prompt**

```text
Extreme macro of a dragonfly wing against a dark ground, the venation reading as an irregular lattice, faint iridescence where the light catches the membrane. Focus-stacked sharpness edge to edge, no other part of the insect visible.
```

`seed: 1381046048`

### Dew on spider silk

<img src="images/macro-nature-002.webp" width="420" alt="Dew on spider silk">

**Prompt**

```text
Macro of dew beads strung along spider silk at dawn, each drop acting as a lens and inverting the blurred green background inside it. The silk sagging under the weight. Extremely shallow depth of field, backlit.
```

`seed: 2054476156`

### Moss and sporophytes

<img src="images/macro-nature-003.webp" width="420" alt="Moss and sporophytes">

**Prompt**

```text
Macro of a moss cushion with sporophyte stalks rising from it, each capsule catching a soft rim of light, the moss leaves translucent green. Damp, a few water droplets held between the leaves. Low angle, dark background.
```

`seed: 36645787`

### Butterfly scales

<img src="images/macro-nature-004.webp" width="420" alt="Butterfly scales">

**Prompt**

```text
Extreme macro of butterfly wing scales, individual overlapping scales visible like roof tiles, colour shifting from orange to black across the frame. So close that the pattern reads as abstract structure rather than as a wing.
```

`seed: 265148793`

### Frost on a leaf edge

<img src="images/macro-nature-005.webp" width="420" alt="Frost on a leaf edge">

**Prompt**

```text
Macro of ice crystals growing along the serrated edge of a fallen leaf, needle-like formations catching cold morning light, the leaf itself dark and out of focus behind. Blue shadows, white crystals, very shallow focus.
```

`seed: 1307082473`

### Bee on a thistle

<img src="images/macro-nature-006.webp" width="420" alt="Bee on a thistle">

**Prompt**

```text
A bumblebee working a thistle flower, pollen visible on the leg baskets and dusting the hairs of the thorax, individual florets sharp. Soft overcast light, green background thrown completely out of focus. 1/1000s.
```

`seed: 33348605`

### Fern crozier unfurling

<img src="images/macro-nature-007.webp" width="420" alt="Fern crozier unfurling">

**Prompt**

```text
A fern crozier beginning to unfurl, the tight spiral covered in fine pale hairs backlit into a halo, the rest of the plant dark. Shallow focus running down the spiral. Damp woodland light, cool and green.
```

`seed: 728116494`

### Seed head, backlit

<img src="images/macro-nature-008.webp" width="420" alt="Seed head, backlit">

**Prompt**

```text
A dandelion seed head backlit against black, each pappus rendered as a fine bright filament, two seeds already detached and drifting at the frame edge. Focus on the near seeds, falling off across the sphere.
```

`seed: 316013847`


## street

_Unposed public scenes_

### Crossing in rain

<img src="images/street-001.webp" width="420" alt="Crossing in rain">

**Prompt**

```text
A pedestrian crossing in heavy rain shot from across the road, umbrellas overlapping into a single dark mass, one figure stepping off the kerb. Wet asphalt reflecting shop light. 35mm, grainy, unposed, faces not identifiable.
```

`seed: 1097435078`

### Market alley, hard shadow

<img src="images/street-002.webp" width="420" alt="Market alley, hard shadow">

**Prompt**

```text
A narrow market alley at midday, a hard band of sunlight cutting diagonally across the frame and everything outside it in deep shade, two figures crossing the light. Awnings, crates, no legible signage. Documentary, 28mm.
```

`seed: 873659330`

### Bus window, condensation

<img src="images/street-003.webp" width="420" alt="Bus window, condensation">

**Prompt**

```text
Seen from outside: a bus window fogged with condensation, one passenger's shoulder and the back of a head visible through a wiped patch, street light smearing on the wet glass. Winter evening, cool colours, nobody identifiable.
```

`seed: 2114954097`

### Laundry between buildings

<img src="images/street-004.webp" width="420" alt="Laundry between buildings">

**Prompt**

```text
Washing strung on lines between two tenement buildings, seen looking straight up so the sheets and shirts read as flat shapes against a bright overcast sky. Cables, satellite dishes, weathered render. High contrast, graphic.
```

`seed: 2017379999`

### Cafe window, reflection layered

<img src="images/street-005.webp" width="420" alt="Cafe window, reflection layered">

**Prompt**

```text
A cafe window at dusk with the interior and the reflected street overlapping into one layered image — a seated figure inside, passing traffic reflected across them. Nobody identifiable. 50mm, available light, slight motion.
```

`seed: 1477003290`

### Underpass, single figure

<img src="images/street-006.webp" width="420" alt="Underpass, single figure">

**Prompt**

```text
A tiled pedestrian underpass lit by strip lights, one distant figure walking away, the tiling receding to a bright mouth at the far end. Symmetrical, wide, damp floor reflecting the lights. Nobody's face visible.
```

`seed: 1057881872`

### Fish market, early

<img src="images/street-007.webp" width="420" alt="Fish market, early">

**Prompt**

```text
An early-morning fish market: crushed ice, crates, hoses running water across a concrete floor, workers in rubber aprons at the edge of frame with their backs to camera. Cold overhead light, wet everywhere, unposed.
```

`seed: 698283678`

### Steps in low sun

<img src="images/street-008.webp" width="420" alt="Steps in low sun">

**Prompt**

```text
A flight of city steps in low evening sun, the treads throwing a hard sawtooth of shadow, one figure climbing halfway up rendered almost as a silhouette. Long lens compression, warm light, no faces.
```

`seed: 1750591874`


## night

_After dark — available light, long exposure, astro_

### Star trails over a ridge

<img src="images/night-001.webp" width="420" alt="Star trails over a ridge">

**Prompt**

```text
Star trails circling the pole above a dark ridgeline, concentric arcs of white and faint colour on a deep blue-black sky, the land below rendered only as a black silhouette. Very long exposure, no light pollution, no foreground light.
```

`seed: 123461485`

### Petrol station at 3am

<img src="images/night-003.webp" width="420" alt="Petrol station at 3am">

**Prompt**

```text
An empty petrol station forecourt at three in the morning, fluorescent canopy lights the only source, spilling hard white onto wet concrete and falling to black beyond. No cars, no people. Wide, tripod, long exposure.
```

`seed: 105373578`

### Fog under a streetlight

<img src="images/night-004.webp" width="420" alt="Fog under a streetlight">

**Prompt**

```text
Thick fog under a single sodium streetlight, the beam made visible as a solid orange cone, everything beyond it lost. A bare tree half-visible at the edge of the light. Long exposure, no other light source in frame.
```

`seed: 1765268212`

### City from a hill, blue hour

<img src="images/night-005.webp" width="420" alt="City from a hill, blue hour">

**Prompt**

```text
A city seen from a hill at the end of blue hour, streetlights and windows as a dense field of warm points against the last cold blue in the sky. Foreground grass dark and unlit. Long lens compression, tripod, no star trails.
```

`seed: 662128052`

### Lightning over plain

<img src="images/night-006.webp" width="420" alt="Lightning over plain">

**Prompt**

```text
A single lightning bolt striking a flat plain at night, branching downward, the flash illuminating the underside of the storm cloud and a thin strip of ground. Everything else black. Long exposure caught mid-strike.
```

`seed: 766980854`

### Campfire, faces out of frame

<img src="images/night-007.webp" width="420" alt="Campfire, faces out of frame">

**Prompt**

```text
A campfire at night shot low and close, the flames the only light source, sparks rising, a ring of stones and two pairs of boots at the edge of the light. Nobody's face in frame. Warm falloff to complete black.
```

`seed: 1933212622`

### Aurora over snow

<img src="images/night-008.webp" width="420" alt="Aurora over snow">

**Prompt**

```text
An aurora arc over a snow-covered plain, green with a magenta lower fringe, its structure showing vertical rays. The snow picking up the green cast faintly. A dark treeline at the horizon. No moon, no artificial light.
```

`seed: 1239744985`


## Contributing

Open a PR adding an entry to `prompts.json` plus your output image. Two rules: the prompt must reproduce, and the image must be the unedited output.

## License

Prompts are MIT — take them.

**The images are AI-generated.** They were produced with Krea 2 Turbo and are presented as model output, not as photographs or human artwork. Under the Krea 2 Community License you own outputs you generate yourself; commercial use is permitted below $1M annual company revenue, and the licence separately requires content filtering, which was left enabled for every image here. One entry was dropped after the safety checker flagged it.

Nothing here was retouched, upscaled or cropped. Every seed is recorded so you can regenerate the exact file.
