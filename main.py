  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h