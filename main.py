  import os
  def get_current_working_directory():
        return os.getcwd()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h