  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)