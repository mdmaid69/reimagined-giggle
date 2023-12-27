  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"