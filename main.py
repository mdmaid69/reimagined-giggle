  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)