  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)