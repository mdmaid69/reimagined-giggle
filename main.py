  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)