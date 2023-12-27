  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)