import math
def calculate_gamma_function(x):
        return math.gamma(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"