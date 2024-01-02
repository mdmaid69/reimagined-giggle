import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)