  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)