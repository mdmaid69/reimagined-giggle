import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)