import pyrebase
from flask import Flask, render_template, request, redirect ,g ,session,url_for

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

app.secret_key = "dgsgsfgggedg"

@app.route("/")
def home():
   data = db.child('items').get().val or {}
   return render_template('index.html', data=data)

@app.route("/admin")
def admin():
  if 'user' in session:
    data = db.child("items").get().val() or {}
    return render_template("admin.html",data=data)
  return redirect('/login')

@app.route("/login" ,methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop("user",None)

@app.route('/admin', methods=['GET', 'POST'])
def form():
   if request.method == 'POST':
      name = request.form.get("name")
      email = request.form.get("email")
      subject = request.form.get("subject")
      message = request.form.get("message")

      new_item = {
         "name": name,
         "email": email,
         "subject": subject,
         "message": message,
      }

      db.child("items").push(new_item)
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

@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit(item_id):
    if request.method == 'GET':
        item = db.child('items').child(item_id).get().val() or {}
        return render_template('edit.html', item=item)

    elif request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        updated_item = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }
        
        db.child('items').child(item_id).update(updated_item)

        return redirect(url_for('admin'))

if __name__ == '_main_':
  app.run(debug=True)



