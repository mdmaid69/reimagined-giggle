  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)