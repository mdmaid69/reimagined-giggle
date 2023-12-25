  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"