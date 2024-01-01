import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)