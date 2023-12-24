from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)