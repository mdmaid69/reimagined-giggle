import math
def calculate_arc_sine(x):
        return math.asin(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"