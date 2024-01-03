  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)