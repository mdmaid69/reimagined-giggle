import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"