from helpers.api_client import APIClient

class OrdersAPI:
    """Page Object for /orders API endpoints."""

    def __init__(self):
        self.client = APIClient()
        self.base_path = "/orders"

    def create_order(self, payload):
        return self.client.post(self.base_path, json=payload)

    def get_all_orders(self):
        return self.client.get(self.base_path)

    def get_order_by_id(self, order_id):
        return self.client.get(f"{self.base_path}/{order_id}")

    def update_order(self, order_id, payload):
        return self.client.put(f"{self.base_path}/{order_id}", json=payload)

    def delete_order(self, order_id):
        return self.client.delete(f"{self.base_path}/{order_id}")
