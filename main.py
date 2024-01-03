  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)