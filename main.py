import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)