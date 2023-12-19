  import os
  def split_path(path):
        return os.path.split(path)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)