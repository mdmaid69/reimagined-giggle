  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)