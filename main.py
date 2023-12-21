def calculate_area_triangle(b, h):
        return 0.5 * b * h
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"