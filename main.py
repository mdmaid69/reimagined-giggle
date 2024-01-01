  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)