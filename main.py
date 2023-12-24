  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)