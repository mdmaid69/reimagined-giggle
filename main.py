  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)