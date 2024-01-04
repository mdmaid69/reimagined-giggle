  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)