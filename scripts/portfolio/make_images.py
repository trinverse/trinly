"""Rasterise the generated SVG artwork to PNG for the PPTX build.

Headless Chrome is used rather than a standalone SVG converter so the PNGs are
rendered by the same engine (and with the same web fonts) as the PDF.
"""
import os
import subprocess
import sys

from visuals import ART, DIAGRAMS

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&'
         'family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" '
         'rel="stylesheet">')
SIZES = {"cover": (240, 200)}
DEFAULT_ART = (200, 200)
DIAGRAM_SIZE = (690, 480)
SCALE = 2


def _shoot(svg, w, h, out, transparent):
    tmp = out + ".html"
    bg = "transparent" if transparent else "#fff"
    open(tmp, "w").write(
        f'<meta charset="utf-8">{FONTS}'
        f'<style>html,body{{margin:0;padding:0;background:{bg};width:{w}px;height:{h}px;'
        f'overflow:hidden}} svg{{display:block;width:{w}px;height:{h}px}}</style>{svg}')
    cmd = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
           f"--force-device-scale-factor={SCALE}",
           f"--window-size={w},{h}", "--virtual-time-budget=6000",
           f"--screenshot={out}", tmp]
    if transparent:
        cmd.insert(2, "--default-background-color=00000000")
    subprocess.run(cmd, capture_output=True)
    os.remove(tmp)
    if not os.path.exists(out):
        raise SystemExit(f"failed to render {out}")


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    made = []
    for name, fn in DIAGRAMS.items():
        out = os.path.join(outdir, f"diagram-{name}.png")
        _shoot(fn(), *DIAGRAM_SIZE, out, transparent=False)
        made.append(out)
    for name, fn in ART.items():
        w, h = SIZES.get(name, DEFAULT_ART)
        out = os.path.join(outdir, f"art-{name}.png")
        _shoot(fn(), w, h, out, transparent=True)
        made.append(out)
    for m in made:
        print(f"  {os.path.basename(m):<22} {os.path.getsize(m)//1024:>4} KB")
    return made


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "images")
