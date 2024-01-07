from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))