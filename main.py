  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)