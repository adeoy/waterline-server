from flask import Flask, request, jsonify
from flask_cors import CORS

from services.sales import SalesService
from services.deletedSales import DeletedSalesService

app = Flask(__name__)
cors = CORS(app, resources={r"/report/*": {"origins": "http://localhost:8100"}})


@app.route("/report/<string:tipo>/", methods=['POST'])
def report(tipo):
    if tipo == 'sales':
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'Nada que reportar'}), 400

        employee = data.get('employee', [])
        sales = data.get('sales', [])
        deleted_sales = data.get('deletedSales', [])
        if len(sales) == 0:
            return jsonify({'message': 'Nada que reportar'}), 400

        ss = SalesService()
        dss = DeletedSalesService()

        for sale in sales:
            sale['employee'] = employee
            ss.create_sale(sale)
        for deleted_sale in deleted_sales:
            deleted_sale['employee'] = employee
            dss.create_deleted_sale(deleted_sale)

        return jsonify({'message': 'Carga completa'}), 201
    else:
        return jsonify({'message': 'Carga desconocida'}), 404
