from flask import request, jsonify, Blueprint
from .models import Product
from project import db

product = Blueprint('product', __name__, template_folder='templates')

@product.route('/products', methods=['GET', 'POST'])
@product.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def products():
    if request.method == 'GET':
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])
    elif request.method == 'POST':
        data = request.get_json()
        product = Product(name=data['name'], description=data['description'], category_id=data['category_id'])
        db.session.add(product)
        db.session.commit()
        return jsonify(product.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        product.name = data['name']
        product.description = data['description']
        product.category_id = data['category_id']
        db.session.commit()
        return jsonify(product.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Deleted'})

# @app.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
# def product(product_id):
#     product = Product.query.get(product_id)
#     if product is None:
#         return jsonify({'error': 'Not found'}), 404
#     if request.method == 'GET':
#         return jsonify(product.to_dict())
#     elif request.method == 'PUT':
#         data = request.get_json()
#         product.name = data['name']
#         product.description = data['description']
#         product.category_id = data['category_id']
#         db.session.commit()
#         return jsonify(product.to_dict())
#     elif request.method == 'DELETE':
#         db.session.delete(product)
#         db.session.commit()
#         return jsonify({'message': 'Deleted'})


