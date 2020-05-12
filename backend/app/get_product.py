from flask import Blueprint, jsonify, json
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from .models import db, Product
from sqlalchemy import update
prod_bp = Blueprint('prod_bp', __name__)

@prod_bp.route('/product' , methods = ['GET'])
def get_product():
    data = []
    product_list = Product.query.all()
    for prod in product_list:
        dict = {'pid' : prod.pid, 'name': prod.name, 'mrp': prod.mrp, 'price': prod.price , 'img_file': prod.img_file, 'slug': prod.slug, 'description': prod.description}
        data.append(dict)
    return jsonify(data)
