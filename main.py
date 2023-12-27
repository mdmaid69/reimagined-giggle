def calculate_perimeter_triangle(a, b, c):
        return a + b + c
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"