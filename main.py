from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import collections
def count_elements(iterable):
        return collections.Counter(iterable)