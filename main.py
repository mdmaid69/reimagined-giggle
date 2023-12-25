  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)