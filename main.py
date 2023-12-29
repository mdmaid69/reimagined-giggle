  import os
  def get_current_working_directory():
        return os.getcwd()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)