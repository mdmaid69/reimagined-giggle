  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)