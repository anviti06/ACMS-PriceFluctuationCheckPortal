from flask import (Flask, render_template, request,Blueprint)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, UserMixin, login_required, logout_user
from apscheduler.schedulers.background import BackgroundScheduler
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask("__main__")

#Defining Global variables
scheduler = BackgroundScheduler()
db = SQLAlchemy(app)

#Registering Blueprints - For Home page routes
from home import home_bp as home_blueprint
app.register_blueprint(home_blueprint)


#Importing Database - User
class User( UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phoneNo = db.Column(db.String(12))
    password = db.Column(db.String(40))
    notification = db.Column(db.String(10))


#Defining App configurations
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'


#Login Manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 


"""
    
    Signin/SignUp Routes

"""

@app.route('/signin' , methods = ['POST' , 'GET'])
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

    
#Signup Portal#
@app.route('/signup', methods = ['POST' , 'GET'])
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
@app.route('/logout')
@login_required
def logout():
    logout_user()










    
app.run(debug=True,host='0.0.0.0',port=5000)

    

