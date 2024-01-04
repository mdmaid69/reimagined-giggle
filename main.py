  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h