import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"