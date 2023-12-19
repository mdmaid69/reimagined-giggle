  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)