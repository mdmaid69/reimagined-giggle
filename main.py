from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import math
def calculate_sine(x):
        return math.sin(x)