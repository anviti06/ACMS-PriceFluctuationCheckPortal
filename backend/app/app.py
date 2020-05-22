
from flask import (Flask, render_template, request,Blueprint, session)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from datetime import timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# Globally accessible libraries
db = SQLAlchemy()
scheduler = BackgroundScheduler(daemon=True)    


def create_app():
    
    app = Flask(__name__, instance_relative_config=False,template_folder='../templates', static_folder='../static')
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
    login_manager.refresh_view = 'relogin'
    login_manager.needs_refresh_message = (u"Session timedout, please login again")
    login_manager.needs_refresh_message_category = "info"


    @app.before_request
    def before_request():
        app.permanent_session_lifetime = timedelta(seconds =10)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    """
        Initializing Scheduler Function 
    """
    with app.app_context():
        def check_price():
            with app.app_context():

                waitlist_table = Waitlist.query.all()
                for row in waitlist_table:
                    temp_product = Product.query.filter_by(pid = row.pid).first()
                    #print(temp_product.name)
                    if(temp_product and temp_product.price <= row.threshold):
                        #print("Found product")
                        if (raise_notification(row.id , temp_product.pid)):
                            #If Notifiaction Func has been called for particular product then deleting it from waitlist table
                            db.session.delete(row)
                            db.session.commit()
                    #else: 
                        #print("Scheduler Working")
                    #else:
                        #print("Not Found")
            return




        #Register Blueprint
        from .login import login_bp as login_blueprint
        app.register_blueprint(login_blueprint)

        from .home import home_bp as home_blueprint
        app.register_blueprint(home_blueprint)
          
        from .homePageUpdate_dynamic import prod_bp as product_blueprint
        app.register_blueprint(product_blueprint)
        
        from .priceUpdate_mocking import mock as mock_blueprint
        app.register_blueprint(mock_blueprint)
        

        #Initializing Scheduler - event will occur every 30 seconds
        scheduler.add_job(check_price, 'interval', seconds = 30)          
        scheduler.start()
        
        #db.create_all()
        return app
    
