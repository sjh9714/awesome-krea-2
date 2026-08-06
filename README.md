<h1 align="center">awesome-krea-2</h1>
<p align="center">475 Krea 2 Turbo prompts with the seed that produced each one, plus the 65 generations that failed and why. Every claim here was measured against those images, not quoted from the model card.</p>

<p align="center">
  <img src="hero.webp" width="912" alt="A six-panel grid, a working case above a failure in each of three columns. Text: a brass nameplate carrying eight specified strings, all correct, above a chalkboard menu whose unspecified rows came back as nonsense words. Hands: a hand raising exactly the three fingers asked for, on a hand with six digits, above clasped hands where interlaced fingers were asked for. Interlocking: a chain with every link through its neighbour, above a rope lying in a figure-eight shape that was never tied.">
</p>

<p align="center">
<a href="https://github.com/sjh9714/awesome-krea-2/stargazers"><img src="https://img.shields.io/github/stars/sjh9714/awesome-krea-2?style=flat&color=1f5d4c" alt="stars"></a>
<a href="https://sjh9714.github.io/awesome-krea-2/"><img src="https://img.shields.io/badge/gallery-browse%20all-1f5d4c" alt="gallery"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/prompts-MIT-1f5d4c" alt="license"></a>
</p>

<p align="center"><a href="README_ZH.md">ZH</a> · <a href="README_KO.md">KO</a> · <a href="https://sjh9714.github.io/awesome-krea-2/"><b>Browse the gallery →</b></a></p>

## Take the prompts and go

If you came here to feed a wildcard node, everything below is optional.

| | |
|---|---|
| **[all.txt](https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/all.txt)** | all 475 prompts, one per line, 104 KB. Right click, save. |
| **[krea2-wildcards.zip](https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/krea2-wildcards.zip)** | the same thing split into one file per category plus the style clauses, 96 KB |
| **[styles.txt](https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/styles.txt)** | just the "the whole scene drawn as ..." clauses |

Drop the folder into `ComfyUI/wildcards/` and reference `__all__` or `__photography__` from a dynamic prompt node. No clone, no install, no account.

Two things worth knowing before you run them. **The failures are excluded**, so nothing in these files is a prompt already known to break. And **the seeds are not in here and would not help you anyway**: they were recorded against a hosted endpoint that publishes no sampler or step count, so they do not transfer to your graph. [REPRODUCING.md](REPRODUCING.md) explains exactly why.

## What this model actually does

Fourteen findings, each measured against the images in this repo rather than quoted
from the model card. Five of them replace earlier findings I had to withdraw — four
overturned by experiments built to confirm them, one by a reader who counted fingers I
had only glanced at.

|  | Finding | What it costs you if you don't know |
|---|---|---|
| **Text** | It renders any string you write out, at any count. It cannot invent one. | Menu rows left to the model came back `CAPEME`, `CABIELO`. Write every string. |
| **Text** | Small and rotated type is a second, independent limit. | Nine station names written out, four correct. |
| **Korean** | Mostly works, and the words that fail repeat the same misspelling at a different seed. | Rerolling the seed is the wrong fix. Change the wording. |
| **Hands** | **Withdrawn.** I claimed 7 of 8 sound. Two readers counted; three had six or four digits. | The whole category is in the failures now, with seeds. |
| **Identity** | A face does not survive into a new scene. 0.45 keeps the face and the old composition; 0.72 keeps neither. | There is no working value in between. Train a LoRA. |
| **Editing** | Medium conversion is reliable at strength 0.50–0.60. Adding or removing objects is not. | Asked to remove steam, the steam came back. |
| **Counting** | Objects count correctly from 2 to 8. Attributes do not. | "Exactly two flat colours" returned four. |
| **Lighting** | Name the fixture and the fixture walks into frame. | Say what the light *does*, not what it is. |
| **Stationery** | Six for six, and not because the strings were short. | The one category that never failed. |
| **UI** | Layout always right, text only as good as your prompt. | Nine of ten mockups failed on invented labels. |
| **Letters** | Side by side is fine. Asking two letterforms to share strokes is not. | Interlocked `R`+`W` reads as a `P`. |
| **Patterns** | `seamless` does not tile. One of eight had a joinable edge. | Wallpaper and textile pipelines will show the seam. |
| **Aerial** | `straight down` is a request, not an instruction. | Five of eight came back oblique. |
| **Similes** | A size comparison can replace your subject. | "A beetle the size of a pony" returned a pony. |
| **Styles** | Name a style and it may draw the style as an *object*. Describe the whole scene as the medium and the frame converts. | Asked for children's-book style, it put a picture book on the table. "The whole scene drawn as ..." fixed it. |
| **Negatives** | **Measured, and weaker than the folklore.** Half of these prompts contain a "no X" clause; their failure rate is 12.4% against 11.6% for prompts without one. | 3 of 65 failures are a negative being ignored outright. Do not blame a negative before checking the rest of your prompt. |

**[Read the evidence for each one → FINDINGS.md](FINDINGS.md)** Every claim with its images, seeds, the experiments that overturned the earlier version, and the one rule this catalog built, tested and had to throw away.

**[The words that carry the technique → VOCABULARY.md](VOCABULARY.md)** The 62 terms that recur across these prompts and travel between subjects, what each one does, and the seven that a finding here measured *not* doing what they say.

**[Settings, and what the seeds are worth to you → REPRODUCING.md](REPRODUCING.md)** The exact call behind all 475 images, and the limit on it: `fal-ai/krea-2/turbo` exposes no step count, no CFG, no sampler and no scheduler, so **these seeds reproduce on that endpoint and not in your local graph.** The prompts transfer; the seeds do not.

**[How to ask this model for a style → styles/](styles/README.md)** The eight "whole scene drawn as ..." clauses from the Reddit post, the picture-book trap, the three styles that never converted, and an earlier sweep with a FLUX.1 dev cross-check.

## Categories

All **475** entries live in the [gallery](https://sjh9714.github.io/awesome-krea-2/), one page, every prompt with its seed and its image. The category links go straight to the right section.

[photography](https://sjh9714.github.io/awesome-krea-2/#photography) 18 · [typography](https://sjh9714.github.io/awesome-krea-2/#typography) 15 · [product](https://sjh9714.github.io/awesome-krea-2/#product) 18 · [illustration](https://sjh9714.github.io/awesome-krea-2/#illustration) 18 · [reference-sheet](https://sjh9714.github.io/awesome-krea-2/#reference-sheet) 1 · [isometric-3d](https://sjh9714.github.io/awesome-krea-2/#isometric-3d) 10 · [editing](https://sjh9714.github.io/awesome-krea-2/#editing) 5 · [portrait](https://sjh9714.github.io/awesome-krea-2/#portrait) 8 · [infographic](https://sjh9714.github.io/awesome-krea-2/#infographic) 8 · [collectible](https://sjh9714.github.io/awesome-krea-2/#collectible) 5 · [stationery](https://sjh9714.github.io/awesome-krea-2/#stationery) 6 · [food](https://sjh9714.github.io/awesome-krea-2/#food) 9 · [interior](https://sjh9714.github.io/awesome-krea-2/#interior) 10 · [pattern](https://sjh9714.github.io/awesome-krea-2/#pattern) 8 · [brand-mark](https://sjh9714.github.io/awesome-krea-2/#brand-mark) 7 · [miniature](https://sjh9714.github.io/awesome-krea-2/#miniature) 8 · [coloring-page](https://sjh9714.github.io/awesome-krea-2/#coloring-page) 6 · [ui](https://sjh9714.github.io/awesome-krea-2/#ui) 1 · [stringcount](https://sjh9714.github.io/awesome-krea-2/#stringcount) 8 · [animal](https://sjh9714.github.io/awesome-krea-2/#animal) 10 · [landscape](https://sjh9714.github.io/awesome-krea-2/#landscape) 10 · [fashion](https://sjh9714.github.io/awesome-krea-2/#fashion) 7 · [automotive](https://sjh9714.github.io/awesome-krea-2/#automotive) 7 · [exterior](https://sjh9714.github.io/awesome-krea-2/#exterior) 8 · [abstract](https://sjh9714.github.io/awesome-krea-2/#abstract) 7 · [objectcount](https://sjh9714.github.io/awesome-krea-2/#objectcount) 7 · [monogram](https://sjh9714.github.io/awesome-krea-2/#monogram) 2 · [poster](https://sjh9714.github.io/awesome-krea-2/#poster) 9 · [still-life](https://sjh9714.github.io/awesome-krea-2/#still-life) 8 · [macro-nature](https://sjh9714.github.io/awesome-krea-2/#macro-nature) 8 · [street](https://sjh9714.github.io/awesome-krea-2/#street) 8 · [night](https://sjh9714.github.io/awesome-krea-2/#night) 7 · [respecify](https://sjh9714.github.io/awesome-krea-2/#respecify) 2 · [hangul](https://sjh9714.github.io/awesome-krea-2/#hangul) 4 · [sport](https://sjh9714.github.io/awesome-krea-2/#sport) 6 · [scifi](https://sjh9714.github.io/awesome-krea-2/#scifi) 8 · [underwater](https://sjh9714.github.io/awesome-krea-2/#underwater) 8 · [aerial](https://sjh9714.github.io/awesome-krea-2/#aerial) 3 · [period](https://sjh9714.github.io/awesome-krea-2/#period) 8 · [jewellery](https://sjh9714.github.io/awesome-krea-2/#jewellery) 8 · [fantasy](https://sjh9714.github.io/awesome-krea-2/#fantasy) 9 · [comic](https://sjh9714.github.io/awesome-krea-2/#comic) 7 · [childrens-book](https://sjh9714.github.io/awesome-krea-2/#childrens-book) 8 · [technical-drawing](https://sjh9714.github.io/awesome-krea-2/#technical-drawing) 8 · [vehicle](https://sjh9714.github.io/awesome-krea-2/#vehicle) 10 · [weather](https://sjh9714.github.io/awesome-krea-2/#weather) 8 · [glass](https://sjh9714.github.io/awesome-krea-2/#glass) 8 · [material](https://sjh9714.github.io/awesome-krea-2/#material) 5 · [crowd](https://sjh9714.github.io/awesome-krea-2/#crowd) 8 · [weave](https://sjh9714.github.io/awesome-krea-2/#weave) 7 · [tattoo](https://sjh9714.github.io/awesome-krea-2/#tattoo) 7 · [pixel-art](https://sjh9714.github.io/awesome-krea-2/#pixel-art) 7 · [anatomy](https://sjh9714.github.io/awesome-krea-2/#anatomy) 8 · [sculpture](https://sjh9714.github.io/awesome-krea-2/#sculpture) 8 · [plant](https://sjh9714.github.io/awesome-krea-2/#plant) 10 · [tool](https://sjh9714.github.io/awesome-krea-2/#tool) 8 · [knolling](https://sjh9714.github.io/awesome-krea-2/#knolling) 5 · [silhouette](https://sjh9714.github.io/awesome-krea-2/#silhouette) 7 · [mirror](https://sjh9714.github.io/awesome-krea-2/#mirror) 7 · [mineral](https://sjh9714.github.io/awesome-krea-2/#mineral) 8 · [seasonal](https://sjh9714.github.io/awesome-krea-2/#seasonal) 8

### What one entry looks like

<img src="images/photography-001.webp" width="420" alt="Ceramicist at golden hour, 85mm">

```text
A ceramicist in her studio at golden hour, hands wet with slip, throwing a bowl on a kick wheel. Shot on 85mm at f/1.8, shallow depth of field, warm rim light from a west-facing window, dust motes in the beam. Muted earth palette, visible clay dust on her forearms.
```

`seed: 1913817765`

The gallery highlights the words that recur across this catalog and travel to other subjects. This one carries `85mm`, `muted`, `palette`, `shallow depth of field`. [What each of them does → VOCABULARY.md](VOCABULARY.md)

[**Browse all 475 →**](https://sjh9714.github.io/awesome-krea-2/)

## The image-to-image entries, taken further

The five `editing-*` entries were pulled out into [**same-frame**](https://github.com/sjh9714/same-frame), an agent skill for Claude Code and Codex, and each one was re-run against a source it was *not* derived from. Two held, two came back partial, one failed — and the failures produced a sharper rule than this catalog started with: **geometry is locked, material is not.** Relighting wet rice terraces under hard sun keeps every contour in position and returns dry stone.

That repo also carries the two edits cut from here as refusals: it blocks an object-removal or character-consistency request before it is spent, and shows you the image where it already failed.

## Check any of this yourself

`python3 scripts/regen.py --id typography-012` re-runs any entry from its recorded seed. Two text-to-image entries came back at a mean per-pixel difference of 1.3 and 1.5 out of 255, which is WebP re-encoding loss, and the endpoint is deterministic at identical inputs. The five `editing-*` entries are the exception and the number is much larger. [REPRODUCING.md](REPRODUCING.md) has the exact call, the numbers, and why none of this transfers to a local graph.

## The failures, kept as evidence

Deliberately reproduced failures. Every claim in the README's findings section points at one of these, with the seed that produced it, so the limits are checkable rather than asserted. These are NOT part of the 85-entry catalog.

| | What was asked for | What came back |
|---|---|---|
| <img src="images/failures/abstract-004.webp" width="150" alt="Colour: 'coloured light trails' came back as four pale near-white lines"> | Crossing, looping, coloured trails | Colour: 'coloured light trails' came back as four pale near-white lines <br>`seed: 478699619` |
| <img src="images/failures/aerial-001.webp" width="150" alt="Angle: asked for straight down, returned a high oblique"> | Nadir framing | Angle: asked for straight down, returned a high oblique <br>`seed: 786641017` |
| <img src="images/failures/aerial-003.webp" width="150" alt="Angle: asked for straight down, returned an oblique with the cranes standing up in frame"> | Nadir framing | Angle: asked for straight down, returned an oblique with the cranes standing up in frame <br>`seed: 372479606` |
| <img src="images/failures/aerial-005.webp" width="150" alt="Angle: asked for straight down on a suburb, returned a view from the pavement"> | Nadir framing | Angle: asked for straight down on a suburb, returned a view from the pavement <br>`seed: 1337059737` |
| <img src="images/failures/aerial-007.webp" width="150" alt="Angle: asked for straight down, returned a high oblique - the terrace risers are visible and the hillside recedes into haze"> | Nadir framing | Angle: asked for straight down, returned a high oblique - the terrace risers are visible and the hillside recedes into haze <br>`seed: 1421294354` |
| <img src="images/failures/aerial-008.webp" width="150" alt="Angle: asked for straight down on an interchange, returned a view from bridge height"> | Nadir framing | Angle: asked for straight down on an interchange, returned a view from bridge height <br>`seed: 202936705` |
| <img src="images/failures/automotive-002.webp" width="150" alt="Text: the tyre sidewall lettering is legible enough to read as wrong"> | Out-of-focus sidewall lettering | Text: the tyre sidewall lettering is legible enough to read as wrong <br>`seed: 318918336` |
| <img src="images/failures/brand-mark-002.webp" width="150" alt="Letters: asked for the monogram 'KJ', got three letterforms that are not those two"> | The letters K and J interlocked | Letters: asked for the monogram 'KJ', got three letterforms that are not those two <br>`seed: 1276536027` |
| <img src="images/failures/collectible-003.webp" width="150" alt="Text: four keycap legends came back as letter-shaped noise"> | Four legible dye-sublimated legends | Text: four keycap legends came back as letter-shaped noise <br>`seed: 1958353167` |
| <img src="images/failures/collectible-004.webp" width="150" alt="Layout: the creature artwork went to the top and the centre panel stayed empty"> | Illustrated creature artwork in the central panel | Layout: the creature artwork went to the top and the centre panel stayed empty <br>`seed: 167021886` |
| <img src="images/failures/collectible-008.webp" width="150" alt="Equipment: naming the softbox put the softbox in the frame"> | A single softbox lighting the duck, out of shot | Equipment: naming the softbox put the softbox in the frame <br>`seed: 1935262212` |
| <img src="images/failures/comic-003.webp" width="150" alt="Composition: a flat cyan field with the figure pushed to the edge, and no rosette worth the name"> | A newsprint panel with visible CMYK rosette | Composition: a flat cyan field with the figure pushed to the edge, and no rosette worth the name <br>`seed: 312992160` |
| <img src="images/failures/fail-identity.webp" width="150" alt="Identity: at strength 0.72 the scene is new and the person is not the same. The middle figure also carries three arms - one holding the laptop and a second silver sleeve hanging beside it - which I did not see until a reader pointed at it on 2026-07-31."> | The woman from reference-sheet-001 | Identity: at strength 0.72 the scene is new and the person is not the same. The middle figure also carries three arms - one holding the laptop and a second silver sleeve hanging beside it - which I did not see until a reader pointed at it on 2026-07-31. <br>`seed: 1317515569` |
| <img src="images/failures/fail-korean.webp" width="150" alt="Text: Korean fails one character in, and looks clean if you cannot read it"> | 정직한 국수 | Text: Korean fails one character in, and looks clean if you cannot read it <br>`seed: 1910572019` |
| <img src="images/failures/fail-map.webp" width="150" alt="Text: thirty station names, none of them words"> | Legible station names | Text: thirty station names, none of them words <br>`seed: 57616412` |
| <img src="images/failures/fail-menu.webp" width="150" alt="Text: a list of many strings collapses after the first few"> | Ten legible menu rows | Text: a list of many strings collapses after the first few <br>`seed: 1729505870` |
| <img src="images/failures/fail-removal.webp" width="150" alt="Editing: asked to remove the steam, returns the steam"> | No steam | Editing: asked to remove the steam, returns the steam <br>`seed: 1499506316` |
| <img src="images/failures/fail-spines.webp" width="150" alt="Text: twelve independent strings in one frame, all unreadable"> | Twelve readable invented titles | Text: twelve independent strings in one frame, all unreadable <br>`seed: 1095803014` |
| <img src="images/failures/fail-terminal.webp" width="150" alt="Text: the command line renders, the output beneath it does not"> | $ make install plus three lines of build output | Text: the command line renders, the output beneath it does not <br>`seed: 1530960951` |
| <img src="images/failures/fail-timeline.webp" width="150" alt="Text: years render, labels do not"> | Eight year+label pairs | Text: years render, labels do not <br>`seed: 797625079` |
| <img src="images/failures/fantasy-009.webp" width="150" alt="Simile: 'a beetle the size of a pony' returned a pony — the comparison replaced the subject"> | A pony-sized beetle in a harness | Simile: 'a beetle the size of a pony' returned a pony — the comparison replaced the subject <br>`seed: 1007230101` |
| <img src="images/failures/fashion-007.webp" width="150" alt="Composition: asked for the rail end-on as receding silhouettes, got it side-on with the hangers showing"> | An end-on rail reading as layered silhouettes | Composition: asked for the rail end-on as receding silhouettes, got it side-on with the hangers showing <br>`seed: 1999599151` |
| <img src="images/failures/food-003.webp" width="150" alt="Mechanism: the espresso renders as an amber disc where the basket should be, and one stream instead of two"> | Two thin streams from a portafilter | Mechanism: the espresso renders as an amber disc where the basket should be, and one stream instead of two <br>`seed: 117001054` |
| <img src="images/failures/hands-1.webp" width="150" alt="Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight"> | Five digits per hand | Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight <br>`seed: 1481878687` |
| <img src="images/failures/hands-2.webp" width="150" alt="Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight"> | Five digits per hand | Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight <br>`seed: 115868128` |
| <img src="images/failures/hands-3.webp" width="150" alt="Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight"> | Five digits per hand | Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight <br>`seed: 1328002727` |
| <img src="images/failures/hands-4.webp" width="150" alt="Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight"> | Five digits per hand | Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight <br>`seed: 1095933455` |
| <img src="images/failures/hands-5.webp" width="150" alt="Gesture: asked for fingers fully interlaced, returned a clasp with the fingers lying over the other hand"> | Fingers woven between fingers | Gesture: asked for fingers fully interlaced, returned a clasp with the fingers lying over the other hand <br>`seed: 1164604099` |
| <img src="images/failures/hands-6.webp" width="150" alt="Digits: the near hand has six fingers wrapped around the grip; the pose reads correct and the count does not"> | A two-person handshake with five digits per hand | Digits: the near hand has six fingers wrapped around the grip; the pose reads correct and the count does not <br>`seed: 1319396385` |
| <img src="images/failures/hands-7.webp" width="150" alt="Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight"> | Five digits per hand | Digits unverified: I judged this anatomically sound at 1.5-2x and two readers found errors in three of the eight <br>`seed: 387883077` |
| <img src="images/failures/hands-8.webp" width="150" alt="Digits: asked for exactly 3 fingers raised, and the hand carries six digits in total"> | Three raised, thumb and little finger folded, five digits | Digits: asked for exactly 3 fingers raised, and the hand carries six digits in total <br>`seed: 1353379060` |
| <img src="images/failures/hangul-003.webp" width="150" alt="Korean: 정직한 came back 정적한 again, at a different seed from the first attempt"> | 정직한 국수 | Korean: 정직한 came back 정적한 again, at a different seed from the first attempt <br>`seed: 1167746582` |
| <img src="images/failures/hangul-005.webp" width="150" alt="Korean: 밭 came back 뾃, a syllable that does not exist"> | 한밭식당 | Korean: 밭 came back 뾃, a syllable that does not exist <br>`seed: 1086365627` |
| <img src="images/failures/infographic-004.webp" width="150" alt="Text: the chalk heading rendered, the three bullet lines under it did not"> | A heading plus three short bullet lines | Text: the chalk heading rendered, the three bullet lines under it did not <br>`seed: 1043088059` |
| <img src="images/failures/infographic-007.webp" width="150" alt="Count: 'five regions' returned eight, and the ink coastline never appeared"> | Five regions with a thin brown ink coastline | Count: 'five regions' returned eight, and the ink coastline never appeared <br>`seed: 125241101` |
| <img src="images/failures/knolling-001.webp" width="150" alt="Text: the lens caps carry invented branding, legible and wrong, in an otherwise perfect knoll"> | No text on the equipment | Text: the lens caps carry invented branding, legible and wrong, in an otherwise perfect knoll <br>`seed: 914939340` |
| <img src="images/failures/knolling-002.webp" width="150" alt="Arrangement: asked for the pocket contents laid flat on a grid, returned them heaped in the pocket"> | Objects square to the frame with even gaps | Arrangement: asked for the pocket contents laid flat on a grid, returned them heaped in the pocket <br>`seed: 2139908382` |
| <img src="images/failures/knolling-004.webp" width="150" alt="Contents: bicycle-specific tools were asked for and generic ones arrived, with invented sticker text"> | Tyre levers, patches, a pump | Contents: bicycle-specific tools were asked for and generic ones arrived, with invented sticker text <br>`seed: 545841073` |
| <img src="images/failures/material-003.webp" width="150" alt="Surface: boiled wool felt came back as uniform grey noise with no nap and no fibre"> | Matted directional wool fibres | Surface: boiled wool felt came back as uniform grey noise with no nap and no fibre <br>`seed: 419888631` |
| <img src="images/failures/material-004.webp" width="150" alt="Surface: asked for a fine crazed network in aged leather, returned smooth leather with soft creases"> | Crazed, worn leather grain | Surface: asked for a fine crazed network in aged leather, returned smooth leather with soft creases <br>`seed: 67212683` |
| <img src="images/failures/material-007.webp" width="150" alt="Material: sand-cast bronze came back as pitted pale stone with no metal in it"> | Cast bronze, dark in the recesses and polished on the high points | Material: sand-cast bronze came back as pitted pale stone with no metal in it <br>`seed: 324747702` |
| <img src="images/failures/mirror-004.webp" width="150" alt="Instruction: asked for nobody in the reflection, returned two hands pressed against the glass"> | An empty fogged mirror with a wiped arc | Instruction: asked for nobody in the reflection, returned two hands pressed against the glass <br>`seed: 404637919` |
| <img src="images/failures/monogram-001.webp" width="150" alt="Letters: asked to interlock R and W, the R reads as a P where the two forms overlap"> | R and W, both legible | Letters: asked to interlock R and W, the R reads as a P where the two forms overlap <br>`seed: 1193159535` |
| <img src="images/failures/night-002.webp" width="150" alt="Scene: the reflection never resolves into water; the lower half reads as a second sky"> | The Milky Way reflected in still water | Scene: the reflection never resolves into water; the lower half reads as a second sky <br>`seed: 1089231047` |
| <img src="images/failures/pixel-art-002.webp" width="150" alt="Animation: a four-frame walk cycle came back as six identical frames in the same pose"> | Four distinct frames of a walk | Animation: a four-frame walk cycle came back as six identical frames in the same pose <br>`seed: 1526433893` |
| <img src="images/failures/portrait-006.webp" width="150" alt="Portrait: asked for a silhouette, got a fully modelled face"> | A clean dark silhouette, exposed for the sky | Portrait: asked for a silhouette, got a fully modelled face <br>`seed: 2099062475` |
| <img src="images/failures/portrait-008.webp" width="150" alt="Count: 'exactly two flat colours plus white' returned four plus shading"> | Two flat colours, no gradients | Count: 'exactly two flat colours plus white' returned four plus shading <br>`seed: 1251562984` |
| <img src="images/failures/portrait-010.webp" width="150" alt="Light: two named colours from opposite sides did not cross on the face"> | Magenta from frame left and cyan from frame right meeting across the face | Light: two named colours from opposite sides did not cross on the face <br>`seed: 416503906` |
| <img src="images/failures/portrait-012.webp" width="150" alt="Equipment: naming the softbox put the softbox in the frame"> | Seamless mid-grey background, light source out of shot | Equipment: naming the softbox put the softbox in the frame <br>`seed: 639894452` |
| <img src="images/failures/poster-004.webp" width="150" alt="Glyph: the string is right and both R's are drawn mirrored — NOЯTHEЯN LIGHT"> | NORTHERN LIGHT | Glyph: the string is right and both R's are drawn mirrored — NOЯTHEЯN LIGHT <br>`seed: 1064082710` |
| <img src="images/failures/respecify-map.webp" width="150" alt="Text: specifying the names fixed four of nine; the small rotated labels still fail — MILL LANE became MILLLANYNE, CENTRAL became EECTFRAL"> | Nine legible station names | Text: specifying the names fixed four of nine; the small rotated labels still fail — MILL LANE became MILLLANYNE, CENTRAL became EECTFRAL <br>`seed: 1334788167` |
| <img src="images/failures/silhouette-004.webp" width="150" alt="Exposure: asked for hands as solid black against the window, returned them backlit and translucent"> | Hands as flat black shapes | Exposure: asked for hands as solid black against the window, returned them backlit and translucent <br>`seed: 1616657488` |
| <img src="images/failures/sport-003.webp" width="150" alt="Framing: asked for no face in frame, the face is in frame behind the hands"> | Hands on the ropes, no face | Framing: asked for no face in frame, the face is in frame behind the hands <br>`seed: 769044869` |
| <img src="images/failures/sport-006.webp" width="150" alt="Count inside a noun: a rowing EIGHT came back as a single sculler"> | An eight-person crew | Count inside a noun: a rowing EIGHT came back as a single sculler <br>`seed: 603162714` |
| <img src="images/failures/tattoo-008.webp" width="150" alt="Framing: asked for a healed and a fresh tattoo on one arm, returned two arms with matching stars"> | Two tattoos side by side on one arm | Framing: asked for a healed and a fresh tattoo on one arm, returned two arms with matching stars <br>`seed: 378283143` |
| <img src="images/failures/ui-001.webp" width="150" alt="UI: every invented label is noise while the currency amounts render correctly"> | Transaction names, dates and amounts | UI: every invented label is noise while the currency amounts render correctly <br>`seed: 1378883083` |
| <img src="images/failures/ui-002.webp" width="150" alt="UI: the first section header reads 'Settings'; the next two degrade to 'Sectings'"> | Three section headers and six row labels | UI: the first section header reads 'Settings'; the next two degrade to 'Sectings' <br>`seed: 1537435411` |
| <img src="images/failures/ui-003.webp" width="150" alt="UI: metric numbers survive, every label around them does not"> | Four labelled metric cards and a five-row table | UI: metric numbers survive, every label around them does not <br>`seed: 401297056` |
| <img src="images/failures/ui-005.webp" width="150" alt="UI: a code editor renders as convincing syntax-coloured noise with no readable token"> | Syntax-highlighted code | UI: a code editor renders as convincing syntax-coloured noise with no readable token <br>`seed: 1224413193` |
| <img src="images/failures/ui-006.webp" width="150" alt="UI: the day headers fail and so do the dates — 5, 6, 51, 13 is not a week"> | Seven weekday headers and a sequential date grid | UI: the day headers fail and so do the dates — 5, 6, 51, 13 is not a week <br>`seed: 982476354` |
| <img src="images/failures/ui-007.webp" width="150" alt="UI: 'Add to cart' is correct, the product title is not, and the size buttons all read 'Size'"> | A product title, a price, and size options | UI: 'Add to cart' is correct, the product title is not, and the size buttons all read 'Size' <br>`seed: 1056892936` |
| <img src="images/failures/ui-008.webp" width="150" alt="UI: chat bubbles are structurally perfect and every message is unreadable"> | Readable alternating messages | UI: chat bubbles are structurally perfect and every message is unreadable <br>`seed: 880659524` |
| <img src="images/failures/ui-009.webp" width="150" alt="UI: the illustration is good, the headline and the button label are not"> | A headline, supporting text and a button label | UI: the illustration is good, the headline and the button label are not <br>`seed: 727964264` |
| <img src="images/failures/ui-010.webp" width="150" alt="UI: all three columns are literally headed 'Kanban' — the model rendered the word from the prompt"> | Three distinct column names | UI: all three columns are literally headed 'Kanban' — the model rendered the word from the prompt <br>`seed: 1672153217` |
| <img src="images/failures/weave-4.webp" width="150" alt="Knot: asked for a figure-eight knot, returned a figure-eight shape — two loops with a single crossing, never tied"> | A tied figure-eight knot | Knot: asked for a figure-eight knot, returned a figure-eight shape — two loops with a single crossing, never tied <br>`seed: 518928111` |

## How this compares

Verified on 2026-07-25 by reading each repository's tree, README and data files, and by requesting the image URLs. These are good catalogs and two of them do the in-repo thing better than I expected, so the table gives them credit for it. The two columns where nothing exists yet are the reason this repo bothered.

| | Prompts | Images in repo | Seeds / params | Failures shown | Measured cost |
|---|---|---|---|---|---|
| **this repo** | 475 | ✅ 540 | ✅ **all 475** | ✅ **65, with seeds** | ✅ **$4.54 / 561 gens** |
| [YouMind/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) · 12,956★ | 14,916 claimed, 129 in README | ❌ external CMS | ❌ | ❌ | ❌ |
| [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) · 10,190★ | 70 | ❌ external, 3 already dead | ❌ | ❌ | ❌ |
| [YouMind/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) · 8,772★ | 13,663 claimed, 126 in README | ❌ external CMS | ❌ | ❌ | ❌ |
| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) · 8,687★ | 517 | ✅ 549 | ❌ | ⚠️ prose caveats, no images | ❌ |
| [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) · 8,097★ | 100 | ✅ 100 | ❌ | ❌ | ⚠️ tool per case, no cost |

- **Nobody records seeds.** Checked every entry in all five: YouMind's per-entry block carries Author / Source / Published / Languages and nothing else, and its submission form has no seed field either. freestylefly's `cases.json` has thirteen keys, none of them a seed. jamez's `case.yml` and `ATTRIBUTION.yml` schemas have no seed field. This is the only claim here that holds without qualification.
- **A seed is worth less than it sounds, and the column above does not say so.** `fal-ai/krea-2/turbo` publishes no step count, CFG, sampler or scheduler, so a seed recorded against it reproduces there and not in a local ComfyUI graph. Nobody else records seeds, and this repo does; that is still true and still narrower than it reads. [REPRODUCING.md](REPRODUCING.md) has the exact call and the measured pixel differences.
- **Nobody publishes what it cost.** jamez does record `creation_tool` (Sora on 97 of 100 cases, GPT-4o on 3) and freestylefly documents its generation path, which is more than the others — but neither states a figure.
- **Credit where it is due on reproducibility.** freestylefly commits 549 images and jamez 100, both with relative paths and copy-pasteable prompts. Those two are self-contained and I am not claiming otherwise.
- **Link rot is not hypothetical.** ZeroLu's 86 images are all external. Requesting them on 2026-07-25 found three already gone — two Twitter CDN links returning 403/404 and one path that no longer exists in the repo. That is why the images here are committed rather than linked.
- **Scale claims deserve reading twice.** The two YouMind repos advertise 14,916 and 13,663 prompts. Their own FAQ says images live on a CMS, not in git, and their README says GitHub's length limit caps the visible list — 129 and 126 entries respectively, under 1% of the headline number. The rest are on their website.
- jamez-bondos has not been pushed since 2025-05-26.


## Contributing

Open a PR adding an entry to `prompts.json` plus your output image. Two rules: the prompt must reproduce, and the image must be the unedited output.

## License

Prompts are MIT — take them.

**The images are AI-generated.** They were produced with Krea 2 Turbo and are presented as model output, not as photographs or human artwork. Under the Krea 2 Community License you own outputs you generate yourself; commercial use is permitted below $1M annual company revenue, and the licence separately requires content filtering, which was left enabled for every image here. One entry was dropped after the safety checker flagged it.

Nothing here was retouched, upscaled or cropped. Every seed is recorded so you can regenerate the exact file.
