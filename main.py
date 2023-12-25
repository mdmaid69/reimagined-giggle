  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h