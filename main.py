  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)