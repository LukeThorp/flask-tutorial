# flask_app.py
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api")
def api():
    data = {"some":"json"}
    return jsonify(data)