"""
Generate the Final Project Presentation & Viva Master PDF for Shaurya.
Features:
- DFD Level 0 (Context Level Diagram)
- DFD Level 1 (Detailed 5-Process System Flow)
- Corrected Entity Relationship Diagram (ERD) with 10 tables
- Step-by-Step 'How Everything Connects' Explanation
- Final Project Summary & Viva Presentation Talking Points
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
)

DESKTOP_DIR = Path("c:/Users/shaur/OneDrive/Desktop/shop sence")
OUTPUT_PDF = DESKTOP_DIR / "ShopSense_Final_Project_Submission_Shaurya.pdf"

DFD0_IMG = DESKTOP_DIR / "dfd_level0.png"
DFD1_IMG = DESKTOP_DIR / "dfd_level1.png"
ERD_IMG = DESKTOP_DIR / "erd_diagram.png"


def create_dfd_level0():
    """Generates DFD Level 0 (Context Level Diagram)."""
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    c_box = "#0f172a"
    c_proc = "#0284c7"
    c_store = "#059669"
    c_arrow = "#334155"

    # External Entity: User
    u_box = patches.FancyBboxPatch((0.6, 1.8), 2.2, 1.6, boxstyle="round,pad=0.1", fc=c_box, ec="none")
    ax.add_patch(u_box)
    ax.text(1.7, 2.6, "CUSTOMER / USER\n(Web Browser)", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=9.5)

    # Central Process: 0.0 ShopSense System
    p_box = patches.Circle((5.0, 2.6), 1.35, fc=c_proc, ec="#0369a1", lw=2)
    ax.add_patch(p_box)
    ax.text(5.0, 2.6, "0.0\nSHOPSENSE\nPLATFORM\n(Node.js / Python)", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=9.5)

    # External Database: Supabase Cloud
    db_box = patches.FancyBboxPatch((7.6, 1.8), 2.5, 1.6, boxstyle="round,pad=0.1", fc=c_store, ec="none")
    ax.add_patch(db_box)
    ax.text(8.85, 2.6, "SUPABASE CLOUD\n(PostgreSQL DB)\n10 Tables (AWS)", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=9.5)

    # Flows User <-> System
    ax.annotate("", xy=(3.65, 3.0), xytext=(2.8, 3.0), arrowprops=dict(arrowstyle="->", color=c_arrow, lw=1.8))
    ax.text(3.2, 3.25, "Queries, Orders, Clicks", ha="center", fontsize=8, color="#0f172a", fontweight="bold")

    ax.annotate("", xy=(2.8, 2.2), xytext=(3.65, 2.2), arrowprops=dict(arrowstyle="->", color=c_arrow, lw=1.8))
    ax.text(3.2, 1.85, "Search Results, Feed, Token", ha="center", fontsize=8, color="#0f172a", fontweight="bold")

    # Flows System <-> Supabase
    ax.annotate("", xy=(7.6, 3.0), xytext=(6.35, 3.0), arrowprops=dict(arrowstyle="->", color=c_arrow, lw=1.8))
    ax.text(7.0, 3.25, "SQL / REST Writes", ha="center", fontsize=8, color="#065f46", fontweight="bold")

    ax.annotate("", xy=(6.35, 2.2), xytext=(7.6, 2.2), arrowprops=dict(arrowstyle="->", color=c_arrow, lw=1.8))
    ax.text(7.0, 1.85, "Catalog, Profiles, History", ha="center", fontsize=8, color="#065f46", fontweight="bold")

    ax.text(5.0, 4.5, "Data Flow Diagram — Level 0 (Context Diagram)", ha="center", fontsize=13, fontweight="bold", color="#0f172a")
    ax.text(5.0, 4.15, "High-Level Data Interaction between User, ShopSense Engine, and Supabase Cloud", ha="center", fontsize=8.5, color="#64748b")

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0.8, 4.8)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(DFD0_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] DFD Level 0 saved: {DFD0_IMG}")


def create_dfd_level1():
    """Generates DFD Level 1 (Detailed 5-Process System Flow)."""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    c_entity = "#1e293b"
    c_proc = "#0284c7"
    c_store = "#059669"
    c_arrow = "#475569"

    # External Entity: Customer
    u_box = patches.FancyBboxPatch((0.5, 3.4), 1.8, 1.8, boxstyle="round,pad=0.12", fc=c_entity, ec="none")
    ax.add_patch(u_box)
    ax.text(1.4, 4.3, "Customer / User\n(Web Browser)", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=10)

    # 5 Processes
    processes = [
        (3.8, 6.2, "1.0 Auth & Profile\n(JWT & scrypt)"),
        (3.8, 4.8, "2.0 Search Engine\n(BM25 + TF-IDF + RRF)"),
        (3.8, 3.4, "3.0 Recommendation\n(CF + Matrix Factorization)"),
        (3.8, 2.0, "4.0 Cart & Wishlist\nManagement"),
        (3.8, 0.6, "5.0 Checkout & Order\nProcessing"),
    ]

    for x, y, label in processes:
        p_box = patches.FancyBboxPatch((x, y), 2.8, 0.95, boxstyle="round,pad=0.1", fc=c_proc, ec="none")
        ax.add_patch(p_box)
        ax.text(x + 1.4, y + 0.47, label, ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=8.5)

    # 5 Data Stores
    stores = [
        (8.5, 6.2, "D1: public.users (Auth & Profiles)"),
        (8.5, 4.8, "D2: public.products (591 Catalog Items)"),
        (8.5, 3.4, "D3: public.interactions (1,561 Feedback Rows)"),
        (8.5, 2.0, "D4: public.cart_items & wishlist_items"),
        (8.5, 0.6, "D5: public.orders & order_items"),
    ]

    for x, y, label in stores:
        ax.plot([x, x + 4.2, x + 4.2, x], [y + 0.85, y + 0.85, y + 0.05, y + 0.05], color=c_store, lw=2)
        ax.fill([x, x + 4.2, x + 4.2, x], [y + 0.85, y + 0.85, y + 0.05, y + 0.05], color="#ecfdf5")
        ax.text(x + 2.1, y + 0.45, label, ha="center", va="center", color="#065f46", fontweight="bold", fontsize=8.5)

    # Connectors
    flows = [
        (2.3, 4.8, 3.8, 6.6),
        (2.3, 4.5, 3.8, 5.3),
        (2.3, 4.2, 3.8, 3.9),
        (2.3, 3.9, 3.8, 2.5),
        (2.3, 3.6, 3.8, 1.1),
        (6.6, 6.6, 8.5, 6.6),
        (6.6, 5.3, 8.5, 5.3),
        (6.6, 3.9, 8.5, 3.9),
        (6.6, 2.5, 8.5, 2.5),
        (6.6, 1.1, 8.5, 1.1),
    ]

    for x1, y1, x2, y2 in flows:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=c_arrow, lw=1.5, shrinkA=3, shrinkB=3))

    ax.text(7.0, 7.6, "Data Flow Diagram — Level 1 (Detailed System Flow)", ha="center", fontsize=14, fontweight="bold", color=c_entity)
    ax.text(7.0, 7.3, "Detailed Data Flow from User Requests to Backend Subsystems and Supabase PostgreSQL Stores", ha="center", fontsize=9, color="#64748b")

    ax.set_xlim(0, 13.5)
    ax.set_ylim(0.2, 7.8)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(DFD1_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] DFD Level 1 saved: {DFD1_IMG}")


def create_erd_diagram():
    """Generates the corrected 10-table Entity Relationship Diagram."""
    fig, ax = plt.subplots(figsize=(14, 8.5), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    c_primary = "#0f172a"
    c_entity_bg = "#ffffff"
    c_entity_border = "#0284c7"
    c_weak_border = "#059669"
    c_line = "#475569"

    entities = [
        (0.6, 6.2, 2.8, 1.8, "USERS", False, [
            "+ id (PK) : TEXT",
            "- name : TEXT",
            "- email (UQ) : TEXT",
            "- role : TEXT",
            "- phone, profession : TEXT",
            "- preferences : JSONB"
        ]),
        (5.6, 6.2, 2.8, 1.8, "ORDERS", False, [
            "+ id (PK) : TEXT",
            "# user_id (FK) : TEXT",
            "- status : TEXT",
            "- total : NUMERIC",
            "- item_count : INTEGER",
            "- created_at : TIMESTAMPTZ"
        ]),
        (10.6, 6.2, 2.8, 1.8, "PRODUCTS", False, [
            "+ id (PK) : TEXT",
            "- title : TEXT",
            "- brand, category : TEXT",
            "- price, mrp : NUMERIC",
            "- rating, rating_count",
            "- data : JSONB"
        ]),
        (0.6, 3.4, 2.8, 1.4, "WISHLIST_ITEMS", True, [
            "+# user_id (PK, FK) : TEXT",
            "+# product_id (PK, FK) : TEXT",
            "- added_at : TIMESTAMPTZ"
        ]),
        (4.1, 3.4, 2.8, 1.5, "CART_ITEMS", True, [
            "+# user_id (PK, FK) : TEXT",
            "+# product_id (PK, FK) : TEXT",
            "- quantity : INTEGER",
            "- added_at : TIMESTAMPTZ"
        ]),
        (7.6, 3.4, 2.8, 1.6, "ORDER_ITEMS", True, [
            "+# order_id (PK, FK) : TEXT",
            "+# product_id (PK, FK) : TEXT",
            "- price_at_purchase : NUMERIC",
            "- quantity : INTEGER",
            "- title : TEXT"
        ]),
        (10.6, 3.4, 2.8, 1.6, "INTERACTIONS", False, [
            "+ id (PK) : TEXT",
            "# user_id (FK, null) : TEXT",
            "# product_id (FK) : TEXT",
            "- type : 'view'|'cart'|'buy'",
            "- ts : TIMESTAMPTZ"
        ]),
        (1.5, 0.8, 2.6, 1.4, "SEARCH_HISTORY", False, [
            "+ id (PK) : BIGSERIAL",
            "# user_id (FK) : TEXT",
            "- query : TEXT",
            "- total : INTEGER",
            "- ts : TIMESTAMPTZ"
        ]),
        (5.6, 0.8, 2.8, 1.5, "EVENTS", False, [
            "+ id (PK) : BIGSERIAL",
            "# user_id (FK, null) : TEXT",
            "# product_id (FK, null) : TEXT",
            "- type, session_id : TEXT",
            "- ts : TIMESTAMPTZ"
        ]),
        (9.8, 0.8, 2.8, 1.4, "SEARCH_LOGS", False, [
            "+ id (PK) : BIGSERIAL",
            "- query : TEXT",
            "- total : INTEGER",
            "# clicked_product_id (FK)",
            "- ts : TIMESTAMPTZ"
        ]),
    ]

    for x, y, w, h, title, is_weak, attrs in entities:
        border_c = c_weak_border if is_weak else c_entity_border
        lw = 2.0 if is_weak else 1.5

        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", fc=c_entity_bg, ec=border_c, lw=lw)
        ax.add_patch(rect)

        header_h = 0.38
        header_rect = patches.Rectangle((x, y + h - header_h), w, header_h, fc=border_c, ec="none")
        ax.add_patch(header_rect)

        badge = " [Junction Table]" if is_weak else ""
        ax.text(x + w/2, y + h - header_h/2, f"{title}{badge}", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=8.5)

        attr_y = y + h - header_h - 0.16
        for attr in attrs:
            bold = attr.startswith("+")
            ax.text(x + 0.12, attr_y, attr, ha="left", va="center", color="#1e293b", fontsize=7.2, fontweight="bold" if bold else "normal")
            attr_y -= 0.18

    # Relationships
    lines = [
        (3.4, 7.1, 5.6, 7.1, "1", "N"),
        (2.0, 6.2, 2.0, 4.8, "1", "N"),
        (2.8, 6.2, 4.8, 4.9, "1", "N"),
        (7.0, 6.2, 8.5, 5.0, "1", "N"),
        (10.6, 6.5, 9.8, 5.0, "1", "N"),
        (10.6, 6.8, 6.9, 4.4, "1", "N"),
        (10.6, 7.1, 3.4, 4.2, "1", "N"),
        (12.0, 6.2, 12.0, 5.0, "1", "N"),
        (2.0, 6.2, 2.5, 2.2, "1", "N"),
        (2.8, 6.2, 6.5, 2.3, "1", "N"),
        (12.0, 6.2, 11.2, 2.2, "1", "N"),
    ]

    for x1, y1, x2, y2, c1, c2 in lines:
        ax.plot([x1, x2], [y1, y2], color=c_line, lw=1.2, linestyle="--")
        ax.text(x1 + (x2-x1)*0.15, y1 + (y2-y1)*0.15 + 0.1, c1, fontsize=8, color="#dc2626", fontweight="bold")
        ax.text(x2 - (x2-x1)*0.15, y2 - (y2-y1)*0.15 + 0.1, c2, fontsize=8, color="#dc2626", fontweight="bold")

    ax.text(7.0, 8.25, "ShopSense — Entity Relationship Diagram (ERD)", ha="center", fontsize=14, fontweight="bold", color=c_primary)
    ax.text(7.0, 7.95, "10-Table Normalized Schema with Primary, Foreign, and Composite Junction Keys", ha="center", fontsize=9, color="#64748b")

    ax.set_xlim(0, 14)
    ax.set_ylim(0.4, 8.5)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(ERD_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] ERD image saved: {ERD_IMG}")


def generate_submission_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor("#0f172a")
    c_accent = colors.HexColor("#0284c7")
    c_border = colors.HexColor("#cbd5e1")

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=c_primary,
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        textColor=c_accent,
        spaceAfter=12,
    )
    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=6,
    )
    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=c_accent,
        spaceBefore=8,
        spaceAfter=3,
    )
    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.8,
        leading=13,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=4,
    )

    story = []

    # =========================================================================
    # PAGE 1: TITLE, PROJECT SUMMARY & DFD LEVEL 0
    # =========================================================================
    story.append(Paragraph("ShopSense — Final Project Architecture & Diagrams", title_style))
    story.append(Paragraph("Official Technical Report: DFD Level 0 & 1, Complete ERD, and Connection Guide", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceAfter=8))

    meta = [
        [
            Paragraph("<b>Candidate Name:</b> Shaurya (shauryadeep707@gmail.com)", body_style),
            Paragraph("<b>Target Database:</b> Supabase PostgreSQL (Cloud AWS)", body_style),
        ],
        [
            Paragraph("<b>Host URL:</b> nzccgolsbffelzdxtkom.supabase.co", body_style),
            Paragraph("<b>Project Scope:</b> Hybrid Search, Recommendations, Cloud DB", body_style),
        ],
    ]
    t_meta = Table(meta, colWidths=[270, 270])
    t_meta.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
                ("BOX", (0, 0), (-1, -1), 0.5, c_border),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#f1f5f9")),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(t_meta)
    story.append(Spacer(1, 10))

    story.append(Paragraph("1. Data Flow Diagram — Level 0 (Context Diagram)", h1_style))
    story.append(Paragraph(
        "The Level 0 Context Diagram establishes the global boundary of the system. It shows the bidirectional "
        "flow between the external <b>Customer/User</b>, the central <b>ShopSense Processing Platform</b>, and the "
        "persistent <b>Supabase PostgreSQL Cloud Database</b>.",
        body_style
    ))
    story.append(Spacer(1, 4))

    if DFD0_IMG.exists():
        story.append(Image(str(DFD0_IMG), width=520, height=250))

    story.append(Spacer(1, 6))

    # =========================================================================
    # PAGE 2: DFD LEVEL 1 (DETAILED SYSTEM FLOW)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("2. Data Flow Diagram — Level 1 (Detailed Subsystems)", h1_style))
    story.append(Paragraph(
        "The Level 1 DFD decomposes the platform into its <b>5 core processing subsystems</b> and maps their input/output "
        "data streams to the respective Supabase cloud tables (D1 through D5):",
        body_style
    ))
    story.append(Spacer(1, 4))

    if DFD1_IMG.exists():
        story.append(Image(str(DFD1_IMG), width=540, height=310))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Process & Data Store Mapping in DFD Level 1:", h2_style))

    dfd_table_data = [
        ["Process ID", "Subsystem", "Incoming Data", "Outgoing Data", "Connected Supabase Table"],
        ["1.0", "Auth & Profile", "User credentials, profile form", "JWT Bearer Token, sanitized session", "D1: public.users (41 Users)"],
        ["2.0", "Search Engine", "User query, category/brand filters", "BM25 + TF-IDF RRF Ranked List", "D2: public.products (591 Items)"],
        ["3.0", "Recommender", "Implicit clicks, views, purchases", "Personalized candidate rankings", "D3: public.interactions (1,561 Rows)"],
        ["4.0", "Cart & Wishlist", "Add/remove items, quantity changes", "Cart totals, line-item breakdowns", "D4: cart_items & wishlist_items"],
        ["5.0", "Order Processing", "Confirmed cart items & checkout", "Atomic order ID, purchased receipt", "D5: orders & order_items"],
    ]
    t_dfd = Table(dfd_table_data, colWidths=[60, 95, 130, 130, 125])
    t_dfd.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0284c7")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7.8),
                ("GRID", (0, 0), (-1, -1), 0.5, c_border),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
            ]
        )
    )
    story.append(t_dfd)

    # =========================================================================
    # PAGE 3: COMPLETE ENTITY RELATIONSHIP DIAGRAM (ERD)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("3. Complete Entity Relationship Diagram (ERD)", h1_style))
    story.append(Paragraph(
        "The ER Diagram illustrates the 10 database tables, their attributes, and their relational links. "
        "Notice the <b>green boxes</b> denoting associative junction tables with composite primary keys that eliminate redundancy.",
        body_style
    ))
    story.append(Spacer(1, 4))

    if ERD_IMG.exists():
        story.append(Image(str(ERD_IMG), width=540, height=310))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Relational Schema Summary:", h2_style))

    erd_summary_data = [
        ["Table Name", "Role in System", "Primary Key", "Foreign Keys (FK)", "Cardinality"],
        ["users", "Customer & Admin Profiles", "id (TEXT)", "—", "1 : N with Orders, Cart, Wishlist"],
        ["products", "E-Commerce Catalog", "id (TEXT)", "—", "1 : N with Cart, Wishlist, Order Items"],
        ["orders", "Customer Orders", "id (TEXT)", "user_id -> users(id)", "1 : N with Order Items"],
        ["order_items", "Order Line Items", "(order_id, product_id)", "order_id, product_id", "Associative Junction (Composite PK)"],
        ["cart_items", "Active Shopping Carts", "(user_id, product_id)", "user_id, product_id", "Associative Junction (Composite PK)"],
        ["wishlist_items", "Saved Customer Items", "(user_id, product_id)", "user_id, product_id", "Associative Junction (Composite PK)"],
        ["interactions", "Recommender Signals", "id (TEXT)", "user_id, product_id", "ML Feedback Loop (1,561 records)"],
        ["events", "User Activity Telemetry", "id (BIGSERIAL)", "user_id, product_id", "Clickstream Tracking"],
        ["search_history", "Personalized Queries", "id (BIGSERIAL)", "user_id -> users(id)", "Recent searches per user"],
        ["search_logs", "Aggregated Query Log", "id (BIGSERIAL)", "clicked_product_id -> products", "Search effectiveness analytics"],
    ]
    t_erd = Table(erd_summary_data, colWidths=[80, 115, 110, 125, 110])
    t_erd.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e293b")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                ("GRID", (0, 0), (-1, -1), 0.5, c_border),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(t_erd)

    # =========================================================================
    # PAGE 4: HOW EVERYTHING CONNECTS (DEEP DIVE)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("4. Technical Deep Dive: How the Entire System Connects", h1_style))

    story.append(Paragraph("4.1 How Tables Connect Inside PostgreSQL (Relational Integrity)", h2_style))
    story.append(Paragraph(
        "• <b>Composite Primary Keys:</b> In junction tables (<code>cart_items</code>, <code>wishlist_items</code>, <code>order_items</code>), "
        "the primary key consists of two columns: <code>PRIMARY KEY (user_id, product_id)</code>. This database constraint prevents duplicate rows "
        "for the same item per user and simplifies updating item quantities.<br/>"
        "• <b>Foreign Key Constraints with Cascades:</b> <code>user_id REFERENCES public.users(id) ON DELETE CASCADE</code> ensures that if an account "
        "is deleted, associated orphan records in carts and orders are automatically cleaned up.<br/>"
        "• <b>Machine Learning Feedback Connection:</b> The <code>interactions</code> table connects users and products through explicit signals "
        "('view', 'cart', 'purchase'). The recommendation algorithms (Item-Item CF & Matrix Factorization) query this table to calculate user affinity scores.",
        body_style
    ))

    story.append(Paragraph("4.2 How the Backend Connects to the Database (Dual Runtime)", h2_style))
    story.append(Paragraph(
        "• <b>Node.js Backend (<code>backend/db/supabaseClient.js</code>):</b> Connects over HTTPS on port 443 using <code>@supabase/supabase-js</code>. "
        "Loads credentials dynamically from <code>.env</code> (<code>SUPABASE_URL</code> and <code>SUPABASE_SERVICE_ROLE_KEY</code>). Used by API routes.<br/>"
        "• <b>Python Database Module (<code>database/client.py</code>):</b> Connects via <code>supabase-py</code> for data science, models, and repositories. "
        "Also features <code>apply_schema.py</code> which uses <code>psycopg2</code> on <b>TCP port 5432</b> to execute DDL migrations over SSL.",
        body_style
    ))

    story.append(Paragraph("4.3 How the Frontend Connects to the Backend", h2_style))
    story.append(Paragraph(
        "• The client web application (<code>public/app.js</code>) communicates with the backend via asynchronous <code>fetch()</code> calls to REST endpoints.<br/>"
        "• <b>Stateless JWT Bearer Token:</b> When users login, the server issues an HMAC-SHA256 JWT token stored in <code>localStorage</code>. "
        "Every authenticated request passes <code>Authorization: Bearer &lt;token&gt;</code>.<br/>"
        "• <b>Real-Time Synchronization:</b> Actions performed on the frontend are saved immediately to local in-memory structures for sub-millisecond "
        "responsiveness, while simultaneously syncing to Supabase Cloud PostgreSQL in the background.",
        body_style
    ))

    story.append(Spacer(1, 8))
    story.append(Paragraph("5. Final Presentation & Viva Highlights (Talking Points)", h1_style))
    story.append(Paragraph(
        "• <b>100% Cloud Persistence:</b> Migrated project from a single-node SQLite file into an enterprise-grade cloud database on Supabase.<br/>"
        "• <b>Dual Runtime Support:</b> Built complete Python database layer (models, repository, seeders) alongside Node.js server.<br/>"
        "• <b>Hybrid Search Engine:</b> Combines BM25 keyword matching with TF-IDF Vector Space semantic search using Reciprocal Rank Fusion (RRF).<br/>"
        "• <b>Hybrid Recommender:</b> Blends item-item collaborative filtering, matrix factorization (SGD), and popularity decay to solve the cold-start problem.<br/>"
        "• <b>Rigorous Verification:</b> Live connection verified on AWS, 591 products seeded, and <b>65/65 unit tests passing (100%)</b>.",
        body_style
    ))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=8))
    story.append(Paragraph(
        "<i>ShopSense E-Commerce Project 2026. Final Examination & Project Presentation Document.</i>",
        ParagraphStyle("Footer", parent=styles["Italic"], fontSize=8, textColor=colors.HexColor("#94a3b8"), alignment=1)
    ))

    doc.build(story)
    print(f"[+] Final Submission PDF successfully generated: {OUTPUT_PDF}")


if __name__ == "__main__":
    create_dfd_level0()
    create_dfd_level1()
    create_erd_diagram()
    generate_submission_pdf()
