import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"