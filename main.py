import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)