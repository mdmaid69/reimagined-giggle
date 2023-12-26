import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)