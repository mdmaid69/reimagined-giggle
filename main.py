import math
def calculate_square_root(x):
        return math.sqrt(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"