import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"