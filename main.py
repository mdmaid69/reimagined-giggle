  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)