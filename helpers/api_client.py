#api_client.py
import requests
from tests.config import BASE_URL

class APIClient:
    """Reusable API client for making HTTP requests."""

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, **kwargs):
        """Send a GET request."""
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, json=None, **kwargs):
        """Send a POST request."""
        return self.session.post(f"{self.base_url}{endpoint}", json=json, **kwargs)

    def put(self, endpoint, json=None, **kwargs):
        """Send a PUT request."""
        return self.session.put(f"{self.base_url}{endpoint}", json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        """Send a DELETE request."""
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

    def close(self):
        """Close the HTTP session."""
        self.session.close()
