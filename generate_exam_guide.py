"""
Generate a comprehensive Exam Preparation & Viva Study Guide PDF for Shaurya.
Covers ER Diagrams, Supabase/PostgreSQL, Search Algorithms (BM25, RRF),
Recommendation Systems (CF, Matrix Factorization), Full-Stack Architecture,
and Top 20 Viva Questions with Model Answers.
"""

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
    PageBreak,
    HRFlowable,
    KeepTogether,
)

ROOT_DIR = Path("C:/Users/shaur/.gemini/antigravity/scratch/e-commerce-repo")
OUTPUT_PDF = ROOT_DIR / "ShopSense_Exam_Preparation_Guide_Shaurya.pdf"


def build_exam_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()

    # Typography styles
    c_primary = colors.HexColor("#0f172a")     # Slate 900
    c_accent = colors.HexColor("#0284c7")      # Sky 600
    c_secondary = colors.HexColor("#475569")   # Slate 600
    c_qbg = colors.HexColor("#f1f5f9")         # Slate 100
    c_border = colors.HexColor("#cbd5e1")      # Slate 300

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
    section_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=6,
    )
    sub_section_style = ParagraphStyle(
        "SubSectionHeader",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=c_accent,
        spaceBefore=8,
        spaceAfter=3,
    )
    body_style = ParagraphStyle(
        "BodyText_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=c_primary,
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "Bullet_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12.5,
        textColor=c_primary,
        leftIndent=12,
        spaceAfter=3,
    )
    q_style = ParagraphStyle(
        "QuestionText",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#0369a1"),
    )
    a_style = ParagraphStyle(
        "AnswerText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b"),
    )

    story = []

    # =========================================================================
    # COVER / HEADER
    # =========================================================================
    story.append(Paragraph("ShopSense — Exam & Viva Master Preparation Guide", title_style))
    story.append(
        Paragraph(
            "Essential Theory, Architecture, Algorithms, Database Design & Viva Q&A | Candidate: Shaurya",
            subtitle_style,
        )
    )
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceAfter=8))

    # Meta Table
    meta = [
        [
            Paragraph("<b>Subject:</b> E-Commerce System & Database Engineering", body_style),
            Paragraph("<b>Target Tech:</b> PostgreSQL, Supabase, Python, Node.js", body_style),
        ],
        [
            Paragraph("<b>Core Topics:</b> ERD, Normalization, Search (BM25+RRF), Recommenders (CF+MF)", body_style),
            Paragraph("<b>Database:</b> Live Cloud (nzccgolsbffelzdxtkom.supabase.co)", body_style),
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
    story.append(Spacer(1, 8))

    # =========================================================================
    # MODULE 1: DATABASE & ER DIAGRAM THEORY
    # =========================================================================
    story.append(Paragraph("Module 1: Database Architecture, ER Diagrams & Normalization", section_style))
    story.append(
        Paragraph(
            "<b>1.1 What is an Entity-Relationship (ER) Diagram?</b><br/>"
            "An ER Diagram visually models the data requirements of a system using three core constructs:<br/>"
            "• <b>Entities</b>: Real-world objects represented as tables (e.g., <code>USERS</code>, <code>PRODUCTS</code>, <code>ORDERS</code>).<br/>"
            "• <b>Attributes</b>: Properties describing an entity (e.g., <code>price</code>, <code>email</code>, <code>status</code>).<br/>"
            "• <b>Relationships & Cardinality</b>: Associations between entities (e.g., 1 User places N Orders ➔ <b>1:N</b>; Orders and Products connect via <b>M:N</b> junction tables).",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>1.2 Weak Entities & Composite Primary Keys</b><br/>"
            "• <b>Weak Entity:</b> An entity that cannot be uniquely identified by its own attributes alone and depends on a foreign key from a parent entity.<br/>"
            "• In ShopSense, <code>CART_ITEMS</code>, <code>WISHLIST_ITEMS</code>, and <code>ORDER_ITEMS</code> are associative weak entities.<br/>"
            "• <b>Composite Primary Key:</b> A primary key consisting of two or more columns. In <code>cart_items</code>, the composite PK <code>(user_id, product_id)</code> ensures a customer cannot have duplicate entries for the same product; instead, quantity is incremented.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>1.3 Database Normalization (Applied in ShopSense)</b><br/>"
            "• <b>1NF (First Normal Form):</b> All column values are atomic (no arrays/repeating groups in relational columns). Primary key is defined.<br/>"
            "• <b>2NF (Second Normal Form):</b> Must be in 1NF and have no partial dependencies (every non-key attribute must depend on the whole composite key). For example, in <code>order_items</code>, attributes like <code>quantity</code> depend on both <code>(order_id, product_id)</code>.<br/>"
            "• <b>3NF (Third Normal Form):</b> Must be in 2NF and have no transitive dependencies (non-key attributes do not depend on other non-key attributes). Product metadata belongs in <code>products</code>, not duplicated in <code>cart_items</code>.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>1.4 Why Supabase (Cloud PostgreSQL)?</b><br/>"
            "• <b>PostgreSQL Power:</b> Enterprise relational database with full ACID compliance, foreign key constraints, indexes, and JSONB support.<br/>"
            "• <b>Row Level Security (RLS):</b> Enforces security policies at the database engine level (e.g., <code>auth.uid() = user_id</code>). Even if an API bug occurs, users cannot access other users' carts or orders.<br/>"
            "• <b>Cloud Persistence:</b> Solves the ephemeral container disk problem (e.g., on Render or Heroku) by persisting data safely in the cloud.",
            body_style,
        )
    )
    story.append(Spacer(1, 6))

    # =========================================================================
    # MODULE 2: INFORMATION RETRIEVAL & SEARCH ENGINE
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Module 2: Search Engine & Information Retrieval (IR)", section_style))
    story.append(
        Paragraph(
            "ShopSense implements a custom <b>hybrid search engine</b> built from algorithmic first principles without external search servers:",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>2.1 Inverted Index & Tokenization Pipeline</b><br/>"
            "• <b>Tokenization:</b> Breaking text into individual words, converting to lowercase, and stripping punctuation.<br/>"
            "• <b>Stemming:</b> Reducing inflected words to their root form (e.g., 'running', 'runs', 'ran' ➔ 'run') using algorithmic rule sets.<br/>"
            "• <b>Inverted Index:</b> A mapping from terms to the document IDs containing them: <code>Term ➔ [Doc1, Doc5, Doc12]</code>. Allows looking up matching documents in <b>O(1)</b> average time rather than scanning all products <b>O(N)</b>.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>2.2 BM25 (Best Matching 25) Keyword Ranking</b><br/>"
            "• State-of-the-art probabilistic relevance ranking algorithm used by industrial search engines.<br/>"
            "• Evaluates term saturation using non-linear TF: multiple occurrences of a word provide diminishing returns.<br/>"
            "• Document Length Normalization: Penalizes very long titles/descriptions to prevent spamming keywords.<br/>"
            "• Formula components: <code>IDF(q_i) * (TF * (k1 + 1)) / (TF + k1 * (1 - b + b * (|D| / avgdl)))</code>.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>2.3 Vector Space Model & Cosine Similarity</b><br/>"
            "• Represents product documents and user queries as high-dimensional TF-IDF vectors.<br/>"
            "• Calculates angle cosine: <code>cos(θ) = (A · B) / (||A|| ||B||)</code>. Values close to 1 indicate strong topical similarity.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>2.4 Reciprocal Rank Fusion (RRF)</b><br/>"
            "• Combines disparate ranked lists (BM25 keyword search + Vector semantic search) without needing score calibration:<br/>"
            "• <code>RRF_Score(d) = Σ [ 1 / (k + rank_i(d)) ]</code> (where k = 60 is a smoothing constant).<br/>"
            "• Products ranking high in both BM25 and vector spaces are boosted to the top of the search results.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>2.5 Trie for Autocomplete & Levenshtein for Typo Tolerance</b><br/>"
            "• <b>Trie (Prefix Tree):</b> Fast autocomplete suggestions in <code>O(M)</code> time (where M is query length), independent of catalog size.<br/>"
            "• <b>Levenshtein Distance:</b> Dynamic programming edit distance calculating the minimum insertions, deletions, or substitutions to match a word. Corrects typos (e.g., 'shose' ➔ 'shoes').",
            body_style,
        )
    )
    story.append(Spacer(1, 6))

    # =========================================================================
    # MODULE 3: RECOMMENDATION SYSTEMS
    # =========================================================================
    story.append(Paragraph("Module 3: Recommendation Algorithms & Machine Learning", section_style))
    story.append(
        Paragraph(
            "<b>3.1 Cold-Start Problem</b><br/>"
            "• <b>Problem:</b> New users have zero interaction history, making personalized collaborative filtering impossible.<br/>"
            "• <b>ShopSense Solution:</b> Hybrid fallback. Unauthenticated or new users receive popularity-decayed trending items, curated category shelves, and demographic picks until their first interaction is logged.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>3.2 Item-Item Collaborative Filtering (CF)</b><br/>"
            "• Finds item relationships based on user behavior: 'Customers who viewed/bought item X also viewed item Y'.<br/>"
            "• Computes similarity using co-occurrence matrices weighted by interaction types (purchases weighted higher than views).",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>3.3 Matrix Factorization (Latent Factor Model via SGD)</b><br/>"
            "• Decomposes the sparse User-Item interaction matrix <code>R (users × items)</code> into two low-rank dense matrices: <code>P (users × k)</code> and <code>Q (items × k)</code>.<br/>"
            "• <code>Predicted_Rating(u, i) = P_u · Q_i^T</code>.<br/>"
            "• Trained using <b>Stochastic Gradient Descent (SGD)</b> to minimize squared reconstruction error with L2 regularization.",
            body_style,
        )
    )
    story.append(Spacer(1, 6))

    # =========================================================================
    # MODULE 4: TOP 20 VIVA QUESTIONS & MODEL ANSWERS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Module 4: Top 20 Viva / Oral Exam Questions & Model Answers", section_style))
    story.append(
        Paragraph(
            "These questions represent the most frequently asked questions during technical viva evaluations. Study these high-scoring answers:",
            body_style,
        )
    )
    story.append(Spacer(1, 4))

    viva_qa = [
        (
            "Q1: What is the main objective and architecture of ShopSense?",
            "ShopSense is a full-stack product discovery e-commerce platform featuring hybrid search (BM25 + TF-IDF Vector Space + RRF), hybrid recommendations (CF + Matrix Factorization + Trending), and a cloud PostgreSQL database hosted on Supabase.",
        ),
        (
            "Q2: Explain the ER Diagram design for this project.",
            "The ER diagram consists of 10 tables: USERS, PRODUCTS, and ORDERS as primary entities; CART_ITEMS, WISHLIST_ITEMS, and ORDER_ITEMS as associative junction tables with composite primary keys; and INTERACTIONS, EVENTS, SEARCH_HISTORY, and SEARCH_LOGS for telemetry and ML recommendations.",
        ),
        (
            "Q3: Why did you use composite primary keys in CART_ITEMS and ORDER_ITEMS?",
            "A composite key (user_id, product_id) in cart_items prevents duplicate rows for the same product per user. It enforces uniqueness and integrity at the database schema level while simplifying updates to quantity.",
        ),
        (
            "Q4: What is the difference between SQLite and Supabase PostgreSQL?",
            "SQLite is an embedded, single-node file database suitable for local development. Supabase is a cloud-hosted, enterprise PostgreSQL database with multi-user concurrency, network access, ACID transactions, and Row Level Security (RLS) suitable for production.",
        ),
        (
            "Q5: How is Row Level Security (RLS) implemented?",
            "RLS policies are defined on cart_items, wishlist_items, and orders using `auth.uid() = user_id`. This guarantees that queries only return data belonging to the authenticated user, enforcing authorization directly in the database engine.",
        ),
        (
            "Q6: How does the BM25 search algorithm work?",
            "BM25 is a probabilistic retrieval model that scores documents based on query term frequency with diminishing returns (term saturation) and normalizes for document length to prevent long product descriptions from artificially dominating search results.",
        ),
        (
            "Q7: What is Reciprocal Rank Fusion (RRF) and why is it used?",
            "RRF is an ensemble ranking technique that merges ordered results from keyword search (BM25) and semantic vector search using the formula score = Σ [1 / (k + rank)]. It eliminates the need to normalize raw scores from different algorithms.",
        ),
        (
            "Q8: What data structure is used for autocomplete and why?",
            "A Trie (prefix tree) is used. It allows prefix matching in O(M) time, where M is the prefix length, making suggestions virtually instantaneous regardless of how many thousands of terms exist in the catalog.",
        ),
        (
            "Q9: How does the system handle typos in user queries?",
            "It computes Levenshtein Distance (minimum character insertions, deletions, and substitutions) using dynamic programming. If a query term has no exact matches, it suggests or substitutes the closest catalog terms within edit distance 1 or 2.",
        ),
        (
            "Q10: What is Matrix Factorization in recommendation systems?",
            "Matrix Factorization decomposes a high-dimensional sparse user-item interaction matrix into two low-rank dense matrices representing latent user preferences and latent item features. Their dot product predicts user affinity for unseen items.",
        ),
        (
            "Q11: How do you address the Cold-Start problem?",
            "For new users without interaction history, the system serves popularity-ranked trending products with time-decay scores, featured brand shelves, and curated lists until their first views or clicks are recorded.",
        ),
        (
            "Q12: How are passwords stored securely?",
            "Passwords are never stored in plaintext. They are hashed using scrypt with a cryptographic salt (16 bytes) and 64-byte derived key, making them resistant to rainbow table and brute-force GPU attacks.",
        ),
        (
            "Q13: How does JWT authentication work?",
            "A JSON Web Token consists of Header, Payload, and Signature encoded in Base64URL. The server verifies identity statelessly by validating the HMAC-SHA256 signature using a secret key without querying the database for session state.",
        ),
        (
            "Q14: Explain the role of the Python `database/` module.",
            "The `database/` folder provides an object-oriented Python layer featuring dataclass models (models.py), repository classes for CRUD operations (repository.py), automated cloud migration (seed.py), and diagnostic verification (test_connection.py).",
        ),
        (
            "Q15: What happens when a user checks out their cart?",
            "An atomic database transaction creates a new row in `orders`, moves all lines from `cart_items` into `order_items`, logs a 'purchase' interaction for the recommender, and clears the user's cart.",
        ),
        (
            "Q16: What HTTP methods and status codes are used?",
            "Standard REST conventions: GET (200), POST (201 Created), PUT/PATCH (200), DELETE (200), 400 Bad Request, 401 Unauthorized, 404 Not Found, and 409 Conflict (e.g. duplicate email registration).",
        ),
        (
            "Q17: How is CI/CD configured for deployment?",
            "Deployment is managed via Render Blueprints (`render.yaml`). Every `git push origin main` triggers an automated build webhook that installs dependencies, executes migrations, and starts the service with zero downtime.",
        ),
        (
            "Q18: What is the purpose of the `interactions` vs `events` tables?",
            "`interactions` logs domain-specific signals (views, cart adds, purchases) strictly used by the collaborative filtering and matrix factorization engines. `events` records general client-side telemetry and audit logs.",
        ),
        (
            "Q19: How are database constraints enforced?",
            "Foreign keys with `ON DELETE CASCADE` ensure child records (e.g. order items when an order is deleted) are cleaned up. Column check constraints (`quantity > 0`) prevent invalid transaction data.",
        ),
        (
            "Q20: What are your key contributions to this repository?",
            "Designed and implemented the complete 10-table Supabase PostgreSQL cloud migration, built the modular Python database package, synchronized cloud persistence with the Node.js API, configured Render CI/CD, and authored 8 verified commits.",
        ),
    ]

    for q, a in viva_qa:
        q_box = [
            [Paragraph(q, q_style)],
            [Paragraph(a, a_style)],
        ]
        t_q = Table(q_box, colWidths=[540])
        t_q.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f9ff")),
                    ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#ffffff")),
                    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#bae6fd")),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )
        story.append(t_q)
        story.append(Spacer(1, 4))

    doc.build(story)
    print(f"[+] Exam Guide PDF generated successfully: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_exam_pdf()
