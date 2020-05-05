from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, UserMixin
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)


#Defining Global variables
scheduler = BackgroundScheduler()
db = SQLAlchemy(app)


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
    

#Importing Databases
from models import User, Product, Waitlist,Notification

#Scheduler functions
#from schedule import check_price

#Initializing Scheduler
#scheduler.add_job(check_price, 'interval', seconds=5)          
#scheduler.start()

#Registering Blueprints - For routes
from login import login_bp as login_blueprint
from home import main_bp as main_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(login_blueprint)

  
app.run(debug=True,host='0.0.0.0',port=5000)
