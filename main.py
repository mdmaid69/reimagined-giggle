  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h