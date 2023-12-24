import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"