  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h