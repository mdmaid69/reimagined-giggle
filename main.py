  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)