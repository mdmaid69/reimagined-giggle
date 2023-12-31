import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"