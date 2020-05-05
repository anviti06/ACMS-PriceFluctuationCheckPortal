from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from main import User,db


login_bp = Blueprint('login_bp', __name__)


#LoginPortal#
@login_bp.route('/signin' , methods = ['POST' , 'GET'])
def signin():
    data = request.get_json()
    #print(data)
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
        
    if not user or not check_password_hash(user.password, password):
        #print("Error")
        return "Invalid credentials.Try again!"
    else:
        return "True"



#Register Portal#
@login_bp.route('/register')
def register():
    return render_template('register.html')

@login_bp.route('/signup', methods = ['POST' , 'GET'])
def signup():
    data = request.get_json()
    #print(data)
        
    email = data['email']
    password = data['password']
    name = data['name']
    phoneNo = data['phoneNumber']
        
    user = User.query.filter_by(email=email).first()

    if user:
        return "User already exists"

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), phoneNo = phoneNo)

    db.session.add(new_user)
    db.session.commit()
        
    return "True"


#Logout Portal#
@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    