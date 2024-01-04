  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)