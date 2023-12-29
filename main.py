import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"