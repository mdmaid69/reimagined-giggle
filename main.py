import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)