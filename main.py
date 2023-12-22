  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)