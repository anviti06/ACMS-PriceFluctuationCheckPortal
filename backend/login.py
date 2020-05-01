from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import *


login_bp = Blueprint('login_bp', __name__)


#SignInPortal#
@login_bp.route('/signin')
def signin():
    return "True"
@login_bp.route('/signin' , methods = ['POST'])
def signin_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('login_bp.signin'))

    


#Signup Portal#
@login_bp.route('/signup')
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        phoneNo = request.form.get('phoneNo')

        user = User.query.filter_by(email=email).first()

        if user:
            return redirect(url_for('login_bp.signup'))

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256') , phoneNo = phoneNo)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login_bp.signin'))


#Logout Portal#
@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_bp.home'))
