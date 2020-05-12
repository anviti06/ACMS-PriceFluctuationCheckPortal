from flask import (Flask, render_template)
from flask_cors import CORS,cross_origin
from flask import request
from flask import jsonify
app = Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html",token="Hello   world")
@app.route('/signup', methods = ['POST'])
def get_query_from_react():
    data=request.get_json()
    print(data)
    response="True"
    return response
@app.route('/signin', methods = ['POST'])
def get_from_react():
    data=request.get_json()
    print(data)
    response="True"
    return response
@app.route('/Home', methods = ['POST'])
def get_qfrom_react():
    data=request.get_json()
    print(data)
    response="True"
    return response
@app.route('/product', methods = ['GET'])
def get_react():
    data=[ 
    {
        "pid": 1,
        "name": "im d best",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    },
    {
        "pid": 2,
        "name": " World",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    },
    {
        "pid": 3,
        "name": "Hel World",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    },
    {
        "pid": 4,
        "name": "Hello World",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    },
    {
        "pid": 5,
        "name": "ibest",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    },
    {
        "pid": 6,
        "name": "Helhar",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    }
    ,
    {
        "pid": 7,
        "name": "Heljhj",
        "img_file": "learn",
        "mrp": "12-04-2017",
        "price": "hello-world",
        "description":"hi"
    }
]
    print(data)
    
    return jsonify(data)
app.run(debug=True,host='127.0.0.1',port=5000)
flask_cors.CORS(app, resources={ r'/*': {'origins': "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
