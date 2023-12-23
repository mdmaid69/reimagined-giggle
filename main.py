import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)