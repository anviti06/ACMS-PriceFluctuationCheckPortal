from flask import Flask,Blueprint, render_template, redirect, url_for, request, flash , jsonify, json
from flask_login import LoginManager,login_user, logout_user, login_required ,current_user
from .models import db,User
from .models import Product
from .models import Waitlist
from .app import db
from sqlalchemy import update



homepost_bp = Blueprint('homepost_bp', __name__)



@homepost_bp.route('/Home' , methods = ['POST' , 'GET'])
def homepost():
	if request.method =="POST":
		data = request.get_json()
		threshold = data['threshold']
		pid = data['pid']
		
		id= current_user.id

		prod = Product.query.filter_by(pid=pid).first()
		if threshold == "":
			return "enter a non-empty value!"
		else:
			lower = 0.3 * prod.mrp
			if int(threshold) >= lower and int(threshold) <= prod.mrp:
				qe = Waitlist.query.filter((Waitlist.id == id) , (Waitlist.pid == pid)).first()
				if qe is None:
					entry = Waitlist(id=id, pid=pid, threshold=threshold)
					db.session.add(entry)
					db.session.commit()
					return "True"
				else:
					return "You already have this item in your waitlist . Check your waitlist to edit threshold."
			else:
				return "Enter a value in range!"
	else:
		return render_template('index.html')
	
@homepost_bp.route('/customer',methods=['GET'])
def get_cart():
	id = current_user.id
	prod = []
	mylist = Waitlist.query.filter(Waitlist.id == id).all()

	if mylist:
		for pr in mylist:
			data = Product.query.filter(Product.pid == pr.pid).first()
			print("Current Wishlist items are: ")
			print("User id:" + id)
			print("product id:" + data.pid)
			print("product name:"+data.name)
			print("threshold:" + pr.threshold)

			#sending product as well as threshold details
			dict = {'pid':data.pid , 'name':data.name , 'mrp':data.mrp , 'price':data.price, 'img_file':data.img_file , 'slug': data.slug , 'description':data.description , 'threshold':pr.threshold}
			prod.append(dict)
		return jsonify(prod)
	else:
		return "No items in your list. Go to home to add items to your waitlits"

@homepost_bp.route('/wishlist',methods = ['GET','POST'])
def wishlist():
	data = request.get_json()
	id = current_user
	threshold = ""
	dele = ""
	pid = data['pid']
	if 'threshold' in data:
		#print('threshold request')
		threshold = data['threshold']
		print(threshold)
		prod = Waitlist.query.filter((Waitlist.id == id) , (Waitlist.pid == pid)).first()
		data = Product.query.filter_by(pid=prod.pid).first()
		if threshold == "":
			return "enter a non-empty value!"
		else:
			lower = 0.3 * data.mrp
			if int(threshold) >= lower and int(threshold) <= data.mrp:
				prod.threshold = threshold
				db.session.commit()
				return "True"
			else:
				return "enter a value in range!"

	if 'del' in data:
		print('delete request')
		
		prod = Waitlist.query.filter((Waitlist.id == id) , (Waitlist.pid == pid)).first()
		db.session.delete(prod)
		db.session.commit()
		return "True"
	
