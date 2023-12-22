import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"