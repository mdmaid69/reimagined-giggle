  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)