  import os
  def get_base_name(path):
        return os.path.basename(path)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)