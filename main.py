  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)