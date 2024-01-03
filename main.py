  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)