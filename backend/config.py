from os import environ , path



class Config:

    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'ACMS'

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
    #environ.get('DB_CONNECTION_STRING') #
    SQLALCHEMY_TRACK_MODIFICATIONS = False #environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')



key = Config.SECRET_KEY