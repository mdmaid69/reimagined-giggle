  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)