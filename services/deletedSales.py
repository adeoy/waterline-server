from services.base import BaseService


class DeletedSalesService(BaseService):
    def __init__(self):
        super().__init__('deleted_sales')

    def get_deleted_sales(self, query=None):
        return self._get_all_data(query)

    def get_deleted_sale(self, deleted_sale_id):
        return self._get_data(deleted_sale_id)

    def create_deleted_sale(self, deleted_sale):
        return self._create_data(deleted_sale)

    def update_deleted_sale(self, deleted_sale_id, deleted_sale):
        return self._update_data(deleted_sale_id, deleted_sale)

    def delete_deleted_sale(self, deleted_sale_id):
        return self._delete_data(deleted_sale_id)
