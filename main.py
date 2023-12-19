import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)