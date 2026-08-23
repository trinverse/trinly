"""Build the editable PowerPoint deck from the same content model as the PDF.

Text is native PowerPoint text (so it can be edited or excerpted); the
architecture diagrams and domain glyphs are PNGs rendered from the SVG artwork
in visuals.py.

Fonts: Arial and Courier New are used deliberately. The PDF uses Sora / Inter /
JetBrains Mono, but those are not installed on most machines, and PowerPoint
substitutes silently and badly. If the recipient has the Google fonts installed,
set F_HEAD/F_BODY/F_MONO below to "Sora"/"Inter"/"JetBrains Mono".
"""
import copy
import os

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

from content import META, SLIDES

F_HEAD, F_BODY, F_MONO = "Arial", "Arial", "Courier New"

EMU_PX = 9525
SLIDE_W, SLIDE_H = 1280, 720
M, W = 64, 1152

ACCENT = RGBColor(0x7C, 0x3A, 0xED)
ACCENT2 = RGBColor(0x4F, 0x46, 0xE5)
INK = RGBColor(0x0A, 0x0A, 0x1A)
BODYC = RGBColor(0x3A, 0x3A, 0x5C)
MUT = RGBColor(0x64, 0x64, 0x8A)
FAINT = RGBColor(0xA0, 0xA0, 0xB8)
BORD = RGBColor(0xE0, 0xE0, 0xEC)
SOFT = RGBColor(0xFB, 0xFA, 0xFE)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def E(px):
    return Emu(int(round(px * EMU_PX)))


def P(px):
    """HTML px -> points (both at 96 dpi / 72 pt per inch)."""
    return Pt(px * 0.75)


def spacing(run, hundredths):
    """Letter-spacing, which python-pptx does not expose."""
    run.font._rPr.set("spc", str(int(hundredths)))


# --------------------------------------------------------------------------

def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    return tf


def para(tf, text, px, *, font=None, bold=False, color=BODYC, line=1.35,
         before=0, after=0, first=False, spc=None, align=None):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.line_spacing = line
    if before:
        p.space_before = P(before)
    if after:
        p.space_after = P(after)
    if align:
        p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = P(px)
    r.font.bold = bold
    r.font.name = font or F_BODY
    r.font.color.rgb = color
    if spc:
        spacing(r, spc)
    return p


def rect(slide, x, y, w, h, *, fill=None, line=None, radius=None, width=1.1):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        E(x), E(y), E(w), E(h))
    if radius:
        shape.adjustments[0] = min(0.5, radius / min(w, h))
    if fill is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(width)
    shape.shadow.inherit = False
    style = shape._element.find(qn("p:style"))
    if style is not None:
        shape._element.remove(style)
    shape.text_frame.word_wrap = True
    return shape


def eyebrow(slide, y, text, px=8.5, color=ACCENT, spc=150):
    # Courier New is lighter than JetBrains Mono, so these run bold to match the PDF
    tf = textbox(slide, M, y, W, 18)
    para(tf, text.upper(), px, font=F_MONO, bold=True, color=color, spc=spc, first=True)


def head(slide, s, *, lead_w=900):
    if s.get("number"):
        eyebrow(slide, 52, s["number"])
    tf = textbox(slide, M, 70, W, 54)
    para(tf, s["title"], 34, font=F_HEAD, bold=True, color=INK, line=1.06, first=True)
    rect(slide, M, 128, 54, 3, fill=ACCENT, radius=1.5)
    if s.get("lead"):
        tf = textbox(slide, M, 146, lead_w, 46)
        para(tf, s["lead"], 14.5, color=MUT, line=1.5, first=True)


def footer(slide, i, n):
    tf = textbox(slide, M, 684, 700, 14)
    para(tf, META["footer"], 9.5, font=F_MONO, color=FAINT, first=True)
    tf = textbox(slide, SLIDE_W - M - 120, 684, 120, 14)
    para(tf, f"{i:02d} / {n:02d}", 9.5, font=F_MONO, color=ACCENT,
         align=PP_ALIGN.RIGHT, first=True)


def bullets(slide, x, y, w, items, px=12.8, gap=11, sq=7):
    """Bulleted list with a violet square marker, laid out as real text."""
    tf = textbox(slide, x + 20, y, w - 20, 400)
    for i, t in enumerate(items):
        para(tf, t, px, color=BODYC, line=1.45, after=gap * 0.75, first=(i == 0))
    return tf


def picture(slide, path, x, y, w, h):
    slide.shapes.add_picture(path, E(x), E(y), E(w), E(h))


def set_bullet(p, char="▪", color=ACCENT, indent=20):
    """Native PowerPoint bullet, so wrapped lines hang correctly."""
    from pptx.oxml.ns import qn
    pPr = p._pPr if p._pPr is not None else p._p.get_or_add_pPr()
    pPr.set("marL", str(int(indent * EMU_PX)))
    pPr.set("indent", str(int(-indent * EMU_PX)))
    clr = pPr.makeelement(qn("a:buClr"), {})
    srgb = clr.makeelement(qn("a:srgbClr"), {"val": f"{color.__str__()}"})
    clr.append(srgb)
    fnt = pPr.makeelement(qn("a:buFont"), {"typeface": F_BODY})
    bu = pPr.makeelement(qn("a:buChar"), {"char": char})
    for el in (clr, fnt, bu):
        pPr.append(el)


def bullet_list(slide, x, y, w, h, items, px=12.8, after=9, char="▪"):
    tf = textbox(slide, x, y, w, h)
    for i, t in enumerate(items):
        p = para(tf, t, px, color=BODYC, line=1.42, after=after, first=(i == 0))
        set_bullet(p, char=char)
    return tf


def label(slide, x, y, w, text, color=ACCENT, px=8.5, spc=120):
    tf = textbox(slide, x, y, w, 16)
    para(tf, text.upper(), px, font=F_MONO, bold=True, color=color, spc=spc, first=True)


def card(slide, x, y, w, h, title, body, *, tone="plain", title_px=15.5, body_px=12.4):
    fill, line = (SOFT, RGBColor(0xD8, 0xCF, 0xF8)) if tone == "soft" else (WHITE, BORD)
    rect(slide, x, y, w, h, fill=fill, line=line, radius=13)
    tf = textbox(slide, x + 20, y + 19, w - 40, h - 34)
    para(tf, title, title_px, font=F_HEAD, bold=True, color=INK, line=1.2, after=7, first=True)
    para(tf, body, body_px, color=MUT, line=1.5)


def glow(slide):
    """PowerPoint has no radial gradient here; a hard-edged oval reads worse
    than clean white, so the cover and closing slides stay flat."""
    return


import math


def est_h(text, px, w, line=1.45):
    """Rough wrapped-text height, used to stack rows without a layout engine."""
    cpl = max(8, int(w / (px * 0.505)))
    lines = max(1, math.ceil(len(text) / cpl))
    return lines * px * line


# --------------------------------------------------------------------------
# slide renderers
# --------------------------------------------------------------------------

def s_cover(slide, s, img):
    glow(slide)
    picture(slide, img("art-cover"), 930, 250, 240, 200)
    eyebrow(slide, 252, s["eyebrow"])
    tf = textbox(slide, M, 272, 820, 80)
    para(tf, s["title"], 64, font=F_HEAD, bold=True, color=INK, line=1.02, first=True)
    tf = textbox(slide, M, 366, 760, 34)
    para(tf, s["subtitle"], 21, font=F_HEAD, bold=True, color=ACCENT2, line=1.2, first=True)
    tf = textbox(slide, M, 410, 620, 70)
    para(tf, s["blurb"], 14.5, color=MUT, line=1.55, first=True)
    tf = textbox(slide, M, 608, 700, 60)
    for i, t in enumerate((META["founder"], META["email"])):
        para(tf, t, 11.5, font=F_MONO, color=MUT, line=1.5, first=(i == 0), spc=60)


def s_two_card(slide, s, img):
    head(slide, s)
    y, h = 214, 320
    for i, c in enumerate(s["cards"]):
        x = M + i * 592
        rect(slide, x, y, 560, h, fill=SOFT, line=BORD, radius=16)
        tf = textbox(slide, x + 26, y + 24, 500, 36)
        para(tf, c["name"], 26, font=F_HEAD, bold=True, color=INK, first=True)
        pill = rect(slide, x + 26, y + 72, 16 + len(c["tag"]) * 7.0, 26,
                    fill=WHITE, line=RGBColor(0xD8, 0xCF, 0xF8), radius=12)
        ptf = pill.text_frame
        ptf.margin_left = ptf.margin_right = ptf.margin_top = ptf.margin_bottom = 0
        ptf.vertical_anchor = MSO_ANCHOR.MIDDLE
        para(ptf, c["tag"].upper(), 8, font=F_MONO, bold=True, color=ACCENT, spc=90,
             align=PP_ALIGN.CENTER, first=True)
        tf = textbox(slide, x + 26, y + 112, 500, 120)
        para(tf, c["body"], 13, color=MUT, line=1.55, first=True)
        tf = textbox(slide, x + 26, y + 244, 500, 20)
        para(tf, c["link"], 11, font=F_MONO, color=ACCENT2, first=True, spc=40)
    for i, (n, l) in enumerate(s["stats"]):
        x = M + i * 190
        tf = textbox(slide, x, 578, 180, 44)
        para(tf, n, 36, font=F_HEAD, bold=True, color=ACCENT, line=1.0, first=True)
        tf = textbox(slide, x, 626, 180, 20)
        para(tf, l, 11.5, color=MUT, first=True)


def s_grid(slide, s, img):
    head(slide, s)
    cols = s.get("columns", 4)
    cards = s["cards"]
    rows = -(-len(cards) // cols)
    row_h = s.get("row_h") or (168 if cols <= 3 else 230)
    gap = 14
    cw = (W - gap * (cols - 1)) / cols
    total = rows * row_h + (rows - 1) * gap
    y0 = 214 + max(0, (446 - total) / 2)
    for i, (t, b) in enumerate(cards):
        x = M + (i % cols) * (cw + gap)
        y = y0 + (i // cols) * (row_h + gap)
        card(slide, x, y, cw, row_h, t, b)


def s_table(slide, s, img):
    head(slide, s)
    widths = s.get("widths") or [100 / len(s["head"])] * len(s["head"])
    xs, acc = [], M
    for p in widths:
        xs.append(acc)
        acc += W * p / 100
    y = 210
    for i, h in enumerate(s["head"]):
        label(slide, xs[i], y, W * widths[i] / 100 - 14, h)
    y += 22
    rect(slide, M, y, W, 1.5, fill=RGBColor(0xD8, 0xCF, 0xF8))
    y += 14
    for row in s["rows"]:
        hh = max(est_h(c, 12.6 if i else 13.5, W * widths[i] / 100 - 16)
                 for i, c in enumerate(row))
        for i, c in enumerate(row):
            tf = textbox(slide, xs[i], y + 2, W * widths[i] / 100 - 16, hh + 6)
            para(tf, c, 13.5 if i == 0 else 12.6, font=F_HEAD if i == 0 else F_BODY,
                 bold=(i == 0), color=INK if i == 0 else MUT, line=1.45, first=True)
        y += hh + 24
        rect(slide, M, y - 10, W, 0.75, fill=RGBColor(0xED, 0xEC, 0xF5))


def s_story(slide, s, img):
    picture(slide, img(f"art-{s['visual']}"), 1046, 40, 176, 176)
    eyebrow(slide, 52, s["number"])
    tf = textbox(slide, M, 72, 900, 22)
    para(tf, s["project"], 15, font=F_HEAD, bold=True, color=ACCENT, first=True)
    tf = textbox(slide, M, 98, 940, 44)
    para(tf, s["title"], 34, font=F_HEAD, bold=True, color=INK, line=1.1, first=True)
    eyebrow(slide, 148, s["kicker"], px=8, color=RGBColor(0x88, 0x88, 0xA0), spc=120)
    label(slide, M, 186, 340, "The context")
    tf = textbox(slide, M, 206, 340, 120)
    para(tf, s["context"], 12.8, color=MUT, line=1.55, first=True)
    y2 = 206 + est_h(s["context"], 12.8, 330, 1.6) + 26
    label(slide, M, y2, 340, "The problem")
    tf = textbox(slide, M, y2 + 20, 340, 160)
    para(tf, s["problem"], 12.8, color=MUT, line=1.55, first=True)
    label(slide, 438, 186, 700, "What we built")
    bullet_list(slide, 438, 206, 778, 340, s["built"], px=12.8, after=9)
    hb_y, hb_h = 556, 104
    rect(slide, M, hb_y, W, hb_h, fill=SOFT, line=None)
    rect(slide, M, hb_y, 3, hb_h, fill=ACCENT)
    label(slide, M + 20, hb_y + 16, 600, s["hard_title"])
    tf = textbox(slide, M + 20, hb_y + 36, W - 60, 60)
    para(tf, s["hard"], 12.8, color=BODYC, line=1.5, first=True)


def s_proof(slide, s, img):
    tf = textbox(slide, M, 52, 900, 22)
    para(tf, s["project"], 15, font=F_HEAD, bold=True, color=ACCENT, first=True)
    tf = textbox(slide, M, 76, 900, 44)
    para(tf, s["title"], 28, font=F_HEAD, bold=True, color=INK, first=True)
    rect(slide, M, 134, 54, 3, fill=ACCENT, radius=1.5)
    picture(slide, img(f"diagram-{s['diagram']}"), M, 150, 690, 480)
    rx, rw = 784, 432
    label(slide, rx, 146, rw, "Stack")
    y = 168
    for k, v in s["stack"]:
        hh = max(est_h(v, 11.6, rw - 116, 1.45), 16)
        tf = textbox(slide, rx, y + 2, 108, 16)
        para(tf, k.upper(), 8, font=F_MONO, bold=True, color=ACCENT, spc=70, first=True)
        tf = textbox(slide, rx + 112, y, rw - 112, hh + 4)
        para(tf, v, 11.6, color=BODYC, line=1.45, first=True)
        y += hh + 15
        rect(slide, rx, y - 7, rw, 0.75, fill=RGBColor(0xF0, 0xEF, 0xF7))
    y += 14
    label(slide, rx, y, rw, "Notable")
    bullet_list(slide, rx, y + 22, rw, 260, s["highlights"], px=11.6, after=8, char="›")


def s_steps(slide, s, img):
    head(slide, s)
    gap, h = 16, 300
    cw = (W - gap * 3) / 4
    y = 214 + (446 - h) / 2
    for i, (n, t, d) in enumerate(s["steps"]):
        x = M + i * (cw + gap)
        rect(slide, x, y, cw, h, fill=SOFT, line=BORD, radius=14)
        tf = textbox(slide, x + 22, y + 24, cw - 44, 34)
        para(tf, n, 26, font=F_MONO, bold=True, color=RGBColor(0xC4, 0xB5, 0xFD),
             first=True)
        tf = textbox(slide, x + 22, y + 70, cw - 44, 26)
        para(tf, t, 16, font=F_HEAD, bold=True, color=INK, line=1.2, first=True)
        tf = textbox(slide, x + 22, y + 104, cw - 44, 140)
        para(tf, d, 12.2, color=MUT, line=1.5, first=True)


def s_feature(slide, s, img):
    head(slide, s)
    tf = textbox(slide, M, 226, 1000, 80)
    para(tf, s["body"], 13.4, color=BODYC, line=1.55, first=True)
    y0 = 226 + est_h(s["body"], 13.4, 1000, 1.55) + 26
    for i, (t, d) in enumerate(s["points"]):
        x = M + (i % 2) * 588
        y = y0 + (i // 2) * 76
        tf = textbox(slide, x, y, 560, 20)
        para(tf, t, 13, font=F_HEAD, bold=True, color=INK, first=True)
        tf = textbox(slide, x, y + 22, 560, 34)
        para(tf, d, 11.5, color=MUT, line=1.4, first=True)
    py = y0 + 3 * 76 + 8
    x = M
    for t in s["tools"]:
        w = 20 + len(t) * 6.2
        sh = rect(slide, x, py, w, 26, fill=SOFT, line=RGBColor(0xD8, 0xCF, 0xF8), radius=13)
        ptf = sh.text_frame
        ptf.margin_left = ptf.margin_right = ptf.margin_top = ptf.margin_bottom = 0
        ptf.vertical_anchor = MSO_ANCHOR.MIDDLE
        para(ptf, t, 10, font=F_MONO, color=ACCENT, align=PP_ALIGN.CENTER, first=True)
        x += w + 8


def _dl_column(slide, x, w, y0, title, items):
    label(slide, x, y0, w, title)
    rect(slide, x, y0 + 20, w, 1.5, fill=RGBColor(0xD8, 0xCF, 0xF8))
    y = y0 + 34
    for t, d in items:
        tf = textbox(slide, x, y, w, 20)
        para(tf, t, 14, font=F_HEAD, bold=True, color=INK, first=True)
        hh = est_h(d, 12.4, w, 1.5)
        tf = textbox(slide, x, y + 22, w, hh + 6)
        para(tf, d, 12.4, color=MUT, line=1.5, first=True)
        y += 24 + hh + 18
        rect(slide, x, y - 10, w, 0.75, fill=RGBColor(0xF0, 0xEF, 0xF7))


def s_two_col_list(slide, s, img):
    head(slide, s)
    _dl_column(slide, M, 554, 212, s["left_title"], s["left"])
    _dl_column(slide, 660, 556, 212, s["right_title"], s["right"])


def s_two_col_pills(slide, s, img):
    head(slide, s)
    y0 = 212
    label(slide, M, y0, 400, s["left_title"])
    rect(slide, M, y0 + 20, 400, 1.5, fill=RGBColor(0xD8, 0xCF, 0xF8))
    y, x = y0 + 40, M
    for t in s["pills"]:
        w = 24 + len(t) * 6.6
        if x + w > M + 404:
            x, y = M, y + 38
        sh = rect(slide, x, y, w, 30, fill=SOFT, line=RGBColor(0xD8, 0xCF, 0xF8), radius=15)
        ptf = sh.text_frame
        ptf.margin_left = ptf.margin_right = ptf.margin_top = ptf.margin_bottom = 0
        ptf.vertical_anchor = MSO_ANCHOR.MIDDLE
        para(ptf, t, 12, color=ACCENT, align=PP_ALIGN.CENTER, first=True)
        x += w + 8
    tf = textbox(slide, M, y + 52, 400, 24)
    para(tf, s["pills_note"], 11.8, color=MUT, first=True)
    _dl_column(slide, 660, 556, y0, s["right_title"], s["reasons"])


def s_closing(slide, s, img):
    glow(slide)
    eyebrow(slide, 112, s["eyebrow"])
    tf = textbox(slide, M, 132, 820, 60)
    para(tf, s["title"], 46, font=F_HEAD, bold=True, color=INK, line=1.08, first=True)
    rect(slide, M, 202, 54, 3, fill=ACCENT, radius=1.5)
    tf = textbox(slide, M, 220, 680, 60)
    para(tf, s["lead"], 14.5, color=MUT, line=1.55, first=True)
    rect(slide, M, 318, 560, 150, fill=SOFT, line=RGBColor(0xD8, 0xCF, 0xF8), radius=18)
    tf = textbox(slide, M + 34, 348, 500, 28)
    para(tf, s["founder"], 19, font=F_HEAD, bold=True, color=INK, first=True)
    for i, (t, c) in enumerate(((s["email"], ACCENT2), (s["phones"], MUT))):
        tf = textbox(slide, M + 34, 388 + i * 28, 500, 22)
        para(tf, t, 12.5 if i != 1 else 11.5, font=F_MONO, color=c, first=True, spc=40)


RENDER = {
    "cover": s_cover, "two_card": s_two_card, "grid": s_grid, "table": s_table,
    "story": s_story, "proof": s_proof, "steps": s_steps, "feature": s_feature,
    "two_col_list": s_two_col_list, "two_col_pills": s_two_col_pills, "closing": s_closing,
}


def build(outfile, imgdir):
    def img(name):
        return os.path.join(imgdir, name + ".png")

    prs = Presentation()
    prs.slide_width, prs.slide_height = E(SLIDE_W), E(SLIDE_H)
    blank = prs.slide_layouts[6]
    n = len(SLIDES)
    for i, s in enumerate(SLIDES, 1):
        slide = prs.slides.add_slide(blank)
        RENDER[s["type"]](slide, s, img)
        if s["type"] != "cover":
            footer(slide, i, n)
    prs.core_properties.title = META["title"]
    prs.core_properties.author = META["founder"]
    prs.save(outfile)
    return outfile


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "portfolio.pptx"
    imgs = sys.argv[2] if len(sys.argv) > 2 else "images"
    print("wrote", build(out, imgs))
