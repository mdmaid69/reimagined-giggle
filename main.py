  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)