from os import environ , path



class Config:

    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'ACMS'
    

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:acms_2021@database-1.ctsfs4q05mza.us-east-2.rds.amazonaws.com/ACMS'
    #environ.get('DB_CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


#EMAIL API CREDENTIALS
SENDGRID_API_KEY = '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'
DEFAULT_MAIL = 'sharmainaaya2@gmail.com'  #Sender Mail id - authenticated as sender email with SENDGRID

#MESSAGE API CREDENTIALS
TWILIO_ACCOUNT_SID ='AC9767ddfc3eee56535facea375a0790c0'
TWILIO_AUTH_TOKEN ='c7f19966d9c08db90407062fda6e2495'
PHONE_NO ='+12015810784' #Twilio phone number from which you send message
DUMMY_PNO = '' #dummy phone number can be any registered number on which messages can be sent using TWILIO "TRIAL ACCOUNT"

key = Config.SECRET_KEY