import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"