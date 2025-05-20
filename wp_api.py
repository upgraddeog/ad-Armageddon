import os
import requests
from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

WP_SITE      = os.getenv('WP_SITE')
WP_APP_USER  = os.getenv('WP_APP_USER')
WP_APP_PASS  = os.getenv('WP_APP_PASSWORD')

def wp_api_base():
    return urljoin(WP_SITE, "/wp-json/openai/v1/")

def _auth():
    return HTTPBasicAuth(WP_APP_USER, WP_APP_PASS)

def publish_post(title, content, optimize=True, status='publish',
                categories=None, tags=None, image_url=None):
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

def optimize_post(post_id):
    resp = requests.post(
        urljoin(wp_api_base(), "optimize"),
        auth=_auth(),
        json={"post_id": post_id},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()

def schedule_post(title, content, date):
    payload = {
        "title": title,
        "content": content,
        "date": date  # "YYYY-MM-DD HH:MM:SS"
    }
    resp = requests.post(
        urljoin(wp_api_base(), "schedule"),
        auth=_auth(),
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()

def save_serp(post_id, rank):
    resp = requests.post(
        urljoin(wp_api_base(), "serp"),
        auth=_auth(),
        json={"post_id": post_id, "rank": rank},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()
