from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)