  import os
  def get_base_name(path):
        return os.path.basename(path)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)