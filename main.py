  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h