import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)