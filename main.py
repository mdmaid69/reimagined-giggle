  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)