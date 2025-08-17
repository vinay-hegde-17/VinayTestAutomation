import pytest
from pages_api.items_api import ItemsAPI
from tests.test_data import items_data

@pytest.fixture(scope="function")
def items_api():
    return ItemsAPI()

def test_create_item_with_valid_data(items_api):
    resp = items_api.create_item(items_data.valid_item)
    assert resp.status_code == 200
    assert "inserted_id" in resp.json()

@pytest.mark.parametrize("payload", [
    items_data.invalid_item_missing_name,
    items_data.invalid_item_negative_price
])
def test_create_item_with_invalid_data(items_api, payload):
    resp = items_api.create_item(payload)
    assert resp.status_code == 422
