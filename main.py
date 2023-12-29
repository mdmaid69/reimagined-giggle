import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)