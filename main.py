import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)