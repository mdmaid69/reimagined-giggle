  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)