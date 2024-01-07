  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)