import pytest
import requests
from config import BASE_URL

@pytest.fixture(scope="session")
def api_client():
    """Provide a reusable requests session."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()

@pytest.fixture(scope="function")
def create_test_user(api_client):
    """Create a user before test, delete after test."""
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "address": "Test Address",
        "phone": "1234567890"
    }
    response = api_client.post(f"{BASE_URL}/users", json=payload)
    user_id = response.json()["inserted_id"]
    yield user_id
    api_client.delete(f"{BASE_URL}/users/{user_id}")  # Optional if delete route exists
