  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h