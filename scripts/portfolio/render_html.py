"""Render the portfolio content model to a 16:9 slide deck in HTML.

The same HTML is printed to PDF by headless Chrome (build_pdf.py) and used as
the visual reference for the PPTX build.
"""
import html

from content import META, SLIDES
from visuals import ART, DIAGRAMS

E = html.escape

CSS = """
@page { size: 13.333in 7.5in; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; -webkit-print-color-adjust: exact;
             print-color-adjust: exact; }
body { font-family: 'Inter', -apple-system, 'Helvetica Neue', Arial, sans-serif; color: #0A0A1A; }

.slide { position: relative; width: 1280px; height: 720px; padding: 54px 64px 58px;
         page-break-after: always; overflow: hidden; background: #fff; display: flex;
         flex-direction: column; }
.slide:last-child { page-break-after: auto; }

.eyebrow { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px;
           letter-spacing: 2.4px; text-transform: uppercase; color: #7C3AED; margin: 0 0 10px; }
h1 { font-family: 'Sora', sans-serif; font-size: 64px; line-height: 1.05; font-weight: 700;
     letter-spacing: -1.6px; margin: 0; }
h2 { font-family: 'Sora', sans-serif; font-size: 34px; line-height: 1.14; font-weight: 700;
     letter-spacing: -0.7px; margin: 0; }
h3 { font-family: 'Sora', sans-serif; font-size: 15px; font-weight: 600; margin: 0 0 6px; }
.lead { font-size: 14.5px; line-height: 1.55; color: #64648A; max-width: 900px; margin: 12px 0 0; }
.rule { height: 3px; width: 54px; border-radius: 2px; margin: 16px 0 0;
        background: linear-gradient(90deg,#7C3AED,#4F46E5); }

.head { flex: 0 0 auto; }
.body { flex: 1 1 auto; display: flex; min-height: 0; margin-top: 26px; }

.foot { position: absolute; left: 64px; right: 64px; bottom: 24px; display: flex;
        justify-content: space-between; font-size: 9.5px; color: #A0A0B8;
        font-family: 'JetBrains Mono', monospace; letter-spacing: 0.4px; }
.pagenum { color: #7C3AED; }

/* cover + closing */
.cover { justify-content: center; }
.glow { position: absolute; width: 900px; height: 900px; border-radius: 50%; top: -420px;
        right: -260px; background: radial-gradient(circle, rgba(124,58,237,0.16), rgba(124,58,237,0) 62%); }
.glow2 { position: absolute; width: 700px; height: 700px; border-radius: 50%; bottom: -400px;
         left: -220px; background: radial-gradient(circle, rgba(79,70,229,0.13), rgba(79,70,229,0) 62%); }
.cover-sub { font-family: 'Sora', sans-serif; font-size: 21px; color: #4F46E5; margin: 20px 0 0;
             font-weight: 500; }
.cover-blurb { font-size: 14.5px; line-height: 1.6; color: #64648A; max-width: 620px; margin: 18px 0 0; }
.cover-meta { position: absolute; left: 64px; bottom: 54px; font-size: 11.5px; color: #64648A;
              font-family: 'JetBrains Mono', monospace; letter-spacing: 0.6px; }
.cover-art { position: absolute; right: 84px; top: 50%; transform: translateY(-50%); width: 300px; }

/* cards */
.grid { display: grid; gap: 14px; width: 100%; align-content: stretch;
        grid-auto-rows: 1fr; }
.card { border: 1px solid #E0E0EC; border-radius: 13px; padding: 20px 20px; background: #fff;
        display: flex; flex-direction: column; justify-content: center; }
.card h3 { color: #0A0A1A; font-size: 15.5px; margin-bottom: 8px; }
.card p { font-size: 12.4px; line-height: 1.55; color: #64648A; margin: 0; }
.card.accent { background: #FBFAFE; border-color: rgba(124,58,237,0.28); }

.stats { display: flex; gap: 54px; }
.stat .n { font-family: 'Sora', sans-serif; font-size: 36px; font-weight: 700;
           color: #7C3AED; line-height: 1; letter-spacing: -1px; }
.stat .l { font-size: 11.5px; color: #64648A; margin-top: 8px; }

.co { flex: 1; border: 1px solid #E0E0EC; border-radius: 16px; padding: 26px 26px 22px;
      background: linear-gradient(180deg,#FBFAFE,#fff); }
.co .name { font-family: 'Sora', sans-serif; font-size: 26px; font-weight: 700; }
.co .tag { display: inline-block; font-family: 'JetBrains Mono', monospace; font-size: 9.5px;
           letter-spacing: 1.2px; text-transform: uppercase; color: #7C3AED;
           background: rgba(124,58,237,0.09); border: 1px solid rgba(124,58,237,0.22);
           border-radius: 999px; padding: 4px 11px; margin: 10px 0 14px; }
.co p { font-size: 13px; line-height: 1.6; color: #64648A; margin: 0; }
.co .link { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4F46E5; margin-top: 16px; }

/* table */
table { width: 100%; border-collapse: collapse; }
th { text-align: left; font-family: 'JetBrains Mono', monospace; font-size: 9.5px; letter-spacing: 1.4px;
     text-transform: uppercase; color: #7C3AED; padding: 0 14px 10px 0; border-bottom: 1.5px solid rgba(124,58,237,0.25); }
td { padding: 13px 14px 13px 0; border-bottom: 1px solid #EDECF5; font-size: 12.6px;
     line-height: 1.5; color: #64648A; vertical-align: top; }
td.k { font-family: 'Sora', sans-serif; font-weight: 600; color: #0A0A1A; font-size: 13.5px; }

/* story */
.story-art { position: absolute; right: 56px; top: 40px; width: 176px; opacity: 0.95; }
.kicker { font-family: 'JetBrains Mono', monospace; font-size: 10px; letter-spacing: 1.8px;
          text-transform: uppercase; color: #8888A0; margin-top: 8px; }
.pname { font-family: 'Sora', sans-serif; font-size: 15px; font-weight: 700; color: #7C3AED;
         letter-spacing: 0.2px; }
.two { display: flex; gap: 34px; width: 100%; }
.col-l { width: 340px; flex: 0 0 340px; }
.col-r { flex: 1; }
.blocklabel { font-family: 'JetBrains Mono', monospace; font-size: 9.5px; letter-spacing: 1.6px;
              text-transform: uppercase; color: #7C3AED; margin: 0 0 8px; }
.blocktext { font-size: 12.8px; line-height: 1.62; color: #64648A; margin: 0; }
.hardbox { border-left: 3px solid #7C3AED; background: #FBFAFE; border-radius: 0 10px 10px 0;
           padding: 16px 20px; margin-top: 18px; }
.hardbox .blocktext { max-width: 1020px; }
.hardbox .blocktext { color: #3A3A5C; }
ul.bul { list-style: none; margin: 0; padding: 0; }
ul.bul li { position: relative; padding-left: 20px; font-size: 12.8px; line-height: 1.5;
            color: #3A3A5C; margin-bottom: 11px; }
ul.bul li:before { content: ''; position: absolute; left: 0; top: 7px; width: 7px; height: 7px;
                   border-radius: 2px; background: linear-gradient(135deg,#7C3AED,#4F46E5); }

/* proof */
.diagram { flex: 0 0 690px; }
.diagram svg { width: 690px; height: 480px; }
.proof-r { flex: 1; padding-left: 30px; }
.stacktbl { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
.stacktbl td { padding: 7px 0; border-bottom: 1px solid #F0EFF7; font-size: 11.6px; line-height: 1.45; }
.stacktbl td.lab { width: 108px; font-family: 'JetBrains Mono', monospace; font-size: 9.5px;
                   letter-spacing: 0.8px; text-transform: uppercase; color: #7C3AED; vertical-align: top;
                   padding-top: 9px; }
.stacktbl td.val { color: #3A3A5C; }
ul.hi { list-style: none; margin: 0; padding: 0; }
ul.hi li { position: relative; padding-left: 18px; font-size: 11.6px; line-height: 1.5;
           color: #64648A; margin-bottom: 9px; }
ul.hi li:before { content: '→'; position: absolute; left: 0; top: 0; color: #7C3AED; font-size: 11px; }

/* steps */
.steps { display: flex; gap: 16px; width: 100%; align-items: stretch; }
.step { flex: 1; border: 1px solid #E0E0EC; border-radius: 14px; padding: 24px 22px;
        background: linear-gradient(180deg,#FBFAFE,#fff); }
.step .n { font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 700;
           color: rgba(124,58,237,0.32); }
.step h3 { margin: 14px 0 8px; font-size: 16px; }
.step p { font-size: 12.2px; line-height: 1.55; color: #64648A; margin: 0; }

/* feature */
.feat-body { font-size: 13.4px; line-height: 1.62; color: #3A3A5C; }
.pointgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px 26px; margin-top: 20px; }
.point h3 { font-size: 13px; margin-bottom: 4px; }
.point p { font-size: 11.5px; line-height: 1.45; color: #64648A; margin: 0; }
.pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 22px; }
.pill { font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #7C3AED;
        background: rgba(124,58,237,0.08); border: 1px solid rgba(124,58,237,0.2);
        border-radius: 999px; padding: 6px 13px; }
.pill.big { font-family: 'Inter', sans-serif; font-size: 12px; padding: 8px 15px; }

/* definition lists */
.dl { margin: 0; }
.dl .row { padding: 15px 0; border-bottom: 1px solid #F0EFF7; }
.dl .row:last-child { border-bottom: none; }
.dl .t { font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #0A0A1A; }
.dl .d { font-size: 12.4px; line-height: 1.5; color: #64648A; margin-top: 4px; }
.colhead { font-family: 'JetBrains Mono', monospace; font-size: 9.5px; letter-spacing: 1.6px;
           text-transform: uppercase; color: #7C3AED; padding-bottom: 8px;
           border-bottom: 1.5px solid rgba(124,58,237,0.25); margin-bottom: 4px; }

/* closing */
.close-card { border: 1px solid rgba(124,58,237,0.25); border-radius: 18px; padding: 30px 34px;
              background: linear-gradient(135deg,#FBFAFE,#fff); max-width: 640px; margin-top: 30px; }
.close-card .who { font-family: 'Sora', sans-serif; font-size: 19px; font-weight: 700; }
.close-card .line { font-family: 'JetBrains Mono', monospace; font-size: 12.5px; color: #4F46E5;
                    margin-top: 12px; letter-spacing: 0.3px; }
.close-card .line.m { color: #64648A; font-size: 11.5px; }
"""


def foot(i, n):
    return (f'<div class="foot"><div>{E(META["footer"])}</div>'
            f'<div class="pagenum">{i:02d} / {n:02d}</div></div>')


def head(s):
    o = []
    if s.get("number"):
        o.append(f'<p class="eyebrow">{E(s["number"])} — {E(s["title"])}</p>'
                 if False else f'<p class="eyebrow">{E(s["number"])}</p>')
    o.append(f'<h2>{E(s["title"])}</h2>')
    o.append('<div class="rule"></div>')
    if s.get("lead"):
        o.append(f'<p class="lead">{E(s["lead"])}</p>')
    return f'<div class="head">{"".join(o)}</div>'


# --------------------------------------------------------------------------
# slide types
# --------------------------------------------------------------------------

def r_cover(s):
    return (f'<div class="glow"></div><div class="glow2"></div>'
            f'<div class="cover-art">{ART["cover"]()}</div>'
            f'<p class="eyebrow">{E(s["eyebrow"])}</p>'
            f'<h1>{E(s["title"])}</h1>'
            f'<p class="cover-sub">{E(s["subtitle"])}</p>'
            f'<p class="cover-blurb">{E(s["blurb"])}</p>'
            f'<div class="cover-meta">{E(META["founder"])}<br>{E(META["email"])}</div>')


def r_two_card(s):
    cards = "".join(
        f'<div class="co"><div class="name">{E(c["name"])}</div>'
        f'<div class="tag">{E(c["tag"])}</div><p>{E(c["body"])}</p>'
        f'<div class="link">{E(c["link"])}</div></div>' for c in s["cards"])
    stats = "".join(f'<div class="stat"><div class="n">{E(n)}</div><div class="l">{E(l)}</div></div>'
                    for n, l in s["stats"])
    return (head(s) + f'<div class="body" style="flex-direction:column;'
            f'justify-content:space-between;padding-bottom:14px">'
            f'<div class="two" style="gap:22px;flex:1;max-height:330px">{cards}</div>'
            f'<div class="stats">{stats}</div></div>')


def r_grid(s):
    cols = s.get("columns", 4)
    rows = -(-len(s["cards"]) // cols)
    # wide cards hold less text, so cap the row height rather than let them go hollow
    row_h = s.get("row_h") or (168 if cols <= 3 else 230)
    maxh = rows * row_h + (rows - 1) * 14
    cards = "".join(f'<div class="card"><h3>{E(t)}</h3><p>{E(b)}</p></div>' for t, b in s["cards"])
    return (head(s) + f'<div class="body" style="align-items:center"><div class="grid" '
            f'style="grid-template-columns:repeat({cols},1fr);max-height:{maxh}px">{cards}</div></div>')


def r_table(s):
    w = s.get("widths") or []
    th = "".join(f'<th{f" style=width:{w[i]}%" if i < len(w) else ""}>{E(h)}</th>'
                 for i, h in enumerate(s["head"]))
    rows = "".join("<tr>" + "".join(
        f'<td class="{"k" if i == 0 else ""}">{E(c)}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in s["rows"])
    return head(s) + f'<div class="body"><table><tr>{th}</tr>{rows}</table></div>'


def r_story(s):
    art = ART.get(s.get("visual"))
    art_html = f'<div class="story-art">{art()}</div>' if art else ""
    bullets = "".join(f"<li>{E(b)}</li>" for b in s["built"])
    return (f'{art_html}<div class="head" style="max-width:960px">'
            f'<p class="eyebrow">{E(s["number"])}</p>'
            f'<div class="pname">{E(s["project"])}</div>'
            f'<h2 style="margin-top:6px">{E(s["title"])}</h2>'
            f'<div class="kicker">{E(s["kicker"])}</div></div>'
            f'<div class="body" style="flex-direction:column">'
            f'<div class="two" style="flex:1">'
            f'<div class="col-l">'
            f'<p class="blocklabel">The context</p><p class="blocktext">{E(s["context"])}</p>'
            f'<p class="blocklabel" style="margin-top:20px">The problem</p>'
            f'<p class="blocktext">{E(s["problem"])}</p>'
            f'</div>'
            f'<div class="col-r"><p class="blocklabel">What we built</p>'
            f'<ul class="bul">{bullets}</ul></div></div>'
            f'<div class="hardbox"><p class="blocklabel">{E(s["hard_title"])}</p>'
            f'<p class="blocktext">{E(s["hard"])}</p></div></div>')


def r_proof(s):
    stack = "".join(f'<tr><td class="lab">{E(k)}</td><td class="val">{E(v)}</td></tr>'
                    for k, v in s["stack"])
    hi = "".join(f"<li>{E(h)}</li>" for h in s["highlights"])
    return (f'<div class="head"><div class="pname">{E(s["project"])}</div>'
            f'<h2 style="margin-top:6px;font-size:28px">{E(s["title"])}</h2>'
            f'<div class="rule" style="margin-top:12px"></div></div>'
            f'<div class="body" style="margin-top:16px">'
            f'<div class="diagram">{DIAGRAMS[s["diagram"]]()}</div>'
            f'<div class="proof-r"><p class="blocklabel">Stack</p>'
            f'<table class="stacktbl">{stack}</table>'
            f'<p class="blocklabel">Notable</p><ul class="hi">{hi}</ul></div></div>')


def r_steps(s):
    steps = "".join(f'<div class="step"><div class="n">{E(n)}</div><h3>{E(t)}</h3>'
                    f'<p>{E(d)}</p></div>' for n, t, d in s["steps"])
    return (head(s) + f'<div class="body" style="align-items:center">'
            f'<div class="steps" style="max-height:300px">{steps}</div></div>')


def r_feature(s):
    pts = "".join(f'<div class="point"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t, d in s["points"])
    pills = "".join(f'<span class="pill">{E(p)}</span>' for p in s["tools"])
    return (head(s) + f'<div class="body" style="flex-direction:column;justify-content:center">'
            f'<p class="feat-body" style="max-width:1000px">{E(s["body"])}</p>'
            f'<div class="pointgrid">{pts}</div>'
            f'<div class="pills">{pills}</div></div>')


def r_two_col_list(s):
    def col(title, items):
        rows = "".join(f'<div class="row"><div class="t">{E(t)}</div>'
                       f'<div class="d">{E(d)}</div></div>' for t, d in items)
        return f'<div style="flex:1"><div class="colhead">{E(title)}</div><div class="dl">{rows}</div></div>'
    return (head(s) + f'<div class="body" style="align-items:center">'
            f'<div class="two" style="gap:44px">'
            f'{col(s["left_title"], s["left"])}{col(s["right_title"], s["right"])}</div></div>')


def r_two_col_pills(s):
    pills = "".join(f'<span class="pill big">{E(p)}</span>' for p in s["pills"])
    reasons = "".join(f'<div class="row"><div class="t">{E(t)}</div>'
                      f'<div class="d">{E(d)}</div></div>' for t, d in s["reasons"])
    return (head(s) + f'<div class="body" style="align-items:center">'
            f'<div class="two" style="gap:44px">'
            f'<div style="flex:0 0 400px"><div class="colhead">{E(s["left_title"])}</div>'
            f'<div class="pills" style="margin-top:16px">{pills}</div>'
            f'<p class="blocktext" style="margin-top:20px;font-size:11.8px">{E(s["pills_note"])}</p></div>'
            f'<div style="flex:1"><div class="colhead">{E(s["right_title"])}</div>'
            f'<div class="dl">{reasons}</div></div></div></div>')


def r_closing(s):
    return (f'<div class="glow"></div><div class="glow2"></div>'
            f'<div class="head" style="margin-top:60px"><p class="eyebrow">{E(s["eyebrow"])}</p>'
            f'<h1 style="font-size:46px;max-width:820px">{E(s["title"])}</h1>'
            f'<div class="rule"></div>'
            f'<p class="lead" style="max-width:680px">{E(s["lead"])}</p></div>'
            f'<div class="body" style="align-items:flex-start"><div class="close-card">'
            f'<div class="who">{E(s["founder"])}</div>'
            f'<div class="line">{E(s["email"])}</div>'
            f'<div class="line m">{E(s["phones"])}</div></div></div>')


RENDER = {
    "cover": r_cover, "two_card": r_two_card, "grid": r_grid, "table": r_table,
    "story": r_story, "proof": r_proof, "steps": r_steps, "feature": r_feature,
    "two_col_list": r_two_col_list, "two_col_pills": r_two_col_pills, "closing": r_closing,
}


def build_html():
    n = len(SLIDES)
    pages = []
    for i, s in enumerate(SLIDES, 1):
        cls = "slide cover" if s["type"] in ("cover", "closing") else "slide"
        inner = RENDER[s["type"]](s)
        chrome = "" if s["type"] == "cover" else foot(i, n)
        pages.append(f'<section class="{cls}">{inner}{chrome}</section>')
    return (
        '<meta charset="utf-8">'
        f'<title>{E(META["title"])}</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&'
        'family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" '
        'rel="stylesheet">'
        f'<style>{CSS}</style>{"".join(pages)}')


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "portfolio.html"
    open(out, "w").write(build_html())
    print("wrote", out)
