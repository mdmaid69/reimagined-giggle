from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)