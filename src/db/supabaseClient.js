"use strict";
/**
 * Supabase client configuration for ShopSense.
 * Connects directly to Supabase Cloud PostgreSQL instance:
 * https://nzccgolsbffelzdxtkom.supabase.co
 *
 * Secret credentials are securely loaded from .env or environment variables.
 */
const fs = require("fs");
const path = require("path");
const { createClient } = require("@supabase/supabase-js");

// 1. Auto-load .env if present in root
const envPath = path.join(__dirname, "..", "..", ".env");
if (fs.existsSync(envPath)) {
  try {
    const content = fs.readFileSync(envPath, "utf8");
    for (const line of content.split("\n")) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) continue;
      const eqIdx = trimmed.indexOf("=");
      if (eqIdx !== -1) {
        const k = trimmed.slice(0, eqIdx).trim();
        const v = trimmed.slice(eqIdx + 1).trim().replace(/^['"]|['"]$/g, "");
        if (!process.env[k]) process.env[k] = v;
      }
    }
  } catch {
    /* ignore */
  }
}

// 2. Default project URL
const DEFAULT_SUPABASE_URL = "https://nzccgolsbffelzdxtkom.supabase.co";

const supabaseUrl = process.env.SUPABASE_URL || DEFAULT_SUPABASE_URL;
const supabaseKey =
  process.env.SUPABASE_SERVICE_ROLE_KEY ||
  process.env.SUPABASE_ANON_KEY;

let supabase = null;

function getSupabaseClient() {
  if (!supabase) {
    if (!supabaseUrl || !supabaseKey) {
      throw new Error(
        "Supabase credentials missing. Please set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in your .env file."
      );
    }
    supabase = createClient(supabaseUrl, supabaseKey, {
      auth: {
        persistSession: false,
        autoRefreshToken: false,
      },
    });
  }
  return supabase;
}

function isSupabaseConfigured() {
  return Boolean(supabaseUrl && supabaseKey);
}

module.exports = {
  getSupabaseClient,
  isSupabaseConfigured,
  SUPABASE_URL: supabaseUrl,
};
