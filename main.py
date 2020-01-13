from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def getIndex():
  return "<h1><a href='/about'>Edžus Kivilands</a></h1>"

@app.route("/about")
def getAbout():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html",phone=28834050)

@app.route("/home")
def home():
  return render_template("home.html")

app.run(host="0.0.0.0", port=8020)