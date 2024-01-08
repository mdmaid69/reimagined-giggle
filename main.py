  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)