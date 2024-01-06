import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"