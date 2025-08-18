import pytest
from pages_api.users_api import UsersAPI
from tests.test_data import users_data

@pytest.fixture(scope="function")
def users_api():
    return UsersAPI()

def test_create_user_with_valid_data(users_api):
    resp = users_api.create_user(users_data.valid_user)
    assert resp.status_code == 200
    assert "inserted_id" in resp.json()

@pytest.mark.parametrize("payload", [
    users_data.invalid_user_missing_name,
    users_data.invalid_user_invalid_email,
    users_data.edge_case_empty_fields
])
def test_create_user_with_invalid_data(users_api, payload):
    resp = users_api.create_user(payload)
    assert resp.status_code == 422  # Expect validation error

def test_get_user_by_id(users_api):
    # Create user first
    create_resp = users_api.create_user(users_data.valid_user)
    user_id = create_resp.json()["inserted_id"]

    # Fetch same user
    fetch_resp = users_api.get_user_by_id(user_id)
    assert fetch_resp.status_code == 200
    assert fetch_resp.json()["name"] == users_data.valid_user["name"]
