  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)