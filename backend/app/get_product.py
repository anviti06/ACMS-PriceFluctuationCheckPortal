from flask import Blueprint, jsonify, json,redirect , url_for
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

@prod_bp.route('/update/<int:product_pid>/<int:product_price>', methods = ['POST' , 'GET'])
@login_required
def update_price(product_pid,product_price):
    product_pid = int(product_pid)
    """ Updtaing the price of Product  - Permission (Admin Only)"""
    if(current_user.email == "admin@acms.com" and check_password_hash(current_user.password, "acms") ):
        #prod = Product.query.filter_by(pid = product_pid).first()
        prod = Product.query.filter_by(pid = product_pid).update(dict(price=product_price))
        #prod.price = product_price
        db.session.commit()
        prod = Product.query.filter_by(pid = product_pid).first()
        if prod.price != product_price:    
            return "Error! Product Price could not be Updated"
        else:
            #print("Update done")
            return True
    else: 
        return "Admin is only allowed to update price"