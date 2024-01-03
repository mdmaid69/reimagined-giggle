  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)