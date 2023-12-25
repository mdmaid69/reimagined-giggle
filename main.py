  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)