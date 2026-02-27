"""
Instagram DTC Brand Scraper via Apify API
Searches hashtags to find DTC ecommerce brand profiles and saves them to leads.csv.

Two-phase approach:
  Phase 1 — Scrape hashtag posts to collect unique author usernames.
  Phase 2 — Scrape each profile URL for full details (followers, bio, website, etc.).
"""

import csv
import os
import time
import sys
from apify_client import ApifyClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

APIFY_API_TOKEN = os.environ.get("APIFY_API_TOKEN", "")

# Hashtags to search (without the # symbol)
HASHTAGS = [
    "dtcbrand",
    "skincare",
    "supplements",
    "fitness",
]

# Follower count filter range
MIN_FOLLOWERS = 5_000
MAX_FOLLOWERS = 500_000

OUTPUT_FILE = "leads.csv"

# Official Apify Instagram Scraper actor
ACTOR_ID = "apify/instagram-scraper"

# How many profile URLs to pass to the actor in one batch.
# Keeps individual runs from timing out on very large username sets.
PROFILE_BATCH_SIZE = 50

CSV_FIELDS = ["username", "follower_count", "bio", "website_url", "post_count"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def validate_token(token: str) -> None:
    if not token:
        print(
            "ERROR: APIFY_API_TOKEN environment variable is not set.\n"
            "Export your token before running:\n"
            "  export APIFY_API_TOKEN='your_token_here'"
        )
        sys.exit(1)


def safe_int(value) -> int:
    """Convert a value to int, returning 0 on any failure."""
    # FIX 6: unsafe int() calls previously had no error handling.
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _actor_call(client: ApifyClient, run_input: dict, context: str) -> dict:
    """
    Call an Apify actor and return the run object.
    FIX 3: actor.call() can return None on failure; raise explicitly instead of
    letting a later KeyError/TypeError obscure the real problem.
    """
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise RuntimeError(f"Apify actor run returned None ({context}). "
                           "Check your API token and actor ID.")
    return run


# ---------------------------------------------------------------------------
# Phase 1: collect usernames from hashtag posts
# ---------------------------------------------------------------------------

def collect_usernames_for_hashtag(client: ApifyClient, hashtag: str) -> set[str]:
    """
    Scrape posts for a hashtag and return the set of unique author usernames.

    FIX 1 & 2: The original code passed 'addParentData=True' (not a real field)
    and expected full profile fields (ownerFollowersCount etc.) to appear on post
    records — they don't. We now only extract the username here and fetch full
    profile data in Phase 2.
    """
    print(f"  Phase 1 — scraping posts for #{hashtag} ...")
    run_input = {
        "hashtags": [hashtag],
        "resultsType": "posts",
        "resultsLimit": 200,
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
    """
    Scrape full profile details for a batch of usernames.
    Uses resultsType='details' on direct profile URLs to get follower count,
    biography, external URL, and post count.
    """
    profile_urls = [f"https://www.instagram.com/{u}/" for u in usernames]
    run_input = {
        "directUrls": profile_urls,
        "resultsType": "details",
        "resultsLimit": 1,
    }

    run = _actor_call(client, run_input, f"profile batch ({len(usernames)} accounts)")

    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


def extract_profile(item: dict) -> dict | None:
    """
    Build a clean profile dict from a 'details' result item.

    FIX 4 & 5: The original code used 'or' chains which silently skip a value
    of 0 (falsy), and fell back to 'likesCount' (a post metric) as a follower
    count proxy. We now use explicit 'is not None' checks and remove the
    likesCount fallback entirely.
    """
    username = (item.get("username") or item.get("ownerUsername") or "").strip()
    if not username:
        return None

    raw_followers = item.get("followersCount")
    follower_count = safe_int(raw_followers) if raw_followers is not None else 0

    raw_posts = item.get("postsCount")
    post_count = safe_int(raw_posts) if raw_posts is not None else 0

    bio = (item.get("biography") or "").replace("\n", " ").strip()
    website_url = (item.get("externalUrl") or "").strip()

    return {
        "username": username.lstrip("@"),
        "follower_count": follower_count,
        "bio": bio,
        "website_url": website_url,
        "post_count": post_count,
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
    print(f"\nSaved {len(profiles)} profiles to {filepath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    validate_token(APIFY_API_TOKEN)

    client = ApifyClient(APIFY_API_TOKEN)

    # ---- Phase 1: collect unique usernames across all hashtags ----
    all_usernames: set[str] = set()

    for hashtag in HASHTAGS:
        try:
            usernames = collect_usernames_for_hashtag(client, hashtag)
            all_usernames |= usernames
        except Exception as exc:
            print(f"  WARNING: failed to scrape #{hashtag}: {exc}")
        time.sleep(2)

    print(f"\nTotal unique accounts across all hashtags: {len(all_usernames)}")

    if not all_usernames:
        print("No accounts found. Check your hashtags and API token.")
        save_to_csv([], OUTPUT_FILE)
        return

    # ---- Phase 2: fetch full profile details in batches ----
    username_list = sorted(all_usernames)
    raw_profiles: list[dict] = []

    for i in range(0, len(username_list), PROFILE_BATCH_SIZE):
        batch = username_list[i : i + PROFILE_BATCH_SIZE]
        batch_num = i // PROFILE_BATCH_SIZE + 1
        total_batches = (len(username_list) + PROFILE_BATCH_SIZE - 1) // PROFILE_BATCH_SIZE
        print(f"  Phase 2 — fetching profile details "
              f"(batch {batch_num}/{total_batches}, {len(batch)} accounts) ...")
        try:
            items = fetch_profiles_batch(client, batch)
            for item in items:
                profile = extract_profile(item)
                if profile:
                    raw_profiles.append(profile)
        except Exception as exc:
            print(f"  WARNING: profile batch {batch_num} failed: {exc}")
        time.sleep(2)

    print(f"Profile details retrieved: {len(raw_profiles)}")

    # ---- Filter by follower count ----
    filtered = [p for p in raw_profiles if in_follower_range(p)]
    print(
        f"Accounts after follower filter "
        f"({MIN_FOLLOWERS:,} – {MAX_FOLLOWERS:,}): {len(filtered)}"
    )

    if not filtered:
        print(
            "No accounts matched the filter criteria. "
            "Try broadening the hashtag list or adjusting the follower range."
        )
        save_to_csv([], OUTPUT_FILE)
        return

    # Sort by follower count descending for easy review
    filtered.sort(key=lambda p: p["follower_count"], reverse=True)

    save_to_csv(filtered, OUTPUT_FILE)


if __name__ == "__main__":
    main()
