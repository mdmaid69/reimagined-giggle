import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)