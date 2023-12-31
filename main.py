import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def delete_file(file_name):
        os.remove(file_name)