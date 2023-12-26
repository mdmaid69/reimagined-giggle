  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)