"""
All Main Page routes are defined here

"""

from flask import Blueprint, render_template 
from flask_login import login_required, current_user

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/home')
def home():
    return ""

