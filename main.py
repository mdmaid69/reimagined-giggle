  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)