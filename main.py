  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import json
def read_from_json(json_string):
        return json.loads(json_string)