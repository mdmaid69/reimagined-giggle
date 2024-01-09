import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"