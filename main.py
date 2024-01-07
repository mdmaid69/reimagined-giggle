import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)