  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"