#!/usr/bin/env python3
"""Build both portfolio deliverables from one content model.

    python3 scripts/portfolio/build.py

Outputs, at the repository root:
    Trinly-Work-Portfolio.pdf    16:9 PDF  (render_html.py -> headless Chrome)
    Trinly-Work-Portfolio.pptx   editable  (build_pptx.py -> python-pptx)

Intermediates:
    assets/portfolio-pdf.html    the slide deck as HTML (matches capabilities-pdf.html)
    assets/portfolio-images/     PNGs rasterised from the SVG artwork, for the PPTX

Requires: python-pptx, Google Chrome.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HTML = os.path.join(ROOT, "assets", "portfolio-pdf.html")
IMGDIR = os.path.join(ROOT, "assets", "portfolio-images")
PDF = os.path.join(ROOT, "Trinly-Work-Portfolio.pdf")
PPTX = os.path.join(ROOT, "Trinly-Work-Portfolio.pptx")

CREDITS = """# Portfolio deck artwork — credits

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
"""


def run(cmd, what):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"{what} failed:\n{r.stderr[-2000:]}")


def main():
    os.chdir(HERE)
    import build_pptx
    import make_images
    from render_html import build_html

    print("1/4  rendering slide HTML")
    os.makedirs(os.path.dirname(HTML), exist_ok=True)
    open(HTML, "w").write(build_html())

    print("2/4  printing PDF via headless Chrome")
    run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         "--virtual-time-budget=10000", f"--print-to-pdf={PDF}", HTML], "chrome")

    print("3/4  rasterising artwork")
    make_images.main(IMGDIR)
    open(os.path.join(IMGDIR, "CREDITS.md"), "w").write(CREDITS)

    print("4/4  building PPTX")
    build_pptx.build(PPTX, IMGDIR)

    for f in (PDF, PPTX):
        print(f"     {os.path.relpath(f, ROOT):<32} {os.path.getsize(f) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
