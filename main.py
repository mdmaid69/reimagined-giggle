  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h