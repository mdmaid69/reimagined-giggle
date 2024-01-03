  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h