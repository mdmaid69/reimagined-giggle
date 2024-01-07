import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"