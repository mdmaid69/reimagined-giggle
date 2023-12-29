  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)