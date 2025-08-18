#db_utils.py
from pymongo import MongoClient
from tests.config import MONGO_URL, MONGO_DB_NAME

class DBUtils:
    """Database utility functions for MongoDB."""

    def __init__(self, mongo_url=MONGO_URL, db_name=MONGO_DB_NAME):
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]

    def clear_collection(self, collection_name):
        """Delete all documents from a collection."""
        result = self.db[collection_name].delete_many({})
        return result.deleted_count

    def find_document(self, collection_name, query):
        """Find a single document by query."""
        return self.db[collection_name].find_one(query)

    def insert_document(self, collection_name, document):
        """Insert a document into a collection."""
        return self.db[collection_name].insert_one(document).inserted_id

    def close(self):
        """Close DB connection."""
        self.client.close()
