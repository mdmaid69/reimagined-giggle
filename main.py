import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"