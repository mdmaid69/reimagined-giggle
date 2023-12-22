  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)