
from flask import (Flask, render_template, request,Blueprint,session , redirect , url_for)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import timedelta
import datetime
# Globally accessible libraries
db = SQLAlchemy()
scheduler = BackgroundScheduler(daemon=True)    


def create_app():
    
    app = Flask(__name__, instance_relative_config=False,template_folder='../templates', static_folder='../static')
    app.config.from_object('config.Config')
   
    #Session Management - Session Expires after every 30 min
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds = 10)
   
    # Initialize Plugins
    db.init_app(app)
    
    
    #Importing Files
    from .models import User,Product,Waitlist
    from .notification import raise_notification

    #Forming user cookie - whenever we want we can use the currently working user as ' current_user '
    login_manager = LoginManager()
    login_manager.login_view = 'login_bp.signin'
    login_manager.init_app(app)
    login_manager.refresh_view = 'login_bp.signin'
    login_manager.refresh_message = (u"Session timedout, please login again")
    
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
                    if(temp_product and temp_product.price <= row.threshold):
                        if (raise_notification(row.id , temp_product.pid)):
                            #If Notifiaction Func has been called for particular product then deleting it from waitlist table
                            temp_product.isActive = False
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

        from .homepost import homepost_bp
        app.register_blueprint(homepost_bp)
        

        #Initializing Scheduler - event will occur every 30 seconds
        scheduler.add_job(check_price, 'interval', seconds = 30)          
        
        scheduler.start()
        

        #Error Handler
        """
        @app.errorhandler(500)
        def internal_error(exception):
            app.logger.error(exception)
            return redirect(url_for(login_bp.signin))
        
        """
        #db.create_all()
        return app
        
