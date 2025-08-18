import pytest
from pages_api.orders_api import OrdersAPI
from tests.test_data import orders_data

@pytest.fixture(scope="function")
def orders_api():
    return OrdersAPI()

def test_create_order_with_valid_data(orders_api):
    resp = orders_api.create_order(orders_data.valid_order)
    assert resp.status_code == 200
    assert "inserted_id" in resp.json()

@pytest.mark.parametrize("payload", [
    orders_data.invalid_order_missing_user,
    orders_data.invalid_order_empty_items
])
def test_create_order_with_invalid_data(orders_api, payload):
    resp = orders_api.create_order(payload)
    assert resp.status_code == 422
