  def calculate_area_circle(r):
        return 3.14 * r**2
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"