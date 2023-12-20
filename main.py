  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)