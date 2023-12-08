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
   if request.method == 'POST':
      name = request.form.get("name")
      email = request.form.get("email")
      subject = request.form.get("subject")
      message = request.form.get("message")

      data = {
         "name": name,
         "email": email,
         "subject": subject,
         "message": message,
      }

      db.child("data").push(data)
      return redirect('/')
   
   data_list = db.child("data").post().val()

@app.route('/form')
def show():
   return render_template('form.html')

if __name__ == '_main_':
  app.run(debug=True)



