from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import math
  def calculate_square_root(n):
        return math.sqrt(n)