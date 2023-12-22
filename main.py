import math
def calculate_error_function(x):
        return math.erf(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"