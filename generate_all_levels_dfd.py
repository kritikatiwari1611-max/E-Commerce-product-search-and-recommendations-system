"""
ShopSense All-Level Data Flow Diagrams (DFD) & Master Technical Submission
Author: Shaurya (shauryadeep707@gmail.com)
Scope:
- DFD Level 0 (Context Diagram)
- DFD Level 1 (Complete System Functional Decomposition)
- DFD Level 2A (Sub-Process Decomposition: Hybrid Search & AI Recommender Engine)
- DFD Level 2B (Sub-Process Decomposition: Cart Junction, Checkout & Financial Pipeline)
- Complete 10-Table ERD (Corrected with Composite Keys)
- Master Multi-Page PDF compilation with crystal clear formatting
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

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

DESKTOP = Path(r"c:\Users\shaur\OneDrive\Desktop\shop sence")
DFD0_IMG = DESKTOP / "dfd_level0.png"
DFD1_IMG = DESKTOP / "dfd_level1.png"
DFD2A_IMG = DESKTOP / "dfd_level2_search.png"
DFD2B_IMG = DESKTOP / "dfd_level2_checkout.png"
ERD_IMG = DESKTOP / "erd_diagram.png"
MASTER_PDF = DESKTOP / "ShopSense_Final_Project_Submission_Shaurya.pdf"


def draw_pill(ax, x, y, text, color="#0f172a", bg="#ffffff", border="#cbd5e1", fontsize=7.2, fontweight="bold"):
    """Pill badge for flow labels to prevent text collision."""
    bbox = dict(boxstyle="round,pad=0.22,rounding_size=0.18", fc=bg, ec=border, lw=0.85, alpha=0.96)
    ax.text(x, y, text, ha="center", va="center", color=color, fontsize=fontsize, fontweight=fontweight, bbox=bbox, zorder=12)


# =====================================================================
# 1. DFD LEVEL 0 (CONTEXT DIAGRAM)
# =====================================================================
def create_dfd_level0():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    ax.text(6.5, 7.05, "ShopSense Platform — DFD Level 0 (Context Diagram)", ha="center", va="center", fontsize=15, fontweight="bold", color="#0f172a")
    ax.text(6.5, 6.7, "High-Level Environmental Boundary & System Information Exchange", ha="center", va="center", fontsize=9.2, color="#64748b")

    # Central Process
    glow = patches.Circle((6.5, 3.8), 1.7, fc="#e0f2fe", ec="#bae6fd", lw=2, zorder=2)
    ax.add_patch(glow)
    core = patches.Circle((6.5, 3.8), 1.5, fc="#0284c7", ec="#0369a1", lw=2.5, zorder=3)
    ax.add_patch(core)
    ax.text(6.5, 4.4, "0.0", ha="center", va="center", color="#bae6fd", fontsize=11, fontweight="bold", zorder=4)
    ax.text(6.5, 3.9, "SHOPSENSE\nSYSTEM", ha="center", va="center", color="#ffffff", fontsize=12, fontweight="heavy", zorder=4)
    ax.text(6.5, 3.3, "Search, Recommender &\nE-Commerce Core Engine\n(Node.js / Python / AI)", ha="center", va="center", color="#e0f2fe", fontsize=7.5, zorder=4)

    # Entities
    # Customer
    c_box = patches.FancyBboxPatch((0.6, 2.8), 2.4, 2.0, boxstyle="round,pad=0.15", fc="#1e293b", ec="#0f172a", lw=1.5, zorder=3)
    ax.add_patch(c_box)
    ax.text(1.8, 4.4, "EXTERNAL ENTITY", ha="center", va="center", color="#38bdf8", fontsize=7, fontweight="bold", zorder=4)
    ax.text(1.8, 3.8, "Customer /\nShopper", ha="center", va="center", color="#ffffff", fontsize=11, fontweight="bold", zorder=4)
    ax.text(1.8, 3.2, "Web Client & Browser\n(Search, Cart, Buy)", ha="center", va="center", color="#cbd5e1", fontsize=7.5, zorder=4)

    # Store Admin
    a_box = patches.FancyBboxPatch((5.3, 0.4), 2.4, 1.5, boxstyle="round,pad=0.15", fc="#334155", ec="#1e293b", lw=1.5, zorder=3)
    ax.add_patch(a_box)
    ax.text(6.5, 1.6, "EXTERNAL ENTITY", ha="center", va="center", color="#cbd5e1", fontsize=6.5, fontweight="bold", zorder=4)
    ax.text(6.5, 1.2, "Store Administrator", ha="center", va="center", color="#ffffff", fontsize=9.5, fontweight="bold", zorder=4)
    ax.text(6.5, 0.75, "Catalog, Stock & Analytics", ha="center", va="center", color="#94a3b8", fontsize=7, zorder=4)

    # Supabase Cloud
    db_box = patches.FancyBboxPatch((10.0, 4.0), 2.4, 1.9, boxstyle="round,pad=0.15", fc="#065f46", ec="#047857", lw=1.5, zorder=3)
    ax.add_patch(db_box)
    ax.text(11.2, 5.5, "DATA REPOSITORY", ha="center", va="center", color="#a7f3d0", fontsize=6.5, fontweight="bold", zorder=4)
    ax.text(11.2, 4.95, "Supabase Cloud\n(PostgreSQL)", ha="center", va="center", color="#ffffff", fontsize=10.5, fontweight="bold", zorder=4)
    ax.text(11.2, 4.35, "10 Relational Tables\nAWS Hosted (Direct SSL)", ha="center", va="center", color="#d1fae5", fontsize=7.5, zorder=4)

    # Payment Gateway
    pay_box = patches.FancyBboxPatch((10.0, 1.6), 2.4, 1.7, boxstyle="round,pad=0.15", fc="#581c87", ec="#6b21a8", lw=1.5, zorder=3)
    ax.add_patch(pay_box)
    ax.text(11.2, 2.95, "EXTERNAL SERVICE", ha="center", va="center", color="#e9d5ff", fontsize=6.5, fontweight="bold", zorder=4)
    ax.text(11.2, 2.45, "Payment Gateway", ha="center", va="center", color="#ffffff", fontsize=10, fontweight="bold", zorder=4)
    ax.text(11.2, 1.95, "Stripe / Razorpay\nTokenized Payment API", ha="center", va="center", color="#f3e8ff", fontsize=7.5, zorder=4)

    # Flows
    ax.annotate("", xy=(5.0, 4.4), xytext=(3.0, 4.4), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=2, mutation_scale=14), zorder=5)
    draw_pill(ax, 4.0, 4.75, "Search Queries, Cart Actions,\nOrders, Clickstream", color="#0369a1")

    ax.annotate("", xy=(3.0, 3.3), xytext=(5.0, 3.3), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=2, mutation_scale=14), zorder=5)
    draw_pill(ax, 4.0, 2.95, "Personalized Feed, Search Results,\nOrder Invoices & Auth Token", color="#065f46")

    ax.annotate("", xy=(6.0, 2.3), xytext=(6.0, 1.9), arrowprops=dict(arrowstyle="-|>", color="#475569", lw=1.8, mutation_scale=12), zorder=5)
    draw_pill(ax, 5.0, 2.1, "Stock & Product Updates", color="#334155", fontsize=7)

    ax.annotate("", xy=(7.0, 1.9), xytext=(7.0, 2.3), arrowprops=dict(arrowstyle="-|>", color="#475569", lw=1.8, mutation_scale=12), zorder=5)
    draw_pill(ax, 8.0, 2.1, "Search Logs & Conversion Stats", color="#334155", fontsize=7)

    ax.annotate("", xy=(10.0, 5.1), xytext=(8.0, 4.4), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.8, mutation_scale=12), zorder=5)
    draw_pill(ax, 9.0, 4.95, "SQL INSERT / UPDATE / UPSERT", color="#065f46", fontsize=7)

    ax.annotate("", xy=(8.0, 4.0), xytext=(10.0, 4.4), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.8, mutation_scale=12), zorder=5)
    draw_pill(ax, 9.0, 3.9, "Query Records, Embeddings & State", color="#065f46", fontsize=7)

    ax.annotate("", xy=(10.0, 2.6), xytext=(7.8, 3.1), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.8, mutation_scale=12), zorder=5)
    draw_pill(ax, 9.0, 2.95, "Order Amount & Customer Token", color="#6b21a8", fontsize=7)

    ax.annotate("", xy=(7.8, 2.7), xytext=(10.0, 2.1), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.8, mutation_scale=12), zorder=5)
    draw_pill(ax, 8.85, 2.35, "Payment Verification Webhook", color="#6b21a8", fontsize=7)

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.5)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(DFD0_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] DFD Level 0 saved: {DFD0_IMG}")


# =====================================================================
# 2. DFD LEVEL 1 (FUNCTIONAL DECOMPOSITION)
# =====================================================================
def create_dfd_level1():
    fig, ax = plt.subplots(figsize=(17, 11), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    ax.text(8.5, 10.5, "ShopSense Architecture — DFD Level 1 (Detailed Subsystems Data Flow)", ha="center", va="center", fontsize=16, fontweight="bold", color="#0f172a")
    ax.text(8.5, 10.15, "Complete Functional Decomposition: 6 Processes, 6 Cloud Data Stores, 2 External Entities, and Directed Data Vectors", ha="center", va="center", fontsize=9.5, color="#64748b")

    # Legend
    p_leg = patches.FancyBboxPatch((0.8, 9.7), 2.2, 0.45, boxstyle="round,pad=0.08", fc="#0284c7", ec="#0369a1", lw=1)
    ax.add_patch(p_leg)
    ax.text(1.9, 9.92, "Process (Core Subsystem)", ha="center", va="center", color="#ffffff", fontsize=7.5, fontweight="bold")

    s_leg = patches.FancyBboxPatch((3.4, 9.7), 2.2, 0.45, boxstyle="round,pad=0.08", fc="#ecfdf5", ec="#059669", lw=1.5)
    ax.add_patch(s_leg)
    ax.text(4.5, 9.92, "Data Store (Supabase Table)", ha="center", va="center", color="#065f46", fontsize=7.5, fontweight="bold")

    e_leg = patches.FancyBboxPatch((6.0, 9.7), 2.2, 0.45, boxstyle="round,pad=0.08", fc="#1e293b", ec="#0f172a", lw=1)
    ax.add_patch(e_leg)
    ax.text(7.1, 9.92, "External Entity (Actor)", ha="center", va="center", color="#ffffff", fontsize=7.5, fontweight="bold")

    # Entities
    cust_box = patches.FancyBboxPatch((0.6, 5.0), 2.0, 3.2, boxstyle="round,pad=0.15", fc="#0f172a", ec="#334155", lw=2, zorder=3)
    ax.add_patch(cust_box)
    ax.text(1.6, 7.8, "EXTERNAL ENTITY", ha="center", va="center", color="#38bdf8", fontsize=7, fontweight="bold", zorder=4)
    ax.text(1.6, 7.2, "CUSTOMER\n(Shopper)", ha="center", va="center", color="#ffffff", fontsize=11, fontweight="heavy", zorder=4)
    ax.text(1.6, 6.2, "• Query Searches\n• Cart Operations\n• Place Orders\n• Browse & Click", ha="center", va="center", color="#cbd5e1", fontsize=8, zorder=4)

    adm_box = patches.FancyBboxPatch((0.6, 1.2), 2.0, 2.2, boxstyle="round,pad=0.15", fc="#334155", ec="#475569", lw=1.5, zorder=3)
    ax.add_patch(adm_box)
    ax.text(1.6, 3.0, "EXTERNAL ENTITY", ha="center", va="center", color="#94a3b8", fontsize=7, fontweight="bold", zorder=4)
    ax.text(1.6, 2.5, "STORE ADMIN", ha="center", va="center", color="#ffffff", fontsize=10.5, fontweight="bold", zorder=4)
    ax.text(1.6, 1.8, "• Manage Catalog\n• Inspect Telemetry\n• Query Latency Logs", ha="center", va="center", color="#cbd5e1", fontsize=7.5, zorder=4)

    # 6 Core Processes
    processes = [
        ("1.0", "User Authentication &\nProfile Management", "JWT Issuance, Passwords,\nRole Permissions", 4.8, 8.2, "#0284c7"),
        ("2.0", "Hybrid Search Engine\n(BM25 + TF-IDF + RRF)", "Tokenization, Lexical Match,\nReciprocal Rank Fusion", 4.8, 6.6, "#0369a1"),
        ("3.0", "Personalized Recommendation\n& Collaborative Filtering", "User-Item Matrix, Similarities,\nReal-time Candidate Ranking", 4.8, 5.0, "#0284c7"),
        ("4.0", "Cart & Wishlist Manager\n(Junction State Handler)", "Composite Key Upsert,\nQuantity Management", 4.8, 3.4, "#0369a1"),
        ("5.0", "Order Processing, Payment\n& Invoicing Engine", "Stock Reservation, Total Calc,\nFinancial Records", 4.8, 1.8, "#0284c7"),
        ("6.0", "Telemetry, Interaction &\nSearch Analytics Tracker", "Dwell Time, Click Logs,\nAsync Event Pipeline", 4.8, 0.2, "#0369a1"),
    ]

    for pid, title, desc, px, py, pcol in processes:
        box = patches.FancyBboxPatch((px, py), 3.5, 1.2, boxstyle="round,pad=0.12", fc=pcol, ec="#0f172a", lw=1.5, zorder=4)
        ax.add_patch(box)
        ax.text(px + 0.45, py + 0.95, pid, ha="center", va="center", color="#bae6fd", fontsize=9, fontweight="heavy", zorder=5)
        ax.text(px + 1.9, py + 0.85, title, ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=5)
        ax.text(px + 1.9, py + 0.32, desc, ha="center", va="center", color="#e0f2fe", fontsize=7, zorder=5)

    # 6 Data Stores
    stores = [
        ("D1", "public.users", "id, email, password_hash, role,\nmetadata, created_at", 11.4, 8.2),
        ("D2", "public.products", "id, title, category, price,\nstock, description, image_url", 11.4, 6.6),
        ("D3", "public.interactions & events", "id, user_id, product_id, weight,\nevent_name, payload", 11.4, 5.0),
        ("D4", "public.cart_items & wishlist_items", "Composite PK (user_id, product_id),\nquantity, added_at", 11.4, 3.4),
        ("D5", "public.orders & order_items", "order_id, user_id, total, status,\norder_items line table", 11.4, 1.8),
        ("D6", "public.search_history & search_logs", "query, execution_ms, results_count,\nuser_id, timestamp", 11.4, 0.2),
    ]

    for sid, name, fields, sx, sy in stores:
        ax.plot([sx, sx + 4.8, sx + 4.8, sx], [sy + 1.2, sy + 1.2, sy, sy], color="#059669", lw=2, zorder=3)
        ax.fill([sx, sx + 4.8, sx + 4.8, sx], [sy + 1.2, sy + 1.2, sy, sy], color="#ecfdf5", zorder=2)
        ax.plot([sx + 0.9, sx + 0.9], [sy, sy + 1.2], color="#059669", lw=1.5, linestyle="--", zorder=3)
        ax.text(sx + 0.45, sy + 0.6, sid, ha="center", va="center", color="#065f46", fontsize=10, fontweight="bold", zorder=4)
        ax.text(sx + 2.8, sy + 0.85, name, ha="center", va="center", color="#065f46", fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(sx + 2.8, sy + 0.35, fields, ha="center", va="center", color="#047857", fontsize=6.8, zorder=4)

    # Annotated flows
    ax.annotate("", xy=(4.8, 8.8), xytext=(2.6, 7.8), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.6, 8.4, "Email & Password", color="#0369a1", fontsize=7)

    ax.annotate("", xy=(2.6, 7.5), xytext=(4.8, 8.4), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.7, 7.85, "JWT & User Profile", color="#065f46", fontsize=7)

    ax.annotate("", xy=(11.4, 8.8), xytext=(8.3, 8.8), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 9.05, "Verify / Insert User", color="#065f46", fontsize=7)
    ax.annotate("", xy=(8.3, 8.4), xytext=(11.4, 8.4), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 8.2, "User Record & Salt", color="#065f46", fontsize=7)

    ax.annotate("", xy=(4.8, 7.3), xytext=(2.6, 6.9), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 7.25, "Query String & Price Filters", color="#0369a1", fontsize=7)

    ax.annotate("", xy=(2.6, 6.6), xytext=(4.8, 6.9), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 6.65, "Ranked Products List", color="#065f46", fontsize=7)

    ax.annotate("", xy=(11.4, 7.2), xytext=(8.3, 7.2), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 7.45, "Catalog Full-Text Query", color="#065f46", fontsize=7)
    ax.annotate("", xy=(8.3, 6.8), xytext=(11.4, 6.8), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 6.6, "Matching Products (591 items)", color="#065f46", fontsize=7)

    ax.annotate("", xy=(11.4, 1.0), xytext=(8.3, 6.7), arrowprops=dict(arrowstyle="-|>", color="#b45309", lw=1.4, mutation_scale=10, connectionstyle="arc3,rad=-0.15"), zorder=6)
    draw_pill(ax, 10.1, 5.9, "Log Search Query & Latency (ms)", color="#92400e", bg="#fffbeb", border="#fde68a", fontsize=6.8)

    ax.annotate("", xy=(4.8, 5.7), xytext=(2.6, 6.2), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 5.85, "Request Recommendations", color="#0369a1", fontsize=7)
    ax.annotate("", xy=(2.6, 5.8), xytext=(4.8, 5.3), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 5.4, "Top-K Recommendations", color="#065f46", fontsize=7)

    ax.annotate("", xy=(8.3, 5.6), xytext=(11.4, 5.6), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 5.8, "Fetch Historical Interactions", color="#065f46", fontsize=7)
    ax.annotate("", xy=(11.4, 5.2), xytext=(8.3, 5.2), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 5.0, "1,561 User-Item Weights", color="#065f46", fontsize=7)

    ax.annotate("", xy=(4.8, 4.0), xytext=(2.6, 5.3), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 4.5, "Add/Remove Item ID, Qty", color="#0369a1", fontsize=7)
    ax.annotate("", xy=(2.6, 5.0), xytext=(4.8, 3.6), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 4.05, "Live Cart / Wishlist State", color="#065f46", fontsize=7)

    ax.annotate("", xy=(11.4, 4.0), xytext=(8.3, 4.0), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 4.25, "Upsert (user_id, product_id)", color="#065f46", fontsize=7)
    ax.annotate("", xy=(8.3, 3.6), xytext=(11.4, 3.6), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 3.4, "Current Line Items & Qty", color="#065f46", fontsize=7)

    ax.annotate("", xy=(4.8, 2.5), xytext=(2.6, 4.8), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 3.25, "Submit Checkout & Payment", color="#0369a1", fontsize=7)
    ax.annotate("", xy=(2.6, 4.5), xytext=(4.8, 2.1), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.65, 2.8, "Order Receipt & Confirmation", color="#065f46", fontsize=7)

    ax.annotate("", xy=(11.4, 2.4), xytext=(8.3, 2.4), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 2.65, "Insert orders & order_items", color="#065f46", fontsize=7)
    ax.annotate("", xy=(8.3, 2.0), xytext=(11.4, 2.0), arrowprops=dict(arrowstyle="-|>", color="#047857", lw=1.6, mutation_scale=11), zorder=6)
    draw_pill(ax, 9.85, 1.8, "Order Number & Status", color="#065f46", fontsize=7)

    ax.annotate("", xy=(11.4, 3.4), xytext=(8.3, 2.6), arrowprops=dict(arrowstyle="-|>", color="#dc2626", lw=1.4, mutation_scale=10, linestyle="--"), zorder=6)
    draw_pill(ax, 9.6, 3.0, "DELETE FROM cart_items", color="#991b1b", bg="#fef2f2", border="#fecaca", fontsize=6.8)

    ax.annotate("", xy=(4.8, 0.8), xytext=(2.4, 4.8), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.5, mutation_scale=11), zorder=6)
    draw_pill(ax, 3.5, 1.7, "Telemetry: Click, Dwell, View", color="#6b21a8", bg="#faf5ff", border="#e9d5ff", fontsize=7)

    ax.annotate("", xy=(11.4, 5.0), xytext=(8.3, 0.9), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.4, mutation_scale=10, connectionstyle="arc3,rad=-0.1"), zorder=6)
    draw_pill(ax, 10.3, 4.3, "Async Telemetry Stream (weight 1..5)", color="#6b21a8", bg="#faf5ff", border="#e9d5ff", fontsize=6.8)

    ax.annotate("", xy=(4.8, 6.7), xytext=(2.6, 2.8), arrowprops=dict(arrowstyle="-|>", color="#475569", lw=1.4, mutation_scale=10, linestyle=":"), zorder=6)
    draw_pill(ax, 3.65, 2.3, "Catalog Sync & Price Edit", color="#334155", fontsize=7)

    ax.annotate("", xy=(2.6, 1.6), xytext=(11.4, 0.4), arrowprops=dict(arrowstyle="-|>", color="#334155", lw=1.4, mutation_scale=10, connectionstyle="arc3,rad=0.08"), zorder=6)
    draw_pill(ax, 7.0, 0.55, "Query Latency Logs & Conversion Reports", color="#1e293b", bg="#f1f5f9", border="#cbd5e1", fontsize=7)

    ax.set_xlim(0, 17)
    ax.set_ylim(-0.3, 11)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(DFD1_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] DFD Level 1 saved: {DFD1_IMG}")


# =====================================================================
# 3. DFD LEVEL 2A: SEARCH & RECOMMENDER DECOMPOSITION
# =====================================================================
def create_dfd_level2_search():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    ax.text(8.0, 9.6, "ShopSense Architecture — DFD Level 2A (Search & Recommender Pipeline)", ha="center", va="center", fontsize=15, fontweight="bold", color="#0f172a")
    ax.text(8.0, 9.25, "Sub-Process Decomposition of Processes 2.0 (Hybrid Search) and 3.0 (Recommendation Engine)", ha="center", va="center", fontsize=9.2, color="#64748b")

    # External User
    u_box = patches.FancyBboxPatch((0.5, 4.0), 2.0, 2.2, boxstyle="round,pad=0.12", fc="#0f172a", ec="#334155", lw=1.5, zorder=3)
    ax.add_patch(u_box)
    ax.text(1.5, 5.5, "USER / CLIENT", ha="center", va="center", color="#38bdf8", fontsize=8, fontweight="bold", zorder=4)
    ax.text(1.5, 4.9, "Shopper Browser", ha="center", va="center", color="#ffffff", fontsize=10.5, fontweight="bold", zorder=4)
    ax.text(1.5, 4.4, "Query & Filter Input\nPersonal Feed Request", ha="center", va="center", color="#cbd5e1", fontsize=7.2, zorder=4)

    # Subprocesses for 2.0 (Search)
    p21 = patches.FancyBboxPatch((3.8, 7.2), 2.8, 1.2, boxstyle="round,pad=0.1", fc="#0284c7", ec="#0369a1", lw=1.5, zorder=3)
    ax.add_patch(p21)
    ax.text(5.2, 8.0, "2.1 Query Preprocessor", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(5.2, 7.5, "Tokenization, Lowercasing,\nStop-words & Spell Match", ha="center", va="center", color="#e0f2fe", fontsize=7, zorder=4)

    p22 = patches.FancyBboxPatch((7.6, 7.8), 2.8, 1.1, boxstyle="round,pad=0.1", fc="#0369a1", ec="#075985", lw=1.5, zorder=3)
    ax.add_patch(p22)
    ax.text(9.0, 8.5, "2.2 Lexical BM25 Engine", ha="center", va="center", color="#ffffff", fontsize=8.2, fontweight="bold", zorder=4)
    ax.text(9.0, 8.1, "Exact Keyword Frequency &\nInverted Index Match", ha="center", va="center", color="#e0f2fe", fontsize=6.8, zorder=4)

    p23 = patches.FancyBboxPatch((7.6, 6.4), 2.8, 1.1, boxstyle="round,pad=0.1", fc="#0369a1", ec="#075985", lw=1.5, zorder=3)
    ax.add_patch(p23)
    ax.text(9.0, 7.1, "2.3 Semantic Vector Match", ha="center", va="center", color="#ffffff", fontsize=8.2, fontweight="bold", zorder=4)
    ax.text(9.0, 6.7, "TF-IDF / Dense Embeddings\nCosine Similarity Scoring", ha="center", va="center", color="#e0f2fe", fontsize=6.8, zorder=4)

    p24 = patches.FancyBboxPatch((11.4, 7.1), 3.0, 1.3, boxstyle="round,pad=0.1", fc="#0f766e", ec="#115e59", lw=1.5, zorder=3)
    ax.add_patch(p24)
    ax.text(12.9, 7.9, "2.4 Reciprocal Rank Fusion", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(12.9, 7.4, "RRF Score = sum(1/(60+rank))\nPrice & Category Filtering", ha="center", va="center", color="#ccfbf1", fontsize=7, zorder=4)

    # Subprocesses for 3.0 (Recommendation)
    p31 = patches.FancyBboxPatch((3.8, 2.0), 3.0, 1.2, boxstyle="round,pad=0.1", fc="#7c3aed", ec="#6d28d9", lw=1.5, zorder=3)
    ax.add_patch(p31)
    ax.text(5.3, 2.8, "3.1 Implicit Telemetry Scorer", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(5.3, 2.3, "Views=1, Carts=3, Buys=5\nTime-decayed User Matrix", ha="center", va="center", color="#f3e8ff", fontsize=7, zorder=4)

    p32 = patches.FancyBboxPatch((7.8, 2.0), 3.0, 1.2, boxstyle="round,pad=0.1", fc="#6d28d9", ec="#5b21b6", lw=1.5, zorder=3)
    ax.add_patch(p32)
    ax.text(9.3, 2.8, "3.2 Collaborative Filtering", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(9.3, 2.3, "Item-Item Similarity Matrix\nNearest Neighbor Candidates", ha="center", va="center", color="#f3e8ff", fontsize=7, zorder=4)

    p33 = patches.FancyBboxPatch((11.8, 2.0), 3.0, 1.2, boxstyle="round,pad=0.1", fc="#4c1d95", ec="#3b0764", lw=1.5, zorder=3)
    ax.add_patch(p33)
    ax.text(13.3, 2.8, "3.3 Feed Personalizer", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(13.3, 2.3, "Deduplication vs Past Purchases\nCold-start Fallback Hybrid", ha="center", va="center", color="#f3e8ff", fontsize=7, zorder=4)

    # Data Stores
    # D2 Products
    ax.plot([7.6, 11.0, 11.0, 7.6], [5.7, 5.7, 4.7, 4.7], color="#059669", lw=2, zorder=3)
    ax.fill([7.6, 11.0, 11.0, 7.6], [5.7, 5.7, 4.7, 4.7], color="#ecfdf5", zorder=2)
    ax.text(8.0, 5.2, "D2", ha="center", va="center", color="#065f46", fontsize=9, fontweight="bold", zorder=4)
    ax.text(9.5, 5.3, "public.products (591 items)", ha="center", va="center", color="#065f46", fontsize=8, fontweight="bold", zorder=4)
    ax.text(9.5, 4.95, "title, category, price, stock, metadata", ha="center", va="center", color="#047857", fontsize=6.8, zorder=4)

    # D3 Interactions
    ax.plot([7.6, 11.0, 11.0, 7.6], [1.4, 1.4, 0.4, 0.4], color="#059669", lw=2, zorder=3)
    ax.fill([7.6, 11.0, 11.0, 7.6], [1.4, 1.4, 0.4, 0.4], color="#ecfdf5", zorder=2)
    ax.text(8.0, 0.9, "D3", ha="center", va="center", color="#065f46", fontsize=9, fontweight="bold", zorder=4)
    ax.text(9.5, 1.05, "public.interactions (1,561 rows)", ha="center", va="center", color="#065f46", fontsize=8, fontweight="bold", zorder=4)
    ax.text(9.5, 0.7, "user_id, product_id, weight (1..5)", ha="center", va="center", color="#047857", fontsize=6.8, zorder=4)

    # D6 Search History / Logs
    ax.plot([11.8, 15.2, 15.2, 11.8], [5.7, 5.7, 4.7, 4.7], color="#b45309", lw=2, zorder=3)
    ax.fill([11.8, 15.2, 15.2, 11.8], [5.7, 5.7, 4.7, 4.7], color="#fffbeb", zorder=2)
    ax.text(12.2, 5.2, "D6", ha="center", va="center", color="#92400e", fontsize=9, fontweight="bold", zorder=4)
    ax.text(13.6, 5.3, "public.search_logs & history", ha="center", va="center", color="#92400e", fontsize=8, fontweight="bold", zorder=4)
    ax.text(13.6, 4.95, "query, execution_ms, results_count", ha="center", va="center", color="#b45309", fontsize=6.8, zorder=4)

    # Flows in Search Pipeline
    ax.annotate("", xy=(3.8, 7.8), xytext=(2.5, 5.8), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.6, mutation_scale=11), zorder=5)
    draw_pill(ax, 3.0, 6.9, "Raw Search Query", color="#0369a1", fontsize=7)

    ax.annotate("", xy=(7.6, 8.3), xytext=(6.6, 8.0), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 7.1, 8.35, "Cleaned Tokens", color="#0369a1", fontsize=6.8)

    ax.annotate("", xy=(7.6, 7.0), xytext=(6.6, 7.5), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 7.1, 7.1, "Dense Embeddings", color="#0369a1", fontsize=6.8)

    # Database connections
    ax.annotate("", xy=(9.0, 7.8), xytext=(9.0, 5.7), arrowprops=dict(arrowstyle="<|-|>", color="#059669", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 9.0, 6.1, "Inverted Index & Vectors", color="#065f46", fontsize=6.8)

    # BM25 & Semantic to RRF
    ax.annotate("", xy=(11.4, 7.9), xytext=(10.4, 8.3), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 10.9, 8.3, "BM25 Ranked List", color="#0369a1", fontsize=6.8)

    ax.annotate("", xy=(11.4, 7.4), xytext=(10.4, 7.0), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 10.9, 7.05, "Semantic Ranked List", color="#0369a1", fontsize=6.8)

    # RRF to D6 Log
    ax.annotate("", xy=(13.0, 5.7), xytext=(13.0, 7.1), arrowprops=dict(arrowstyle="-|>", color="#b45309", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 13.0, 6.4, "Log Execution Latency", color="#92400e", fontsize=6.8)

    # RRF back to User
    ax.annotate("", xy=(2.5, 5.3), xytext=(12.0, 7.1), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.8, mutation_scale=12, connectionstyle="arc3,rad=0.18"), zorder=5)
    draw_pill(ax, 6.5, 6.2, "Fused, Deduplicated & Ranked Catalog Results", color="#065f46", fontsize=7.5)

    # Flows in Recommender Pipeline
    ax.annotate("", xy=(3.8, 2.6), xytext=(2.5, 4.4), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.5, mutation_scale=11), zorder=5)
    draw_pill(ax, 3.0, 3.4, "Real-time Click / View Event", color="#6d28d9", fontsize=7)

    # 3.1 <-> D3
    ax.annotate("", xy=(7.6, 0.9), xytext=(6.8, 2.2), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 7.1, 1.5, "Save Event Weight", color="#6d28d9", fontsize=6.8)

    # D3 -> 3.2
    ax.annotate("", xy=(9.3, 2.0), xytext=(9.3, 1.4), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 9.3, 1.7, "Load Interaction Matrix", color="#065f46", fontsize=6.8)

    # 3.2 -> 3.3
    ax.annotate("", xy=(11.8, 2.6), xytext=(10.8, 2.6), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 11.3, 2.9, "Candidate Items", color="#6d28d9", fontsize=6.8)

    # 3.3 back to User
    ax.annotate("", xy=(2.5, 4.6), xytext=(12.5, 2.0), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.8, mutation_scale=12, connectionstyle="arc3,rad=-0.16"), zorder=5)
    draw_pill(ax, 6.8, 3.8, "Personalized Recommendations Carousel (Top-10)", color="#065f46", fontsize=7.5)

    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(DFD2A_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] DFD Level 2A saved: {DFD2A_IMG}")


# =====================================================================
# 4. DFD LEVEL 2B: CART & CHECKOUT DECOMPOSITION
# =====================================================================
def create_dfd_level2_checkout():
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8fafc")

    ax.text(8.0, 9.1, "ShopSense Architecture — DFD Level 2B (Cart, Checkout & Order Pipeline)", ha="center", va="center", fontsize=15, fontweight="bold", color="#0f172a")
    ax.text(8.0, 8.75, "Sub-Process Decomposition of Processes 4.0 (Cart & Wishlist) and 5.0 (Checkout, Payment & Orders)", ha="center", va="center", fontsize=9.2, color="#64748b")

    # User
    u_box = patches.FancyBboxPatch((0.5, 4.0), 2.0, 2.5, boxstyle="round,pad=0.12", fc="#0f172a", ec="#334155", lw=1.5, zorder=3)
    ax.add_patch(u_box)
    ax.text(1.5, 5.8, "USER / SHOPPER", ha="center", va="center", color="#38bdf8", fontsize=8, fontweight="bold", zorder=4)
    ax.text(1.5, 5.2, "Shopper Client", ha="center", va="center", color="#ffffff", fontsize=11, fontweight="bold", zorder=4)
    ax.text(1.5, 4.6, "• Add / Edit Cart Item\n• Toggle Wishlist\n• Submit Checkout\n• Receive Confirmation", ha="center", va="center", color="#cbd5e1", fontsize=7.2, zorder=4)

    # Subprocesses for 4.0 (Cart & Wishlist)
    p41 = patches.FancyBboxPatch((3.8, 6.6), 3.2, 1.2, boxstyle="round,pad=0.1", fc="#0284c7", ec="#0369a1", lw=1.5, zorder=3)
    ax.add_patch(p41)
    ax.text(5.4, 7.4, "4.1 Junction Key Deduplicator", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(5.4, 6.9, "Enforce PK(user_id, product_id)\nON CONFLICT DO UPDATE quantity", ha="center", va="center", color="#e0f2fe", fontsize=7, zorder=4)

    p42 = patches.FancyBboxPatch((7.8, 6.6), 3.2, 1.2, boxstyle="round,pad=0.1", fc="#0369a1", ec="#075985", lw=1.5, zorder=3)
    ax.add_patch(p42)
    ax.text(9.4, 7.4, "4.2 Stock & Price Validator", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(9.4, 6.9, "Check stock > quantity\nFetch current price from D2", ha="center", va="center", color="#e0f2fe", fontsize=7, zorder=4)

    # Subprocesses for 5.0 (Checkout & Order)
    p51 = patches.FancyBboxPatch((3.8, 1.8), 3.2, 1.2, boxstyle="round,pad=0.1", fc="#0f766e", ec="#115e59", lw=1.5, zorder=3)
    ax.add_patch(p51)
    ax.text(5.4, 2.6, "5.1 Invoice & Tax Calculator", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(5.4, 2.1, "Subtotal, Shipping, Tax\nValidate Line Item Totals", ha="center", va="center", color="#ccfbf1", fontsize=7, zorder=4)

    p52 = patches.FancyBboxPatch((7.8, 1.8), 3.2, 1.2, boxstyle="round,pad=0.1", fc="#581c87", ec="#6b21a8", lw=1.5, zorder=3)
    ax.add_patch(p52)
    ax.text(9.4, 2.6, "5.2 Payment Gateway Adapter", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(9.4, 2.1, "Stripe/Razorpay Webhook Handshake\nCapture Financial Charge", ha="center", va="center", color="#f3e8ff", fontsize=7, zorder=4)

    p53 = patches.FancyBboxPatch((11.8, 1.8), 3.4, 1.2, boxstyle="round,pad=0.1", fc="#065f46", ec="#047857", lw=1.5, zorder=3)
    ax.add_patch(p53)
    ax.text(13.5, 2.6, "5.3 Transactional Order Committer", ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="bold", zorder=4)
    ax.text(13.5, 2.1, "Write orders & order_items\nClear cart_items atomically", ha="center", va="center", color="#d1fae5", fontsize=7, zorder=4)

    # Data Stores
    # D4 Cart & Wishlist
    ax.plot([12.0, 15.6, 15.6, 12.0], [7.8, 7.8, 6.6, 6.6], color="#059669", lw=2, zorder=3)
    ax.fill([12.0, 15.6, 15.6, 12.0], [7.8, 7.8, 6.6, 6.6], color="#ecfdf5", zorder=2)
    ax.text(12.4, 7.2, "D4", ha="center", va="center", color="#065f46", fontsize=9, fontweight="bold", zorder=4)
    ax.text(13.9, 7.4, "public.cart_items & wishlist_items", ha="center", va="center", color="#065f46", fontsize=8, fontweight="bold", zorder=4)
    ax.text(13.9, 6.95, "PK(user_id, product_id), quantity", ha="center", va="center", color="#047857", fontsize=6.8, zorder=4)

    # D2 Products
    ax.plot([7.8, 11.0, 11.0, 7.8], [5.2, 5.2, 4.2, 4.2], color="#059669", lw=2, zorder=3)
    ax.fill([7.8, 11.0, 11.0, 7.8], [5.2, 5.2, 4.2, 4.2], color="#ecfdf5", zorder=2)
    ax.text(8.2, 4.7, "D2", ha="center", va="center", color="#065f46", fontsize=9, fontweight="bold", zorder=4)
    ax.text(9.5, 4.85, "public.products (stock, price)", ha="center", va="center", color="#065f46", fontsize=8, fontweight="bold", zorder=4)
    ax.text(9.5, 4.45, "Atomic Stock Decrement on Buy", ha="center", va="center", color="#047857", fontsize=6.8, zorder=4)

    # D5 Orders
    ax.plot([11.8, 15.6, 15.6, 11.8], [4.4, 4.4, 3.4, 3.4], color="#059669", lw=2, zorder=3)
    ax.fill([11.8, 15.6, 15.6, 11.8], [4.4, 4.4, 3.4, 3.4], color="#ecfdf5", zorder=2)
    ax.text(12.2, 3.9, "D5", ha="center", va="center", color="#065f46", fontsize=9, fontweight="bold", zorder=4)
    ax.text(13.8, 4.05, "public.orders & order_items", ha="center", va="center", color="#065f46", fontsize=8, fontweight="bold", zorder=4)
    ax.text(13.8, 3.65, "Immutable Financial Records", ha="center", va="center", color="#047857", fontsize=6.8, zorder=4)

    # Flows
    ax.annotate("", xy=(3.8, 7.2), xytext=(2.5, 5.8), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 3.1, 6.7, "Item ID & Qty Change", color="#0369a1", fontsize=7)

    ax.annotate("", xy=(7.8, 7.2), xytext=(7.0, 7.2), arrowprops=dict(arrowstyle="-|>", color="#0284c7", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 7.4, 7.5, "Deduplicated Row", color="#0369a1", fontsize=6.8)

    ax.annotate("", xy=(9.4, 6.6), xytext=(9.4, 5.2), arrowprops=dict(arrowstyle="<|-|>", color="#059669", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 9.4, 5.9, "Verify Available Stock", color="#065f46", fontsize=6.8)

    ax.annotate("", xy=(12.0, 7.2), xytext=(11.0, 7.2), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 11.5, 7.5, "Persist / Upsert Row", color="#065f46", fontsize=6.8)

    # Cart back to User
    ax.annotate("", xy=(2.5, 5.4), xytext=(12.0, 6.8), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.6, mutation_scale=11, connectionstyle="arc3,rad=0.12"), zorder=5)
    draw_pill(ax, 6.8, 6.3, "Updated Cart State & Subtotal", color="#065f46", fontsize=7.2)

    # Checkout flows
    ax.annotate("", xy=(3.8, 2.4), xytext=(2.5, 4.4), arrowprops=dict(arrowstyle="-|>", color="#0f766e", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 3.1, 3.2, "Place Order Request", color="#0f766e", fontsize=7)

    ax.annotate("", xy=(7.8, 2.4), xytext=(7.0, 2.4), arrowprops=dict(arrowstyle="-|>", color="#0f766e", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 7.4, 2.7, "Final Total Amount", color="#0f766e", fontsize=6.8)

    ax.annotate("", xy=(11.8, 2.4), xytext=(11.0, 2.4), arrowprops=dict(arrowstyle="-|>", color="#581c87", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 11.4, 2.7, "Payment Authorized", color="#6b21a8", fontsize=6.8)

    # Commit to D5
    ax.annotate("", xy=(13.5, 3.4), xytext=(13.5, 3.0), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.5, mutation_scale=10), zorder=5)
    draw_pill(ax, 14.5, 3.2, "INSERT INTO orders, order_items", color="#065f46", fontsize=6.8)

    # Decrement D2 stock
    ax.annotate("", xy=(10.0, 4.2), xytext=(12.5, 2.8), arrowprops=dict(arrowstyle="-|>", color="#dc2626", lw=1.4, mutation_scale=10, linestyle="--"), zorder=5)
    draw_pill(ax, 10.6, 3.6, "stock = stock - qty", color="#991b1b", bg="#fef2f2", border="#fecaca", fontsize=6.8)

    # Delete D4 cart
    ax.annotate("", xy=(13.8, 6.6), xytext=(13.8, 4.4), arrowprops=dict(arrowstyle="-|>", color="#dc2626", lw=1.4, mutation_scale=10, linestyle="--"), zorder=5)
    draw_pill(ax, 14.7, 5.5, "DELETE FROM cart_items", color="#991b1b", bg="#fef2f2", border="#fecaca", fontsize=6.8)

    # Confirmation back to User
    ax.annotate("", xy=(2.5, 4.8), xytext=(12.0, 2.0), arrowprops=dict(arrowstyle="-|>", color="#059669", lw=1.8, mutation_scale=12, connectionstyle="arc3,rad=-0.14"), zorder=5)
    draw_pill(ax, 6.5, 3.8, "Order Receipt, Invoice # & Payment Success", color="#065f46", fontsize=7.5)

    ax.set_xlim(0, 16.5)
    ax.set_ylim(0.5, 9.5)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(DFD2B_IMG, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[+] DFD Level 2B saved: {DFD2B_IMG}")


# =====================================================================
# 5. MASTER SUBMISSION PDF WITH ALL LEVELS
# =====================================================================
def generate_all_levels_pdf():
    doc = SimpleDocTemplate(
        str(MASTER_PDF),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#475569"),
        spaceAfter=10,
    )
    h2_style = ParagraphStyle(
        "DocH2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor("#0284c7"),
        spaceBefore=8,
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "DocBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6,
    )
    bullet_style = ParagraphStyle(
        "DocBullet",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3,
    )

    story = []

    # -------------------------------------------------------------
    # PAGE 1: DFD LEVEL 0 (CONTEXT DIAGRAM) + SYSTEM OVERVIEW
    # -------------------------------------------------------------
    story.append(Paragraph("ShopSense — All-Level Data Flow & Architecture Specification", title_style))
    story.append(Paragraph("Complete Technical Documentation: DFD Levels 0, 1, 2A, 2B, Corrected 10-Table ERD, and Cloud Database Integration", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=8))

    meta_data = [
        [
            Paragraph("<b>Candidate Name:</b> Shaurya (shauryadeep707@gmail.com)", body_style),
            Paragraph("<b>Database Host:</b> nzccgolsbffelzdxtkom.supabase.co", body_style),
        ],
        [
            Paragraph("<b>Cloud DB:</b> Supabase PostgreSQL (AWS)", body_style),
            Paragraph("<b>Core Modules:</b> Hybrid Search, Recommendations, Cart, Orders", body_style),
        ],
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
            ("PADDING", (0, 0), (-1, -1), 4),
            ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ])
    )
    story.append(meta_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Data Flow Diagram — Level 0 (Context Diagram)", h2_style))
    story.append(Paragraph(
        "The Level 0 Context Diagram establishes the environmental boundary of ShopSense. It models the entire platform as a single centralized processing entity (0.0) and charts the fundamental bidirectional data exchanges between the customer browser, the catalog administrator, the Supabase PostgreSQL cloud repository, and the external payment gateway.",
        body_style,
    ))
    story.append(Image(str(DFD0_IMG), width=540, height=270))
    story.append(Spacer(1, 6))

    l0_table_data = [
        ["External Entity / Store", "Input Data to System (0.0)", "Output Data from System (0.0)"],
        ["Customer / Shopper", "Search queries, filters, cart additions, checkout payloads, clickstream", "Personalized product feed, ranked search results, live cart state, invoices"],
        ["Store Administrator", "Catalog updates, price revisions, inventory stock adjustments", "Search latency analytics, user query history, conversion reports"],
        ["Supabase Cloud (DB)", "Database records, product catalog, user profiles, past interaction matrix", "Transactional SQL queries: INSERT, UPDATE, UPSERT, and DELETE"],
        ["Payment Gateway", "Webhook verification callback, transaction settlement status", "Order total amount, currency, and customer payment authorization token"],
    ]
    l0_table = Table(l0_table_data, colWidths=[130, 205, 205])
    l0_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.5),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 4),
        ])
    )
    story.append(l0_table)

    # -------------------------------------------------------------
    # PAGE 2: DFD LEVEL 1 (SUBSYSTEM FUNCTIONAL DECOMPOSITION)
    # -------------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("2. Data Flow Diagram — Level 1 (Subsystems Functional Flow)", h2_style))
    story.append(Paragraph(
        "Level 1 decomposes the root system into its 6 core functional processes and explicitly connects each process to its corresponding Supabase PostgreSQL cloud table (Data Stores D1 through D6):",
        body_style,
    ))
    story.append(Image(str(DFD1_IMG), width=540, height=310))
    story.append(Spacer(1, 6))

    l1_table_data = [
        ["Process ID", "Subsystem Name", "Connected Supabase Table", "Primary Data Responsibility"],
        ["1.0", "Auth & Identity", "D1: public.users", "JWT issuance, scrypt/bcrypt password hashing, role permissions."],
        ["2.0", "Hybrid Search", "D2: products, D6: search_logs", "BM25 keyword matching + TF-IDF cosine similarity fused via RRF."],
        ["3.0", "Recommender", "D3: interactions & events", "Builds user-item interaction matrix (weights 1-5) for collaborative filtering."],
        ["4.0", "Cart & Wishlist", "D4: cart_items, wishlist_items", "Junction table state management with composite PK (user_id, product_id)."],
        ["5.0", "Checkout & Order", "D5: orders, order_items", "Transactional line-item generation, stock decrement, and cart flush."],
        ["6.0", "Telemetry Tracker", "D3: interactions, D6: search_logs", "Asynchronously records dwell time, query execution latency, and conversion logs."],
    ]
    l1_table = Table(l1_table_data, colWidths=[55, 110, 155, 220])
    l1_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0284c7")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7.5),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 4),
        ])
    )
    story.append(l1_table)

    # -------------------------------------------------------------
    # PAGE 3: DFD LEVEL 2A (SEARCH & RECOMMENDATION PIPELINE)
    # -------------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("3. Data Flow Diagram — Level 2A (Search & Recommender Pipeline)", h2_style))
    story.append(Paragraph(
        "Level 2A zooms into Process 2.0 (Search Engine) and Process 3.0 (Recommendation Engine). It shows the exact internal atomic processes that transform raw customer queries and telemetry into highly ranked products.",
        body_style,
    ))
    story.append(Image(str(DFD2A_IMG), width=540, height=310))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Key Architectural Highlights in Level 2A:</b>", body_style))
    story.append(Paragraph("&bull; <b>Hybrid Fusion (2.4):</b> Lexical BM25 (Process 2.2) and Dense Semantic TF-IDF (Process 2.3) run in parallel over 591 catalog products. Their results are merged using Reciprocal Rank Fusion (RRF: <i>score = &Sigma; 1/(60 + rank)</i>) to balance precision and recall.", bullet_style))
    story.append(Paragraph("&bull; <b>Implicit Feedback Matrix (3.1 & 3.2):</b> Rather than relying solely on explicit star ratings, the platform assigns dynamic weights (View = 1, Dwell &gt; 10s = 2, Cart Add = 3, Order = 5) to generate an interaction matrix across 1,561 entries.", bullet_style))
    story.append(Paragraph("&bull; <b>Query Latency Telemetry (D6):</b> Process 2.4 logs search execution time (in milliseconds) into <code>public.search_logs</code> to monitor indexing performance.", bullet_style))

    # -------------------------------------------------------------
    # PAGE 4: DFD LEVEL 2B (CART, CHECKOUT & FINANCIAL PIPELINE)
    # -------------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("4. Data Flow Diagram — Level 2B (Cart, Checkout & Order Fulfillment)", h2_style))
    story.append(Paragraph(
        "Level 2B details the transactional lifecycle of cart items, inventory validation, financial calculation, and atomic database commits across Processes 4.0 and 5.0.",
        body_style,
    ))
    story.append(Image(str(DFD2B_IMG), width=540, height=300))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Key Transactional Invariants in Level 2B:</b>", body_style))
    story.append(Paragraph("&bull; <b>Composite Key Deduplication (4.1):</b> Cart and Wishlist items are keyed by <code>(user_id, product_id)</code>. Any repeated addition performs an atomic quantity upsert, completely avoiding duplicate rows.", bullet_style))
    story.append(Paragraph("&bull; <b>Atomic Inventory Decrement (5.3 &rarr; D2):</b> Upon payment confirmation, the system executes <code>UPDATE public.products SET stock = stock - quantity WHERE id = product_id</code> within the checkout transaction.", bullet_style))
    story.append(Paragraph("&bull; <b>Cart Flush (5.3 &rarr; D4):</b> Once the order and line items are successfully written to <code>public.orders</code> and <code>public.order_items</code>, the user's active cart rows are purged atomically.", bullet_style))

    # -------------------------------------------------------------
    # PAGE 5: COMPLETE 10-TABLE ENTITY RELATIONSHIP DIAGRAM (ERD)
    # -------------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("5. Complete Entity Relationship Diagram (ERD)", h2_style))
    story.append(Paragraph(
        "The relational schema encompasses 10 PostgreSQL tables deployed live on Supabase AWS. Junction tables feature composite primary keys that maintain strict referential integrity:",
        body_style,
    ))
    story.append(Image(str(ERD_IMG), width=540, height=310))
    story.append(Spacer(1, 6))

    erd_table_data = [
        ["Table Name", "Type", "Primary Key", "Foreign Keys", "Business Function"],
        ["users", "Master", "id (TEXT)", "None", "Stores customer & admin credentials, scrypt password hashes, and roles."],
        ["products", "Master", "id (TEXT)", "None", "591 catalog items with title, category, price, stock, and descriptions."],
        ["cart_items", "Junction", "(user_id, product_id)", "user_id &rarr; users, product_id &rarr; products", "Active shopping basket items with quantity and updated timestamps."],
        ["wishlist_items", "Junction", "(user_id, product_id)", "user_id &rarr; users, product_id &rarr; products", "Saved items for future purchase with added_at timestamps."],
        ["orders", "Transactional", "id (TEXT)", "user_id &rarr; users", "Financial order headers with total_amount, currency, and status."],
        ["order_items", "Junction", "(order_id, product_id)", "order_id &rarr; orders, product_id &rarr; products", "Immutable line items preserving purchase price and quantity at checkout time."],
        ["interactions", "Telemetry", "id (TEXT)", "user_id &rarr; users, product_id &rarr; products", "1,561 rows of user behavior (view, click, cart, purchase) with weights."],
        ["events", "Telemetry", "id (TEXT)", "user_id &rarr; users", "Unstructured system events stored as JSONB payloads for auditing."],
        ["search_history", "Analytics", "id (TEXT)", "user_id &rarr; users", "User-specific search queries and returned result counts."],
        ["search_logs", "Analytics", "id (TEXT)", "None", "System-wide query latency benchmarks (execution_ms) and query strings."],
    ]
    erd_table = Table(erd_table_data, colWidths=[70, 50, 95, 155, 170])
    erd_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#065f46")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 6.8),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0, 0), (-1, -1), 3),
        ])
    )
    story.append(erd_table)

    # -------------------------------------------------------------
    # PAGE 6: VIVA DEFENSE & HOW EVERYTHING CONNECTS
    # -------------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("6. Technical Defense: How the Entire Platform Connects", h2_style))
    story.append(Paragraph(
        "This section delivers exact architectural talking points for technical interviews, viva presentations, and project grading:",
        body_style,
    ))

    story.append(Paragraph("<b>6.1 Dual Node.js + Python Architecture</b>", body_style))
    story.append(Paragraph(
        "&bull; <b>Node.js (Express & Supabase JS):</b> Powers the high-concurrency API server (<code>backend/server.js</code>). It handles customer sessions, cart mutations, live checkout flows, and forwards mutations to Supabase Cloud via HTTPS REST (PostgREST).",
        bullet_style,
    ))
    story.append(Paragraph(
        "&bull; <b>Python (psycopg2 & SQLAlchemy):</b> Powers the data science and batch analytics engine (<code>database/</code>). It establishes direct SSL connections over port 5432 to train collaborative filtering models, calculate item-item similarity matrices, and execute schema migrations.",
        bullet_style,
    ))

    story.append(Paragraph("<b>6.2 Relational Integrity & Cascading Deletions</b>", body_style))
    story.append(Paragraph(
        "&bull; All child tables enforce <code>ON DELETE CASCADE</code> referencing parent keys in <code>users</code> and <code>products</code>. When a user or product is removed, all orphaned cart entries, wishlist rows, and interaction records are cleared automatically by PostgreSQL.",
        bullet_style,
    ))
    story.append(Paragraph(
        "&bull; <b>Financial Immutability:</b> Unlike <code>cart_items</code> which holds temporary quantities, <code>order_items</code> captures the exact <code>unit_price</code> at the time of purchase. Even if a product's price changes in <code>products</code> tomorrow, historic order invoices remain financially accurate.",
        bullet_style,
    ))

    story.append(Paragraph("<b>6.3 Viva Questions & Model Answers</b>", body_style))
    qas = [
        ("Q: Why use Reciprocal Rank Fusion (RRF) instead of just BM25 or just embeddings?",
         "A: BM25 excels at exact keyword matching (e.g., brand names, product codes) but fails when queries use synonyms. Vector embeddings excel at semantic intent but can miss exact SKU matches. RRF normalizes rank positions from both models without needing score calibration, producing superior hybrid recall."),
        ("Q: Why are composite primary keys used in cart_items and wishlist_items?",
         "A: Using PRIMARY KEY (user_id, product_id) prevents duplicate entries at the database engine level. It guarantees O(1) row lookups and makes upsert operations trivial via Postgres ON CONFLICT DO UPDATE."),
        ("Q: How does the system handle cold-start users in recommendations?",
         "A: For new users with zero interaction rows in D3, Process 3.3 falls back to a global popularity and category trending hybrid model based on high-conversion products from D2 until user clickstream telemetry is collected."),
    ]
    for q, a in qas:
        story.append(Paragraph(f"<b>{q}</b>", body_style))
        story.append(Paragraph(a, bullet_style))
        story.append(Spacer(1, 2))

    doc.build(story)
    print(f"[+] Complete Master Submission PDF generated: {MASTER_PDF}")


if __name__ == "__main__":
    create_dfd_level0()
    create_dfd_level1()
    create_dfd_level2_search()
    create_dfd_level2_checkout()
    # ERD generation
    import generate_final_submission_pdf
    generate_final_submission_pdf.create_erd_diagram()
    generate_all_levels_pdf()
