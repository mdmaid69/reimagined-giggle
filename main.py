  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)