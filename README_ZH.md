<h1 align="center">awesome-krea-2</h1>
<p align="center">475 条 Krea 2 Turbo 提示词，每条都附带产出它的 seed，外加 65 次失败的生成及其原因。这里的每条结论都是在这些图上实测出来的，不是抄模型卡。</p>

<p align="center">
  <img src="hero.webp" width="912" alt="A six-panel grid, a working case above a failure in each of three columns. Text: a brass nameplate carrying eight specified strings, all correct, above a chalkboard menu whose unspecified rows came back as nonsense words. Hands: a hand raising exactly the three fingers asked for, on a hand with six digits, above clasped hands where interlaced fingers were asked for. Interlocking: a chain with every link through its neighbour, above a rope lying in a figure-eight shape that was never tied.">
</p>

<p align="center">
<a href="https://github.com/sjh9714/awesome-krea-2/stargazers"><img src="https://img.shields.io/github/stars/sjh9714/awesome-krea-2?style=flat&color=1f5d4c" alt="stars"></a>
<a href="https://sjh9714.github.io/awesome-krea-2/"><img src="https://img.shields.io/badge/gallery-browse%20all-1f5d4c" alt="gallery"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/prompts-MIT-1f5d4c" alt="license"></a>
</p>

<p align="center"><a href="README.md">EN</a> · <a href="README_KO.md">KO</a> · <a href="https://sjh9714.github.io/awesome-krea-2/"><b>浏览画廊 →</b></a></p>

## 直接把提示词拿走

If you came here to feed a wildcard node, everything below is optional.

| | |
|---|---|
| **[all.txt](https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/all.txt)** | all 475 prompts, one per line, 104 KB. Right click, save. |
| **[krea2-wildcards.zip](https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/krea2-wildcards.zip)** | the same thing split into one file per category plus the style clauses, 96 KB |
| **[styles.txt](https://raw.githubusercontent.com/sjh9714/awesome-krea-2/main/wildcards/styles.txt)** | just the "the whole scene drawn as ..." clauses |

Drop the folder into `ComfyUI/wildcards/` and reference `__all__` or `__photography__` from a dynamic prompt node. No clone, no install, no account.

Two things worth knowing before you run them. **The failures are excluded**, so nothing in these files is a prompt already known to break. And **the seeds are not in here and would not help you anyway**: they were recorded against a hosted endpoint that publishes no sampler or step count, so they do not transfer to your graph. [REPRODUCING.md](REPRODUCING.md) explains exactly why.

## 这个模型实际能做什么

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

## 类别

[photography](https://sjh9714.github.io/awesome-krea-2/#photography) 18 · [typography](https://sjh9714.github.io/awesome-krea-2/#typography) 15 · [product](https://sjh9714.github.io/awesome-krea-2/#product) 18 · [illustration](https://sjh9714.github.io/awesome-krea-2/#illustration) 18 · [reference-sheet](https://sjh9714.github.io/awesome-krea-2/#reference-sheet) 1 · [isometric-3d](https://sjh9714.github.io/awesome-krea-2/#isometric-3d) 10 · [editing](https://sjh9714.github.io/awesome-krea-2/#editing) 5 · [portrait](https://sjh9714.github.io/awesome-krea-2/#portrait) 8 · [infographic](https://sjh9714.github.io/awesome-krea-2/#infographic) 8 · [collectible](https://sjh9714.github.io/awesome-krea-2/#collectible) 5 · [stationery](https://sjh9714.github.io/awesome-krea-2/#stationery) 6 · [food](https://sjh9714.github.io/awesome-krea-2/#food) 9 · [interior](https://sjh9714.github.io/awesome-krea-2/#interior) 10 · [pattern](https://sjh9714.github.io/awesome-krea-2/#pattern) 8 · [brand-mark](https://sjh9714.github.io/awesome-krea-2/#brand-mark) 7 · [miniature](https://sjh9714.github.io/awesome-krea-2/#miniature) 8 · [coloring-page](https://sjh9714.github.io/awesome-krea-2/#coloring-page) 6 · [ui](https://sjh9714.github.io/awesome-krea-2/#ui) 1 · [stringcount](https://sjh9714.github.io/awesome-krea-2/#stringcount) 8 · [animal](https://sjh9714.github.io/awesome-krea-2/#animal) 10 · [landscape](https://sjh9714.github.io/awesome-krea-2/#landscape) 10 · [fashion](https://sjh9714.github.io/awesome-krea-2/#fashion) 7 · [automotive](https://sjh9714.github.io/awesome-krea-2/#automotive) 7 · [exterior](https://sjh9714.github.io/awesome-krea-2/#exterior) 8 · [abstract](https://sjh9714.github.io/awesome-krea-2/#abstract) 7 · [objectcount](https://sjh9714.github.io/awesome-krea-2/#objectcount) 7 · [monogram](https://sjh9714.github.io/awesome-krea-2/#monogram) 2 · [poster](https://sjh9714.github.io/awesome-krea-2/#poster) 9 · [still-life](https://sjh9714.github.io/awesome-krea-2/#still-life) 8 · [macro-nature](https://sjh9714.github.io/awesome-krea-2/#macro-nature) 8 · [street](https://sjh9714.github.io/awesome-krea-2/#street) 8 · [night](https://sjh9714.github.io/awesome-krea-2/#night) 7 · [respecify](https://sjh9714.github.io/awesome-krea-2/#respecify) 2 · [hangul](https://sjh9714.github.io/awesome-krea-2/#hangul) 4 · [sport](https://sjh9714.github.io/awesome-krea-2/#sport) 6 · [scifi](https://sjh9714.github.io/awesome-krea-2/#scifi) 8 · [underwater](https://sjh9714.github.io/awesome-krea-2/#underwater) 8 · [aerial](https://sjh9714.github.io/awesome-krea-2/#aerial) 3 · [period](https://sjh9714.github.io/awesome-krea-2/#period) 8 · [jewellery](https://sjh9714.github.io/awesome-krea-2/#jewellery) 8 · [fantasy](https://sjh9714.github.io/awesome-krea-2/#fantasy) 9 · [comic](https://sjh9714.github.io/awesome-krea-2/#comic) 7 · [childrens-book](https://sjh9714.github.io/awesome-krea-2/#childrens-book) 8 · [technical-drawing](https://sjh9714.github.io/awesome-krea-2/#technical-drawing) 8 · [vehicle](https://sjh9714.github.io/awesome-krea-2/#vehicle) 10 · [weather](https://sjh9714.github.io/awesome-krea-2/#weather) 8 · [glass](https://sjh9714.github.io/awesome-krea-2/#glass) 8 · [material](https://sjh9714.github.io/awesome-krea-2/#material) 5 · [crowd](https://sjh9714.github.io/awesome-krea-2/#crowd) 8 · [weave](https://sjh9714.github.io/awesome-krea-2/#weave) 7 · [tattoo](https://sjh9714.github.io/awesome-krea-2/#tattoo) 7 · [pixel-art](https://sjh9714.github.io/awesome-krea-2/#pixel-art) 7 · [anatomy](https://sjh9714.github.io/awesome-krea-2/#anatomy) 8 · [sculpture](https://sjh9714.github.io/awesome-krea-2/#sculpture) 8 · [plant](https://sjh9714.github.io/awesome-krea-2/#plant) 10 · [tool](https://sjh9714.github.io/awesome-krea-2/#tool) 8 · [knolling](https://sjh9714.github.io/awesome-krea-2/#knolling) 5 · [silhouette](https://sjh9714.github.io/awesome-krea-2/#silhouette) 7 · [mirror](https://sjh9714.github.io/awesome-krea-2/#mirror) 7 · [mineral](https://sjh9714.github.io/awesome-krea-2/#mineral) 8 · [seasonal](https://sjh9714.github.io/awesome-krea-2/#seasonal) 8


## 参与贡献

提交 PR，在 `prompts.json` 中添加条目并附上你的输出图片。两条规则：提示词必须可复现，图片必须是未经编辑的原始输出。

## 许可

提示词采用 MIT 许可。生成的图片受模型提供方条款约束，商用前请自行确认。
