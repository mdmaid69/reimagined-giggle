  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)