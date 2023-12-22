import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)