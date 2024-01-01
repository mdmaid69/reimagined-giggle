  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)