  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)