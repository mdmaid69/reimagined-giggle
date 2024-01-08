def calculate_work(force, distance):
        return force * distance
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"