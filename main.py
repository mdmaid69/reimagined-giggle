  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)