  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)