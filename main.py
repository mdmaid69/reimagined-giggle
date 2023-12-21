  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)