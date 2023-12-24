import math
def calculate_factorial(n):
        return math.factorial(n)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"