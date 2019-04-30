# flask_app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Set debug status
if config.ENVIRONMENT == 'development':
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

# Set db config
for key, value in config.DB[config.ENVIRONMENT].items():
    app.config[key] = value
db = SQLAlchemy(app)


class ApiRequest(db.Model):
    __tablename__ = "ApiModel"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        return jsonify([{"some": "json"}])
    data = [{"some": "post"}]
    return jsonify(data)


@app.route("/api2", methods=["GET", "POST"])
def api2():
    api_request = ApiRequest(username="username3", email="luke3@email.com")
    db.session.add(api_request)
    db.session.commit()
    return '{"status-code":200}'
