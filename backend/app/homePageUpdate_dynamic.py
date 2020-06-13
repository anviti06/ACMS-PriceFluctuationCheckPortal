"""
    Dynamically Updating the Home Page whenever a new Product is added in the 'product' table.

"""

from flask import Blueprint, jsonify,redirect , url_for
from .models import db, Product
from flask_login import LoginManager,current_user, fresh_login_required,logout_user

prod_bp = Blueprint('prod_bp', __name__)

@prod_bp.route('/product' , methods = ['GET'])
@fresh_login_required
def get_product():
    data = []
    if(current_user.is_authenticated):
        product_list = Product.query.all()
        for prod in product_list:
            dict = {'pid' : prod.pid, 'name': prod.name, 'mrp': prod.mrp, 'price': prod.price , 'img_file': prod.img_file, 'slug': prod.slug, 'description': prod.description}
            data.append(dict)
        return jsonify(data)
    else:
        print("session expired")
        logout_user()
        return redirect(url_for('login_bp.signin'))

