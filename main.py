import json
def convert_to_json(data):
        return json.dumps(data)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"