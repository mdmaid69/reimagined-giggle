  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)