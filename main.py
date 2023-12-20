import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]