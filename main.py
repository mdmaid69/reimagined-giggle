  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)