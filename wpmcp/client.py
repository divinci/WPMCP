import requests
from typing import Any, Dict, Optional


class WordPressClient:
    """Simple wrapper for the WordPress REST API."""

    def __init__(self, base_url: str, token: Optional[str] = None) -> None:
        """Initialize the client with a base URL and optional auth token."""
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        """Send an HTTP request and return the raw response."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    def get(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        """Perform a GET request and return the parsed JSON data."""
        response = self._request("GET", endpoint, **kwargs)
        return response.json()

    def post(self, endpoint: str, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """Perform a POST request with JSON data and return the parsed response."""
        response = self._request("POST", endpoint, json=data, **kwargs)
        return response.json()

    def put(self, endpoint: str, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """Perform a PUT request with JSON data and return the parsed response."""
        response = self._request("PUT", endpoint, json=data, **kwargs)
        return response.json()

    def delete(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        """Perform a DELETE request and return the parsed JSON data."""
        response = self._request("DELETE", endpoint, **kwargs)
        return response.json()
