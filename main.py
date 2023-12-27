  import os
  def get_current_directory():
        return os.getcwd()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)