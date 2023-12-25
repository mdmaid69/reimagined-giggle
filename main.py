import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)