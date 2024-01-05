import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags