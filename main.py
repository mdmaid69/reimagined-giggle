  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h