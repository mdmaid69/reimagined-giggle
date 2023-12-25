  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)