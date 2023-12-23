  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)