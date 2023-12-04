from flask iport Flask

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
