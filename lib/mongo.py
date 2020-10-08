import pymongo
from bson import ObjectId
import os

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

if not DB_USER:
    MONGO_URI = f'mongodb://localhost:27017/{DB_NAME}'
else:
    MONGO_URI = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true&w=majority'


class MongoLib:
    connection = None

    def __init__(self):
        self.db_name = DB_NAME

    def connect(self):
        if MongoLib.connection is None:
            client = pymongo.MongoClient(MONGO_URI)
            MongoLib.connection = client[self.db_name]
            print('Connected to MongoDB')
        return MongoLib.connection

    def get_all(self, collection, query):
        self.connect()
        return self.connection[collection].find(query)

    def get(self, collection, _id):
        self.connect()
        return self.connection[collection].find_one({'_id': ObjectId(_id)})

    def create(self, collection, data):
        self.connect()
        return self.connection[collection].insert_one(data).inserted_id

    def update(self, collection, _id, data):
        self.connect()
        return self.connection[collection].update_one(
            {'_id': ObjectId(_id)},
            {'$set': data},
            upsert=True).upserted_id or _id

    def delete(self, collection, _id):
        self.connect()
        return self.connection[collection].delete_one({'_id': ObjectId(_id)})

    def update_custom(self, collection, query, data):
        self.connect()
        return self.connection[collection].update_one(
            query,
            {'$set': data},
            upsert=True).upserted_id

    def get_custom(self, collection, query):
        self.connect()
        return self.connection[collection].find_one(query)
