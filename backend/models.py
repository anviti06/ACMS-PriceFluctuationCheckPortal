from flask_login import UserMixin
from main import db

#Defining Databases
class User( UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phoneNo = db.Column(db.String(12))
    password = db.Column(db.String(40))
    notification = db.Column(db.String(10))

class Waitlist(db.Model):
    __tablename__ = 'waitlist'
    id = db.Column(db.Integer)
    pid = db.Column(db.Integer, primary_key = True)
    threshold = db.Column(db.Integer)

class  Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer)
    pid = db.Column(db.Integer, primary_key = True)

class Product(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    mrp = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img_file = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    description = db.Column(db.String(100))