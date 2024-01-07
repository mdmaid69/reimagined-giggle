  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)