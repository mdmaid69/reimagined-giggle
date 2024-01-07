from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_circle_area(radius):
        return math.pi * radius**2