  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)