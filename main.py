  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)