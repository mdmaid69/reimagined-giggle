import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)