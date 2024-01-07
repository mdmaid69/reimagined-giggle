from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)