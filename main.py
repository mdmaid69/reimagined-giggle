  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)