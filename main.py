  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)