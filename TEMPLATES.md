# Templates

Slot-and-fill recipes, the way a reader actually reuses a catalog. Every one of them is here because something in this repository measured it, and each names that evidence. Nothing was turned into a template because it looked like it would generalise.

*A template is a shape, not a guarantee. The evidence column says what was tested and how widely; a recipe measured on one subject at one seed is an observation, not a rate.*

6 of them. Every prompt in the catalog is a finished sentence; these are the shapes underneath the ones that were tested.

## 1. Convert the whole frame to a drawn medium

```text
[medium] of [subject]
```

| slot | what goes in it |
|---|---|
| `[medium]` | hand-drawn black and white manga · a watercolour storybook illustration · a mosaic fresco |
| `[subject]` | what is in the picture, with no lens, focus, camera or lighting words in it |

Naming a style makes the model draw the style as an object in a photograph. Leading with the medium, and stripping the photographic vocabulary out of the subject, converts the whole frame including the background.

**Evidence** [the styles page](styles/README.md) · **tested on** 11 clauses at one seed and one subject, all 11 converted, including three previously recorded as impossible
 · **ready-made** [`wildcards/styles.txt`](wildcards/styles.txt)

---

## 2. Make a texture visible

```text
[subject], raking light across [the surface]
```

| slot | what goes in it |
|---|---|
| `[the surface]` | the thing whose texture you want: the plaster, the fabric, the solder joint |

Light skimming at a shallow angle is the most reused lighting phrase in this catalog.

**Evidence** [`raking light`](VOCABULARY.md) · **tested on** 27 entries across 14 categories

---

## 3. Ask for light without summoning the fixture

```text
[subject], [what the light does], never [the name of the lamp]
```

| slot | what goes in it |
|---|---|
| `[what the light does]` | soft even light · hard light from frame right · overcast light |
| `[the name of the lamp]` | softbox, ring light, window |

Name a fixture and the fixture walks into the frame.

**Evidence** [Name a light and you get the light. Name the softbox and you get the softbox.](FINDINGS.md) · **tested on** the lighting category, plus 7 window-light and 7 fluorescent entries where the fixture is visible

---

## 4. Change the medium of an image you already have

```text
Re-render this [subject] as [medium]: [what the medium looks like]
```

| slot | what goes in it |
|---|---|
| `[medium]` | a gouache painting · a cyanotype blueprint |
| `[what the medium looks like]` | visible brush loading, paper tooth, no photographic grain |

Image-to-image converts medium reliably at strength 0.50 to 0.60 and does not reliably add or remove objects.

**Evidence** [It changes medium willingly and scene content reluctantly](FINDINGS.md) · **tested on** 5 editing entries, plus 5 re-runs against sources they were not derived from: 2 held, 2 partial, 1 failed

---

## 5. Put text in the image

```text
[subject] reading exactly "[the string]"
```

| slot | what goes in it |
|---|---|
| `[the string]` | every character you want, written out. The model will not invent one for you |

It renders any string you write out, at any count, and invents nothing.

**Evidence** [It renders text you write. It cannot invent text.](FINDINGS.md) · **tested on** the typography and stringcount categories; nine station names written out, four rendered correctly at small or rotated sizes

---

## 6. Constrain the palette

```text
[subject], limited palette: [name each colour]
```

| slot | what goes in it |
|---|---|
| `[name each colour]` | ink black, bone white, one ochre. Name them, do not count them |

Objects count correctly from 2 to 8. Attributes do not: "exactly two flat colours" returned four.

**Evidence** [It counts objects. It does not count attributes.](FINDINGS.md) · **tested on** 8 limited-palette entries across 4 categories, and the objectcount ladder

---

## What is not here

A template for every entry. Deciding which clause of a prompt is the substitutable one is a claim about the model, and making that claim 475 times without testing it once is how this catalog got two findings wrong before. If you substitute into one of these and it breaks, that is worth an issue: it is a measurable thing and nobody has measured it yet.
