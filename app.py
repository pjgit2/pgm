import pyrebase

config = {
  "apiKey": "AIzaSyCv4mI1d_S63C00yn_OPQiX8qwPQHQl_oc",
  "authDomain": "tesla-15857.firebaseapp.com",
  "databaseURL": "https://tesla-15857-default-rtdb.firebaseio.com",
  "projectId": "tesla-15857",
  "storageBucket": "tesla-15857.appspot.com",
  "messagingSenderId": "860727547248",
  "appId": "1:860727547248:web:01f4b44b9039cc9895abb5",
  "measurementId": "G-BPWDCB06B7"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#db.child("name").child("name").update({"name":"Paulu"})

from flask import *
from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def home():
  return "<h1> Welcome to the World of Flask Application Framework</h1>"

@app.route('/about')
def about():
  return "<h1> All about the Page</h1> 
          "<p> This Application was build under Flask Framework </p>"

if __name__=="__main__";
  app.run(debug=True)
