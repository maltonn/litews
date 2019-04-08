from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! ver2"

@app.route("/html")
def SampleHTML():
    return render_template("index.html")
