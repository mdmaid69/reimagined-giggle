import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"