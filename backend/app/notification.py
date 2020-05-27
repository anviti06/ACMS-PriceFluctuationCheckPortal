"""
Functions for Notification system

"""
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
from .models import Product,User
from config import SENDGRID_API_KEY , DEFAULT_MAIL ,TWILIO_ACCOUNT_SID ,TWILIO_AUTH_TOKEN ,PHONE_NO

def send_mail(prod ,user):
    message = Mail(
        from_email=DEFAULT_MAIL,
        to_emails=user.email,
        subject='Price Fluctuation Notification',
        html_content=('Hey <strong>' + str(user.name) + '!</strong><br> Price for <strong>'+str(prod.name)
                      +'</strong> is as per your requirement !<br> Grab the opportunity NOW!!<br><br>https://www.amazon.in'))
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return True
    except Exception as e:
        print(e.to_dict)
        return False


def send_sms(prod,user):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            to='+918368311499',
            from_=PHONE_NO,
            body=("HEY " + str(user.name) +"! You can now buy "
                 + str(prod.name) + "!! Click on the link: https://www.amazon.in")
        )
        #print(message.sid)
        return True
    except Exception as e:
        print(e)
        return False


def raise_notification(id,pid):
    """
    If Notification send - return True
    else return False
    """
    user = User.query.get(id)
    product = Product.query.get(pid)
    print("Customer id :", id)
    print("Product id is :", pid)

    if user.phoneNo:
        return send_sms(product, user)
    return send_mail(product, user)
