import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)