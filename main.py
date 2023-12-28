from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)