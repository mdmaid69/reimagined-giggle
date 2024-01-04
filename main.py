  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)