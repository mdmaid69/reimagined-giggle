  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)