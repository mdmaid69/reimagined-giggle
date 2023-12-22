  def calculate_area_rectangle(l, w):
        return l * w
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"