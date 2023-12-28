  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)