  import os
  def split_path(path):
        return os.path.split(path)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)