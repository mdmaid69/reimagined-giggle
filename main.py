import math
def calculate_sign(x):
        return math.copysign(1, x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"