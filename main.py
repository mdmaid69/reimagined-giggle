import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"