  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)