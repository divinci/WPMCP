import os
from typing import Any, Dict

import requests

BASE_URL = os.getenv("WP_BASE_URL")
API_KEY = os.getenv("WP_API_KEY")

if not BASE_URL:
    raise EnvironmentError("WP_BASE_URL environment variable not set")


def _request(method: str, endpoint: str, json: Dict[str, Any] | None = None):
    url = f"{BASE_URL.rstrip('/')}/wp-json/wp/v2/{endpoint.lstrip('/')}"
    headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
    response = requests.request(method.upper(), url, json=json, headers=headers)
    response.raise_for_status()
    return response.json()


def list_posts():
    return _request("GET", "posts")


def create_post(title: str, content: str, status: str = "draft"):
    data = {"title": title, "content": content, "status": status}
    return _request("POST", "posts", json=data)
