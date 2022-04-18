from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask App worked!</H1>"

@app.route("/health")
def home():
    return "Success", 200