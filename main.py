import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags