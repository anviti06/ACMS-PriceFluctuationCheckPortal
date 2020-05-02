
from flask import Blueprint, render_template 
from flask_login import login_required, current_user

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    return render_template("index.html",token="Hello   world")

"""
@app.route('/signup', methods = ['POST'])
def get_query_from_react():
    data=request.get_json()
    print(data)
    response="Whatever you wish too return"
    return response
@app.route('/signin', methods = ['POST'])
def get_from_react():
    data=request.get_json()
    print(data)
    response="Whatever you wish too return"
    return response
"""
