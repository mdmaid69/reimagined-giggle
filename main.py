  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)