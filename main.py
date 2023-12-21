import math
def calculate_absolute_value(x):
        return math.fabs(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"