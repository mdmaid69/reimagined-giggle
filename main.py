  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)