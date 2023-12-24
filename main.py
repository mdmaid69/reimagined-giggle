import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"