"""In-house SVG artwork for the portfolio deck.

Two kinds of visual:
  * diagram_<project>()  -- the real architecture / data flow, taken from each
    repository's own README, redrawn in the Trinly palette.
  * art_<project>()      -- a decorative domain illustration for story slides.

Everything is vector and generated here, so there is no third-party image
licence anywhere in the deck.
"""

A = "#7C3AED"        # violet
A2 = "#4F46E5"       # indigo
AL = "#A78BFA"       # light violet
INK = "#0A0A1A"
MUT = "#64648A"
BORD = "#DCDCEC"
SOFT = "#F4F2FD"

# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------

def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def box(x, y, w, h, label, sub=None, tone="plain", rx=10, fs=13, subfs=10.5):
    """A labelled node. tone: plain | accent | solid | ghost"""
    if tone == "solid":
        fill, stroke, tcol, scol = A, A, "#FFFFFF", "#EDE6FE"
    elif tone == "accent":
        fill, stroke, tcol, scol = SOFT, A, INK, MUT
    elif tone == "ghost":
        fill, stroke, tcol, scol = "#FFFFFF", BORD, MUT, MUT
    else:
        fill, stroke, tcol, scol = "#FFFFFF", BORD, INK, MUT
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
         f'stroke="{stroke}" stroke-width="1.4"/>']
    cx = x + w / 2
    if sub:
        o.append(f'<text x="{cx}" y="{y + h/2 - 3}" text-anchor="middle" font-family="Sora,Inter,sans-serif" '
                 f'font-size="{fs}" font-weight="600" fill="{tcol}">{_esc(label)}</text>')
        o.append(f'<text x="{cx}" y="{y + h/2 + 13}" text-anchor="middle" font-family="Inter,sans-serif" '
                 f'font-size="{subfs}" fill="{scol}">{_esc(sub)}</text>')
    else:
        o.append(f'<text x="{cx}" y="{y + h/2 + 4.5}" text-anchor="middle" font-family="Sora,Inter,sans-serif" '
                 f'font-size="{fs}" font-weight="600" fill="{tcol}">{_esc(label)}</text>')
    return "".join(o)


def band(x, y, w, h, label, sub=None):
    """A full-width supporting band (e.g. the audit log under everything)."""
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{SOFT}" '
         f'stroke="{A}" stroke-width="1.2" stroke-dasharray="5 4"/>']
    o.append(f'<text x="{x+18}" y="{y + h/2 + 4}" font-family="Sora,Inter,sans-serif" font-size="12.5" '
             f'font-weight="600" fill="{A}">{_esc(label)}</text>')
    if sub:
        o.append(f'<text x="{x+w-18}" y="{y + h/2 + 4}" text-anchor="end" font-family="Inter,sans-serif" '
                 f'font-size="11" fill="{MUT}">{_esc(sub)}</text>')
    return "".join(o)


def arrow(x1, y1, x2, y2, label=None, dashed=False, curve=0, color=None):
    c = color or "#B9B4D6"
    d = ' stroke-dasharray="5 4"' if dashed else ""
    if curve:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + curve
        path = f"M{x1},{y1} Q{mx},{my} {x2},{y2}"
    else:
        path = f"M{x1},{y1} L{x2},{y2}"
    o = [f'<path d="{path}" fill="none" stroke="{c}" stroke-width="1.6"{d} marker-end="url(#ar)"/>']
    if label:
        # keep the label clear of a bowed path rather than striking through it
        lx = (x1 + x2) / 2
        ly = (y1 + y2) / 2 + (curve * 0.5 + 15 if curve else -8)
        o.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" font-family="Inter,sans-serif" '
                 f'font-size="10" fill="{MUT}">{_esc(label)}</text>')
    return "".join(o)


def caption(x, y, text, anchor="start", size=10.5, color=None, weight="400"):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Inter,sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{color or MUT}">{_esc(text)}</text>')


def zone(x, y, w, h, label):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#FBFAFE" stroke="{BORD}" '
         f'stroke-width="1.2"/>']
    o.append(f'<text x="{x+16}" y="{y+21}" font-family="JetBrains Mono,ui-monospace,monospace" '
             f'font-size="9.5" letter-spacing="1.4" fill="{A}">{_esc(label.upper())}</text>')
    return "".join(o)


def svg(w, h, body, bg="#FFFFFF"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" '
            f'preserveAspectRatio="xMidYMid meet">'
            f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
            f'markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0,1 L9,5 L0,9 z" fill="#B9B4D6"/></marker>'
            f'<linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0%" stop-color="{A}"/><stop offset="100%" stop-color="{A2}"/></linearGradient>'
            f'<linearGradient id="g2" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0%" stop-color="{A}" stop-opacity="0.18"/>'
            f'<stop offset="100%" stop-color="{A2}" stop-opacity="0.02"/></linearGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


# --------------------------------------------------------------------------
# architecture diagrams (690 x 480) -- redrawn from each repository's README
# --------------------------------------------------------------------------

def diagram_helix():
    b = []
    lx, lw = 36, 300
    rx_, rw = 380, 274
    rows = [
        ("ODM-XML ingest", "CDISC ODM v1.3.2 validation", "plain"),
        ("Mapping decisions", "review → comment → approve", "accent"),
        ("SDTM → ADaM", "transformation layer", "plain"),
        ("Regulatory output", "Define-XML 2.1 · eCTD Module 5", "plain"),
    ]
    side = [
        ("AI suggestions", "confidence scored"),
        ("Precedent library", "semantic search · lineage"),
        ("Code generation", "SAS · R · Python"),
        ("Trial simulation", "17-tool agent · synthetic arms"),
    ]
    for i, (t, s, tone) in enumerate(rows):
        y = 46 + i * 86
        b.append(box(lx, y, lw, 54, t, s, tone))
        if i < 3:
            b.append(arrow(lx + lw / 2, y + 56, lx + lw / 2, y + 84))
    for i, (t, s) in enumerate(side):
        y = 46 + i * 86
        b.append(box(rx_, y, rw, 54, t, s, "ghost"))
    # side boxes feed the decision layer
    b.append(arrow(rx_ - 4, 73, lx + lw + 6, 128, dashed=True))
    b.append(arrow(rx_ - 4, 159, lx + lw + 6, 159, dashed=True))
    b.append(arrow(lx + lw + 6, 245, rx_ - 4, 245, dashed=True))
    b.append(arrow(lx + lw + 6, 331, rx_ - 4, 331, dashed=True))
    b.append(band(36, 400, 618, 50, "21 CFR Part 11 audit log",
                  "SHA-256 checksum chaining · e-signatures · RBAC"))
    return svg(690, 480, "".join(b))


def diagram_sentinel():
    b = []
    r1 = [("Drone survey", "visual + thermal", "plain"),
          ("YOLO26 detection", "draft annotations", "solid"),
          ("Inspector review", "approve · correct", "accent")]
    for i, (t, s, tone) in enumerate(r1):
        x = 36 + i * 214
        b.append(box(x, 58, 190, 58, t, s, tone))
        if i < 2:
            b.append(arrow(x + 192, 87, x + 212, 87))
    r2 = [("PDF report", "issued to client", "plain"),
          ("Field remediation", "crew closes out", "plain"),
          ("Work orders", "assigned · SLA-bound", "accent")]
    for i, (t, s, tone) in enumerate(r2):
        x = 36 + i * 214
        b.append(box(x, 196, 190, 58, t, s, tone))
        if i < 2:
            b.append(arrow(x + 212, 225, x + 192, 225))
    b.append(arrow(559, 118, 559, 194))
    b.append(arrow(490, 148, 200, 148, label="approved annotations → fine-tune → redeploy",
                   dashed=True, curve=26, color=A))
    b.append(zone(36, 288, 618, 152, "platform services"))
    svc = [("Geospatial", "PostGIS · LIDAR · no-fly checks"),
           ("Photogrammetry", "NodeODM · ortho · DSM · 3D"),
           ("Async & storage", "Celery + Redis · MinIO")]
    for i, (t, s) in enumerate(svc):
        b.append(box(56 + i * 194, 334, 178, 68, t, s, "ghost"))
    return svg(690, 480, "".join(b))


def diagram_cortex():
    b = []
    b.append(zone(36, 44, 250, 306, "edge · raspberry pi 5"))
    edge = [("Arducam IMX296", "CSI camera"), ("GPS", "position per frame"),
            ("SIM7600G-H", "4G / LTE HAT")]
    for i, (t, s) in enumerate(edge):
        b.append(box(56, 82 + i * 66, 210, 54, t, s, "plain"))
    b.append(box(56, 280, 210, 54, "Buffer & upload", "resumable, offline-tolerant", "accent"))
    b.append(arrow(290, 307, 374, 307, label="HTTPS over LTE", color=A))
    b.append(zone(380, 44, 274, 306, "cloud"))
    cloud = [("Nginx → FastAPI", "ingest API", "plain"),
             ("Celery → YOLO", "crack · fastener · gauge", "solid"),
             ("PostgreSQL + PostGIS", "geolocated findings", "plain"),
             ("MinIO", "captured imagery", "plain")]
    for i, (t, s, tone) in enumerate(cloud):
        b.append(box(400, 82 + i * 66, 234, 54, t, s, tone))
    b.append(box(36, 384, 618, 58, "Next.js operator dashboard",
                 "Leaflet map · run history · finding review · fleet registration", "accent"))
    b.append(arrow(517, 380, 517, 356))
    return svg(690, 480, "".join(b))


def diagram_rdactd():
    b = []
    b.append(box(70, 46, 230, 58, "Next.js 15 web", "App Router · Tailwind 4", "plain"))
    b.append(box(390, 46, 230, 58, "Expo 53 mobile", "iOS · Android · Expo Router", "plain"))
    b.append(box(70, 156, 550, 70, "Shared TypeScript core",
                 "models · services · tRPC client · WebSocket client · design tokens", "solid"))
    b.append(arrow(185, 106, 185, 154))
    b.append(arrow(505, 106, 505, 154))
    b.append(box(70, 278, 260, 58, "Drizzle ORM", "PostgreSQL schema + migrations", "accent"))
    b.append(box(360, 278, 260, 58, "Socket.io server", "real-time case chat", "accent"))
    b.append(arrow(200, 228, 200, 276))
    b.append(arrow(490, 228, 490, 276))
    b.append(band(70, 384, 550, 50, "Turborepo build orchestration",
                  "Docker · Google Cloud Build · Firebase Storage"))
    return svg(690, 480, "".join(b))


def diagram_oac():
    b = []
    cx_, cw = 196, 300
    mid = [("Next.js 16 site", "typed content · MDX blog", "accent"),
           ("Server Action", "Zod-validated submission", "plain"),
           ("PostgreSQL — Neon", "lead persistence", "plain"),
           ("Admin inbox", "bcrypt auth · status · filter", "plain")]
    for i, (t, s, tone) in enumerate(mid):
        y = 44 + i * 84
        b.append(box(cx_, y, cw, 56, t, s, tone))
        if i < 3:
            b.append(arrow(cx_ + cw / 2, y + 58, cx_ + cw / 2, y + 82))
    b.append(box(30, 44, 150, 56, "Visitor", "organic · local search", "ghost"))
    b.append(arrow(182, 72, cx_ - 4, 72))
    b.append(box(30, 128, 150, 56, "Resend", "email notification", "ghost"))
    b.append(arrow(cx_ - 4, 156, 182, 156))
    b.append(box(512, 44, 148, 56, "Technical SEO", "JSON-LD · sitemap", "ghost"))
    b.append(arrow(cx_ + cw + 4, 72, 508, 72))
    b.append(box(512, 296, 148, 56, "JobTread CRM", "+ AI enrichment", "ghost"))
    b.append(arrow(cx_ + cw + 4, 324, 510, 324, dashed=True))
    b.append(band(30, 392, 630, 50, "Vercel deployment",
                  "Vitest + Testing Library · Lighthouse SEO 100"))
    return svg(690, 480, "".join(b))


DIAGRAMS = {
    "helix": diagram_helix,
    "sentinel": diagram_sentinel,
    "cortex": diagram_cortex,
    "rdactd": diagram_rdactd,
    "oac": diagram_oac,
}


# --------------------------------------------------------------------------
# decorative domain glyphs (200 x 200) for story slides
# --------------------------------------------------------------------------

_G = f'stroke="url(#g1)" fill="none" stroke-width="2.6" stroke-linecap="round"'
_GT = f'stroke="{AL}" fill="none" stroke-width="1.6" stroke-linecap="round"'


def _glyph(body):
    return svg(200, 200, f'<circle cx="100" cy="100" r="92" fill="url(#g2)"/>{body}', bg="none")


def art_helix():
    """Two out-of-phase strands with data rungs — a double helix, not an hourglass."""
    import math
    b = []
    def strand(phase):
        pts = []
        for i in range(41):
            t = i / 40.0
            y = 30 + t * 148
            x = 100 + 40 * math.sin(t * math.pi * 2.4 + phase)
            pts.append(f"{x:.1f},{y:.1f}")
        return "M" + " L".join(pts)
    b.append(f'<path d="{strand(0)}" {_G}/>')
    b.append(f'<path d="{strand(math.pi)}" {_G}/>')
    for i in range(1, 11):
        t = i / 11.0
        y = 30 + t * 148
        x1 = 100 + 40 * math.sin(t * math.pi * 2.4)
        x2 = 100 + 40 * math.sin(t * math.pi * 2.4 + math.pi)
        b.append(f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" {_GT}/>')
        b.append(f'<circle cx="{x1:.1f}" cy="{y:.1f}" r="3.4" fill="{A}"/>')
        b.append(f'<circle cx="{x2:.1f}" cy="{y:.1f}" r="3.4" fill="{A2}"/>')
    return _glyph("".join(b))


def art_sentinel():
    b = [f'<rect x="86" y="44" width="28" height="16" rx="5" fill="url(#g1)"/>',
         f'<line x1="86" y1="52" x2="56" y2="38" {_G}/>',
         f'<line x1="114" y1="52" x2="144" y2="38" {_G}/>',
         f'<ellipse cx="52" cy="36" rx="16" ry="4" fill="{AL}"/>',
         f'<ellipse cx="148" cy="36" rx="16" ry="4" fill="{AL}"/>',
         f'<line x1="100" y1="60" x2="100" y2="76" {_GT}/>',
         f'<circle cx="100" cy="80" r="5" fill="{A}"/>']
    # tower + detection box
    b.append(f'<path d="M78,180 L96,104 L104,104 L122,180" {_G}/>')
    b.append(f'<line x1="86" y1="146" x2="114" y2="146" {_GT}/>')
    b.append(f'<line x1="82" y1="164" x2="118" y2="164" {_GT}/>')
    b.append(f'<rect x="72" y="120" width="56" height="44" rx="4" stroke="{A}" fill="none" '
             f'stroke-width="1.8" stroke-dasharray="6 4"/>')
    b.append(f'<circle cx="128" cy="120" r="4" fill="{A}"/>')
    return _glyph("".join(b))


def art_cortex():
    b = [f'<path d="M46,186 L88,52" {_G}/>', f'<path d="M154,186 L112,52" {_G}/>']
    ys = [186, 158, 132, 110, 92, 78, 66]
    for y in ys:
        t = (186 - y) / 134.0
        half = 54 - 42 * t
        b.append(f'<line x1="{100-half}" y1="{y}" x2="{100+half}" y2="{y}" {_GT}/>')
    b.append(f'<path d="M100,96 a13,13 0 1,1 0.1,0 M100,122 L100,109" stroke="{A}" fill="none" '
             f'stroke-width="2.4"/>')
    b.append(f'<circle cx="100" cy="96" r="5" fill="{A}"/>')
    b.append(f'<rect x="70" y="140" width="24" height="14" rx="3" stroke="{A}" fill="none" '
             f'stroke-width="1.8" stroke-dasharray="4 3"/>')
    return _glyph("".join(b))


def art_rdactd():
    b = [f'<path d="M56,34 L124,34 L148,58 L148,166 L56,166 Z" {_G}/>',
         f'<path d="M124,34 L124,58 L148,58" {_GT}/>']
    for i, (x, w) in enumerate(((72, 62), (72, 44), (72, 54), (72, 34))):
        y = 78 + i * 20
        fill = A if i in (1, 3) else "none"
        if fill == A:
            b.append(f'<rect x="{x}" y="{y-8}" width="{w}" height="11" rx="2" fill="{A}"/>')
        else:
            b.append(f'<line x1="{x}" y1="{y-3}" x2="{x+w}" y2="{y-3}" {_GT}/>')
    b.append(f'<path d="M128,120 L162,132 L162,158 C162,174 146,182 128,188 '
             f'C110,182 94,174 94,158 L94,132 Z" fill="#FFFFFF" stroke="url(#g1)" stroke-width="2.6"/>')
    b.append(f'<path d="M112,156 L124,168 L146,142" stroke="{A}" fill="none" stroke-width="3" '
             f'stroke-linecap="round" stroke-linejoin="round"/>')
    return _glyph("".join(b))


def art_oac():
    b = [f'<circle cx="150" cy="52" r="18" stroke="{AL}" fill="none" stroke-width="2"/>',
         f'<path d="M34,150 L100,112 L166,150" {_G}/>',
         f'<line x1="52" y1="150" x2="52" y2="182" {_G}/>',
         f'<line x1="148" y1="150" x2="148" y2="182" {_G}/>',
         f'<line x1="100" y1="132" x2="100" y2="182" {_GT}/>']
    for i in range(5):
        y = 158 + i * 7
        b.append(f'<line x1="{40+i*2}" y1="{y}" x2="{160-i*2}" y2="{y}" {_GT}/>')
    b.append(f'<line x1="28" y1="182" x2="172" y2="182" {_G}/>')
    return _glyph("".join(b))


def art_cover():
    pts = [(70, 60), (150, 42), (210, 96), (162, 158), (86, 152), (34, 108), (124, 100)]
    b = []
    for i, (x1, y1) in enumerate(pts):
        for x2, y2 in pts[i + 1:]:
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 < 9000:
                b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{AL}" '
                         f'stroke-width="1.1" opacity="0.55"/>')
    for i, (x, y) in enumerate(pts):
        r = 9 if i == 6 else 6
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#g1)"/>')
    return svg(240, 200, "".join(b), bg="none")


ART = {
    "helix": art_helix, "sentinel": art_sentinel, "cortex": art_cortex,
    "rdactd": art_rdactd, "oac": art_oac, "cover": art_cover,
}
