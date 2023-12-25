  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)