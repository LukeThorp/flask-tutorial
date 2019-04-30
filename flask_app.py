# flask_app.py
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api", methods=["GET","POST"])
def api():
    if request.method == "GET":
        data = [{"some":"json"}]
    data = [{"some":"post"}]
    return jsonify(data)