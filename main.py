from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)