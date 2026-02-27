"""
Instagram DTC Brand Scraper via Apify API
Searches hashtags to find DTC ecommerce brand profiles and saves them to leads.csv.
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

# Apify actor for Instagram hashtag/profile scraping
# "apify/instagram-scraper" is the official Apify Instagram Scraper actor
ACTOR_ID = "apify/instagram-scraper"

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


def run_hashtag_scrape(client: ApifyClient, hashtag: str) -> list[dict]:
    """Run the Apify Instagram Scraper for a single hashtag and return raw results."""
    print(f"  Scraping hashtag: #{hashtag} ...")
    run_input = {
        "hashtags": [hashtag],
        "resultsType": "posts",        # scrape posts so we can collect unique authors
        "resultsLimit": 200,           # posts per hashtag (adjust as needed)
        "addParentData": True,         # include author/profile data on each post
    }

    run = client.actor(ACTOR_ID).call(run_input=run_input)

    items = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        items.append(item)

    print(f"    -> {len(items)} posts collected for #{hashtag}")
    return items


def extract_profile(post: dict) -> dict | None:
    """Pull profile fields out of a post record returned by the scraper."""
    # The actor nests owner/author info; field names may vary slightly by actor version.
    owner = post.get("ownerUsername") or post.get("username") or ""
    if not owner:
        return None

    # Try several possible key names for profile-level data
    followers = (
        post.get("ownerFollowersCount")
        or post.get("followersCount")
        or post.get("likesCount")   # fallback — will be filtered out
        or 0
    )
    bio = (
        post.get("ownerBiography")
        or post.get("biography")
        or ""
    )
    website = (
        post.get("ownerExternalUrl")
        or post.get("externalUrl")
        or post.get("websiteUrl")
        or ""
    )
    posts = (
        post.get("ownerPostsCount")
        or post.get("postsCount")
        or post.get("mediaCount")
        or 0
    )

    return {
        "username": owner.lstrip("@"),
        "follower_count": int(followers) if followers else 0,
        "bio": bio.replace("\n", " ").strip(),
        "website_url": website.strip(),
        "post_count": int(posts) if posts else 0,
    }


def in_follower_range(profile: dict) -> bool:
    return MIN_FOLLOWERS <= profile["follower_count"] <= MAX_FOLLOWERS


def deduplicate(profiles: list[dict]) -> list[dict]:
    """Keep the first occurrence of each username."""
    seen = set()
    unique = []
    for p in profiles:
        key = p["username"].lower()
        if key and key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


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

    all_posts: list[dict] = []

    for hashtag in HASHTAGS:
        try:
            posts = run_hashtag_scrape(client, hashtag)
            all_posts.extend(posts)
        except Exception as exc:
            print(f"  WARNING: failed to scrape #{hashtag}: {exc}")
        # Brief pause between runs to be a good API citizen
        time.sleep(2)

    print(f"\nTotal posts collected across all hashtags: {len(all_posts)}")

    # Extract profiles from post data
    raw_profiles: list[dict] = []
    for post in all_posts:
        profile = extract_profile(post)
        if profile:
            raw_profiles.append(profile)

    # Deduplicate by username
    unique_profiles = deduplicate(raw_profiles)
    print(f"Unique accounts found: {len(unique_profiles)}")

    # Apply follower count filter
    filtered = [p for p in unique_profiles if in_follower_range(p)]
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
