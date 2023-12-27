  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h