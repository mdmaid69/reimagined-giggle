import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"