import math
def calculate_floor(x):
        return math.floor(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"