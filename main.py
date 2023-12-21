  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)