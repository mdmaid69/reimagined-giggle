import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)