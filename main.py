import math
def calculate_combinations(n, k):
        return math.comb(n, k)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"