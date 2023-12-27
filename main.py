import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)