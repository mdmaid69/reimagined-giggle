  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)