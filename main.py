import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime