import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"