import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns