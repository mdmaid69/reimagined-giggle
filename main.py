import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)