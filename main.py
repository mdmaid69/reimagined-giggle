def calculate_force(mass, acceleration):
        return mass * acceleration
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"