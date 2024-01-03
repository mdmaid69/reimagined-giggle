  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h