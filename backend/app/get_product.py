from flask import Blueprint, jsonify, json
from .models import db, Product
prod_bp = Blueprint('prod_bp', __name__)

@prod_bp.route('/product' , methods = ['GET'])
def get_product():
    data = []
    product_list = Product.query.all()
    for prod in product_list:
        dict = {'pid' : prod.pid, 'name': prod.name, 'mrp': prod.mrp, 'price': prod.price , 'img_file': prod.img_file, 'slug': prod.slug, 'description': prod.description}
        data.append(dict)
    return jsonify(data)