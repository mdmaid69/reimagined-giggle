from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import collections
def create_priority_queue():
        return collections.deque()