  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h