  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)