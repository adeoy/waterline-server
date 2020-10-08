from lib.mongo import MongoLib


class BaseService:
    mongo_db = MongoLib()

    def __init__(self, collection):
        self.collection = collection

    def _get_all_data(self, query=None):
        if query is None:
            query = {}
        data = self.mongo_db.get_all(self.collection, query)
        return data or []

    def _get_data(self, category_id):
        data = self.mongo_db.get(self.collection, category_id)
        return data or {}

    def _create_data(self, data):
        created_id = self.mongo_db.create(self.collection, data)
        return created_id

    def _update_data(self, data_id, data):
        updated_id = self.mongo_db.update(self.collection, data_id, data)
        return updated_id

    def _delete_data(self, data_id):
        self.mongo_db.delete(self.collection, data_id)
        return data_id
