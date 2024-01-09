import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"