  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)