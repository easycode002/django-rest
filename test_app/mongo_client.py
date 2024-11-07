# test_app/mongo_client.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from django.conf import settings

def get_mongo_client():
    client = MongoClient(
        host=settings.MONGO_DB["HOST"],
        port=settings.MONGO_DB["PORT"],
        username=settings.MONGO_DB["USERNAME"],
        password=settings.MONGO_DB["PASSWORD"],
        authSource=settings.MONGO_DB["AUTH_SOURCE"],
        authMechanism=settings.MONGO_DB["AUTH_MECHANISM"]
    )
    # Connection check
    try:
        client.admin.command('ping')
        print("MongoDB connection successful.")
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")
    return client

def get_mongo_database():
    client = get_mongo_client()
    db = client[settings.MONGO_DB["NAME"]]
    try:
        db.list_collection_names()  # Connection check by listing collections
        print("Connected to MongoDB database successfully.")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB database: {e}")
    return db