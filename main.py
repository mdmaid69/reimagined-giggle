  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"