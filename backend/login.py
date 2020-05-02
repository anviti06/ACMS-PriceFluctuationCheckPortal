from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import *


login_bp = Blueprint('login_bp', __name__)


#SignInPortal#
@login_bp.route('/signin' , methods = ['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return "Invalid credentials.Try again!"

    


#Signup Portal#
@login_bp.route('/signup', methods = ['POST'])
def signup():
    data = request.get_json()
    print(data)
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    phoneNo = request.form.get('phoneNo')
    """
    user = User.query.filter_by(email=email).first()

    if user:
        return "User already exists"

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256') , phoneNo = phoneNo)

    db.session.add(new_user)
    db.session.commit()6
    """
    return "True"
    
#Logout Portal#
@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    
