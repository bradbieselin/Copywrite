"""
Instagram DTC Brand Scraper via Apify API
Searches hashtags to find DTC ecommerce brand profiles and saves them to leads.csv.

Two-phase approach:
  Phase 1 — Scrape hashtag posts to collect unique author usernames.
  Phase 2 — Scrape each profile URL for full details (followers, bio, etc.)
             and filter to business/brand accounts only.

Usage (CLI):
  python instagram_dtc_scraper.py
  python instagram_dtc_scraper.py --hashtags dtcbrand shopify ecommerce --max-results 100
  python instagram_dtc_scraper.py --output my_leads.csv

Importable (called from the admin portal):
  from instagram_dtc_scraper import run_scraper
  summary = run_scraper(["dtcbrand", "shopifybrand"], 100, "leads.csv", token, on_status=log_fn)
"""

import argparse
import csv
import os
import sys
import time

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Defaults (all overridable via CLI or run_scraper() kwargs)
# ---------------------------------------------------------------------------

DEFAULT_HASHTAGS    = ["dtcbrand", "shopifybrand", "ecommerce"]
MIN_FOLLOWERS       = 5_000
MAX_FOLLOWERS       = 500_000
DEFAULT_OUTPUT      = "leads.csv"
DEFAULT_MAX_RESULTS = 200

ACTOR_ID            = "apify/instagram-scraper"
PROFILE_BATCH_SIZE  = 50

CSV_FIELDS = ["username", "full_name", "follower_count", "bio", "profile_url", "hashtag"]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scrape Instagram for DTC brand accounts via Apify.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--hashtags", nargs="+", default=DEFAULT_HASHTAGS, metavar="TAG",
                   help="Hashtags to search (without #).")
    p.add_argument("--max-results", type=int, default=DEFAULT_MAX_RESULTS, metavar="N",
                   help="Max posts to scrape per hashtag.")
    p.add_argument("--output", default=DEFAULT_OUTPUT, metavar="FILE",
                   help="Output CSV file path.")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _emit(msg: str, log_fn=None) -> None:
    """Print to stdout or call log_fn — used for both CLI and portal modes."""
    if log_fn:
        log_fn(msg)
    else:
        print(msg)


def validate_token(token: str) -> None:
    if not token:
        print(
            "ERROR: APIFY_API_TOKEN is not set.\n"
            "Add it to a .env file or export it in your shell:\n"
            "  export APIFY_API_TOKEN='your_token_here'\n"
            "See .env.example for the required variables."
        )
        sys.exit(1)


def safe_int(value) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


_CSV_INJECT_PREFIXES = ("=", "+", "-", "@", "\t", "\r")

def _sanitize_csv(value: str) -> str:
    """Prevent CSV formula injection (Excel/Sheets) by escaping dangerous leading chars."""
    s = str(value).strip()
    if s and s[0] in _CSV_INJECT_PREFIXES:
        return "'" + s
    return s


def _actor_call(client: ApifyClient, run_input: dict, context: str) -> dict:
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise RuntimeError(
            f"Apify actor returned None ({context}). "
            "Check your API token and actor ID."
        )
    return run


# ---------------------------------------------------------------------------
# Phase 1: collect usernames from hashtag posts
# ---------------------------------------------------------------------------

def collect_usernames_for_hashtag(
    client: ApifyClient, hashtag: str, max_results: int, log_fn=None
) -> set[str]:
    _emit(f"Phase 1 — scraping posts for #{hashtag} ...", log_fn)
    run_input = {
        "hashtags": [hashtag],
        "resultsType": "posts",
        "resultsLimit": max_results,
    }
    run = _actor_call(client, run_input, f"hashtag #{hashtag}")

    usernames: set[str] = set()
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        raw = item.get("ownerUsername") or item.get("username") or ""
        username = raw.lstrip("@").strip().lower()
        if username:
            usernames.add(username)

    _emit(f"  -> {len(usernames)} unique accounts found for #{hashtag}", log_fn)
    return usernames


# ---------------------------------------------------------------------------
# Phase 2: fetch full profile details
# ---------------------------------------------------------------------------

def fetch_profiles_batch(client: ApifyClient, usernames: list[str]) -> list[dict]:
    profile_urls = [f"https://www.instagram.com/{u}/" for u in usernames]
    run_input = {
        "directUrls": profile_urls,
        "resultsType": "details",
        "resultsLimit": 1,
    }
    run = _actor_call(client, run_input, f"profile batch ({len(usernames)} accounts)")
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


def is_business_account(item: dict) -> bool:
    """Return True if Apify marks this profile as a business or creator account."""
    if item.get("isBusinessAccount"):
        return True
    if item.get("businessCategoryName"):
        return True
    account_type = (item.get("accountType") or "").lower()
    return account_type in ("business", "creator")


def extract_profile(item: dict, source_hashtag: str) -> dict | None:
    username = (item.get("username") or item.get("ownerUsername") or "").strip().lstrip("@")
    if not username:
        return None

    raw_followers = item.get("followersCount")
    follower_count = safe_int(raw_followers) if raw_followers is not None else 0

    full_name = _sanitize_csv((item.get("fullName") or "").strip())
    bio = _sanitize_csv((item.get("biography") or "").replace("\n", " ").strip())
    profile_url = f"https://www.instagram.com/{username}/"

    return {
        "username": _sanitize_csv(username),
        "full_name": full_name,
        "follower_count": follower_count,
        "bio": bio,
        "profile_url": profile_url,
        "hashtag": source_hashtag,
    }


# ---------------------------------------------------------------------------
# Filtering / IO
# ---------------------------------------------------------------------------

def in_follower_range(profile: dict) -> bool:
    return MIN_FOLLOWERS <= profile["follower_count"] <= MAX_FOLLOWERS


def save_to_csv(profiles: list[dict], filepath: str, log_fn=None) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(profiles)
    _emit(f"Saved {len(profiles)} lead{'s' if len(profiles) != 1 else ''} to {filepath}", log_fn)


# ---------------------------------------------------------------------------
# Core pipeline — importable from the portal
# ---------------------------------------------------------------------------

def run_scraper(
    hashtags: list[str],
    max_results: int,
    output_file: str,
    token: str,
    on_status=None,
    stop_event=None,
) -> dict:
    """
    Run the full scraper pipeline.

    Args:
        hashtags:    List of hashtag strings (with or without #).
        max_results: Max posts to pull per hashtag.
        output_file: Path for the output CSV.
        token:       Apify API token.
        on_status:   Optional callable(msg: str) for live progress updates.
        stop_event:  Optional threading.Event; set it to request early termination.

    Returns:
        A summary dict with counts and the output file path.
    """
    def stopped() -> bool:
        return stop_event is not None and stop_event.is_set()

    log = lambda msg: _emit(msg, on_status)

    client = ApifyClient(token)
    hashtags = [h.lstrip("#") for h in hashtags]

    log(f"Searching {len(hashtags)} hashtag(s): {', '.join('#' + h for h in hashtags)}")
    log(f"Follower range: {MIN_FOLLOWERS:,} – {MAX_FOLLOWERS:,}")
    log(f"Max posts per hashtag: {max_results}")

    # ── Phase 1: collect usernames, tracking first-seen hashtag ──
    username_to_hashtag: dict[str, str] = {}

    for hashtag in hashtags:
        if stopped():
            log("Stop requested — skipping remaining hashtags.")
            break
        try:
            found = collect_usernames_for_hashtag(client, hashtag, max_results, on_status)
            for u in found:
                if u not in username_to_hashtag:
                    username_to_hashtag[u] = hashtag
        except Exception as exc:
            log(f"WARNING: failed to scrape #{hashtag}: {exc}")
        time.sleep(2)

    total_unique = len(username_to_hashtag)
    log(f"Total unique accounts across all hashtags: {total_unique}")

    if not username_to_hashtag:
        log("No accounts found. Check your hashtags and API token.")
        save_to_csv([], output_file, on_status)
        return {
            "hashtags_searched": len(hashtags),
            "unique_found": 0,
            "personal_skipped": 0,
            "business_found": 0,
            "follower_filtered": 0,
            "leads_saved": 0,
            "output_file": output_file,
        }

    # ── Phase 2: fetch full profile details in batches ──
    username_list = sorted(username_to_hashtag.keys())
    raw_profiles: list[dict] = []
    business_count = 0
    skipped_personal = 0

    total_batches = (len(username_list) + PROFILE_BATCH_SIZE - 1) // PROFILE_BATCH_SIZE

    for i in range(0, len(username_list), PROFILE_BATCH_SIZE):
        if stopped():
            log("Stop requested — saving partial results.")
            break
        batch = username_list[i: i + PROFILE_BATCH_SIZE]
        batch_num = i // PROFILE_BATCH_SIZE + 1
        log(f"Phase 2 — batch {batch_num}/{total_batches} ({len(batch)} accounts) ...")
        try:
            items = fetch_profiles_batch(client, batch)
            for item in items:
                if not is_business_account(item):
                    skipped_personal += 1
                    continue
                business_count += 1
                source_tag = username_to_hashtag.get(
                    (item.get("username") or "").lower(), hashtags[0]
                )
                profile = extract_profile(item, source_tag)
                if profile:
                    raw_profiles.append(profile)
        except Exception as exc:
            log(f"WARNING: profile batch {batch_num} failed: {exc}")
        time.sleep(2)

    # ── Filters + dedup ──
    follower_filtered = [p for p in raw_profiles if in_follower_range(p)]

    seen: set[str] = set()
    final: list[dict] = []
    for p in follower_filtered:
        if p["username"] not in seen:
            seen.add(p["username"])
            final.append(p)

    final.sort(key=lambda p: p["follower_count"], reverse=True)
    save_to_csv(final, output_file, on_status)

    summary = {
        "hashtags_searched": len(hashtags),
        "unique_found": total_unique,
        "personal_skipped": skipped_personal,
        "business_found": business_count,
        "follower_filtered": len(follower_filtered),
        "leads_saved": len(final),
        "output_file": output_file,
    }

    log(f"Done — {len(final)} leads saved to {output_file}.")
    return summary


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()
    token = os.environ.get("APIFY_API_TOKEN", "")
    validate_token(token)

    hashtags = [h.lstrip("#") for h in args.hashtags]
    summary = run_scraper(
        hashtags=hashtags,
        max_results=args.max_results,
        output_file=args.output,
        token=token,
    )

    print()
    print("=" * 50)
    print("  SUMMARY")
    print("=" * 50)
    print(f"  Hashtags searched      : {summary['hashtags_searched']}")
    print(f"  Unique accounts found  : {summary['unique_found']}")
    print(f"  Personal (skipped)     : {summary['personal_skipped']}")
    print(f"  Business/creator accts : {summary['business_found']}")
    print(f"  After follower filter  : {summary['follower_filtered']}"
          f"  ({MIN_FOLLOWERS:,}–{MAX_FOLLOWERS:,})")
    print(f"  Leads saved            : {summary['leads_saved']}")
    print(f"  Output file            : {summary['output_file']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
