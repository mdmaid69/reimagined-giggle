  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)