# How this compares

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
- **Nobody publishes what it cost.** jamez does record `creation_tool` (Sora on 97 of 100 cases, GPT-4o on 3) and freestylefly documents its generation path, which is more than the others. But neither states a figure.
- **Credit where it is due on reproducibility.** freestylefly commits 549 images and jamez 100, both with relative paths and copy-pasteable prompts. Those two are self-contained and I am not claiming otherwise.
- **Link rot is not hypothetical.** ZeroLu's 86 images are all external. Requesting them on 2026-07-25 found three already gone. Two Twitter CDN links returning 403/404 and one path that no longer exists in the repo. That is why the images here are committed rather than linked.
- **Scale claims deserve reading twice.** The two YouMind repos advertise 14,916 and 13,663 prompts. Their own FAQ says images live on a CMS, not in git, and their README says GitHub's length limit caps the visible list, 129 and 126 entries respectively, under 1% of the headline number. The rest are on their website.
- jamez-bondos has not been pushed since 2025-05-26.

Back to [the catalog](../README.md).
