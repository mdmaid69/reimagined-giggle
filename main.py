import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"