import math
def calculate_exponential(x):
        return math.exp(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"