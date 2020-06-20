
"""
Entire code of database and table creation will be written here
"""
from flask_login import UserMixin
from .app import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    # attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phoneNo = db.Column(db.String(15))
    password = db.Column(db.String(40))
    isActive = db.Column(db.Boolean)
    # Relationships
    prods = db.relationship('Product', secondary='waitlist', backref=db.backref('user', lazy='dynamic'))


class Product(UserMixin, db.Model):
    __tablename__ = 'product'
    # attributes
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mrp = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img_file = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    description = db.Column(db.String(100))
    isActive = db.Column(db.Boolean)
    # Relationships
    users = db.relationship('User', secondary='waitlist', backref=db.backref('product', lazy='dynamic'))


class Waitlist(UserMixin, db.Model):
    __tablename__ = 'waitlist'
    # Attributes (Many-to-Many Mapping in this table)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), primary_key=True)
    threshold = db.Column(db.Integer)
    isActive = db.Column(db.Boolean)


