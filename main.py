  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)