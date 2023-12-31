  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)