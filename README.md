<h1 align="center">awesome-krea-2</h1>
<p align="center">161 reproducible prompts for Krea 2 Turbo, across 18 categories. Every prompt is copy-pasteable and every image is the actual output.</p>

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

**161 prompts, every one with its seed** · [photography](#photography) 18 · [typography](#typography) 15 · [product](#product) 18 · [illustration](#illustration) 18 · [reference-sheet](#reference-sheet) 1 · [isometric-3d](#isometric-3d) 10 · [editing](#editing) 5 · [portrait](#portrait) 8 · [infographic](#infographic) 8 · [collectible](#collectible) 5 · [stationery](#stationery) 6 · [food](#food) 9 · [interior](#interior) 10 · [pattern](#pattern) 8 · [brand-mark](#brand-mark) 7 · [miniature](#miniature) 8 · [coloring-page](#coloring-page) 6 · [ui](#ui) 1

## What this model actually does

Everything below was measured while building this catalog, not quoted from the model card. 210 generations across three batches, 161 are here, 49 were cut. Each claim names the entries that demonstrate it, every entry carries the seed that produced it and the batch it came from, so you can check any of this against the images in this repo. Keep rates rose batch over batch — 85 of 114, then 27 of 36, then 49 of 60 — because each batch was written knowing what the last one ruled out. The exception is deliberate: one category in batch three was included expecting it to fail.

### Text survives one sign and dies on a list

I went in expecting a word-count ceiling and my own results kill that theory. `HOLLOW & SON — MILLWRIGHTS — EST 1908` came back letter-perfect at eight words (**typography-008**). So did `PLATFORM 4`, `FRAGILE` + `THIS WAY UP`, `SOURDOUGH` + `£4.20`, `SEOUL` + `GATE 12`, `EST 1884`, `FRESH EGGS`. All 15 typography entries kept the string I asked for, and several of them carry two separate strings.

What breaks is not length, it is **how many independent text elements share the frame, and whether any of them is prose**. A chalkboard menu got `FILTER 4.50` and `CORTADO 4.00` right, then produced `CAPEME`, `CABIELO`, `PANSRUR` for the remaining rows. A shelf of twelve book spines, a transit map of thirty station names and an eight-point timeline were unreadable end to end. A safety sign rendered `DANGER` and `ARC FLASH AND SHOCK HAZARD` correctly and filled the paragraph beneath them with letter-shaped noise.

Korean fails earlier and more quietly. I asked for 정직한 국수 and got 정적한 — one character wrong in a four-syllable string. If you do not read Korean it looks clean; if you do, it is the first thing you see.

Practical rule: one sign, one label, one price tag, at any length. Not a menu, not a bibliography, not a sentence.

Those failures are not in this repo — they are part of the 29 that were cut.

### Character identity does not survive across generations

A reference sheet of a specific person renders well — see **reference-sheet-001**. Reusing that person in a new scene does not work, and image-to-image does not rescue it, because the two useful settings fail in opposite directions:

- `strength 0.72` — genuinely new scene, but a different person. Only the sweater and the palette carry over.
- `strength 0.45` — recognisably the same person, but the source composition comes with her. A three-view studio sheet became the same three views at a harbour.

There is no middle setting that gives the same face in a different photograph. If you need a consistent character, train a LoRA; prompting cannot do it. This is why there is no character-consistency category here.

### It changes medium willingly and scene content reluctantly

Image-to-image is reliable when you ask for a different *rendering* of the same scene. Rice terraces became a convincing gouache painting with the terrace contours intact (**editing-003**); a woodblock wave took a dusk palette while every keyblock outline stayed put (**editing-005**); an exploded camera diagram became a clean cyanotype blueprint with every component in place (**editing-008**).

It is unreliable when you ask it to add or remove *things*. Three attempts failed and were cut rather than shipped with captions that did not match the images: removing the steam from a mug returned the steam; adding snow and sea ice to a coastline returned the same coastline slightly cooler; darkening a sauna's window returned the window still lit.

`strength` between 0.50 and 0.60 preserved composition while allowing the medium to change. No value made object-level edits work.

### Numbers in a prompt are treated as flavour, not as a count

Every constraint phrased as a quantity was ignored while the surrounding description was followed closely.

I asked for a flat avatar in **exactly two flat colours plus white, no gradients** and got four colours with shading on the neck (**portrait-008**). I asked for a watercolour map **divided into five regions** and got eight (**infographic-007**). Both images are otherwise good — the avatar is clean, the map is genuinely lovely watercolour — which is what makes this worth writing down: the failure is invisible unless you go back and count.

Note what did work. `infographic-009` asked for two columns of four rows and delivered exactly that; `infographic-008` asked for five markers and delivered five. The difference is that those counts are **structural** — a layout with a wrong number of rows stops looking like a table. A colour count or a region count has no structure holding it, so nothing pushes back.

Practical rule: if a number matters and the layout would not visibly break without it, count the output yourself.

### Name a light and you get the light. Name the softbox and you get the softbox.

Twice in one batch, naming the physical lighting equipment put that equipment in the frame as a subject.

`portrait-012` asked for a corporate headshot with a **large softbox front and slightly above** against a seamless grey background, and returned a portrait with two large white softboxes flanking the subject. `collectible-008` asked for a rubber duck under **a single large softbox above and behind** and returned a duck with a full lighting umbrella open behind it, filling half the frame.

The prompts that worked describe the *light*, not the *fixture*: "hard low-angle late afternoon sun from frame right", "single hard light high and to camera left", "soft directional daylight". All three rendered the lighting condition with nothing extra in shot.

Practical rule: say what the light does, never what makes it.

### Single-string stationery is where this model is strongest

The six `stationery-*` entries all rendered their text correctly on the first attempt — `NORTHFIELD & CO`, `FRAGILE`, `ADMIT ONE`, `PAID` — with no retries and nothing cut. That is the only category in this catalog with a 100% keep rate.

`stationery-006` is the one to look at: the red `PAID` impression on the paper is correct, and the rubber stamp lying beside it carries the same word **mirrored**, which is what a real stamp face does. Nobody asked for that.

This is the same rule as the typography finding, seen from the useful side. One string in one frame is not a limitation to work around; it is the shape the model is actually good at.

### Interface mockups: the layout is always right and the words are always wrong

I added ten UI mockups to batch three expecting nine of them to fail, and nine of them failed. That was the point — a limit you only predict is not a measured limit.

What is striking is *which* half breaks. The structure is consistently correct: `ui-002` has three grouped sections of three rows with a toggle on each, some on and some off, hairlines between; `ui-008` has alternating chat bubbles with avatars, timestamps and a pinned input; `ui-010` has three kanban columns with count badges, tag pills and avatars. Every one of those is exactly what was asked for.

The strings are not. `ui-002` renders the first section header as `Settings` and then degrades to `Sectings` for the next two. `ui-006` fails at the day headers *and* at the dates — the first week reads 5, 6, 51, 13, which is not a week.

The one that worked is **ui-004**, the login screen, and it worked because it has four short real strings: `Sign in`, `Email`, `Password`, `Continue`. All four are letter-perfect. The same effect shows in the cuts — `ui-007` got `Add to cart` exactly right while inventing gibberish for the product title.

Practical rule: this model will give you a convincing UI *composition* to trace over, and you must replace every word in it.

### It renders words, not letters

`brand-mark-002` asked for a monogram of the letters `KJ` interlocked in a circle. It came back with three letterforms, none of them clearly a J. Everything around it is perfect — the circular rule, the single ink weight, the symmetry.

That is the only text failure in a category that otherwise went seven for eight, and the seven that worked were all *words*: `HALLOW`, `FIELDNOTE`, `OPEN`, `EST 1904`, `ASTER`, `COOPERAGE`, `STUDIO 4`. Nine letters rendered correctly in `COOPERAGE`; two letters failed in `KJ`.

So the limit is not length, and it is not even string count on its own. An arbitrary letter pair has no word for the model to reach for. If you need specific initials, expect to set them yourself.

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


## Contributing

Open a PR adding an entry to `prompts.json` plus your output image. Two rules: the prompt must reproduce, and the image must be the unedited output.

## License

Prompts are MIT — take them.

**The images are AI-generated.** They were produced with Krea 2 Turbo and are presented as model output, not as photographs or human artwork. Under the Krea 2 Community License you own outputs you generate yourself; commercial use is permitted below $1M annual company revenue, and the licence separately requires content filtering, which was left enabled for every image here. One entry was dropped after the safety checker flagged it.

Nothing here was retouched, upscaled or cropped. Every seed is recorded so you can regenerate the exact file.
