  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"