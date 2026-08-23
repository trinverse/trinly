# Portfolio deck artwork — credits

Every visual in `Trinly-Work-Portfolio.pdf` / `.pptx` is generated in-house as
SVG by `scripts/portfolio/visuals.py`:

* `diagram-*.png` — architecture and data-flow diagrams, redrawn from each
  project's own README (../helix, ../sentinel, ../cortex, ../rdactd, ../oac).
* `art-*.png` — decorative domain glyphs for the project story slides.

**No third-party images are used.** There is no stock photography, no external
licence and no attribution requirement anywhere in the deck. If photography is
added later, record each file's source and licence in this file first.

These PNGs are build artefacts — regenerate them with
`python3 scripts/portfolio/build.py` rather than editing them by hand.
