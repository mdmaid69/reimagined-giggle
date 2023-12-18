def calculate_area(radius):
        return 3.14 * radius * radius
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"