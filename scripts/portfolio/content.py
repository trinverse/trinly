"""Single source of truth for the Trinly x ArtSync work portfolio.

Both renderers (build_pdf.py -> HTML -> Chrome -> PDF, and build_pptx.py ->
python-pptx) read this module, so the PPT and the PDF cannot drift apart.

Every project claim here is traceable to the project's own repository
(../helix, ../sentinel, ../cortex, ../rdactd, ../oac).
"""

BRAND = {
    "accent": "#7C3AED",
    "accent2": "#4F46E5",
    "accent_light": "#A78BFA",
    "ink": "#0A0A1A",
    "muted": "#64648A",
    "faint": "#8888A0",
    "bg": "#FFFFFF",
    "surface": "#F7F6FC",
    "border": "#E0E0EC",
    "dark": "#0A0A0F",
    "dark_surface": "#16161E",
}

META = {
    "title": "Trinly × ArtSync — Work Portfolio",
    "subtitle": "AI systems we have designed, built and shipped",
    "company": "Trinly · ArtSync India",
    "founder": "Ashish Tyagi — Founder & CEO",
    "email": "hello@trinly.us  ·  hello@artsync.live",
    "phones": "US +1 919 578 4944  ·  IN +91 84484 12144",
    "sites": "trinly.us  ·  artsync.live",
    "footer": "Trinly · ArtSync India — Work Portfolio · trinly.us · artsync.live",
}

STATS = [
    ("17+", "AI engineers & architects"),
    ("6", "Global delivery hubs"),
    ("5", "Countries"),
    ("24/7", "Follow-the-sun coverage"),
]

# --------------------------------------------------------------------------
# Slides
# --------------------------------------------------------------------------

SLIDES = []


def slide(**kw):
    SLIDES.append(kw)
    return kw


# 1 ------------------------------------------------------------------ cover
slide(
    type="cover",
    eyebrow="AI-First Delivery Partnership",
    title="Trinly × ArtSync",
    subtitle="Work Portfolio — AI systems we have designed, built and shipped",
    blurb="Five production platforms across clinical trials, drone inspection, railway "
          "safety, enterprise integrity and commercial web — plus the full service "
          "and support capability behind them.",
    visual="cover",
)

# 2 ------------------------------------------------------------- who we are
slide(
    type="two_card",
    number="01",
    title="Who we are",
    lead="One allied delivery group covering the complete path from raw data to a "
         "production AI product — senior strategy from the US and Europe, deep "
         "engineering and data capacity from India.",
    cards=[
        {
            "name": "Trinly",
            "tag": "US · AI Consultancy",
            "body": "AI-first technology consultancy turning AI ambitions into shipped, "
                    "production-ready products — RAG systems, model training, AI agents "
                    "and MLOps. Architecture, strategy and delivery leadership.",
            "link": "trinly.us",
        },
        {
            "name": "ArtSync India",
            "tag": "India · AI & Data Intelligence",
            "body": "AI development, data intelligence and annotation at scale — data "
                    "engineering, ML/LLM engineering, automation, enterprise applications "
                    "and ongoing IT support from six hubs across India.",
            "link": "artsync.live",
        },
    ],
    stats=STATS,
)

# 3 ---------------------------------------------------------------- what we do
slide(
    type="grid",
    number="02",
    title="What we do",
    lead="Eight capabilities, each one demonstrated by a project later in this deck.",
    columns=4,
    cards=[
        ("RAG & retrieval systems", "Production retrieval pipelines with vector search, semantic precedent lookup and context-aware grounding."),
        ("Model training & fine-tuning", "Custom training, LoRA and domain adaptation — with evaluation harnesses and retraining loops."),
        ("AI agents & orchestration", "Multi-agent, tool-using systems that carry out multi-step business workflows end to end."),
        ("Computer vision", "Detection and segmentation on visual and thermal imagery, at the edge and in the cloud."),
        ("Data engineering & annotation", "ETL, cleaning, labeling and ML-ready dataset delivery — including physical-AI video annotation."),
        ("MLOps & deployment", "Serving, monitoring, drift detection, A/B testing and continuous deployment."),
        ("Full-stack product engineering", "Web, native mobile and API platforms — monorepos, design systems, CI/CD."),
        ("Regulated & compliant systems", "Audit trails, e-signatures, RBAC and submission packages for regulated industries."),
    ],
)

# 4 --------------------------------------------------------- work at a glance
slide(
    type="table",
    number="03",
    title="Selected work",
    lead="Five systems, deliberately spanning the range — from a regulated clinical "
         "data platform to a contractor website shipped in weeks.",
    head=["Project", "Domain", "What it is"],
    rows=[
        ["Helix", "Clinical trials · regulated life sciences",
         "Decision-intelligence platform for the ODM → SDTM → ADaM pipeline, with AI-assisted mapping and 21 CFR Part 11 compliance."],
        ["Sentinel", "Drone · infrastructure inspection",
         "Drones survey the asset, computer vision finds the defects, the platform turns them into tracked, SLA-bound work orders."],
        ["Cortex", "Railway · edge AI",
         "Cart-mounted Raspberry Pi captures track imagery over 4G; cloud AI detects rail defects on a geospatial operator dashboard."],
        ["RDACTD", "Enterprise integrity · SaaS",
         "Encrypted complaint management, resolution workflows and organizational integrity analytics — web and native mobile."],
        ["Open Air Construction", "Commercial web · local SEO",
         "Contractor marketing site with typed content, MDX blog, lead pipeline and an admin inbox — Lighthouse SEO 100."],
    ],
    widths=[19, 26, 55],
)


# 5/6 ------------------------------------------------------------------ Helix
slide(
    type="story",
    number="04",
    project="Helix",
    kicker="Clinical trials · regulated life sciences",
    title="Institutional memory for clinical data mapping",
    context="Decision Intelligence Platform for Clinical Data — capturing, versioning and "
            "reusing mapping decisions across the ODM → SDTM → ADaM transformation pipeline.",
    problem="Every clinical study re-derives the same data-mapping decisions from scratch. "
            "The reasoning lives in spreadsheets and in people's heads, it is lost when staff "
            "move on, and regulators still expect a defensible audit trail for every one of them.",
    built=[
        "CDISC ODM v1.3.2 ingestion with schema validation, then mapping decisions carried through review, comment and approval chains",
        "Cross-study precedent reuse — semantic search over prior decisions, copied forward with lineage tracking and conflict resolution",
        "AI-assisted mapping suggestions with confidence scoring, plus nine anomaly detectors for cross-study inconsistency",
        "Executable SAS, R and Python code generated straight from approved decisions",
        "Virtual trial simulation: a 17-tool agent runs synthetic cohorts visit by visit, with synthetic control arms and ML enrollment forecasting",
        "Regulatory output — eCTD Module 5 packages, Define-XML 2.1, ClinicalTrials.gov registration, RBQM risk dashboards",
    ],
    hard_title="Why it is hard",
    hard="21 CFR Part 11 compliance is not a feature you bolt on. Every action writes to an "
         "append-only audit log chained with SHA-256 checksums, backed by electronic signatures "
         "and role-based access control — so the record is tamper-evident end to end.",
    visual="helix",
)

slide(
    type="proof",
    project="Helix",
    title="Architecture & stack",
    diagram="helix",
    stack=[
        ("Backend", "FastAPI · Python 3.12 · SQLAlchemy · Alembic"),
        ("Data", "PostgreSQL · vector embeddings for precedent search"),
        ("Frontend", "Expo Web (React Native Web) · shared RN component library"),
        ("Mobile", "Expo native app · biometric auth · mobile approvals"),
        ("AI", "Multi-provider LLM layer — OpenAI, Azure, Anthropic, Ollama"),
        ("Monorepo", "pnpm workspaces · apps/api, apps/web, apps/mobile, packages/*"),
    ],
    highlights=[
        "Compliance by construction — append-only audit log, SHA-256 checksum chaining, e-signatures, RBAC",
        "Integration hub with bidirectional connectors for Medidata Rave, Veeva Vault, Oracle InForm and SAS",
        "Real-world data connectors — FDA FAERS, openFDA, PubMed, CMS — with OMOP CDM and FHIR R4 support",
        "Eight interface languages with multilingual embeddings, so precedent search works across regions",
    ],
)

# 7/8 --------------------------------------------------------------- Sentinel
slide(
    type="story",
    number="05",
    project="Sentinel",
    kicker="Drone operations · infrastructure inspection",
    title="From drone survey to closed work order",
    context="AI-powered infrastructure inspection platform. Drones fly the asset, computer "
            "vision finds the defects, and the platform turns them into tracked, assigned, "
            "SLA-bound work.",
    problem="Infrastructure inspection is manual, slow and hazardous. The findings end up in "
            "photo folders and spreadsheets, disconnected from the crews who have to fix "
            "anything — so nothing is provably closed out.",
    built=[
        "The core loop: survey → visual and thermal imagery → YOLO26 detection → draft annotations → inspector review → work orders → field remediation → PDF report",
        "Geospatial context — KML/Shapefile/GeoJSON import, LIDAR point clouds, corridor encroachment and terrain-risk analytics",
        "Photogrammetry via NodeODM: orthophotos, digital surface models and textured 3D models, served as map tiles and an in-browser point-cloud viewer",
        "Drone operations — flight planning with safety validation, no-fly checks against FAA/AirMap, autonomous and swarm missions",
        "A PX4 SITL simulator so missions are tested in software before any aircraft leaves the ground",
        "Web, native mobile and a public marketing site, all from one Nx monorepo",
    ],
    hard_title="Why it is hard",
    hard="The AI improves itself. Every annotation an inspector approves becomes labelled "
         "training data; the model is fine-tuned and redeployed. Human review is not a cost "
         "centre in this system — it is the training pipeline.",
    visual="sentinel",
)

slide(
    type="proof",
    project="Sentinel",
    title="Architecture & stack",
    diagram="sentinel",
    stack=[
        ("Frontend", "React 19 · TypeScript 5.5 · Vite 6 · Tailwind 4 · Leaflet · Three.js · Konva"),
        ("Backend", "Python 3.11 · FastAPI · SQLAlchemy 2 · Pydantic 2 · Alembic"),
        ("Database", "PostgreSQL + PostGIS"),
        ("Async", "Celery + Redis — queues for AI, reports, work orders, LIDAR"),
        ("AI & imaging", "YOLO26 via Ultralytics (separate visual and thermal models) · NodeODM"),
        ("Platform", "MinIO object storage · React Native/Expo mobile · Astro marketing · Nx"),
    ],
    highlights=[
        "Closed learning loop — approved annotations retrain the detector and redeploy it",
        "Separate visual and thermal models, because a hot joint and a cracked insulator are not the same detection problem",
        "Published documentation site built from the repository and deployed on every merge",
        "Simulation-first drone testing with PX4 SITL — no hardware required to validate a mission",
    ],
)

# 9/10 --------------------------------------------------------------- Cortex
slide(
    type="story",
    number="06",
    project="Cortex",
    kicker="Railway safety · edge AI",
    title="AI track inspection from a cart and a Raspberry Pi",
    context="Railway track inspection system. A cart-mounted Raspberry Pi captures imagery "
            "during inspection runs, uploads it over 4G, and cloud AI identifies track "
            "defects in near real time.",
    problem="Track is still inspected largely on foot. Coverage is slow, defects are found "
            "late, and there is no consistent geolocated record of what was seen on which "
            "run — which makes trends across a corridor invisible.",
    built=[
        "An edge capture daemon on a Raspberry Pi 5 with an Arducam IMX296 camera, GPS and a 4G HAT — geotagged imagery captured on the move",
        "Local buffering and resumable upload over LTE, so a run in a dead zone is never a lost run",
        "Cloud detection pipeline — FastAPI and Celery workers running YOLO models for rail cracks, missing fasteners and gauge deviations",
        "PostGIS-backed findings, so every defect carries its position on the track segment",
        "A Next.js operator dashboard with a Leaflet map, run history and per-finding review",
        "Bot registration and API-key provisioning, so a new cart is added to the fleet in minutes",
    ],
    hard_title="Why it is hard",
    hard="Field connectivity is unreliable by default. The uploader's offline-resilience "
         "behaviour is covered by a test suite that runs on any laptop — no Pi, no camera, "
         "no track — so the hardest failure mode is verified continuously, not on site.",
    visual="cortex",
)

slide(
    type="proof",
    project="Cortex",
    title="Architecture & stack",
    diagram="cortex",
    stack=[
        ("Edge", "Raspberry Pi 5 · Python · picamera2 · pyserial · systemd daemon"),
        ("Hardware", "Arducam IMX296 (CSI) · GPS · SIM7600G-H 4G HAT"),
        ("Backend", "FastAPI · SQLAlchemy · Celery · YOLO detection workers"),
        ("Database", "PostgreSQL + PostGIS for geolocated findings"),
        ("Storage", "MinIO (S3-compatible) for captured imagery"),
        ("Frontend & ops", "Next.js 15 · TypeScript · Tailwind · Leaflet · Docker Compose · Nginx"),
    ],
    highlights=[
        "Runs on commodity hardware — a Pi, a camera and a 4G modem, not a specialised inspection vehicle",
        "Offline-first by design: buffer on the cart, reconcile in the cloud",
        "Single-command local environment (docker-compose up) with an auto-seeded admin user",
        "Provisioning is scripted end to end, from flashing the Pi to starting the capture service",
    ],
)

# 11/12 --------------------------------------------------------------- RDACTD
slide(
    type="story",
    number="07",
    project="RDACTD",
    kicker="Enterprise integrity · multi-tenant SaaS",
    title="Complaints that can be trusted, tracked and measured",
    context="Complaint management and business analytics platform — encrypted reporting, "
            "structured resolution, and integrity analytics for multi-branch organisations.",
    problem="Serious complaints still travel by email. Reporters have no privacy and no "
            "visibility, organisations have no structured record, and neither side can show "
            "afterwards that anything was actually resolved.",
    built=[
        "Encrypted, evidence-backed submission flows with categorical routing and real-time status tracking",
        "End-to-end resolution channels that let a reporter and an organisation lead work a case to closure",
        "Organizational health dashboards for multi-branch entities, with predictive risk modelling and integrity benchmarking",
        "AI-assisted pattern identification across cases, plus automated structural-health forecasting",
        "Public verified profiles showing integrity scores, historical performance and resolution velocity",
        "Multi-tier SaaS framework with billing, team governance and role-based administration",
    ],
    hard_title="Why it is hard",
    hard="Web and native mobile share one TypeScript core — models, service layer, tRPC "
         "client, WebSocket client, Drizzle schema and design tokens all live in shared "
         "packages. The two clients cannot drift apart, because there is only one "
         "implementation of the rules.",
    visual="rdactd",
)

slide(
    type="proof",
    project="RDACTD",
    title="Architecture & stack",
    diagram="rdactd",
    stack=[
        ("Web", "Next.js 15 · Tailwind CSS 4 · SEO-ready App Router"),
        ("Mobile", "Expo 53 · Expo Router · native iOS and Android"),
        ("Shared core", "packages/shared — models, services, tRPC client, WebSocket client"),
        ("Data", "packages/database — Drizzle ORM schema on PostgreSQL"),
        ("Realtime", "packages/websocket — Socket.io server for live case chat"),
        ("Build & deploy", "Turborepo · Docker · Google Cloud Build · Firebase Storage"),
    ],
    highlights=[
        "One monorepo, four packages, two apps — a change to a business rule lands everywhere at once",
        "Design tokens as a package, so web and native render the same product",
        "Real-time case chat over Socket.io, with offline-tolerant client behaviour",
        "Containerised web and websocket services, built and deployed through Cloud Build pipelines",
    ],
)

# 13/14 ------------------------------------------------- Open Air Construction
slide(
    type="story",
    number="08",
    project="Open Air Construction",
    kicker="Commercial web · lead generation · local SEO",
    title="A contractor site built to convert, not just to exist",
    context="Charlotte deck and outdoor-living contractor website — a production marketing "
            "site with a full lead pipeline behind it.",
    problem="A local contractor needs more than a brochure: fast pages, trust signals, "
            "service-area coverage, and a dependable way to turn consultation requests into "
            "leads someone actually follows up — without losing editorial control or SEO.",
    built=[
        "Next.js 16 App Router with Tailwind CSS v4 over a custom Material 3 token layer, light and dark themes",
        "A typed content layer — services, team, FAQs and metadata in TypeScript, so structural mistakes fail the build",
        "An MDX blog the owner can add to by dropping in a file, rendered through a custom loader",
        "Lead pipeline: contact form Server Action with Zod validation, Postgres persistence and Resend email notification",
        "A protected admin inbox with bcrypt auth, lead filtering, status management and CRM sync hooks",
        "Technical SEO — LocalBusiness, Service and FAQ JSON-LD, sitemap, robots, dynamic OG images",
    ],
    hard_title="The result",
    hard="A Lighthouse SEO score of 100, an editor workflow that needs no developer, and "
         "JobTread CRM plus AI enrichment already wired in behind environment keys — they "
         "switch on without touching the plumbing.",
    visual="oac",
)

slide(
    type="proof",
    project="Open Air Construction",
    title="Architecture & stack",
    diagram="oac",
    stack=[
        ("Frontend", "Next.js 16 · TypeScript · Tailwind CSS v4 · Material 3 tokens · next-themes"),
        ("Content", "Typed TS content modules · MDX blog via next-mdx-remote/rsc"),
        ("Backend", "Server Actions · Zod validation · PostgreSQL (Neon)"),
        ("Email & CRM", "Resend notifications · JobTread sync seam · AI enrichment gateway"),
        ("SEO", "JSON-LD (LocalBusiness, Service, FAQ) · sitemap · robots · dynamic OG images"),
        ("Quality & ops", "Vitest + Testing Library · Vercel deployment"),
    ],
    highlights=[
        "Lighthouse SEO score of 100 at launch",
        "Non-developers publish blog posts and update service copy without touching layout code",
        "Integrations activate by setting environment keys — no code change required",
        "Proof that the same team that ships regulated AI platforms also ships a marketing site in weeks",
    ],
)


# 15 --------------------------------------------------------- Trinly services
slide(
    type="grid",
    number="09",
    title="Trinly — services",
    lead="AI strategy through to shipped product. Delivered from the US and Europe, with "
         "the India engineering bench behind every engagement.",
    columns=4,
    cards=[
        ("AI strategy & consulting", "Where AI actually pays in your business, what to build first, and what to leave alone."),
        ("RAG & retrieval systems", "Chunking, embeddings, vector search, reranking and evaluation — grounded answers with citations."),
        ("Model training & fine-tuning", "Custom training, LoRA, domain adaptation, and the eval harness that proves it improved."),
        ("AI agents & automation", "Tool-using agents that complete multi-step workflows, with guardrails and human checkpoints."),
        ("Computer vision", "Detection, segmentation and thermal analysis — cloud pipelines or constrained edge devices."),
        ("Data pipelines & platform", "Ingestion, ETL, geospatial and time-series stores, and the infrastructure underneath."),
        ("MLOps & production", "Serving, monitoring, drift detection, retraining loops, CI/CD and cost control."),
        ("Web & mobile product", "Full product engineering — Next.js and React web, React Native and Expo mobile, APIs and admin tooling."),
    ],
)

# 16 -------------------------------------------------------- ArtSync services
slide(
    type="grid",
    number="10",
    title="ArtSync India — services & support",
    row_h=180,
    lead="Your partner in digital excellence: software development, data intelligence and "
         "dependable IT support, delivered at scale from six hubs across India.",
    columns=3,
    cards=[
        ("Custom software development", "Web applications, enterprise systems and internal tools, built and maintained by dedicated teams."),
        ("Enterprise solutions & integration", "ERP, CRM and line-of-business integration; APIs and middleware between systems that were never designed to talk."),
        ("Data intelligence & engineering", "Data cleaning, transformation, migration and warehousing — turning messy source data into something models can use."),
        ("Data annotation at scale", "Image, video, text and multimodal labeling with human-in-the-loop QA and ontology governance."),
        ("Data entry & back-office operations", "High-volume, accuracy-critical processing with defined SLAs and quality sampling."),
        ("IT support & managed services", "Helpdesk, infrastructure monitoring, patching and maintenance — day-to-day operational cover."),
    ],
)

# 17 --------------------------------------------------------- specialization
slide(
    type="feature",
    number="11",
    title="Specialisation — data annotation for physical AI",
    lead="A core group specialisation: high-quality video and multimodal annotation for "
         "computer-vision and Vision-Language-Action systems.",
    body="Robotics and physical-AI teams are bottlenecked on demonstration data, not on model "
         "architecture. We deliver frame-accurate temporal segmentation, keypoint and "
         "object-interaction labeling, multi-view clip decomposition, and ontology-driven "
         "consistency across large demonstration datasets — backed by in-house ML teams, so "
         "datasets arrive clean, structured and training-ready rather than as a pile of raw "
         "labels someone else has to fix.",
    points=[
        ("Frame-accurate temporal segmentation", "Action boundaries labelled to the frame, not the second."),
        ("Keypoint & object interaction", "Grasp points, contact events and manipulation states across the clip."),
        ("Multi-view decomposition", "Synchronised labeling across camera rigs for the same demonstration."),
        ("Ontology governance", "One label taxonomy, enforced across every annotator and every batch."),
        ("Human-in-the-loop QA", "Sampled review, inter-annotator agreement and correction loops."),
        ("ML teams in the loop", "The people labeling the data work alongside the people training on it."),
    ],
    tools=["CVAT", "Labelbox", "Label Studio", "Temporal segmentation", "Keypoint labeling", "HITL QA", "VLA datasets"],
)

# 18 ------------------------------------------------------------ how we work
slide(
    type="steps",
    number="12",
    title="How we deliver",
    lead="The same four-stage path on every engagement — from a two-week website to a "
         "regulated clinical platform. Only the depth changes.",
    steps=[
        ("01", "Data audit & strategy",
         "Audit what you have, structure it, and define an approach tied to a business outcome — not to a model."),
        ("02", "Build & train",
         "Model selection, training, pipeline and application build, with evaluation gates before anything is called done."),
        ("03", "Production deployment",
         "Scalable, monitored delivery to production — infrastructure, CI/CD, security and handover documentation."),
        ("04", "Continuous optimisation",
         "Live telemetry drives retraining, tuning and the next increment of the roadmap."),
    ],
)

# 19 --------------------------------------------------- engagement & support
slide(
    type="two_col_list",
    number="13",
    title="Engagement & ongoing support",
    lead="Four ways to work with us, and a support commitment that does not end at launch.",
    left_title="Engagement models",
    left=[
        ("Fixed-scope project", "Defined deliverable, defined price, defined timeline. Best when the outcome is clear."),
        ("Retained / dedicated team", "A named team on a monthly retainer, working your roadmap as priorities shift."),
        ("Staff augmentation", "Senior AI, data and full-stack engineers embedded in your existing team."),
        ("Managed support & SLA", "We operate what we built — or what someone else built — under an agreed response SLA."),
    ],
    right_title="What support includes",
    right=[
        ("Production monitoring", "Uptime, error and performance monitoring with defined incident response."),
        ("Model health", "Drift detection, evaluation on live data, and a scheduled retraining cadence."),
        ("Security & maintenance", "Dependency patching, vulnerability response, access reviews and backups."),
        ("Cost optimisation", "Inference, storage and cloud spend reviewed and tuned as usage grows."),
        ("Enablement", "Documentation, handover and training so your team can run the system themselves."),
    ],
)

# 20 ------------------------------------------------------- industries / why
slide(
    type="two_col_pills",
    number="14",
    title="Industries & why clients choose us",
    left_title="Industries we serve",
    pills=[
        "Healthcare & clinical trials", "Rail & transport infrastructure", "Drone & geospatial",
        "Robotics & physical AI", "Financial services & fintech", "B2B SaaS & enterprise software",
        "Construction & home services",
    ],
    pills_note="From early-stage startups to established enterprises.",
    right_title="Why clients choose us",
    reasons=[
        ("End-to-end ownership", "Raw data to deployed product, with no hand-off gap between strategy, data and engineering."),
        ("Regulated-domain experience", "We have built to 21 CFR Part 11 with tamper-evident audit trails and electronic signatures."),
        ("Senior plus scale", "US and Europe based architects, with a deep India engineering and data bench behind them."),
        ("Production-first", "Monitored systems running in production — not proofs of concept that stall at the demo."),
        ("Follow-the-sun delivery", "Hubs across five countries keep work moving while your team sleeps."),
    ],
)

# 21 ---------------------------------------------------------------- closing
slide(
    type="closing",
    eyebrow="Let's talk",
    title="Tell us what you are trying to build",
    lead="Every engagement starts the same way: a 15-minute scoping call, then a written "
         "proposal with scope, timeline and price. No obligation, and no charge for the "
         "conversation.",
    founder=META["founder"],
    email=META["email"],
    phones=META["phones"],
    sites=META["sites"],
)
