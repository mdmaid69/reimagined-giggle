  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)