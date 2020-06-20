from os import environ , path



class Config:

    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'ACMS'
    

    # Database
    SQLALCHEMY_DATABASE_URI = ''
    #environ.get('DB_CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


#EMAIL API CREDENTIALS
SENDGRID_API_KEY = ''
DEFAULT_MAIL = ''  #Sender Mail id - authenticated as sender email with SENDGRID

#MESSAGE API CREDENTIALS
TWILIO_ACCOUNT_SID =''
TWILIO_AUTH_TOKEN =''
PHONE_NO ='' #Twilio phone number from which you send message
DUMMY_PNO = '' #dummy phone number can be any registered number on which messages can be sent using TWILIO "TRIAL ACCOUNT"

key = Config.SECRET_KEY
