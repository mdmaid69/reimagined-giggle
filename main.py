  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)