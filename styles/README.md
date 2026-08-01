# Styles — how to ask this model for one

[← back to the catalog](../README.md)

This page mirrors [the Reddit post](https://www.reddit.com/r/StableDiffusion/comments/1vco6ra/) so that what it promised is one click away: the clauses, the failures, the seeds, the wildcards file.

## The rule

**Name a style and the model may draw it as an object in the scene. Describe the whole scene as the medium and the entire frame converts.**

Asked for *children's picture book drawing* as a style, the model drew a children's picture book and put it on the table. Same length, phrased as an instruction, and the whole frame converts:

<img src="images/cafe/book-named.webp" width="330" alt="named: a picture book appears on the table">
<img src="images/cafe/book-rephrased.webp" width="330" alt="rephrased: the whole frame converts">

- named — `Children's picture book drawing, soft crayon and gouache, simple rounded shapes, gentle flat colour.`
- rephrased — `Drawn the way a children's picture book is drawn: soft crayon and gouache, simple rounded shapes, flat gentle colour.`

## Eight clauses that convert the whole frame

One subject, seed `77220`, the clause is the only variable. Each is ~100 characters; they are plain English and carry nothing model-specific.

<img src="images/cafe/manga.webp" width="330" alt="Manga">

**Manga** — `The whole scene drawn as black-and-white manga: ink linework, screentone shading, no colour anywhere.`

<img src="images/cafe/storybook.webp" width="330" alt="Watercolour storybook">

**Watercolour storybook** — `The whole scene as a watercolour storybook illustration: soft washes, gentle linework, painted background.`

<img src="images/cafe/comicink.webp" width="330" alt="Comic book">

**Comic book** — `The whole scene as comic-book art: bold ink outlines, flat colour, halftone dots, drawn background.`

<img src="images/cafe/chibi.webp" width="330" alt="Chibi">

**Chibi** — `The whole scene drawn chibi: super-deformed proportions, huge head, tiny body, flat cel colour throughout.`

<img src="images/cafe/poster.webp" width="330" alt="Gouache travel poster">

**Gouache travel poster** — `The whole scene as a vintage gouache travel poster: flat opaque paint, simplified shapes, limited warm palette.`

<img src="images/cafe/retroanime.webp" width="330" alt="70s cel anime">

**70s cel anime** — `The whole scene as a 1970s cel anime frame: hand-painted cels, muted palette, film grain, painted background.`

<img src="images/cafe/popart.webp" width="330" alt="Pop art">

**Pop art** — `Printed the way pop art is printed: bold black outlines, flat primary colour, visible halftone dots.`

<img src="images/cafe/sixties.webp" width="330" alt="Mid-century cartoon">

**Mid-century cartoon** — `The whole scene as a 1960s limited-animation cartoon: angular flat shapes, off-register colour, painted backdrop.`

All eight, one per line, for a ComfyUI wildcard or dynamic-prompt node: [`wildcards/styles.txt`](../wildcards/styles.txt)

The subject prompt behind every image:

```
A pretty young woman sitting at an outdoor cafe table in the late afternoon, holding an iced drink up near her face. Long dark hair, a thin white summer top, small gold earrings. Waist-up, facing the camera, warm side light, the street softly out of focus behind her.
```

## The ones that never converted

Three styles arrived as *things* no matter how they were phrased. If the style name is also an object, expect the object.

<img src="images/cafe/rubberhose-guest.webp" width="330" alt="a rubber-hose character seated next to her">
<img src="images/cafe/doodle-twin.webp" width="330" alt="a doodled second her beside the photo">

- **rubber hose** — asked for rubber-hose style; it seated a rubber-hose character next to her
- **doodle** — asked for a doodle of the scene; it doodled a second her beside the photograph
- **mosaic** — three phrasings - named, a 685-character description, and 'no photographic surface anywhere' - all return a mosaic tabletop or grout drawn on the photo:

<img src="images/cafe/mosaic-named.webp" width="220" alt="mosaic attempt">
<img src="images/cafe/mosaic-long.webp" width="220" alt="mosaic attempt">
<img src="images/cafe/mosaic-explicit.webp" width="220" alt="mosaic attempt">

Caveats: one seed, one subject, so one sample per cell; everything judged at full size. Correction from the thread: manga and pop art only half-convert — the figure turns, the street stays a photo, and three stronger phrasings at the same seed did not fix it, so it is 6 of 8.

## Appendix — the earlier sweep

An earlier version of this page varied the style clause over a different subject (two women in a lantern river). Its data is still real and lives in [`sweep.json`](sweep.json): 15 clauses reproduced, 5 failed on that subject, 7 printing-process styles failed on a subject before that, and the same refusals reproduced on FLUX.1 dev at the same seed — so none of this is one endpoint being odd. Those older clauses are kept in [`wildcards/styles-extra.txt`](../wildcards/styles-extra.txt). The long-descriptor comparison started from [this wildcards thread](https://www.reddit.com/r/StableDiffusion/comments/1uzdj7o/krea_2_styles_wildcards_txt/), whose 660-character clauses are worth having regardless.
