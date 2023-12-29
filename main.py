import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"