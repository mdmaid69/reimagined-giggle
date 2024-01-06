  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)