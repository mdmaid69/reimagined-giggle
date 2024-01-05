import collections
def create_counter():
        return collections.Counter()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"