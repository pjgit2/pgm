import pyrebase
from flask import Flask, render_template, request

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

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    

@app.route('/show')
def show():
   return render_template('show.html')

if __name__ == '_main_':
  app.run(host='0.0.0.0', port='8080')



