import math
def calculate_logarithm_base_e(x):
        return math.log(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"