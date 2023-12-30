import math
def calculate_arc_cosine(x):
        return math.acos(x)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"