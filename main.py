  import os
  def split_path(path):
        return os.path.split(path)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)