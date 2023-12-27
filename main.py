  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)