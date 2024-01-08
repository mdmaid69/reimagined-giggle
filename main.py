import json
def convert_to_json(data):
        return json.dumps(data)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)