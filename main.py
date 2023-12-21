import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)