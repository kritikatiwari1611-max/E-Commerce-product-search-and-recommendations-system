"use strict";
/**
 * Data store + service wiring.
 *
 * Backed by Supabase Cloud PostgreSQL (https://nzccgolsbffelzdxtkom.supabase.co).
 * Synchronizes cart, wishlist, orders, users, interactions, and events
 * directly to Supabase cloud tables.
 */
const { SearchService } = require("../search/searchService");
const { RecommendationService } = require("../recommend/recService");
const { annotateAiScores } = require("../catalog/productScore");
const { attachOffers } = require("../../scripts/generate-catalog");
const {
  openDatabase,
  createRepo,
  loadProducts,
  loadUsers,
  loadInteractions,
} = require("../db/database");
const { isSupabaseConfigured, getSupabaseClient, SUPABASE_URL } = require("../db/supabaseClient");
const { createSupabaseRepo } = require("../db/supabaseRepo");

function slugify(s) {
  return String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function buildCuratedLists(products, popularity) {
  const byCategory = new Map();
  for (const p of products) {
    if (!byCategory.has(p.category)) byCategory.set(p.category, []);
    byCategory.get(p.category).push(p);
  }

  const norm = (val, max) => (max > 0 ? val / max : 0);
  const lists = [];

  for (const [category, items] of byCategory) {
    const maxPop = Math.max(...items.map((p) => popularity.get(p.id) || 0), 1);
    const score = (p) => {
      const value = p.mrp > p.price ? (p.mrp - p.price) / p.mrp : 0;
      const ratingN = norm(p.rating || 0, 5);
      const popN = norm(popularity.get(p.id) || 0, maxPop);
      return 0.5 * ratingN + 0.3 * popN + 0.2 * value;
    };
    const ranked = items.slice().sort((a, b) => score(b) - score(a));
    const prices = items.map((p) => p.price).sort((a, b) => a - b);
    const median = prices[Math.floor(prices.length / 2)];

    const makeList = (suffix, title, filterFn) => {
      const subset = ranked.filter(filterFn).slice(0, 10);
      if (subset.length < 3) return;
      lists.push({
        id: "cl_" + slugify(category) + suffix,
        title,
        category,
        intro: `Top ${category.toLowerCase()} picks ranked by rating, popularity and value.`,
        generatedAt: new Date().toISOString(),
        items: subset.map((p, i) => ({
          rank: i + 1,
          product: p,
          score: Math.round(score(p) * 100 * 10) / 10,
        })),
      });
    };

    makeList("", `Best ${category} Picks`, () => true);
    makeList("-budget", `Best Budget ${category}`, (p) => p.price <= median);
    makeList("-premium", `Premium ${category}`, (p) => p.price > median);
  }
  return lists;
}

/** Wire repository mutations to automatically sync to Supabase Cloud */
function attachSupabaseSync(repo) {
  if (!isSupabaseConfigured()) return repo;

  let sbRepo = null;
  try {
    sbRepo = createSupabaseRepo(getSupabaseClient());
  } catch {
    return repo;
  }

  const origCartAdd = repo.cart.add.bind(repo.cart);
  repo.cart.add = (userId, productId, qty) => {
    const res = origCartAdd(userId, productId, qty);
    sbRepo.cart.add(userId, productId, qty).catch(() => {});
    return res;
  };

  const origCartRemove = repo.cart.remove.bind(repo.cart);
  repo.cart.remove = (userId, productId) => {
    const res = origCartRemove(userId, productId);
    sbRepo.cart.remove(userId, productId).catch(() => {});
    return res;
  };

  const origCartClear = repo.cart.clear.bind(repo.cart);
  repo.cart.clear = (userId) => {
    const res = origCartClear(userId);
    sbRepo.cart.clear(userId).catch(() => {});
    return res;
  };

  const origCartSetQty = repo.cart.setQuantity.bind(repo.cart);
  repo.cart.setQuantity = (userId, productId, qty) => {
    const res = origCartSetQty(userId, productId, qty);
    sbRepo.cart.setQuantity(userId, productId, qty).catch(() => {});
    return res;
  };

  const origWishlistAdd = repo.wishlist.add.bind(repo.wishlist);
  repo.wishlist.add = (userId, productId) => {
    const res = origWishlistAdd(userId, productId);
    sbRepo.wishlist.add(userId, productId).catch(() => {});
    return res;
  };

  const origWishlistRemove = repo.wishlist.remove.bind(repo.wishlist);
  repo.wishlist.remove = (userId, productId) => {
    const res = origWishlistRemove(userId, productId);
    sbRepo.wishlist.remove(userId, productId).catch(() => {});
    return res;
  };

  const origOrdersCreate = repo.orders.create.bind(repo.orders);
  repo.orders.create = (order, items) => {
    const res = origOrdersCreate(order, items);
    sbRepo.orders.create(order, items).catch(() => {});
    return res;
  };

  const origUsersInsert = repo.users.insert.bind(repo.users);
  repo.users.insert = (user) => {
    const res = origUsersInsert(user);
    sbRepo.users.insert(user).catch(() => {});
    return res;
  };

  const origEventsInsert = repo.events.insert.bind(repo.events);
  repo.events.insert = (ev) => {
    const res = origEventsInsert(ev);
    sbRepo.events.insert(ev).catch(() => {});
    return res;
  };

  const origInteractionsInsert = repo.interactions.insert.bind(repo.interactions);
  repo.interactions.insert = (ev) => {
    const res = origInteractionsInsert(ev);
    sbRepo.interactions.insert(ev).catch(() => {});
    return res;
  };

  const origSearchLogsInsert = repo.searchLogs.insert.bind(repo.searchLogs);
  repo.searchLogs.insert = (log) => {
    const res = origSearchLogsInsert(log);
    sbRepo.searchLogs.insert(log).catch(() => {});
    return res;
  };

  const origSearchHistoryAdd = repo.searchHistory.add.bind(repo.searchHistory);
  repo.searchHistory.add = (userId, query, total) => {
    const res = origSearchHistoryAdd(userId, query, total);
    sbRepo.searchHistory.add(userId, query, total).catch(() => {});
    return res;
  };

  return repo;
}

function createStore(options = {}) {
  // Use memory DB if specified in tests, otherwise use default
  const db = options.db || openDatabase({ file: options.dbFile, seed: options.seed });
  let repo = createRepo(db);

  // Hook Supabase cloud sync
  if (options.syncSupabase !== false) {
    repo = attachSupabaseSync(repo);
  }

  let products = loadProducts(db);
  if (!products.every((p) => Array.isArray(p.offers))) {
    attachOffers(products);
    repo.products.saveMany(products);
  }
  annotateAiScores(products);
  const interactions = loadInteractions(db);
  const users = loadUsers(db);

  const search = new SearchService(products);
  const recs = new RecommendationService(products, interactions, users, search);
  const curatedLists = buildCuratedLists(products, recs.popularity);
  const curatedById = new Map(curatedLists.map((l) => [l.id, l]));

  const eventLog = [];
  const livePopularity = new Map();
  let eventCounter = 0;

  const store = {
    db,
    repo,
    products,
    users,
    interactions,
    search,
    recs,
    curatedLists,
    curatedById,
    eventLog,
    livePopularity,
    isSupabase: isSupabaseConfigured(),
    supabaseUrl: SUPABASE_URL,

    recordEvent(ev) {
      const record = {
        id: "ev_" + ++eventCounter,
        userId: ev.userId || null,
        productId: ev.productId || null,
        type: ev.type || "view",
        ts: ev.ts || new Date().toISOString(),
        sessionId: ev.sessionId || null,
      };
      eventLog.push(record);
      repo.events.insert(record);
      if (record.productId) {
        livePopularity.set(record.productId, (livePopularity.get(record.productId) || 0) + 1);
      }
      return record;
    },

    recordSearch(query, total, clickedId) {
      repo.searchLogs.insert({ query, total, clickedId: clickedId || null });
    },

    reloadProducts() {
      store.products = repo.products.all();
      if (!store.products.every((p) => Array.isArray(p.offers))) attachOffers(store.products);
      annotateAiScores(store.products);
      store.search = new SearchService(store.products);
      store.recs = new RecommendationService(store.products, store.interactions, store.users, store.search);
      store.curatedLists = buildCuratedLists(store.products, store.recs.popularity);
      store.curatedById = new Map(store.curatedLists.map((l) => [l.id, l]));
    },

    addUser(user) {
      store.users.push(user);
      if (store.recs && store.recs.usersById) store.recs.usersById.set(user.id, user);
    },

    analytics() {
      return {
        searches: repo.searchLogs.count(),
        zeroResultSearches: repo.searchLogs.zeroResultCount(),
        topQueries: repo.searchLogs.topQueries(10).map((r) => ({ query: r.query, count: r.count })),
        events: repo.events.count(),
        catalogue: store.search.stats(),
        recommender: store.recs.stats(),
        database: isSupabaseConfigured() ? `Supabase Cloud (${SUPABASE_URL})` : "Local",
      };
    },
  };

  return store;
}

module.exports = { createStore, buildCuratedLists, slugify };
