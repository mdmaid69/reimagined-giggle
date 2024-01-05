  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)