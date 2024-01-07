  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)