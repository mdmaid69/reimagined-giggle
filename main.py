import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)