"""
Instagram DTC Brand Scraper via Apify API
Searches hashtags to find DTC ecommerce brand profiles and saves them to leads.csv.

Two-phase approach:
  Phase 1 — Scrape hashtag posts to collect unique author usernames.
  Phase 2 — Scrape each profile URL for full details (followers, bio, etc.)
             and filter to business/brand accounts only.

Usage:
  python instagram_dtc_scraper.py
  python instagram_dtc_scraper.py --hashtags dtcbrand shopify ecommerce --max-results 100
  python instagram_dtc_scraper.py --output my_leads.csv
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
# Defaults (all overridable via CLI)
# ---------------------------------------------------------------------------

DEFAULT_HASHTAGS = ["dtcbrand", "shopifybrand", "ecommerce"]
MIN_FOLLOWERS = 5_000
MAX_FOLLOWERS = 500_000
DEFAULT_OUTPUT = "leads.csv"
DEFAULT_MAX_RESULTS = 200

ACTOR_ID = "apify/instagram-scraper"
PROFILE_BATCH_SIZE = 50

CSV_FIELDS = ["username", "full_name", "follower_count", "bio", "profile_url", "hashtag"]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scrape Instagram for DTC brand accounts via Apify.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument(
        "--hashtags",
        nargs="+",
        default=DEFAULT_HASHTAGS,
        metavar="TAG",
        help="Hashtags to search (without #).",
    )
    p.add_argument(
        "--max-results",
        type=int,
        default=DEFAULT_MAX_RESULTS,
        metavar="N",
        help="Max posts to scrape per hashtag.",
    )
    p.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        metavar="FILE",
        help="Output CSV file path.",
    )
    return p.parse_args()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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
    client: ApifyClient, hashtag: str, max_results: int
) -> set[str]:
    print(f"  Phase 1 — scraping posts for #{hashtag} ...")
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

    print(f"    -> {len(usernames)} unique accounts found for #{hashtag}")
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
    # Some actor versions expose accountType: "Business" / "Creator" / "Personal"
    account_type = (item.get("accountType") or "").lower()
    return account_type in ("business", "creator")


def extract_profile(item: dict, source_hashtag: str) -> dict | None:
    username = (item.get("username") or item.get("ownerUsername") or "").strip().lstrip("@")
    if not username:
        return None

    raw_followers = item.get("followersCount")
    follower_count = safe_int(raw_followers) if raw_followers is not None else 0

    full_name = (item.get("fullName") or "").strip()
    bio = (item.get("biography") or "").replace("\n", " ").strip()
    profile_url = f"https://www.instagram.com/{username}/"

    return {
        "username": username,
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


def save_to_csv(profiles: list[dict], filepath: str) -> None:
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(profiles)
    print(f"Saved {len(profiles)} lead{'s' if len(profiles) != 1 else ''} to {filepath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()

    token = os.environ.get("APIFY_API_TOKEN", "")
    validate_token(token)

    client = ApifyClient(token)

    # Strip any leading # the user may have included
    hashtags = [h.lstrip("#") for h in args.hashtags]

    print(f"\nSearching {len(hashtags)} hashtag(s): {', '.join('#' + h for h in hashtags)}")
    print(f"Follower range: {MIN_FOLLOWERS:,} – {MAX_FOLLOWERS:,}")
    print(f"Max posts per hashtag: {args.max_results}\n")

    # ---- Phase 1: collect usernames, tracking first-seen hashtag ----
    # username -> first hashtag it was discovered under
    username_to_hashtag: dict[str, str] = {}

    for hashtag in hashtags:
        try:
            found = collect_usernames_for_hashtag(client, hashtag, args.max_results)
            for u in found:
                if u not in username_to_hashtag:
                    username_to_hashtag[u] = hashtag
        except Exception as exc:
            print(f"  WARNING: failed to scrape #{hashtag}: {exc}")
        time.sleep(2)

    total_unique = len(username_to_hashtag)
    print(f"\nTotal unique accounts across all hashtags: {total_unique}")

    if not username_to_hashtag:
        print("No accounts found. Check your hashtags and API token.")
        save_to_csv([], args.output)
        return

    # ---- Phase 2: fetch full profile details in batches ----
    username_list = sorted(username_to_hashtag.keys())
    raw_profiles: list[dict] = []
    business_count = 0
    skipped_personal = 0

    total_batches = (len(username_list) + PROFILE_BATCH_SIZE - 1) // PROFILE_BATCH_SIZE

    for i in range(0, len(username_list), PROFILE_BATCH_SIZE):
        batch = username_list[i: i + PROFILE_BATCH_SIZE]
        batch_num = i // PROFILE_BATCH_SIZE + 1
        print(
            f"  Phase 2 — fetching profile details "
            f"(batch {batch_num}/{total_batches}, {len(batch)} accounts) ..."
        )
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
            print(f"  WARNING: profile batch {batch_num} failed: {exc}")
        time.sleep(2)

    # ---- Apply follower range filter ----
    follower_filtered = [p for p in raw_profiles if in_follower_range(p)]

    # ---- Deduplicate (shouldn't happen, but be safe) ----
    seen: set[str] = set()
    final: list[dict] = []
    for p in follower_filtered:
        if p["username"] not in seen:
            seen.add(p["username"])
            final.append(p)

    # Sort by follower count descending for easy review
    final.sort(key=lambda p: p["follower_count"], reverse=True)

    save_to_csv(final, args.output)

    # ---- Summary ----
    print()
    print("=" * 50)
    print("  SUMMARY")
    print("=" * 50)
    print(f"  Hashtags searched      : {len(hashtags)}")
    print(f"  Unique accounts found  : {total_unique}")
    print(f"  Personal (skipped)     : {skipped_personal}")
    print(f"  Business/creator accts : {business_count}")
    print(
        f"  After follower filter  : {len(follower_filtered)}"
        f"  ({MIN_FOLLOWERS:,}–{MAX_FOLLOWERS:,})"
    )
    print(f"  Leads saved            : {len(final)}")
    print(f"  Output file            : {args.output}")
    print("=" * 50)


if __name__ == "__main__":
    main()
