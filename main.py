  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)