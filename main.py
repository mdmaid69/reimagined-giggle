  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)