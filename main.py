  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)