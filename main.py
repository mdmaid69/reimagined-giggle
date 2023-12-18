import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"