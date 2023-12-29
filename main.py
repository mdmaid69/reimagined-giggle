import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)