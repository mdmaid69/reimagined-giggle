import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)