from os import environ , path



class Config:

    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'ACMS'

    # Database
    SQLALCHEMY_DATABASE_URI = ''
    #environ.get('DB_CONNECTION_STRING') #
    # #'mysql://admin:acms_2021@database-1.ctsfs4q05mza.us-east-2.rds.amazonaws.com/ACMS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False #environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')



key = Config.SECRET_KEY