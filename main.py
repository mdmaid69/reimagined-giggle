  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h