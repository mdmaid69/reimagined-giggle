  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)