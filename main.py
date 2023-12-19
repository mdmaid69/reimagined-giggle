from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_permutations(n, k):
        return math.perm(n, k)