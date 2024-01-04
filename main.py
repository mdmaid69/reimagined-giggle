  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)