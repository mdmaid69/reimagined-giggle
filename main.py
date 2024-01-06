  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)