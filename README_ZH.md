<h1 align="center">krea2-wildcards</h1>
<p align="center">475 条经过验证的 Krea 2 Turbo 提示词。一个文件，丢进 ComfyUI 就能用。</p>

<p align="center">
  <img src="hero.webp" width="912" alt="Twelve Krea 2 Turbo outputs in a four by three grid, under the heading 475 tested Krea 2 Turbo prompts: a loft under renovation, a desert dune ridge at first light, a backlit seed head, an aurora over snow, ice diving seen from below, a shelf cloud, a barn owl in flight, a prism spectrum on a wall, an icebreaker bow, a quartz point, cut stems in water, and moss with sporophytes.">
</p>

<p align="center">
<a href="https://github.com/sjh9714/krea2-wildcards/stargazers"><img src="https://img.shields.io/github/stars/sjh9714/krea2-wildcards?style=flat&color=1f5d4c" alt="stars"></a>
<a href="https://sjh9714.github.io/krea2-wildcards/"><img src="https://img.shields.io/badge/gallery-browse%20all-1f5d4c" alt="gallery"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/prompts-MIT-1f5d4c" alt="license"></a>
</p>

<p align="center"><a href="README.md">EN</a> · <a href="README_KO.md">KO</a> · <a href="README_JA.md">JA</a> · <a href="README_ES.md">ES</a> · <a href="README_FR.md">FR</a> · <a href="README_DE.md">DE</a> · <a href="README_PT.md">PT</a> · <a href="https://sjh9714.github.io/krea2-wildcards/"><b>浏览画廊 →</b></a></p>

## 📥 直接把提示词拿走

**[Download all.txt](https://raw.githubusercontent.com/sjh9714/krea2-wildcards/main/wildcards/all.txt)** (104 KB): 475 prompts, one per line.

Put it in `ComfyUI/wildcards/` and call `__all__` from a dynamic prompt node. No clone, no install, no account.

[Per-category files and a zip](wildcards/) · [Browse them all as pictures](https://sjh9714.github.io/krea2-wildcards/)

## 🔬 这个模型实际能做什么

Fourteen findings, each measured against the images in this repo rather than quoted
from the model card. Five of them replace earlier findings I had to withdraw. Four
overturned by experiments built to confirm them, one by a reader who counted fingers I
had only glanced at.

|  | Finding | What it costs you if you don't know |
|---|---|---|
| **Text** | It renders any string you write out, at any count. It cannot invent one. | Menu rows left to the model came back `CAPEME`, `CABIELO`. Write every string. |
| **Text** | Small and rotated type is a second, independent limit. | Nine station names written out, four correct. |
| **Korean** | Mostly works, and the words that fail repeat the same misspelling at a different seed. | Rerolling the seed is the wrong fix. Change the wording. |
| **Hands** | **Withdrawn.** I claimed 7 of 8 sound. Two readers counted; three had six or four digits. | The whole category is in the failures now, with seeds. |
| **Identity** | A face does not survive into a new scene. 0.45 keeps the face and the old composition; 0.72 keeps neither. | There is no working value in between. Train a LoRA. |
| **Editing** | Medium conversion is reliable at strength 0.50, 0.60. Adding or removing objects is not. | Asked to remove steam, the steam came back. |
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

**[Fill-in-the-blank recipes → TEMPLATES.md](TEMPLATES.md)** Six shapes rather than 475 finished sentences, each naming the result in this repo that measured it. There are six and not four hundred on purpose.

**[The words that carry the technique → VOCABULARY.md](VOCABULARY.md)** The 62 terms that recur across these prompts and travel between subjects, what each one does, and the seven that a finding here measured *not* doing what they say.

**[Settings, and what the seeds are worth to you → REPRODUCING.md](REPRODUCING.md)** The exact call behind all 475 images, and the limit on it: `fal-ai/krea-2/turbo` exposes no step count, no CFG, no sampler and no scheduler, so **these seeds reproduce on that endpoint and not in your local graph.** The prompts transfer; the seeds do not.

**[How to ask this model for a style → styles/](styles/README.md)** The eight "whole scene drawn as ..." clauses from the Reddit post, the picture-book trap, the three styles that never converted, and an earlier sweep with a FLUX.1 dev cross-check.

## 🗂 类别

[photography](docs/gallery-part-1.md#photography) 18 · [typography](docs/gallery-part-1.md#typography) 15 · [product](docs/gallery-part-1.md#product) 18 · [illustration](docs/gallery-part-1.md#illustration) 18 · [reference-sheet](docs/gallery-part-1.md#reference-sheet) 1 · [isometric-3d](docs/gallery-part-1.md#isometric-3d) 10 · [editing](docs/gallery-part-1.md#editing) 5 · [portrait](docs/gallery-part-1.md#portrait) 8 · [infographic](docs/gallery-part-1.md#infographic) 8 · [collectible](docs/gallery-part-1.md#collectible) 5 · [stationery](docs/gallery-part-1.md#stationery) 6 · [food](docs/gallery-part-1.md#food) 9 · [interior](docs/gallery-part-1.md#interior) 10 · [pattern](docs/gallery-part-1.md#pattern) 8 · [brand-mark](docs/gallery-part-1.md#brand-mark) 7 · [miniature](docs/gallery-part-1.md#miniature) 8 · [coloring-page](docs/gallery-part-1.md#coloring-page) 6 · [ui](docs/gallery-part-1.md#ui) 1 · [stringcount](docs/gallery-part-1.md#stringcount) 8 · [animal](docs/gallery-part-1.md#animal) 10 · [landscape](docs/gallery-part-1.md#landscape) 10 · [fashion](docs/gallery-part-1.md#fashion) 7 · [automotive](docs/gallery-part-2.md#automotive) 7 · [exterior](docs/gallery-part-2.md#exterior) 8 · [abstract](docs/gallery-part-2.md#abstract) 7 · [objectcount](docs/gallery-part-2.md#objectcount) 7 · [monogram](docs/gallery-part-2.md#monogram) 2 · [poster](docs/gallery-part-2.md#poster) 9 · [still-life](docs/gallery-part-2.md#still-life) 8 · [macro-nature](docs/gallery-part-2.md#macro-nature) 8 · [street](docs/gallery-part-2.md#street) 8 · [night](docs/gallery-part-2.md#night) 7 · [respecify](docs/gallery-part-2.md#respecify) 2 · [hangul](docs/gallery-part-2.md#hangul) 4 · [sport](docs/gallery-part-2.md#sport) 6 · [scifi](docs/gallery-part-2.md#scifi) 8 · [underwater](docs/gallery-part-2.md#underwater) 8 · [aerial](docs/gallery-part-2.md#aerial) 3 · [period](docs/gallery-part-2.md#period) 8 · [jewellery](docs/gallery-part-2.md#jewellery) 8 · [fantasy](docs/gallery-part-2.md#fantasy) 9 · [comic](docs/gallery-part-2.md#comic) 7 · [childrens-book](docs/gallery-part-2.md#childrens-book) 8 · [technical-drawing](docs/gallery-part-2.md#technical-drawing) 8 · [vehicle](docs/gallery-part-2.md#vehicle) 10 · [weather](docs/gallery-part-2.md#weather) 8 · [glass](docs/gallery-part-2.md#glass) 8 · [material](docs/gallery-part-2.md#material) 5 · [crowd](docs/gallery-part-2.md#crowd) 8 · [weave](docs/gallery-part-2.md#weave) 7 · [tattoo](docs/gallery-part-2.md#tattoo) 7 · [pixel-art](docs/gallery-part-2.md#pixel-art) 7 · [anatomy](docs/gallery-part-3.md#anatomy) 8 · [sculpture](docs/gallery-part-3.md#sculpture) 8 · [plant](docs/gallery-part-3.md#plant) 10 · [tool](docs/gallery-part-3.md#tool) 8 · [knolling](docs/gallery-part-3.md#knolling) 5 · [silhouette](docs/gallery-part-3.md#silhouette) 7 · [mirror](docs/gallery-part-3.md#mirror) 7 · [mineral](docs/gallery-part-3.md#mineral) 8 · [seasonal](docs/gallery-part-3.md#seasonal) 8


## 🤝 参与贡献

提交 PR，在 `prompts.json` 中添加条目并附上你的输出图片。两条规则：提示词必须可复现，图片必须是未经编辑的原始输出。

## ⚖ 许可

提示词采用 MIT 许可。生成的图片受模型提供方条款约束，商用前请自行确认。
