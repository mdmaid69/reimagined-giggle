  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)