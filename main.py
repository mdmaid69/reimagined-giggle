  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)