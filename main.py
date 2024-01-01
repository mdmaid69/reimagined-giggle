  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)