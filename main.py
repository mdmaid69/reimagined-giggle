  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)