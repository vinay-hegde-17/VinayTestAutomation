from helpers.api_client import APIClient

class ItemsAPI:
    """Page Object for /items API endpoints."""

    def __init__(self):
        self.client = APIClient()
        self.base_path = "/items"

    def create_item(self, payload):
        return self.client.post(self.base_path, json=payload)

    def get_all_items(self):
        return self.client.get(self.base_path)

    def get_item_by_id(self, item_id):
        return self.client.get(f"{self.base_path}/{item_id}")

    def update_item(self, item_id, payload):
        return self.client.put(f"{self.base_path}/{item_id}", json=payload)

    def delete_item(self, item_id):
        return self.client.delete(f"{self.base_path}/{item_id}")
