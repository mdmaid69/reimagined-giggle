  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)