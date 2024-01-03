  import os
  def delete_file(file_name):
        os.remove(file_name)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)