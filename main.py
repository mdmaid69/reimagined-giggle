  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)