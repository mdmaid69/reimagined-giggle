  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)