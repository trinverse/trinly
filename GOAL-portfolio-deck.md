# GOAL — Trinly × ArtSync Work Portfolio (PPT + PDF)

**Owner:** Ashish Tyagi
**Audience:** Malini — potential investor and referral source for client introductions
**Status:** Portfolio deck **built** (21 slides, PPTX + PDF) · investor one-pager pending Q1/Q2 · updated 2026-08-22
**Related:** `PRICING.md`, `assets/capabilities-pdf.html` → `Trinly-ArtSync-Capabilities.pdf` (existing 7-section capabilities one-pager)

---

## 0. Decisions

| Decision | Call |
|---|---|
| **Framing** | **Two documents.** A work portfolio for Malini's network *and* a short investor one-pager for Malini herself. Neither gets compromised by serving both audiences. |
| **Naming** | **Name everything.** Helix, Sentinel, Cortex, RDACTD and Open Air Construction all appear by name, clients included. Maximum credibility. |
| **Pricing** | **Out of the deck.** Every path leads to a scoping call. `Trinly-Pricing.pdf` travels as a separate attachment if she asks for numbers. |
| **Visuals** | **Representative artwork, not real product screenshots.** No live UI, no client data. Architecture diagrams stay real, redrawn as clean vector graphics. |

**Imagery outcome:** stock photography was ruled out at build time. Unsplash and Pexels both require an API key, and the key-free CC sources (Wikimedia Commons, Openverse) return archival photographs that would cheapen an investor-facing document. Every visual is therefore generated in-house as SVG — five architecture diagrams drawn from the projects' own READMEs, plus a domain glyph per project. Zero licensing exposure. If photography is wanted later, an Unsplash API key is the only missing piece; the artwork is isolated in `scripts/portfolio/visuals.py`.

**Imagery sourcing rule:** only royalty-free / permissively licensed sources or vector graphics drawn in-house. Nothing scraped from a search results page — this document goes to an investor and gets forwarded onward, so licensing has to be clean. `assets/portfolio-images/CREDITS.md` records the provenance of every image.

---

## 1. Objective

Produce a single, polished **portfolio deck** that shows Malini *what we have actually built* — not just what we claim we can do — so she can (a) judge the strength of the team as an investor and (b) confidently forward it to potential clients in her network.

Three artifacts, two audiences, one brand:

| Artifact | Format | Audience | Primary use |
|---|---|---|---|
| `Trinly-Work-Portfolio.pptx` | PowerPoint 16:9 | Malini's network | She presents or screen-shares it; editable so she can excerpt slides per contact |
| `Trinly-Work-Portfolio.pdf` | 16:9 PDF | Malini's network | Email attachment, forwards to clients, mobile reading |
| `Trinly-Investor-Onepager.pdf` | A4 PDF, 2 pages | Malini herself | The investment case — team, traction, market, what we'd do with capital |

Success = Malini can open it cold, understand in 60 seconds what we do, and point to two or three projects that match someone in her network.

---

## 2. Positioning

The deck must answer three questions, in this order:

1. **Who is this?** — Trinly (US · AI consultancy) + ArtSync India (AI, data intelligence, annotation, IT support) as one allied delivery group; 17+ engineers, 6 hubs, 5 countries, 24/7 coverage.
2. **What have they shipped?** — five substantial, production-grade systems across regulated, physical-AI, and commercial domains.
3. **What can they do for *my* contacts?** — the full service and support menu, with engagement models and an obvious next step.

Tone: evidence-first, plain language, no hype adjectives. Every capability claim should be traceable to a project on a later slide.

---

## 3. Deliverable structure (target 18–22 slides)

### Part A — Introduction (3 slides)
1. **Cover** — Trinly × ArtSync, "AI-First Technology Solutions", contact block.
2. **Who we are** — the two-company structure, the reach stats, why it matters (senior US/EU strategy + deep India engineering bench).
3. **What we do** — the capability grid (RAG, model training & fine-tuning, AI agents, context engineering, data engineering & annotation, MLOps, full-stack engineering, intelligent automation).

### Part B — Selected work (2 slides per project, 10 slides)
One **story slide** + one **proof slide** per project. Story slide = problem, what we built, outcome. Proof slide = architecture diagram or product screenshots + tech stack.

| # | Project | Domain | The one-line pitch |
|---|---|---|---|
| 1 | **Helix** | Clinical trials / regulated life sciences | Decision-intelligence platform for the ODM → SDTM → ADaM pipeline, with AI-assisted mapping, virtual trial simulation, and full 21 CFR Part 11 audit compliance. |
| 2 | **Sentinel** | Drone & infrastructure inspection | Drones fly the asset, YOLO26 computer vision finds the defects, the platform turns them into tracked, SLA-bound work orders with geospatial, photogrammetry and 3D context. |
| 3 | **Cortex** | Railway / edge AI | Cart-mounted Raspberry Pi captures track imagery over 4G; cloud YOLO pipeline detects rail cracks, missing fasteners and gauge deviations in near real time on a PostGIS-backed operator dashboard. |
| 4 | **RDACTD** | Enterprise document security | Complaint management and business analytics platform with automated PII identification and redaction — Next.js web + Expo mobile from one shared TypeScript core. |
| 5 | **Open Air Construction** | SMB / commercial web | Next.js 16 contractor site with MDX blog, server-action lead pipeline, local SEO and LocalBusiness JSON-LD — the fast-turnaround end of our range. |

Ordering rationale: heaviest technical credibility first (Helix, Sentinel), then edge/AI hardware (Cortex), then product engineering (RDACTD), then the quick-win commercial tier (OAC) — so the deck spans "we build regulated AI platforms" *and* "we can also ship your website in three weeks."

Each story slide carries the same five fields so the set reads consistently:
- **Client / context** (or "internal product" where applicable)
- **The problem**
- **What we built** — 3–4 bullets max
- **Stack** — a mono-font tech strip
- **Why it's hard** — the one detail that proves depth (Part 11 audit chaining, PX4 SITL simulation, edge buffering over LTE, etc.)

### Part C — Services & support (4–5 slides)
4. **Trinly services** — AI/ML consulting, RAG systems, model training & fine-tuning, AI agents, context engineering, data pipelines, MLOps, custom web and mobile product development.
5. **ArtSync services** — software development, data entry and annotation at scale, enterprise applications, and ongoing IT support.
6. **Physical-AI annotation specialization** — video/multimodal labeling for CV and VLA systems (temporal segmentation, keypoint labeling, HITL QA, CVAT/Labelbox/Label Studio).
7. **How we engage & support** — the four-step delivery model (Data audit & strategy → Build & train → Production deployment → Continuous optimization), plus engagement models (fixed-scope project, retained team, staff augmentation, managed support/SLA) and what "support" concretely includes.
### Part D — Close (2 slides)
9. **Industries we serve + why clients choose us** — healthcare & clinical trials, fintech, drone & geospatial, robotics & physical AI, B2B SaaS.
10. **Contact / next step** — founder details, both domains, and a clear ask ("15-minute scoping call for any introduction").

---

### Document 2 — Investor one-pager (2 pages, A4)

A separate, denser document for Malini alone. Not slides — a written brief she can read in five minutes.

**Page 1 — The business**
- What Trinly × ArtSync is, in two sentences.
- The delivery structure and why it's an advantage: US/EU senior strategy, India engineering bench, 17+ engineers across 6 hubs in 5 countries, 24/7 coverage, cost position 40–60% below comparable US/EU agencies at equivalent quality.
- Traction — clients delivered, projects shipped, revenue and pipeline *(needs Q1)*.
- Proof of range in one table: the same five projects, one line each, showing regulated life sciences through to fast commercial web.

**Page 2 — The opportunity**
- Market: where AI services demand is concentrated for us — clinical trials, drone/geospatial inspection, physical-AI data annotation.
- The wedge: annotation for Vision-Language-Action systems is a specialization with real scarcity, and it feeds the consulting business.
- Team: founder and senior bench *(needs Q3)*.
- The ask: what we're raising or seeking, and what it buys *(needs Q2)*.
- Contact and next step.

---

## 4. Build

One command rebuilds both files from one content model:

```bash
python3 scripts/portfolio/build.py
```

| File | What it is |
|---|---|
| `scripts/portfolio/content.py` | **Single source of truth** — every word of the deck |
| `scripts/portfolio/visuals.py` | SVG artwork: 5 architecture diagrams + 6 domain glyphs |
| `scripts/portfolio/render_html.py` | Content → 16:9 HTML slides |
| `scripts/portfolio/make_images.py` | SVG → PNG via headless Chrome (for the PPTX) |
| `scripts/portfolio/build_pptx.py` | Content → editable PowerPoint |
| `Trinly-Work-Portfolio.pdf` | 21 slides, 960×540 pt, 1.2 MB |
| `Trinly-Work-Portfolio.pptx` | 21 slides, native editable text, 0.7 MB |

Because both renderers read `content.py`, the PPT and the PDF cannot drift.

**Font note:** the PDF uses Sora / Inter / JetBrains Mono via Google Fonts. The PPTX uses Arial and Courier New instead — those three fonts are not installed on most machines and PowerPoint substitutes them badly. Switch `F_HEAD` / `F_BODY` / `F_MONO` at the top of `build_pptx.py` if the recipient has them installed.

### Original approach (kept for reference)

Reuse the pipeline already proven in this ecosystem — no new tooling to learn:

- **PDF:** author `assets/portfolio-pdf.html` in the same style as `assets/capabilities-pdf.html` (brand tokens: violet `#7C3AED`, indigo `#4F46E5`, Sora headings, Inter body, JetBrains Mono accents), render with headless Chrome — the same approach as `../sentinel/scripts/make-pdf.sh`.
- **PPTX:** generate with `python-pptx`, following the pattern in `../sentinel/docs/gtm/generate_partner_deck.py`, so the deck is reproducible from a script rather than hand-built.
- **Single source of truth:** slide copy lives in one Markdown/data file that both generators read, so PPT and PDF can never drift.
- **Imagery:** representative royalty-free photography per project domain (railway track, drone over infrastructure, clinical data work, document security, deck construction) paired with clean in-house vector architecture diagrams — Cortex and Sentinel already have ASCII diagrams in their READMEs that redraw well. No live product UI, no client data. Every image logged in `assets/portfolio-images/CREDITS.md` with its source and license.

Everything lands in this repo alongside the existing capabilities collateral.

---

## 5. Acceptance criteria

- [ ] Both files open cleanly (PowerPoint/Keynote/Google Slides for the PPTX; Preview/Acrobat/mobile for the PDF).
- [ ] Every one of the five projects has a story slide and a proof slide with a real visual — no placeholder boxes.
- [ ] Trinly *and* ArtSync services and support offerings are both explicitly covered.
- [ ] No confidential client data, credentials, real patient/inspection data, or live product UI anywhere in the deck.
- [ ] Every image is royalty-free or in-house, and recorded in `CREDITS.md` with its license.
- [ ] The investor one-pager exists as its own document and is never mixed into the portfolio deck.
- [ ] Contact details and both domains appear on the cover and the closing slide.
- [ ] PDF is under ~10 MB so it survives email.
- [ ] Reads correctly at a glance on a phone screen.

---

## 6. Open questions

The portfolio deck can be built now. These block only the parts noted.

1. **Traction numbers** *(investor one-pager, p1; also strengthens the deck)* — clients delivered, revenue, pipeline, and any project metrics we can quote: defects detected, studies mapped, hours saved, users, uptime. Concrete numbers are the single biggest credibility lever in both documents. If nothing is shareable, both documents work without them — they just land softer.
2. **The ask** *(investor one-pager, p2)* — are we raising? How much, for what, and on what terms? Or is Malini an advisor/referral partner first and the investment conversation is exploratory?
3. **Team** — name the senior bench with roles, or keep it to the founder plus aggregate stats?
4. **Client status per project** — for each of the five, is it client work, an internal product, or a product seeking customers? It changes how each story slide is written, and the investor one-pager needs it to describe the revenue base honestly.
