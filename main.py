  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)