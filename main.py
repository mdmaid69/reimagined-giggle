def calculate_pressure(force, area):
        return force / area
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"