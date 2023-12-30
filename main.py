  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"