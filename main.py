  import os
  def split_path(path):
        return os.path.split(path)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)