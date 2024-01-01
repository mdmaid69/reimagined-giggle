  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h