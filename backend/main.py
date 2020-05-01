from flask import (Flask, render_template)
from flask_cors import CORS,cross_origin
from flask import request
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

app.run(debug=True,host='127.0.0.1',port=5000)
flask_cors.CORS(app, resources={ r'/*': {'origins': "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
