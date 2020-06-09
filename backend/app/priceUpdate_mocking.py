"""
    Manually updating the Price of a particular Product to Test working of Notification system.

"""
from flask import Blueprint ,request, render_template,redirect , url_for
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from .models import db, Product
from sqlalchemy import update

mock = Blueprint('mock', __name__)

@mock.route('/update/<int:product_pid>/<int:product_price>', methods = ['POST' , 'GET'])
@login_required
def update_price(product_pid,product_price):
    """ Updtaing the price of Product  - Permission (Admin Only)"""
    
    if request.method =="POST":
        if(current_user.email == "admin@acms.com" and check_password_hash(current_user.password, "!Admin123") ):
        
            prod = Product.query.filter_by(pid = product_pid).update(dict(price=product_price))
            db.session.commit()
            prod = Product.query.filter_by(pid = product_pid).first()
        
            if prod.price != product_price:    
                return "Error! Product Price could not be Updated"
            else:
                return "true"
        else: 
            return "Admin is only allowed to update price"
    elif request.method == "GET": 
        return redirect(url_for('homepost_bp.home'))