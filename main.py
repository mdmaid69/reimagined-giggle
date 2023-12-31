  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)