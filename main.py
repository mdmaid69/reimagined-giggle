  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)