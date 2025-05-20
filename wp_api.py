import os
import requests
from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

# --- Load credentials from environment or secrets.toml ---
WP_SITE = os.getenv("WP_SITE")
WP_APP_USER = os.getenv("WP_APP_USER")
WP_APP_PASS = os.getenv("WP_APP_PASSWORD")

# --- Base API helper ---
def wp_api_base():
    if not WP_SITE:
        raise ValueError("❌ WP_SITE not set in environment.")
    return urljoin(WP_SITE, "/wp-json/openai/v1/")

def _auth():
    if not WP_APP_USER or not WP_APP_PASS:
        raise ValueError("❌ WP credentials missing. Check environment.")
    return HTTPBasicAuth(WP_APP_USER, WP_APP_PASS)

# --- Publish Immediately ---
def publish_post(title, content, optimize=True, status='publish', categories=None, tags=None, image_url=None):
    """Publish a post immediately to WordPress."""
    payload = {
        "title": title,
        "content": content,
        "optimize": optimize,
        "status": status,
        "categories": categories or [],
        "tags": tags or [],
        "image_url": image_url,
    }
    resp = requests.post(
        urljoin(wp_api_base(), "publish"),
        auth=_auth(),
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()

# --- Optimize Existing Post ---
def optimize_post(post_id):
    """Send an existing post to GPT optimization endpoint."""
    resp = requests.post(
        urljoin(wp_api_base(), "optimize"),
        auth=_auth(),
        json={"post_id": post_id},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()

# --- Schedule Future Post ---
def schedule_post(title, content, date):
    """Schedule a WordPress post for later publication."""
    payload = {
        "title": title,
        "content": content,
        "date": date  # Format: "YYYY-MM-DD HH:MM:SS"
    }
    resp = requests.post(
        urljoin(wp_api_base(), "schedule"),
        auth=_auth(),
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()

# --- Save SERP Rank Tracker ---
def save_serp(post_id, rank):
    """Track the SERP rank of a published post."""
    resp = requests.post(
        urljoin(wp_api_base(), "serp"),
        auth=_auth(),
        json={"post_id": post_id, "rank": rank},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()
