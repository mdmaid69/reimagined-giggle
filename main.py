  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h