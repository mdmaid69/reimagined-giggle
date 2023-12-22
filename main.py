  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)