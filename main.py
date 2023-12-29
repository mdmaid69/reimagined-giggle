  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)