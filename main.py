  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)