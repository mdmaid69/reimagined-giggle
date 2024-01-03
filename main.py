import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"