import json
def read_from_json(json_string):
        return json.loads(json_string)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"