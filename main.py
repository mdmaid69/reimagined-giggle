import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"