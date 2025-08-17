from helpers.api_client import APIClient

class UsersAPI:
    """Page Object for /users API endpoints."""

    def __init__(self):
        self.client = APIClient()
        self.base_path = "/users"

    def create_user(self, payload):
        return self.client.post(self.base_path, json=payload)

    def get_all_users(self):
        return self.client.get(self.base_path)

    def get_user_by_id(self, user_id):
        return self.client.get(f"{self.base_path}/{user_id}")

    def update_user(self, user_id, payload):
        return self.client.put(f"{self.base_path}/{user_id}", json=payload)

    def delete_user(self, user_id):
        return self.client.delete(f"{self.base_path}/{user_id}")
