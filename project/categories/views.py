from flask import request, jsonify, Blueprint
from .models import Category
from project import db

category = Blueprint('category', __name__, template_folder='templates')

@category.route('/categories', methods=['GET', 'POST'])
@category.route('/categories/<int:category_id>', methods=['GET', 'PUT', 'DELETE'])
def categories():
    if request.method == 'GET':
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories])
    elif request.method == 'POST':
        data = request.get_json()
        category = Category(name=data['name'], description=data['description'])
        db.session.add(category)
        db.session.commit()
        return jsonify(category.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        category.name = data['name']
        category.description = data['description']
        db.session.commit()
        return jsonify(category.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Deleted'})

# @app.route('/categories/<int:category_id>', methods=['GET', 'PUT', 'DELETE'])
# def category(category_id):
#     category = Category.query.get(category_id)
#     if category is None:
#         return jsonify({'error': 'Not found'}), 404
#     if request.method == 'GET':
#         return jsonify(category.to_dict())
#     elif request.method == 'PUT':
#         data = request.get_json()
#         category.name = data['name']
#         category.description = data['description']
#         db.session.commit()
#         return jsonify(category.to_dict())
#     elif request.method == 'DELETE':
#         db.session.delete(category)
#         db.session.commit()
#         return jsonify({'message': 'Deleted'})

