"""
ShopSense Complete Master Submission Book & Viva Guide
Author: Shaurya (shauryadeep707@gmail.com)
Project: E-Commerce Product Search and Recommendations System (ShopSense)
Database: Supabase PostgreSQL Cloud (AWS) - nzccgolsbffelzdxtkom.supabase.co

Features:
- Chapter 1: Introduction to Data Flow Diagrams (What is DFD, Standard Symbols & Rules)
- Chapter 2: DFD Level 0 (Context Diagram) - Detailed Definition & Explanation of What It Means
- Chapter 3: DFD Level 1 (Subsystems Flow) - Detailed Definition & Explanation of What It Means
- Chapter 4: DFD Level 2A (Search & Recommender Engine) - Deep Sub-Process Meaning
- Chapter 5: DFD Level 2B (Cart, Checkout & Order Pipeline) - Deep Sub-Process Meaning
- Chapter 6: Entity Relationship Diagram (ERD) - Full Meaning, Tables, Keys & Cascades
- Chapter 7: System Integration ("How Everything Connects" - Frontend -> Backend -> Cloud DB)
- Chapter 8: Final Project Viva & Oral Examination Q&A Guide
"""

import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak,
    HRFlowable,
    KeepTogether,
)
from reportlab.pdfgen import canvas

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

DESKTOP = Path(r"c:\Users\shaur\OneDrive\Desktop\shop sence")
DFD0_IMG = DESKTOP / "dfd_level0.png"
DFD1_IMG = DESKTOP / "dfd_level1.png"
DFD2A_IMG = DESKTOP / "dfd_level2_search.png"
DFD2B_IMG = DESKTOP / "dfd_level2_checkout.png"
ERD_IMG = DESKTOP / "erd_diagram.png"

OUTPUT_PDF = DESKTOP / "ShopSense_Final_Project_Submission_Shaurya.pdf"
COMPREHENSIVE_PDF = DESKTOP / "ShopSense_Complete_DFD_and_Architecture_Guide.pdf"


class NumberedCanvas(canvas.Canvas):
    """Canvas that computes total pages dynamically and adds running headers & footers."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 762, "ShopSense — Complete All-Level DFD & Database Architecture Guide")
            self.drawRightString(576, 762, "Candidate: Shaurya")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(36, 756, 576, 756)

        # Footer (All pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 38, 576, 38)
        self.drawString(36, 26, "Supabase PostgreSQL (AWS Cloud) | Node.js Express & Python AI Engine")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 26, page_str)

        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#475569"),
        spaceAfter=10,
    )
    h1_style = ParagraphStyle(
        "DocH1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=10,
        spaceAfter=6,
    )
    h2_style = ParagraphStyle(
        "DocH2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0284c7"),
        spaceBefore=8,
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "DocBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6,
    )
    bullet_style = ParagraphStyle(
        "DocBullet",
        parent=body_style,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3,
    )
    callout_style = ParagraphStyle(
        "DocCallout",
        parent=body_style,
        fontName="Helvetica-Oblique",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0369a1"),
    )

    story = []

    # =========================================================================
    # PAGE 1: TITLE, PROJECT SUMMARY & WHAT A DFD IS
    # =========================================================================
    story.append(Paragraph("ShopSense — Complete All-Level Data Flow Diagrams (DFD) & Architecture Book", title_style))
    story.append(Paragraph("A Comprehensive Engineering Guide to DFD Levels 0, 1, 2A, 2B, 10-Table ERD, and Cloud Database Integration", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#0284c7"), spaceAfter=8))

    meta_table_data = [
        [
            Paragraph("<b>Candidate Name:</b> Shaurya", body_style),
            Paragraph("<b>Target Database:</b> Supabase PostgreSQL (AWS)", body_style),
        ],
        [
            Paragraph("<b>Candidate Email:</b> shauryadeep707@gmail.com", body_style),
            Paragraph("<b>Database Host:</b> nzccgolsbffelzdxtkom.supabase.co", body_style),
        ],
        [
            Paragraph("<b>Project Title:</b> ShopSense E-Commerce Platform", body_style),
            Paragraph("<b>Key Features:</b> Hybrid Search, Recommendations, Cloud DB", body_style),
        ],
    ]
    meta_table = Table(meta_table_data, colWidths=[270, 270])
    meta_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
            ("PADDING", (0, 0), (-1, -1), 4.5),
            ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ])
    )
    story.append(meta_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Chapter 1: Understanding Data Flow Diagrams (What Does a DFD Mean?)", h1_style))
    story.append(Paragraph(
        "A <b>Data Flow Diagram (DFD)</b> is a fundamental software engineering modeling tool that graphically depicts how data moves through an information system. Unlike a traditional flowchart—which illustrates programming control structures, step-by-step loops, and conditional decision logic—a DFD focuses entirely on <b>the flow of information</b>: where data originates, how it is processed and transformed, where it is stored for persistence, and who ultimately receives the output.",
        body_style,
    ))

    story.append(Paragraph("<b>The Four Standard Components of Any DFD (Gane & Sarson / Yourdon Notation):</b>", body_style))
    dfd_components_data = [
        ["DFD Symbol", "Name", "Role in ShopSense", "Notation Used in This Report"],
        ["External Entity", "Terminator / Actor", "Outside people or systems that send data into ShopSense or receive its output.", "Solid Slate Rectangle (Customer, Admin, Stripe)"],
        ["Process", "Transformer / Function", "A computational operation that transforms incoming data into outgoing data.", "Rounded Blue Box or Circle with ID (0.0, 1.0, 2.1)"],
        ["Data Store", "Repository / Database", "Persistent storage where data is retained for future querying.", "Open-Ended Parallel Emerald Green Box (D1 to D6)"],
        ["Data Flow", "Information Packet", "The pipeline along which data travels; arrows show the exact direction of movement.", "Solid or Dashed Labeled Directed Vectors with Badges"],
    ]
    comp_table = Table(dfd_components_data, colWidths=[75, 95, 230, 140])
    comp_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.2),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 3.5),
        ])
    )
    story.append(comp_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>The Concept of Hierarchical Levels (Level 0 &rarr; Level 1 &rarr; Level 2):</b>", body_style))
    story.append(Paragraph(
        "A complex system cannot be understood all at once. DFDs solve this through <b>top-down functional decomposition</b>. You begin at the bird's-eye view (Level 0), zoom into major functional subsystems (Level 1), and then zoom into specific atomic sub-processes (Level 2). This ensures that developers, auditors, and viva examiners can inspect both high-level architecture and deep transactional implementation without confusion.",
        body_style,
    ))

    # =========================================================================
    # PAGE 2: CHAPTER 2: DFD LEVEL 0 (CONTEXT DIAGRAM) & ITS MEANING
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 2: DFD Level 0 — The Context Diagram & What It Means", h1_style))
    story.append(Paragraph(
        "<b>What Does 'Level 0' Mean?</b><br/>"
        "DFD Level 0 is also called the <b>Context Diagram</b>. It represents the <i>entire software application as a single circular or rounded process (designated 0.0)</i>. No internal algorithms, internal tables, or subroutines are visible at this level. Its sole purpose is to establish the <b>system boundary</b>—clearly showing who interacts with the system from the outside and what fundamental data passes across that boundary.",
        body_style,
    ))
    story.append(Image(str(DFD0_IMG), width=540, height=270))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Detailed Data Exchange in Level 0:</b>", body_style))
    story.append(Paragraph("&bull; <b>Customer &rarr; ShopSense (0.0):</b> The user inputs natural language search queries (e.g. 'wireless bluetooth headphones'), filters by price/brand, modifies shopping cart items, submits checkout forms, and emits clickstream dwell interactions.", bullet_style))
    story.append(Paragraph("&bull; <b>ShopSense (0.0) &rarr; Customer:</b> The system outputs personalized product recommendations, ranked hybrid search result cards, real-time cart tallies, authentication JWTs, and verifiable digital purchase receipts.", bullet_style))
    story.append(Paragraph("&bull; <b>Admin &rarr; ShopSense (0.0) &rarr; Admin:</b> Administrators submit bulk catalog CSV updates, adjust product stock levels, and inspect search latency logs and conversion metrics.", bullet_style))
    story.append(Paragraph("&bull; <b>ShopSense (0.0) &harr; Supabase PostgreSQL Cloud:</b> The system issues transactional SQL queries (INSERT, UPDATE, UPSERT) and fetches product embeddings, user profiles, and past behavior matrices.", bullet_style))
    story.append(Paragraph("&bull; <b>ShopSense (0.0) &harr; Payment Gateway:</b> Dispatches the computed invoice amount and receives cryptographic payment verification webhooks.", bullet_style))

    # =========================================================================
    # PAGE 3: CHAPTER 3: DFD LEVEL 1 (SUBSYSTEMS FLOW) & ITS MEANING
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 3: DFD Level 1 — Functional Decomposition & What It Means", h1_style))
    story.append(Paragraph(
        "<b>What Does 'Level 1' Mean?</b><br/>"
        "DFD Level 1 is created by 'exploding' the single 0.0 process from Level 0 into its major functional subsystems (numbered 1.0, 2.0, 3.0, 4.0, 5.0, 6.0). In addition, Level 1 introduces <b>Data Stores (D1 through D6)</b>, making the database tables explicit for the first time. It answers: <i>'Which specific subsystem handles each user action, and which exact database table does it read from or write to?'</i>",
        body_style,
    ))
    story.append(Image(str(DFD1_IMG), width=540, height=300))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>The 6 Subsystems and Their Data Stores in Level 1:</b>", body_style))
    l1_explanation = [
        ["Subsystem", "Process ID", "Data Store", "Detailed Transformation Meaning"],
        ["Authentication & Profiles", "1.0", "D1: public.users", "Receives email/password; verifies scrypt password hash; issues signed JSON Web Token (JWT); returns user profile."],
        ["Hybrid Search Engine", "2.0", "D2: products\nD6: search_logs", "Splits query into lexical keywords (BM25) and semantic vectors (TF-IDF); merges matches via Reciprocal Rank Fusion; logs query latency."],
        ["Recommendation Engine", "3.0", "D3: interactions", "Loads 1,561 historical user-item weights (1 to 5); computes item similarity matrices; generates personalized home feed carousel."],
        ["Cart & Wishlist Manager", "4.0", "D4: cart_items\nwishlist_items", "Manages user baskets; enforces composite key (user_id, product_id) to eliminate duplicate rows; handles real-time quantity updates."],
        ["Checkout & Invoicing", "5.0", "D5: orders\norder_items", "Calculates subtotal, shipping, and tax; executes payment gateway handshake; writes order records; decrements product inventory; clears cart."],
        ["Telemetry Tracker", "6.0", "D3: interactions\nD6: search_logs", "Asynchronously records customer behavioral signals (product views, click events, cart additions) without blocking UI response times."],
    ]
    l1_table = Table(l1_explanation, colWidths=[105, 50, 95, 290])
    l1_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0284c7")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.2),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 3),
        ])
    )
    story.append(l1_table)

    # =========================================================================
    # PAGE 4: CHAPTER 4: DFD LEVEL 2A (SEARCH & RECOMMENDATION PIPELINE)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 4: DFD Level 2A — Deep Dive into Search & Recommendations", h1_style))
    story.append(Paragraph(
        "<b>What Does 'Level 2' Mean?</b><br/>"
        "A Level 2 DFD explodes a single Level 1 process into its internal, algorithmic sub-processes (e.g., Process 2.0 explodes into 2.1, 2.2, 2.3, 2.4). Level 2A reveals the mathematical and algorithmic pipeline behind ShopSense's <b>AI Hybrid Search</b> and <b>Personalized Recommender</b>.",
        body_style,
    ))
    story.append(Image(str(DFD2A_IMG), width=540, height=300))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Step-by-Step Sub-Process Execution in Level 2A:</b>", body_style))
    story.append(Paragraph("&bull; <b>2.1 Query Preprocessor:</b> Receives raw search text (e.g., 'running sneekers'). Performs tokenization, lowercasing, stop-word elimination ('the', 'for'), and spell-correction matching against the product catalog.", bullet_style))
    story.append(Paragraph("&bull; <b>2.2 Lexical BM25 Engine:</b> Queries the inverted text index of 591 products in <code>D2: products</code>. It calculates Term Frequency and Inverse Document Frequency to surface exact keyword matches.", bullet_style))
    story.append(Paragraph("&bull; <b>2.3 Semantic Vector Matcher:</b> Simultaneously computes dense vector TF-IDF/embeddings for the query and measures cosine similarity against product descriptions, capturing contextual meaning even with zero keyword overlap.", bullet_style))
    story.append(Paragraph("&bull; <b>2.4 Reciprocal Rank Fusion (RRF):</b> Merges both ranked result sets using the official formula: <i>RRF Score = &Sigma; 1 / (60 + Rank<sub>model</sub>)</i>. This prevents either algorithm from overpowering the other. Latency is logged to <code>D6: search_logs</code>.", bullet_style))
    story.append(Paragraph("&bull; <b>3.1 to 3.3 Recommender Pipeline:</b> Records implicit telemetry into <code>D3: interactions</code> with assigned weights (View = 1, Cart = 3, Purchase = 5). Process 3.2 uses collaborative filtering to find nearest neighbor products, and Process 3.3 composes the personal homepage carousel.", bullet_style))

    # =========================================================================
    # PAGE 5: CHAPTER 5: DFD LEVEL 2B (CART, CHECKOUT & ORDERS)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 5: DFD Level 2B — Deep Dive into Cart, Checkout & Orders", h1_style))
    story.append(Paragraph(
        "<b>What Does Level 2B Mean?</b><br/>"
        "Level 2B explodes Process 4.0 (Cart & Wishlist) and Process 5.0 (Checkout & Orders). It models the critical business logic of <b>transactional consistency, composite key deduplication, inventory validation, and financial record immutability</b>.",
        body_style,
    ))
    story.append(Image(str(DFD2B_IMG), width=540, height=290))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>The Four Inviolable Transactional Rules in Level 2B:</b>", body_style))
    story.append(Paragraph("&bull; <b>Rule 1: Composite Primary Key Deduplication (4.1 &rarr; D4):</b> Junction tables <code>cart_items</code> and <code>wishlist_items</code> use <code>PRIMARY KEY (user_id, product_id)</code>. If a customer clicks 'Add to Cart' three times, the database does NOT insert three rows; instead, it executes <code>ON CONFLICT DO UPDATE SET quantity = quantity + 1</code>.", bullet_style))
    story.append(Paragraph("&bull; <b>Rule 2: Real-time Stock Verification (4.2 &harr; D2):</b> Before proceeding to payment, the system queries <code>public.products</code> to confirm that <code>stock &gt;= requested_quantity</code>, preventing overselling.", bullet_style))
    story.append(Paragraph("&bull; <b>Rule 3: Multi-Table Transaction Commit (5.3 &rarr; D5):</b> Once Stripe/Razorpay validates payment, the checkout engine runs an atomic SQL transaction: creates the master order record in <code>orders</code>, creates individual line items in <code>order_items</code>, and captures the purchase price.", bullet_style))
    story.append(Paragraph("&bull; <b>Rule 4: Stock Reduction & Cart Purge (5.3 &rarr; D2 & D4):</b> Decrements product stock (<code>UPDATE products SET stock = stock - qty</code>) and clears the user's active cart rows (<code>DELETE FROM cart_items WHERE user_id = :uid</code>).", bullet_style))

    # =========================================================================
    # PAGE 6: CHAPTER 6: ENTITY RELATIONSHIP DIAGRAM (ERD) & WHAT IT MEANS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 6: Entity Relationship Diagram (ERD) & What It Means", h1_style))
    story.append(Paragraph(
        "<b>What Does an ERD Mean?</b><br/>"
        "While a DFD shows data in <i>motion</i> (streams, pipelines, transformations), an <b>Entity Relationship Diagram (ERD)</b> models data at <i>rest</i> (tables, columns, primary keys, foreign keys, and relational cardinality). The ShopSense schema comprises 10 PostgreSQL tables deployed live on Supabase AWS:",
        body_style,
    ))
    story.append(Image(str(ERD_IMG), width=540, height=300))
    story.append(Spacer(1, 6))

    erd_summary_data = [
        ["Table Name", "Role / Type", "Primary Key", "Foreign Keys", "Business Function & Integrity Rules"],
        ["users", "Master Entity", "id (TEXT)", "None", "Stores customer and admin credentials, password hashes, and security roles."],
        ["products", "Master Entity", "id (TEXT)", "None", "591 catalog items: title, category, price, stock, and descriptions."],
        ["cart_items", "Junction (Weak)", "(user_id, product_id)", "user_id, product_id", "Associative table linking users to products with quantity; ON DELETE CASCADE."],
        ["wishlist_items", "Junction (Weak)", "(user_id, product_id)", "user_id, product_id", "Bookmarked items for future purchase; composite primary key prevents duplicate saves."],
        ["orders", "Master Transaction", "id (TEXT)", "user_id &rarr; users", "Financial order headers with total_amount, currency, shipping, and order status."],
        ["order_items", "Junction Line Item", "(order_id, product_id)", "order_id, product_id", "Immutable purchase line items preserving historical unit_price and quantity."],
        ["interactions", "Telemetry Log", "id (TEXT)", "user_id, product_id", "1,561 rows of user behavioral events (view=1, cart=3, purchase=5) for collaborative filtering."],
        ["events", "Telemetry Log", "id (TEXT)", "user_id &rarr; users", "Unstructured system and audit events stored as flexible JSONB payloads."],
        ["search_history", "Analytics Log", "id (TEXT)", "user_id &rarr; users", "Stores user query strings and total product results returned."],
        ["search_logs", "System Benchmark", "id (TEXT)", "None", "Captures global search performance benchmarks and query latency in milliseconds."],
    ]
    erd_table = Table(erd_summary_data, colWidths=[70, 75, 90, 85, 220])
    erd_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#065f46")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 6.8),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 2.8),
        ])
    )
    story.append(erd_table)

    # =========================================================================
    # PAGE 7: CHAPTER 7: HOW EVERYTHING CONNECTS (SYSTEM INTEGRATION)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 7: How Everything Connects (End-to-End System Integration)", h1_style))
    story.append(Paragraph(
        "In a real-world enterprise architecture, the Data Flow Diagrams and the Entity Relationship Diagram are two sides of the same coin. This chapter explains the end-to-end connectivity across all layers of ShopSense:",
        body_style,
    ))

    story.append(Paragraph("<b>7.1 The Three-Tier Architecture of ShopSense:</b>", body_style))
    story.append(Paragraph("&bull; <b>Tier 1: Presentation Tier (Frontend Browser):</b> Vanilla JavaScript and HTML5/CSS3 client. Makes asynchronous HTTP REST calls (<code>fetch()</code>) sending JSON payloads to the Express API server.", bullet_style))
    story.append(Paragraph("&bull; <b>Tier 2: Application Tier (Node.js & Python Services):</b><br/>"
                           "  - <i>Node.js Express Server (<code>backend/server.js</code>):</i> Handles web traffic, authentication token checks, cart mutations, and forward queries to Supabase.<br/>"
                           "  - <i>Python Data Engine (<code>database/</code>):</i> Uses <code>psycopg2</code> and <code>SQLAlchemy</code> over direct SSL port 5432 for analytical queries, model training, and database migrations.", bullet_style))
    story.append(Paragraph("&bull; <b>Tier 3: Persistence Tier (Supabase PostgreSQL Cloud):</b> Hosted in AWS Cloud. Manages row-level security, constraints, foreign key cascades, and ACID transactions.", bullet_style))

    story.append(Paragraph("<b>7.2 Cross-Mapping: How DFD Processes Map to ERD Tables:</b>", body_style))
    mapping_data = [
        ["DFD Process ID", "Process Subsystem Name", "Associated ERD Tables", "Database Operations Executed"],
        ["1.0", "Auth & Profile Management", "public.users", "SELECT user BY email; INSERT INTO users; UPDATE last_login"],
        ["2.0 (2.1-2.4)", "Hybrid Search Engine", "public.products\npublic.search_logs", "SELECT * FROM products WHERE text_vector @@ query; INSERT search_logs"],
        ["3.0 (3.1-3.3)", "Recommendation Engine", "public.interactions\npublic.products", "SELECT user_id, product_id, weight FROM interactions; Matrix dot-product"],
        ["4.0 (4.1-4.2)", "Cart & Wishlist Manager", "public.cart_items\npublic.wishlist_items", "INSERT INTO cart_items ON CONFLICT (user_id, product_id) DO UPDATE quantity"],
        ["5.0 (5.1-5.3)", "Checkout & Order Engine", "public.orders\npublic.order_items\npublic.products\npublic.cart_items", "BEGIN TRANSACTION;\nINSERT INTO orders ...;\nINSERT INTO order_items ...;\nUPDATE products SET stock = stock - qty;\nDELETE FROM cart_items WHERE user_id = :uid;\nCOMMIT;"],
        ["6.0", "Telemetry Tracker", "public.events\npublic.interactions", "INSERT INTO events (payload JSONB); INSERT INTO interactions VALUES (uid, pid, wt)"],
    ]
    map_table = Table(mapping_data, colWidths=[65, 120, 115, 240])
    map_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.2),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 3),
        ])
    )
    story.append(map_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>7.3 Why Composite Primary Keys Are Used:</b>", body_style))
    story.append(Paragraph(
        "A common viva question is: <i>'Why not give cart_items a single auto-incrementing id column?'</i><br/>"
        "<b>Answer:</b> If <code>cart_items</code> has a surrogate <code>id</code>, the database cannot prevent a user from having two rows for the same product without a separate unique index. By defining <code>PRIMARY KEY (user_id, product_id)</code>, the primary key itself enforces logical uniqueness, saves index memory, guarantees O(1) indexed lookups, and makes upserts (<code>ON CONFLICT DO UPDATE</code>) completely seamless.",
        body_style,
    ))

    # =========================================================================
    # PAGE 8: CHAPTER 8: PROJECT VIVA & ORAL EXAM PREPARATION GUIDE
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 8: Project Viva & Oral Examination Guide (Top Questions & Answers)", h1_style))
    story.append(Paragraph(
        "Review these model answers to explain your project with 100% confidence in front of project evaluators and viva professors:",
        body_style,
    ))

    viva_qas = [
        ("Q1: What is the fundamental difference between DFD Level 0, Level 1, and Level 2?",
         "A: DFD Level 0 (Context Diagram) views the entire system as one black-box process (0.0) and defines the external boundaries (who sends and receives data). Level 1 decomposes that black box into major operational subsystems (1.0 to 6.0) and reveals the database stores (D1 to D6). Level 2 explodes individual complex subsystems into their precise algorithmic and transactional steps (e.g., Level 2A for BM25/Semantic Search fusion and Level 2B for transactional checkout)."),
        ("Q2: Why did you choose Supabase PostgreSQL instead of SQLite or MongoDB?",
         "A: SQLite is a file-based embedded database lacking native multi-user cloud concurrency and networked access for deployed web apps (like Render). MongoDB is NoSQL, which lacks strict relational foreign key enforcement and composite primary keys. Supabase provides enterprise PostgreSQL with ACID transactions, Row-Level Security, direct SSL connection for Python data science, and auto-generated HTTPS REST APIs for Node.js."),
        ("Q3: How does your search engine combine keyword search with semantic search?",
         "A: We use a Hybrid Search architecture. Process 2.2 runs BM25 lexical search over title and category terms for exact matches. Process 2.3 computes TF-IDF semantic embeddings for contextual intent. Process 2.4 applies Reciprocal Rank Fusion (RRF: score = sum(1/(60+rank))) to combine both rankings into a final score, ensuring high recall and precision."),
        ("Q4: How do you prevent data corruption when an order is placed?",
         "A: In Process 5.3 (Level 2B), checkout uses a multi-table database transaction (ACID). If the payment succeeds, the order header and line items are written, stock is decremented in public.products, and cart rows are cleared in cart_items. If any operation fails or network drops, the entire transaction rolls back, preventing lost money or inventory mismatches."),
        ("Q5: What happens if a user deletes their account? How do you prevent orphaned records?",
         "A: All foreign key constraints referencing public.users (such as in cart_items, wishlist_items, orders, and interactions) are configured with ON DELETE CASCADE. When a user row is removed, PostgreSQL automatically purges all related rows, maintaining referential integrity with zero orphan records."),
    ]

    for q, a in viva_qas:
        story.append(Paragraph(f"<b>{q}</b>", h2_style))
        story.append(Paragraph(a, body_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284c7"), spaceAfter=6))
    story.append(Paragraph(
        "<b>Summary:</b> This document constitutes the verified master engineering specification for ShopSense. All diagrams, schemas, and live database tables have been verified against the production Supabase PostgreSQL instance at <code>nzccgolsbffelzdxtkom.supabase.co</code>.",
        callout_style,
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Complete Master Submission Book generated: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
