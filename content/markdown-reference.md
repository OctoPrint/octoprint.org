---
title: "Every markdown element, on one page"
date: 2026-07-10
author: "Kevin"
description: "A reference article that exercises every element Liftoff styles. Each section shows the markdown source first, then how it renders."
tags: ["reference", "design"]
categories: ["Reference"]
image: "/img/pipeline.svg"
---

<!-- markdownlint-configure-file {
  "MD010": false,
  "MD014": false,
  "MD028": false,
  "MD029": false,
  "MD040": false
} -->

This article exists to be ugly on purpose. It runs through every
markdown element the theme styles, so you can check typography,
spacing, and dark-mode contrast in one place. If something looks wrong
here, it will look wrong in your content too.

Every section shows the source first, then the result.

<!--more-->

## Headings

Liftoff renders `h1` only for the article title, so body content should
start at `h2`.

```markdown
## Second level
### Third level
#### Fourth level
##### Fifth level
###### Sixth level is uppercase
```

### Third level

Third level is where most nesting stops being useful.

#### Fourth level

##### Fifth level

###### Sixth level is uppercase

## Emphasis and inline elements

```markdown
Regular text with **bold**, *italic*, ***both***, `inline code`,
~~struck-through text~~ and <mark>highlighted text</mark>.

Abbreviations like <abbr title="Static Site Generator">SSG</abbr> get a
dotted underline. Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.

A line ending in two spaces  
forces a break without starting a new paragraph.
```

Regular text with **bold**, *italic*, ***both***, `inline code`,
~~struck-through text~~ and <mark>highlighted text</mark>.

Abbreviations like <abbr title="Static Site Generator">SSG</abbr> get a
dotted underline. Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.

A line ending in two spaces  
forces a break without starting a new paragraph.

## Links

```markdown
An [inline link](/docs), one [with a title](/docs "Theme docs"), a bare
autolink <https://gohugo.io/>, and a [reference link][hugo].

[hugo]: https://gohugo.io/
```

An [inline link](/docs), one [with a title](/docs "Theme docs"), a bare
autolink <https://gohugo.io/>, and a [reference link][hugo].

[hugo]: https://gohugo.io/

Root-relative links are resolved per language, so write `/docs`, not
`/en/docs`.

## Lists

```markdown
- Design tokens live in `tokens.css`
- Components live in `assets/css/components/`
  - One file per component
  - Imported from `main.css`
- Fonts are loaded outside the bundle
```

- Design tokens live in `tokens.css`
- Components live in `assets/css/components/`
  - One file per component
  - Imported from `main.css`
- Fonts are loaded outside the bundle

```markdown
1. Add the theme as a module
2. Copy a blueprint into `content/`
3. Replace the copy with your own
4. Ship
```

1. Add the theme as a module
2. Copy a blueprint into `content/`
3. Replace the copy with your own
4. Ship

An ordered list can start anywhere:

```markdown
7. Seventh
8. Eighth
```

7. Seventh
8. Eighth

Task lists drop the bullet and render a disabled checkbox:

```markdown
- [x] Ship the layout
- [x] Ship the docs
- [ ] Ship the search index
```

- [x] Ship the layout
- [x] Ship the docs
- [ ] Ship the search index

Definition lists:

```markdown
Hugo
: The static site generator this theme targets.

Iconify
: The icon API the theme fetches from at build time.
```

Hugo
: The static site generator this theme targets.

Iconify
: The icon API the theme fetches from at build time.

## Blockquotes

```markdown
> A theme should be a starting point, not a cage. If you have to fork
> it to change a colour, it failed.
>
> > Quotes nest, though rarely usefully.
```

> A theme should be a starting point, not a cage. If you have to fork
> it to change a colour, it failed.
>
> > Quotes nest, though rarely usefully.

## Callouts

A blockquote starting with an alert marker becomes a callout. The label
is translated, so it follows the page language.

```markdown
> [!NOTE]
> Neutral context. Use it for background the reader can skip.

> [!TIP]
> A shortcut or a better way to do the thing.

> [!WARNING]
> Something that will bite you later if you ignore it.

> [!DANGER]
> Something that will break your build right now.
```

> [!NOTE]
> Neutral context. Use it for background the reader can skip.

> [!TIP]
> A shortcut or a better way to do the thing.

> [!WARNING]
> Something that will bite you later if you ignore it.

> [!DANGER]
> Something that will break your build right now.

`[!CAUTION]` is accepted as an alias for `[!DANGER]`.

## Code

A fence with a language gets a label and a copy button.

````markdown
```bash
hugo server --source exampleSite --themesDir ../..
```
````

```bash
hugo server --source exampleSite --themesDir ../..
```

Another language, to check the highlighting theme:

````markdown
```go
func main() {
	site := hugo.New()
	site.Render()
}
```
````

```go
func main() {
	site := hugo.New()
	site.Render()
}
```

A fence with no language falls back to plain text:

````markdown
```
$ hugo mod get codeberg.org/head1328/hugo-liftoff
```
````

```
$ hugo mod get codeberg.org/head1328/hugo-liftoff
```

A long line, to check horizontal scrolling:

```json
{"module":{"imports":[{"path":"codeberg.org/head1328/hugo-liftoff","disable":false,"ignoreConfig":false,"ignoreImports":false}]}}
```

Diffs keep their markers:

```diff
-  --color-accent: #22d3ee;
+  --color-accent: #f97316;
```

## Tables

Colons in the separator row set the alignment.

```markdown
| Token            | Purpose                    | Light mode |
| :--------------- | :------------------------: | ---------: |
| `--color-bg`     | Page background            |        Yes |
| `--color-accent` | Links, buttons, highlights |        Yes |
| `--space-4`      | Default vertical rhythm    |         No |
```

| Token            | Purpose                    | Light mode |
| :--------------- | :------------------------: | ---------: |
| `--color-bg`     | Page background            |        Yes |
| `--color-accent` | Links, buttons, highlights |        Yes |
| `--space-4`      | Default vertical rhythm    |         No |

## Images

A plain image sits on its own line. Wrap it in a `figure` when you want
a caption.

```markdown
![Content feeding layouts, producing a public directory](/img/pipeline.svg)

<figure>
  <img src="/img/pipeline.svg" alt="Content feeding layouts, producing a public directory">
  <figcaption>Markdown in, static HTML out.</figcaption>
</figure>
```

<figure>
  <img src="/img/pipeline.svg" alt="Content feeding layouts, producing a public directory">
  <figcaption>Markdown in, static HTML out.</figcaption>
</figure>

> [!NOTE]
> That SVG is a placeholder shipped with the demo. Replace it with your
> own asset under `static/` or a page bundle.

## Collapsible sections

```markdown
<details>
  <summary>Why is there no search?</summary>

Search needs either an index shipped to the client or a hosted service.

</details>
```

<details>
  <summary>Why is there no search?</summary>

Search needs either an index shipped to the client or a hosted service.
Both are opinionated enough that they belong in your site, not in the
theme.

</details>

## Footnotes

```markdown
Liftoff fetches icons at build time.[^1]

[^1]: The fetched SVGs are cached by Hugo.
```

Liftoff fetches icons at build time rather than shipping an icon
font.[^1] That keeps the payload to the handful of glyphs a page
actually uses.

## Horizontal rule and escaping

```markdown
---

Escape a character with a backslash: \*not italic\*, \# not a heading.
```

---

Escape a character with a backslash: \*not italic\*, \# not a heading.

If you made it here and everything read cleanly, the typography is
doing its job.

[^1]: The fetched SVGs are cached by Hugo, so repeat builds do not hit
    the network.
