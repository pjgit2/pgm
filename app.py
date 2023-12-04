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

#db.child("name").child("name").update({"name":"Paulu"})


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name =  request.form['name']
            db.child("todo").push(name)
            todo = db.child("todo").get()
            to = todo.val()
            return render_template('index.html',t=to.values())
        elif request.form['submit'] == 'delete':
            db.child("todo").remove()
            return render_template('index.html')
        return render.template('index.html')

#if __name__ == '__main__':
  # app.run(debug=true)

if __name__ == '_main_':
  app.run(host='0.0.0.0', port='8080')

@app.route('/show')
def show():
  
  


