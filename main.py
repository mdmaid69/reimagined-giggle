import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)