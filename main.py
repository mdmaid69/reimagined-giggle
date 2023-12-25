import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"