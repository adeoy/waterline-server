from services.base import BaseService


class SalesService(BaseService):
    def __init__(self):
        super().__init__('sales')
        
    def get_sales(self, query=None):
        return self._get_all_data(query)

    def get_sale(self, sale_id):
        return self._get_data(sale_id)

    def create_sale(self, sale):
        return self._create_data(sale)

    def update_sale(self, sale_id, sale):
        return self._update_data(sale_id, sale)

    def delete_sale(self, sale_id):
        return self._delete_data(sale_id)
