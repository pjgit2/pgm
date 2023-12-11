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

@app.route("/")
def home():
   data = db.child('items')
@app.route("/admin")
def admin():
  if 'user' in session:
    all_entries = db.child("data").get()
    return render_template("admin.html",all_entries=all_entries.val())
  return redirect('/login')

@app.route('/admin', methods=['GET', 'POST'])
def form():
   if request.method == 'POST':
      name = request.form.get("name")
      email = request.form.get("email")
      subject = request.form.get("subject")
      message = request.form.get("message")

      data = {
         "name": name,
         "student id": student id,
         "subject": subject,
         "task": task,
      }

      db.child("items").push(data)
      return redirect('/admin')
   
   data_list = db.child("items").get().val()
   return render_template('admin.html', data=data_list)


   @app.route("/login", methods=['GET', 'POST'])
   def login():
      if request.method == 'POST':
         session.pop("user", None)

         if request.form.get("pass") == 'password' and request.form.get("uname") == "mbsa":
            session['user'] = request.form.get('uname')
            return redirect("/admin")
         if 'user' in session:
            return redirect("/admin")
         return render_template("login.html")

if __name__ == '_main_':
  app.run(debug=True)



