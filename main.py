  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)