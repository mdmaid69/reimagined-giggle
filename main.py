  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)