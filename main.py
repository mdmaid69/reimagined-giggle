  import os
  def delete_file(file_name):
        os.remove(file_name)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)