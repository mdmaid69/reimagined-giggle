  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)