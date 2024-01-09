import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"