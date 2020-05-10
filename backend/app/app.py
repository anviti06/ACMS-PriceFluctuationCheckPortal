
from flask import (Flask, render_template, request,Blueprint)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from apscheduler.schedulers.background import BackgroundScheduler

# Globally accessible libraries
db = SQLAlchemy()
scheduler = BackgroundScheduler(daemon=True)    


def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    
    #Importing Files
    from .models import User,Product,Waitlist
    from .notification import raise_notification

    #Forming user cookie - whenever we want we can use the currently working user as ' current_user '
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
        #Register Blueprint
        from .login import login_bp as login_blueprint
        app.register_blueprint(login_blueprint)

        from .home import home_bp as home_blueprint
        app.register_blueprint(home_blueprint)
        
        from .get_product import prod_bp as product_blueprint
        app.register_blueprint(product_blueprint)
            
        #db.create_all()
        return app
    
