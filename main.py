  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)