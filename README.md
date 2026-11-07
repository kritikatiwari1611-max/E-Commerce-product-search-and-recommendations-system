# ShopSense — E-Commerce Search & Recommendation System

A full-stack product discovery app: **hybrid search** (BM25 + TF-IDF vectors + RRF) and a
**hybrid recommender** (popularity, content-based, item-item CF, matrix factorization),
with a persistent cloud backend (auth, wishlist, cart, orders, admin) on **Supabase (PostgreSQL)**.
Built with **zero runtime dependencies** — Node.js built-ins only.

**Live:** https://shopsense-7djf.onrender.com
**Requires:** Node.js **22.5+** (uses the built-in `node:sqlite`)

---

## Features

- **Search** — BM25 keyword ranking, vector/semantic retrieval, reciprocal rank fusion,
  typo tolerance, autocomplete, filters/facets, and 100+ ranked results per query.
- **Recommendations** — trending, similar, "users also viewed", personalized feed
  (activity + search history), cold-start handling, with an explainable reason on each.
- **Catalogue** — 579 deduplicated products with real images, clean categories,
  product specifications and aggregated reviews, plus multi-store price comparison.
- **Backend** — register/login (JWT), wishlist, cart, checkout/orders, admin API,
  events and search analytics, all persisted in SQLite.

---

## Tech stack

| Layer | Technology |
|---|---|
| Runtime | Node.js 22 (`node:http`, `node:sqlite`, `node:crypto`) — no npm dependencies |
| Frontend | Vanilla JavaScript + HTML/CSS (no build step) |
| Database | **Supabase Cloud PostgreSQL** (`https://nzccgolsbffelzdxtkom.supabase.co`) |
| Tests | `node:test` (built-in) |

---

## Quick start

```bash
npm start        # http://localhost:3000  (DB is created and seeded on first run)
npm test         # run the test suite
npm run db:reset # rebuild the database from the seed data
npm run dev      # auto-reload
```

Environment variables: `PORT`, `JWT_SECRET`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`.

---

## Project structure

```
public/         frontend (vanilla JS, no build step)
src/
  api/          REST routes: auth, cart, orders, admin, wishlist
  search/       tokenizer, inverted index, BM25, TF-IDF vectors, trie, fuzzy matching
  recommend/    popularity, content-based, item-item CF, matrix factorization
  catalog/      categories, brands, home shelves, specs, reviews
  db/           schema.sql + SQLite repositories
  auth/         scrypt password hashing + HS256 JWT
  affiliate/    tracking params + product-link resolver
  store/        in-memory indexes wired to SQLite
scripts/        data generators, seed, db reset
tests/          node:test suites
```

---

## API (summary)

Base: `/api`

- **Search**: `GET /search?q=&vertical=&brand=&priceMin=&priceMax=&sort=&page=`, `GET /search/suggest?q=`
- **Products**: `GET /products/:id` (+ `/specs`, `/reviews`, `/similar`, `/recommendations`, `/prices`)
- **Discovery**: `GET /home`, `GET /categories`, `GET /recommendations`, `GET /recommendations/trending`, `GET /curated-lists`, `GET /stats`
- **Auth**: `POST /auth/register`, `POST /auth/login`, `GET /auth/me`
- **Wishlist** 🔒: `GET /wishlist`, `POST /wishlist`, `DELETE /wishlist/:productId`
- **Cart** 🔒: `GET /cart`, `POST /cart`, `PATCH /cart/:productId`, `DELETE /cart/:productId`, `DELETE /cart`
- **Orders** 🔒: `POST /orders`, `GET /orders`, `GET /orders/:id`
- **Admin** 🔒: `/admin/products`, `/admin/catalog/import`, `/admin/users`, `/admin/orders`, `/admin/analytics`

🔒 = requires `Authorization: Bearer <token>`.

---

## Deploy on Render (Cloud Persistent via Supabase)

Live: **https://shopsense-7djf.onrender.com**

Backed by **Supabase PostgreSQL Cloud**, cart, orders, users, and interaction data persist
indefinitely without needing paid persistent disks on Render. The repo includes `render.yaml`
pre-configured with Supabase auto-deployment.

1. Render → **New → Blueprint** → pick this repo.
2. Render automatically reads `render.yaml` and injects Supabase cloud configuration.
3. Click **Apply** → wait for **Live**!

---

## Notes

- Catalogue data comes from public product APIs (DummyJSON, Open Beauty Facts) plus a
  synthetic branded supplement; the seed JSON is committed so deploys work offline.
- Product specs are derived from catalogue data; reviews are clearly-labelled sample data.

## License

MIT.
