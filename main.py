  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)