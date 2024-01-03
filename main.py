import collections
def create_stack():
        return collections.deque()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"