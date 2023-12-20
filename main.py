def calculate_density(mass, volume):
        return mass / volume
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"