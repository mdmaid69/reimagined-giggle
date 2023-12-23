  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"