from flask import (Flask, render_template, request,Blueprint)
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, UserMixin
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask("__main__")

#Defining Global variables
scheduler = BackgroundScheduler()
db = SQLAlchemy(app)

#Defining App configurations
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
app.config['CORS_HEADERS'] = 'Content-Type'


#Registering Blueprints - For Home page
from home import home_bp as home_blueprint
app.register_blueprint(home_blueprint)
 
#Importing Databases
from models import *

#Registering Blueprints - For Login page
from login import login_bp as login_blueprint
app.register_blueprint(login_blueprint)

#Login Manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
app.run(debug=True,host='0.0.0.0',port=5000)

    

"""
@app.route("/")
def my_index():
    return render_template("index.html",token="Hello   world")
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

