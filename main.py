from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)