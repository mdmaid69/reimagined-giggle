  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)