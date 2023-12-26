  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)