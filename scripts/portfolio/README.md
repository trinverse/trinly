# Work portfolio deck

Builds `Trinly-Work-Portfolio.pdf` and `Trinly-Work-Portfolio.pptx` at the
repository root — the Trinly × ArtSync portfolio of shipped work.

```bash
python3 scripts/portfolio/build.py
```

Requires `python-pptx` and Google Chrome.

## Where to edit

**All copy lives in `content.py`.** Both renderers read it, so the PowerPoint
and the PDF cannot fall out of sync. Edit there, never in the renderers.

| File | Role |
|---|---|
| `content.py` | Every word of the deck, as a list of typed slide dicts |
| `visuals.py` | SVG artwork — 5 architecture diagrams, 6 domain glyphs, all in-house |
| `render_html.py` | Slides → HTML (`assets/portfolio-pdf.html`) → Chrome → PDF |
| `make_images.py` | SVG → PNG via headless Chrome, for embedding in the PPTX |
| `build_pptx.py` | Slides → editable PowerPoint via python-pptx |
| `build.py` | Runs all of the above |

## Slide types

`cover`, `two_card`, `grid`, `table`, `story`, `proof`, `steps`, `feature`,
`two_col_list`, `two_col_pills`, `closing`. Adding a slide means appending a
`slide(type=...)` call in `content.py`; adding a *new* type means writing one
renderer in each of `render_html.py` and `build_pptx.py`.

## Notes

- Diagrams are redrawn from each project's own README (`../helix`, `../sentinel`,
  `../cortex`, `../rdactd`, `../oac`) — keep them accurate if those change.
- No third-party imagery is used anywhere. See `assets/portfolio-images/CREDITS.md`.
- The PPTX deliberately uses Arial / Courier New; see the note in `build_pptx.py`.
