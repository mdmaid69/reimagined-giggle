import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]