from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_shop.sqlite3'
db = SQLAlchemy(app)
CORS(app)

from project.categories.views import category
from project.products.views import product 

app.register_blueprint(product)
app.register_blueprint(category)

with app.app_context():
    db.create_all()