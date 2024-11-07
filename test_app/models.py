# test_app/models.py
from .mongo_client import get_mongo_database

class DataSource:
    def __init__(self):
        self.db = get_mongo_database()
        self.collection = self.db["data_sources"]  # Collection name

    def create(self, data):
        """
        Inserts a new document into the data_sources collection.
        """
        result = self.collection.insert_one(data)
        return str(result.inserted_id)  # Convert ObjectId to string for readability

    def read(self, query=None):
        """
        Reads documents from the data_sources collection.
        """
        query = query or {}
        return list(self.collection.find(query))  # Convert cursor to list

    def update(self, query, data):
        """
        Updates a document in the data_sources collection.
        """
        result = self.collection.update_one(query, {"$set": data})
        return result.modified_count  # Returns number of documents updated

    def delete(self, query):
        """
        Deletes a document from the data_sources collection.
        """
        result = self.collection.delete_one(query)
        return result.deleted_count  # Returns number of documents deleted
